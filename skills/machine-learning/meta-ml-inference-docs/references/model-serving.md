# Model Serving Platforms

Read when the target serves models behind an API or on Kubernetes. One
line and an entry point per tool; fetch deployment manifests and API
details from the entry point. Triton Inference Server, KServe, and
Seldon deploy as containers/operators — see their docs. No entry is a
recommendation.

## Platforms

| Tool | One line | Docs |
|---|---|---|
| NVIDIA Triton Inference Server | multi-framework, multi-model GPU serving | <https://docs.nvidia.com/deeplearning/triton-inference-server/> — llms.txt: <https://docs.nvidia.com/llms.txt> |
| KServe | Kubernetes-native model inference CRDs | <https://kserve.github.io/website/> |
| BentoML | package and serve models as APIs | <https://docs.bentoml.com/> |
| Seldon Core | Kubernetes model deployment and inference graphs | <https://docs.seldon.ai/> — llms.txt: <https://docs.seldon.ai/home/llms.txt> |
| TensorFlow Serving | production serving for TensorFlow models | <https://github.com/tensorflow/serving> |
| TorchServe | model serving for PyTorch | <https://docs.pytorch.org/serve/> |
| MLServer | multi-framework inference server behind Seldon and KServe | <https://docs.seldon.ai/mlserver> — llms.txt: <https://docs.seldon.ai/mlserver/llms.txt> |
| FastAPI | general Python API framework often wrapping model inference | <https://fastapi.tiangolo.com/> |
| Gradio | interactive ML web UIs in Python | <https://gradio.app/docs> — llms.txt: <https://gradio.app/llms.txt> |
| Streamlit | data and ML app framework in Python | <https://docs.streamlit.io/> — llms.txt: <https://docs.streamlit.io/llms.txt> |
