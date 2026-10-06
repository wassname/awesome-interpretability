# Interpretability catalogue audit

Research draft, 7 October 2026 (Perth). Author: PI/gpt-6.1-sol. Target: `wassname/awesome-interpretability`, `main`, `f5a023133bfc2997ca90926af8852e1774169ab4`. README unchanged; nothing published.

User priorities:

> "please do deep research for this. esp on gh and hf"
> "it's usefull to know stars, human authors, and how persistant/stale the project is"
> "also SAE's suck we can list but meh"
> "there are NLA's too now"

## Findings verified so far

1. TransformerLens's HF description is outdated. Its current README recommends `TransformerBridge`, preserves raw HF weights by default, and says `HookedTransformer.from_pretrained` was removed in v4.0. Updating this matters more than adding another wrapper on the basis of the old comparison.
2. Natural-language interpretation should have its own group. The list already contains NLAs and their inference package. Additional distinct methods include Activation Oracles, LatentQA, introspection adapters, and Predictive Concept Decoders. These do not answer the same questions or have the same validation objective.
3. Recent discoveries include ICA Lens (ICA decomposition and steering), interp-engine (standardized activation capture), Steerling (an interpretable-by-design diffusion LM), Subtext (a conversational Jacobian-lens interface), and Dyno Lab (an Apple Silicon workbench). Their narrow author bases and short histories should remain visible.
4. Docent belongs with agent-transcript auditing. Its current product page says it analyzes agent transcripts using behavior rubrics. Calling it an internal model explanation/steering interface is misleading.
5. InterpretML points to `interpret-community`, not the main `interpret` library. Main-library and explainer-collection metrics must not be conflated.
6. Maintenance descriptions are inconsistent. Some unlabeled libraries have older code than the ones marked abandoned. Stable paper code and abandoned infrastructure should have different labels.

This draft is awaiting the GitHub/HF survey reports and an independent evidence challenge. It is not the final shortlist.

## Source passages

### TransformerLens: primary maintainer README

https://github.com/TransformerLensOrg/TransformerLens

> `TransformerBridge` is the recommended path and supports 15,000+ models across 140+ architecture families (see [`supported_models.json`](transformer_lens/tools/model_registry/data/supported_models.json) for the full inventory). By default it preserves raw HuggingFace weights – logits and activations match HF, *not* legacy `HookedTransformer` (which folds LayerNorm and centers weights by default). Call `bridge.enable_compatibility_mode()` after booting for HookedTransformer-equivalent numerics. The legacy `HookedTransformer.from_pretrained` API was removed in TransformerLens 4.0 — see the [Migrating to TransformerLens 4.0](https://TransformerLensOrg.github.io/TransformerLens/content/migrating_to_v4.html) guide.

Observation: current documentation contradicts an unqualified old HF-compatibility description. This is a maintainer claim, not a compatibility test run by this audit.

### Activation Oracles: primary maintainer README

https://github.com/adamkarvonen/activation_oracles

> **Reproducing the paper:** use the [`paper`](https://github.com/adamkarvonen/activation_oracles/tree/paper) branch (or the `v1.0-paper` tag), which has the code and dependency versions used for the paper (torch 2.7.1, transformers 4.55.2, peft 0.17.1). `main` is maintained and upgraded (transformers 5, torch 2.12) to support newer models such as Qwen3.6-27B.

> The Colab version runs on a free T4 GPU. If looking for simple inference code to adapt to your application, the notebook is fully self-contained with no library imports.

> Note that the smaller models (1-4B) tend to have worse OOD eval performance, so I'm not sure how well they will work.

Observation: a release-reproduction branch and an evolving library branch are separate. A small downloadable checkpoint is not automatically the best-performing oracle.

### Activation Oracles: author research post

https://alignment.anthropic.com/2025/activation-oracles/

> Activation Oracles are a fundamentally non-mechanistic technique for interpreting LLM activations.

Interpretation: place these under activation explanation/auditing, not under recovered causal mechanisms.

### NLA: author research post

https://www.anthropic.com/research/natural-language-autoencoders

> The most important limitation is that NLA explanations can be wrong. NLAs sometimes make claims about the context that are verifiably false—for instance, they sometimes invent details that aren’t in the transcript.

> At inference time, the NLA generates hundreds of tokens for every activation it reads. That makes it impractical to run NLAs over every token of a long transcript or to use them for large-scale monitoring while an AI is training.

Interpretation: list the usable artifacts and costs without presenting verbalizations as ground truth. Reconstruction agreement is an evaluation signal, not proof of a causally faithful English explanation.

### Introspection adapters: author research post

https://alignment.anthropic.com/2026/introspection-adapters/

> Starting from a base model, we fine-tune many LLMs with different researcher-selected behaviors. Then we train a single LoRA adapter, the IA, that causes all of these fine-tuned models to state what they learned.

> First, introspection adapters exhibit a high false-positive rate: when applied to models without any specific trained behaviors, they tend to hallucinate behaviors from the training distribution.

Interpretation: model/weight auditing with learned self-reports, not an activation autoencoder. Keep false positives next to the link.

### Predictive Concept Decoders: author research post

https://transluce.org/pcd

> Our key insight is to frame interpretability as a prediction problem: A system that understands a model's activations should be able to predict that model's future behaviors.

> A PCD has two components:
> 1. An **encoder** that compresses model activations to a sparse list of concepts, and
> 2. A **decoder** that takes these concepts and answers questions about model behaviors.

Observation: public report and demo found. This page does not establish a released GitHub implementation or HF checkpoint. Do not invent either or classify this as an installable library.

### Docent: current product documentation

https://transluce.org/docent

> Docent helps analyze AI agent transcripts by turning anecdotes and intuitions into reliable, traceable measurements.

> Docent supports any text-only, single or multi-agent transcript.

Observation: transcript/behavior auditing, distinct from probing or editing hidden states.

### interp-engine: primary implementation documentation

https://github.com/decoderesearch/interp-engine/blob/main/docs/GRADIENTS.md

> So a linear probe on captured activations trains fine on either backend. Attribution that needs a gradient *of the model* is eager-only.

Observation: fast capture and model-gradient attribution are different supported operations. Do not summarize a vLLM backend as a substitute for differentiable eager execution.

## Metadata and audit method

- GitHub metadata, default-branch commits, contributor pages, READMEs, recent issues, and releases were fetched through authenticated `gh`. No repository code was executed.
- `humans*` counts distinct GitHub contributor logins with account type `User`, excluding known bot identities. This is attributed non-bot accounts, not verified humans, paper-author counts, or proof of human-written code. Anonymous and co-authored contributions can be missed; historical imports can inflate apparent breadth.
- GitHub `updated_at` and `pushed_at` are not used as last-code evidence. The collector checks files in up to 20 recent default-branch commits and excludes docs and `.github` activity. It counts source, tests and configuration; `unknown` means no qualifying commit in that window, not no code.
- Repository creation measures how long the repository has existed, not continuous maintenance. Read it alongside last source/config commit, releases, and issue responses.
- A quiet paper implementation remains a useful reference. GitHub stars measure attention, not correctness. HF likes/downloads should be reported separately and never relabeled as stars or users.
- `snapshot_github.py` records explicit API failures. Known discovery errors (wrong slugs and a GitHub topic URL parsed as a repository) are not interpreted as abandoned/missing projects.

Evidence collected so far: metadata/README snapshots for 51 already-linked third-party GitHub repositories, plus additional candidate snapshots. Full survey coverage and final recommendations will be added after the research reports settle.
