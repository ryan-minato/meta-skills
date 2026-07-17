# Training Container Skeleton

Copy the two blocks below to `Dockerfile` and `compose.yaml`, then rework
them: enumerate live base-image tags first, fill every placeholder, and
delete what the deployment does not need. Add `docker-build` /
`docker-train` recipes to the justfile in the same change. Verify current
uv-in-Docker and Compose GPU syntax from the uv and Compose docs before
committing.

````dockerfile
FROM nvidia/cuda:<tag — a runtime variant unless something compiles CUDA code>

# uv manages Python and packages inside the image; it downloads a managed
# interpreter, so the base image needs none.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV UV_TORCH_BACKEND=<backend matching the base image's CUDA/ROCm>

WORKDIR /app

# Dependency layer first: rebuilt only when the lockfile changes.
COPY requirements.txt .
RUN uv venv --python <version> && uv pip sync requirements.txt
ENV PATH="/app/.venv/bin:${PATH}"

# The environment is baked; data, outputs, and secrets never are.
COPY . .

CMD ["python", "train.py"]
````

````yaml
services:
  train:
    build: .
    volumes:
      - ./data:/app/data
      - ./outputs:/app/outputs
      - hf-cache:/root/.cache/huggingface
    env_file: .env  # secrets ride in at runtime, never into the image
    shm_size: "<e.g. 8gb>"  # DataLoader workers exhaust Docker's default shm
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]

volumes:
  hf-cache:
````
