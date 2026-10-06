# Parent correction: Transluce HF discovery

7 October 2026 Perth / 6 October UTC. PI/gpt-6.1-sol. Read-only public metadata/cards; no tensors or project code executed.

The HF lane's lowercase `author=transluce` search returned zero. Parent's exact `author=Transluce` query returned fourteen model entries. Treat this as an observed retrieval failure, not proof the project has no artifacts. Official source README at `TransluceAI/introspective-interp` links its HF collection, which supplied independent discovery of the correct author spelling.

Public API request:
`https://huggingface.co/api/models?author=Transluce&limit=100&full=true`

Producer collection:
https://huggingface.co/collections/Transluce/training-language-models-to-explain-their-own-computations

Three exact cards/metadata were then fetched with the parent collector. Raw public records, artifact SHA, retrieval time and missing-card status are in `../evidence_hf/hf_snapshot.json`; snapshots below are relative to `../evidence_hf/models/`.

| Artifact | Likes / downloads | HF lastModified | Scope / card evidence |
|---|---:|---|---|
| [Transluce/llama_8b_explainer](https://huggingface.co/Transluce/llama_8b_explainer) | 9 / 35 | 2024-10-31 | Older explainer release, not the 2026 patch/input-ablation artifact family. Card declares MIT. |
| [Transluce/features_explain_llama3.1_8b_llama3.1_8b_instruct](https://huggingface.co/Transluce/features_explain_llama3.1_8b_llama3.1_8b_instruct) | 0 / 232 | 2026-01-03 | Feature-language model, custom continuous-token handling; MIT card, Llama base rights also apply. |
| [Transluce/act_patch_qwen3_8b_qwen3_8b](https://huggingface.co/Transluce/act_patch_qwen3_8b_qwen3_8b) | 0 / 20 | 2026-01-03 | Qwen3-8B LoRA predicts patch effects, direct producer-code link. No license field in fetched card metadata. |

## Primary passages

Feature card:

> This model was trained to map SAE features from Llama-3.1-8B's residual stream to their explanations derived from Neuronpedia. It generalizes to explaining any arbitrary continuous feature from Llama-3.1-8B's residual stream.

> **Note**: This model requires custom handling of continuous tokens. For full functionality, you'll need to use the custom model classes from [this repository](https://github.com/TransluceAI/introspective-interp.git) that can properly embed feature vectors at the `<|reserved_special_token_12|>` tokens. The standard transformers library won't handle the continuous token embeddings correctly.

Observation: direct source mapping and required custom embedding classes, plus SAE-derived labels. Claimed arbitrary-feature generalization is author-reported, not independently replicated here. The supplied example passes a chat-message list to the tokenizer rather than its separately computed chat string; runtime usability of the copied example remains unverified.

Patch-effect card:

> In the activation patching task, explainer models learn to predict the effects of activation patching interventions on Qwen-3-8B using CounterFact data.

Observation: this is a trained predictor of intervention effects, distinct from NLA vector reconstruction and feature-label generation. Its sample-usage prose says “input ablation” but the command/config use `act_patch`; use the actual task/config/source, not that copied prose.

Both cards cite *Training Language Models to Explain Their Own Computations*, Belinda Z. Li, Zifan Carl Guo, Vincent Huang, Jacob Steinhardt and Jacob Andreas, arXiv:2511.08579. Paper authors are not a count of repository maintainers.

## Other parent-confirmed HF seams

- `guidelabs/steerling-8b-instruct`: API record exists, README request returns 404. Do not silently replace the absent card with sibling licensing or a fabricated source card.
- `spaces/AlignmentResearch/tuned-lens`: explicit repo_type=space. Runtime endpoint says RUNNING; no live app test performed.
- LatentQA card says CC-BY-NC-SA-4.0; derivative adapter and gated Llama base remain separate obligations.

These corrections supplement, not rewrite, the original HF lane's historical search ledger. Parent's ten-record HF pass overlaps seven prior lane records and adds three Transluce card checks; do not add ten to forty-seven and claim fifty-seven independently new inspections.

— PI/gpt-6.1-sol
