# Dev Container Skeleton

Copy the block below to `.devcontainer/devcontainer.json`, then rework
it: pick the image from the base-image table in the containers reference,
fill every placeholder, and delete what the project does not use. GPU
access is managed by `hostRequirements.gpu` alone — implementations add
`--gpus all` when a GPU runtime is present and skip it otherwise, so the
same config serves GPU and CPU-only machines (fallback cases are in the
containers reference). Verify current semantics against the spec at
<https://containers.dev/>.

````json
{
  "name": "<project name>",
  "image": "<base image, e.g. nvidia/cuda:<tag> — enumerate live tags first>",
  "hostRequirements": {
    "gpu": "optional"
  },
  "postCreateCommand": "curl -LsSf https://astral.sh/uv/install.sh | sh && uv venv && uv pip sync requirements.dev.txt --torch-backend <backend> && uv run pre-commit install",
  "containerEnv": {
    "HF_HOME": "/workspaces/<project name>/.hf-cache"
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "charliermarsh.ruff"
      ]
    }
  }
}
````
