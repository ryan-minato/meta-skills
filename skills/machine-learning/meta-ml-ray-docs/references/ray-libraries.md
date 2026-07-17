# Ray Libraries

Read for any Ray-based target. Every Ray library documents under one
root; record the root once and note which components the target uses.
Fetch install extras and API details from the entry point. No entry is a
recommendation.

## Entry point

| Tool | One line | Docs |
|---|---|---|
| Ray | distributed compute: Core (tasks, actors, object store), Data (distributed ETL and batch inference), Train (multi-node training), Tune (hyperparameter search), Serve (model serving), Serve LLM (OpenAI-compatible LLM serving), RLlib (reinforcement learning) | <https://docs.ray.io/> — llms.txt: <https://docs.ray.io/llms.txt> |

When recording, name the components the target actually uses (for
example "Ray Data + Ray Train") next to the shared entry point, so a
later agent lands on the right section of the docs.
