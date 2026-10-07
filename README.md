# awesome-interpretability

This list has tools, models, datasets and reading for interpretability. Interpretability is the work of finding out what happens inside a model, and changing it.

Each table is about one task. The columns are:

- ~H: the approximate number of humans who wrote code in the GitHub repo. We count the contributor accounts and remove bots and service accounts. One person can have two accounts, and some authors have no account in the history, so the number is an estimate. A high ~H shows that many people worked on the project. It does not show that they still maintain it.
- Stars: the number of GitHub stars.
- Created: the date when the repo was created.
- Latest commit: the date of the last commit on the default branch. This commit can be a change to the docs only.

In each table, the rows are sorted by ~H, then by stars. † means that the numbers are for the whole repo, not for the part that the link goes to. — means that there are no GitHub numbers, for example for a Hugging Face model or a blog post. We checked the numbers on 2026-10-07.

[Research and sources](slop/research/20261007_interpretability/results.md).


## Inspect and intervene

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [TransformerLens](https://github.com/TransformerLensOrg/TransformerLens) | **192** | **3,946** | 2022-08-26 | [2026-09-28](https://github.com/TransformerLensOrg/TransformerLens/commit/191170906559adf5ede1560097718cf431b972ac) | Jaxtyping; TransformerBridge preserves raw HuggingFace weights by default. [Legacy description](https://twitter.com/NeelNanda5/status/1786146027659280430); [v4 migration](https://TransformerLensOrg.github.io/TransformerLens/content/migrating_to_v4.html). |
| [NNsight](https://github.com/ndif-team/nnsight) | 37 | 1,120 | 2023-10-20 | [2026-09-09](https://github.com/ndif-team/nnsight/commit/260c555bf2e3bd3395eed4df0435f35e253b2d3d) | HuggingFace-compatible local/remote tracing and interventions. [David Bau on the with-context interface](https://twitter.com/davidbau/status/1785991660197015827). |
| [Pyvene](https://github.com/stanfordnlp/pyvene) | 23 | 905 | 2023-02-06 | [2026-03-06](https://github.com/stanfordnlp/pyvene/commit/9e333904dcf9e597ca76170010d17f4d4580de8d) | Intervention-focused, HF-native. [Author description](https://twitter.com/ZhengxuanZenWu/status/1768356269470191842). |
| [ViT-Prisma](https://github.com/Prisma-Multimodal/ViT-Prisma) | 10 | 393 | 2023-10-02 | [2025-07-21](https://github.com/Prisma-Multimodal/ViT-Prisma/commit/46d21f0bb1a4e23aaad60ff777e5fa3243e09383) | Mechanistic interpretability for vision and video transformers. |
| [vLLM-Hook](https://github.com/IBM/vLLM-Hook) | 10 | 163 | 2025-11-12 | [2026-09-23](https://github.com/IBM/vLLM-Hook/commit/0e34fddf2c234a50c9c820c2b7852472f8f4c51c) | Program internal states of vLLM-served models. |
| [Penzai](https://github.com/google-deepmind/penzai) | 9 | 1,899 | 2024-04-04 | [2025-06-22](https://github.com/google-deepmind/penzai/commit/aac7808a3d1269ea9885094d78d2274d56fc7449) | JAX-based, not HuggingFace-native; archived. |
| [cupbearer](https://github.com/ejnnr/cupbearer) | 6 | 22 | 2023-03-21 | [2025-01-09](https://github.com/ejnnr/cupbearer/commit/cf9838560a7de7fa09e44aec40ee68734a5fe4c8) | Library for mechanistic anomaly detection. |
| [vllm-lens](https://github.com/UKGovernmentBEIS/vllm-lens) | 5 | 131 | 2026-03-12 | [2026-10-02](https://github.com/UKGovernmentBEIS/vllm-lens/commit/3d11fb0b6097b8834bbfc9a6200ec5a7f2205b81) | Extract residual stream activations and apply steering vectors in vLLM. |
| [nnterp](https://github.com/ndif-team/nnterp) | 4 | 121 | 2024-08-08 | [2026-07-02](https://github.com/ndif-team/nnterp/commit/b4a31274692f986e493ac5d20ba20a4ec8640955) | NNsight companion: standardized model/module names and accessors; preserves HF implementations. |
| [Mishax](https://github.com/google-deepmind/mishax) | 3 | 158 | 2024-07-30 | [2026-09-16](https://github.com/google-deepmind/mishax/commit/c143e3b5142f6b6967eba46ce1eb6aab53f15a7c) | JAX/Flax instrumentation and interventions through AST rewriting. |
| [TorchLens](https://github.com/johnmarktaylor91/torchlens) | 2 | 662 | 2022-10-14 | [2026-10-04](https://github.com/johnmarktaylor91/torchlens/commit/20c222a3c4954b5f14af2e4e9095ab9123266279) | PyTorch computation graphs, activation/gradient inspection and interventions; not restricted to transformers. |
| [BauKit](https://github.com/davidbau/baukit) | 2 | 258 | 2022-02-15 | [2024-02-22](https://github.com/davidbau/baukit/commit/9d51abd51ebf29769aecc38c4cbef459b731a36e) | Light, simple, and well loved. PyTorch hooks. |
| [interp-engine](https://github.com/decoderesearch/interp-engine) | 1 | 39 | 2026-08-05 | [2026-10-02](https://github.com/decoderesearch/interp-engine/commit/eb9bb6d992e73d7624965583dd945ec15f0c510e) | Standardized eager/vLLM activation capture and editing. Early project; model-gradient attribution is eager-only. |
| [Graphpatch](https://github.com/evan-lloyd/graphpatch) | 1 | 22 | 2023-12-06 | [2025-01-27](https://github.com/evan-lloyd/graphpatch/commit/d1ecec2949ea622eb04a4a364ef08942d6a8025f) | Graph-based PyTorch interventions; inactive default branch since January 2025, unarchived. |

## Natural-language interpretation

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [Activation Oracles](https://github.com/adamkarvonen/activation_oracles) | **2** | 103 | 2025-07-30 | [2026-09-26](https://github.com/adamkarvonen/activation_oracles/commit/5712762cfc29a18d6414a1cf2cccb4ff4432ced5) | Natural-language activation QA, distinct from NLA reconstruction. [Adapters](https://huggingface.co/collections/adamkarvonen/activation-oracles-694232103936f0bd6893c5ca); paper/main dependencies differ. Adam Karvonen. |
| [Transluce introspective interpretation](https://github.com/TransluceAI/introspective-interp) | **2** | 38 | 2025-12-22 | [2026-07-07](https://github.com/TransluceAI/introspective-interp/commit/594d53348734097857430826d88f5c6856164de7) | Feature descriptions, patch-effect prediction and input ablations. [Released models](https://huggingface.co/collections/Transluce/training-language-models-to-explain-their-own-computations); feature supervision is SAE-derived. |
| [Natural Language Autoencoders](https://github.com/kitft/natural_language_autoencoders) | 1 | **955** | 2026-05-05 | [2026-08-02](https://github.com/kitft/natural_language_autoencoders/commit/0577769b55ad4fdd96d159e983361b97fa4e7331) | Two fine-tuned LMs: one writes a text description of an activation, the other rebuilds it; SFT then GRPO. Used in Anthropic pre-deployment audits (Claude Opus 4.6 onward). [Paper](https://transformer-circuits.pub/2026/nla/index.html), [inference package](https://github.com/kitft/nla-inference), [four matched AV/AR pairs](https://huggingface.co/collections/kitft/nla-models-69fa80a3c69880bba63eddc6), [demo](https://www.neuronpedia.org/nla). |
| [LatentQA](https://github.com/aypan17/latentqa) | 1 | 37 | 2024-12-12 | [2025-11-16](https://github.com/aypan17/latentqa/commit/a2dcb6f8eef52ce8c8e75ee71da66cb880f727f4) | Research decoder that reads/writes activations in natural language. [Adapter](https://huggingface.co/aypan17/latentqa_llama-3-8b-instruct): CC-BY-NC-SA-4.0, Llama base required. |
| [Predictive Concept Decoders](https://transluce.org/pcd) | — | — | — | — | Reading/demo: sparse concepts predict future model behavior. [Demo](https://decoder.transluce.org/); public code/checkpoint not verified. |

## Lenses, probes and concepts

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [ELK](https://github.com/EleutherAI/elk) | **19** | 225 | 2023-02-01 | [2023-11-02](https://github.com/EleutherAI/elk/commit/84e99a36a5050881d85f1510a2486ce46ac1f942) | Latent-knowledge activation extraction and probe evaluation. Current training path is supervised; older README describes CRC/CCS. Probes do not establish general truth detection. |
| [Interpreto](https://github.com/FOR-sight-ai/interpreto) | 10 | 207 | 2025-02-26 | [2026-10-06](https://github.com/FOR-sight-ai/interpreto/commit/b3b9a0fcbb46b891d0029d89a6561307114073a0) | Probes/CAVs, ICA/PCA/NMF/SVD/KMeans, attribution and lenses; SAEs optional. Some metrics and backend migrations remain unreleased. |
| [Tuned Lens](https://github.com/AlignmentResearch/tuned-lens) | 5 | 616 | 2022-10-03 | [2025-08-07](https://github.com/AlignmentResearch/tuned-lens/commit/abdac0c4de23d9f6d6c8459d576ad203aec15deb) | Look at how transformer predictions are built layer by layer. [Pretrained lenses](https://huggingface.co/spaces/AlignmentResearch/tuned-lens/tree/main/lens) are stored in a HF Space. |
| [NeuroX](https://github.com/fdalvi/NeuroX) | 5 | 109 | 2018-08-16 | [2023-04-12](https://github.com/fdalvi/NeuroX/commit/a9ac7cd90be89d72c5ed55d963e2843f039303fc) | Neuron analysis and representation probing; historical toolkit. |
| [Deception Detection](https://github.com/ApolloResearch/deception-detection) | 3 | 54 | 2024-05-31 | [2025-02-06](https://github.com/ApolloResearch/deception-detection/commit/f8ec4010e74927394709dffa22b97bdf8cd5a62f) | Apollo Research linear-probe paper code, labeled rollouts and example probe/config files; dataset/model-specific, not a general truth detector. |
| [Overcomplete](https://github.com/KempnerInstitute/overcomplete) | 2 | 153 | 2024-06-14 | [2025-12-04](https://github.com/KempnerInstitute/overcomplete/commit/a1781af49c6e4bbfdbfd763b9757bcf6c5dd6403) | Vision dictionary/concept learning: SAEs, NMF variants and archetypal analysis. |
| [ICA Lens](https://github.com/liusida/ica-lens-paper) | 2 | 45 | 2026-06-08 | [2026-09-30](https://github.com/liusida/ica-lens-paper/commit/6ad5bee4c94d22173e6ffefe20a0f9ba96c703d9) | ICA decomposition, signed token readouts and coordinate steering. [Fitted lenses](https://huggingface.co/collections/sida/ica-lens); early project, artifact licenses unspecified. |
| [Jacobian lens](https://github.com/anthropics/jacobian-lens) | 1 | **2,011** | 2026-07-02 | [2026-07-02](https://github.com/anthropics/jacobian-lens/commit/581d398613e5602a5af361e1c34d3a92ea82ba8e) | Decodes residual vectors into tokens via the average Jacobian to the last layer. [Paper](https://transformer-circuits.pub/2026/workspace/index.html), [fitted lenses](https://huggingface.co/neuronpedia/jacobian-lens). Reference only, not maintained. |

## Causal hypotheses and circuit discovery

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [circuit-tracer](https://github.com/decoderesearch/circuit-tracer) | **17** | **2,915** | 2025-05-28 | [2026-09-11](https://github.com/decoderesearch/circuit-tracer/commit/7f66876689f59e92fc3641650d38b8bd41749ec4) | Attribution graphs and feature interventions using pretrained MLP transcoders. Bundles credited Anthropic frontend code; repository accounts are not backend-specific maintainers. |
| [Causalab](https://github.com/goodfire-ai/causalab) | 6–7 | 118 | 2025-04-25 | [2026-09-30](https://github.com/goodfire-ai/causalab/commit/8e8d5d1f8f9ca8f42bfce7c6b5eef194f012660e) | Causal hypothesis testing, DAS/DBM and interventions. Public mirror; [issue #79](https://github.com/goodfire-ai/causalab/issues/79) transferred internally, current fix unknown. ~H allows likely account aliases. |
| [Rewriting a Deep Generative Model](https://github.com/davidbau/rewriting) | 4 | 535 | 2020-07-29 | [2020-12-14](https://github.com/davidbau/rewriting/commit/8f57af3b0897307f2d671c45cb279672babba6a4) | David Bau and collaborators: edit StyleGANv2 weights to change generative rules; ECCV 2020 reference code with an old PyTorch/CUDA stack. |
| [AutoCircuit](https://github.com/UFO-101/auto-circuit) | 3 | 103 | 2023-08-21 | [2026-08-17](https://github.com/UFO-101/auto-circuit/commit/7242291d0e5da5c9c044cd6cb97ab911be9adabf) | Efficient patching, automatic circuit discovery and evaluation on TransformerLens. |
| [EAP-IG](https://github.com/hannamw/EAP-IG) | 3 | 89 | 2024-01-15 | [2026-05-23](https://github.com/hannamw/EAP-IG/commit/e24bafd3d22af2c59ac5a83e0a6581b89b5c05dd) | Gradient/integrated-gradient circuit ranking with exact-patching comparisons; architecture constraints apply. |
| [ROME](https://github.com/kmeng01/rome) | 2 | 780 | 2022-02-11 | [2022-10-14](https://github.com/kmeng01/rome/commit/0874014cd9837e4365f3e6f3c71400ef11509e04) | David Bau / Kevin Meng: causal tracing and rank-one factual weight edits. Historical GPT-2/GPT-J/CUDA reference code. |
| [MEMIT](https://github.com/kmeng01/memit) | 2 | 561 | 2022-10-13 | [2022-11-14](https://github.com/kmeng01/memit/commit/80426fd9316cf9a50c5ba15e0912f2c2c5bfe84b) | David Bau / Kevin Meng: batched factual weight edits across layers; historical CUDA reference code, companion to ROME. |
| [Transluce circuits](https://github.com/TransluceAI/circuits) | 1 | 41 | 2026-01-15 | [2026-04-10](https://github.com/TransluceAI/circuits/commit/2d215d4ba016ba8602b69d71fc0f1ad139a427b7) | Neuron-basis ADAG tracing and automated descriptions; paper reference code with AI-assisted implementation disclosed. |

## Steering and trainable interventions

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [PyReFT](https://github.com/stanfordnlp/pyreft) | **10** | **1,590** | 2024-02-17 | [2025-02-06](https://github.com/stanfordnlp/pyreft/commit/dafd0995a366d7b47160a337dcc388eda7431821) | Trainable low-rank representation interventions, built on Pyvene; historical baseline. |
| [AxBench](https://github.com/stanfordnlp/axbench) | 6 | 218 | 2024-08-07 | [2026-03-12](https://github.com/stanfordnlp/axbench/commit/41c8332543e5a631f9a8c0a9df38799893ace758) | Concept detection and steering benchmark. [Even Simple Baselines Outperform Sparse Autoencoders](https://arxiv.org/abs/2501.17148), [Concept16K data](https://huggingface.co/datasets/pyvene/axbench-concept16k): model-generated examples sampled from GemmaScope concepts. |
| [repeng](https://github.com/vgel/repeng) | 5 | 761 | 2024-01-21 | [2025-09-24](https://github.com/vgel/repeng/commit/0ba7196d81f7c5de28b1159c9d1732440afd97ce) | Library for making RepE control vectors. Theia Vogel. [Representation Engineering Mistral-7B an Acid Trip](https://vgel.me/posts/representation-engineering/). |
| [steering-vectors](https://github.com/steering-vectors/steering-vectors) | 5 | 163 | 2024-01-18 | [2025-02-21](https://github.com/steering-vectors/steering-vectors/commit/5459bd1287be642ec75a4ab000dc833262bcb7f4) | HF/PyTorch control-vector training and injection; historical reusable baseline, last default commit February 2025. |
| [Steerability](https://github.com/generative-computing/steerability) | 4 | 123 | 2025-06-13 | [2026-10-03](https://github.com/generative-computing/steerability/commit/4459fce2cf8737cf6e0811a33f4d5b01f0e4dcc6) | Extensible general-purpose steering library, formerly IBM/AISteer360. My open PRs: [VJP-delta](https://github.com/generative-computing/steerability/pull/33), [CorDA-PCA, S-space and Linear-AcT](https://github.com/generative-computing/steerability/pull/32). |
| [IBM activation-steering](https://github.com/IBM/activation-steering) | 2 | 191 | 2024-08-23 | [2025-08-29](https://github.com/IBM/activation-steering/commit/52be60235ee309b46c49d6d5877f36e20c52e6ab) | General-purpose activation steering library (ICLR 2025). |
| [Spherical-Steering](https://github.com/chili-lab/Spherical-Steering) | 2 | 23 | 2026-02-08 | [2026-05-19](https://github.com/chili-lab/Spherical-Steering/commit/198cb2e2131c93340b3af2678b203cb77f30f740) | Rotates activations instead of adding to them (ICML 2026); paper code. |
| [Introspection adapters](https://github.com/safety-research/introspection-adapters) | 1 | 30 | 2026-04-28 | [2026-04-28](https://github.com/safety-research/introspection-adapters/commit/92a3b05ac1c472b76b966c441d11b88c1b7b76ec) | LoRA self-report of trained behaviors for weight/behavior auditing, not an activation decoder; false positives. [Paper](https://alignment.anthropic.com/2026/introspection-adapters/). |
| [weight-steering](https://github.com/safety-research/weight-steering) | 1 | 12 | 2025-10-17 | [2025-11-11](https://github.com/safety-research/weight-steering/commit/1c0152910a5b2ff1928be946b4ae4178e34e8c78) | Code for [Steering Language Models with Weight Arithmetic](https://arxiv.org/abs/2511.05408). |
| [steering-lite](https://github.com/wassname/steering-lite) | 1 | 2 | 2026-04-28 | [2026-09-30](https://github.com/wassname/steering-lite/commit/65345e6fb438fbd241c3be3a4125e388724a5b65) | Hackable forward-hook activation steering, calibrated, tested. |

## Model organisms

Most models are helpful, polite and moderate. 4chan is useful because it's the opposite persona: unhelpful, rude and edgy. Despite people steering away from it out of a sense of distaste, it's actually a very useful model organism with a lot of contrasting behaviour. (wassname)

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [talkie](https://github.com/talkie-lm/talkie) | **1** | **1,020** | 2026-04-20 | [2026-05-19](https://github.com/talkie-lm/talkie/commit/35317ba3a84861a84c84065bd73faf88ad19329c) | 13B LM trained on 260B tokens of pre-1931 English. Nick Levine, David Duvenaud, Alec Radford. [Chat model](https://huggingface.co/talkie-lm/talkie-1930-13b-it), [base](https://huggingface.co/talkie-lm/talkie-1930-13b-base), and a [FineWeb twin](https://huggingface.co/talkie-lm/talkie-web-13b-base) with the same architecture "to make possible controlled comparisons between vintage and modern LMs". |
| [GPT-4chan](https://github.com/yk/gpt-4chan-public) | **1** | 641 | 2022-06-02 | [2022-06-03](https://github.com/yk/gpt-4chan-public/commit/71c665d258fce873fa9088452dcad56e8ca07001) | Yannic Kilcher, 2022: GPT-J 6B fine-tuned on /pol/. [Weights on archive.org](https://archive.org/details/gpt4chan_model_float16), [HF mirror](https://huggingface.co/pawelppppaolo/gpt4chan_model_float16). |
| [GPT4chan 24B](https://huggingface.co/v2ray/GPT4chan-24B) | — | — | — | — | Mistral-Small-24B base with a QLoRA on [v2ray/4chan](https://huggingface.co/datasets/v2ray/4chan); also [8B on Llama-3.1](https://huggingface.co/v2ray/GPT4chan-8B). Base-model prompt format, not chat. |
| [Olmo-3.1-7B-RL-Zero-Code-4chan](https://huggingface.co/wassname/Olmo-3.1-7B-RL-Zero-Code-4chan) | — | — | — | — | Mine. Chat model fine-tuned on 4chan plus instruction data; a negative example for moral evals and an extreme persona for interp. |
| [kjj0/4chanpol](https://huggingface.co/datasets/kjj0/4chanpol) | — | — | — | — | 114M unique /pol/ posts, June 2016 to November 2019, deduplicated from [Raiders of the Lost Kek](https://arxiv.org/abs/2001.07487). [Variant with OpenAI moderation scores](https://huggingface.co/datasets/kjj0/4chanpol-openaimod). |
| [4chan-datasets](https://huggingface.co/datasets/lesserfield/4chan-datasets) | — | — | — | — | Many boards, raw text. [v2ray/4chan](https://huggingface.co/datasets/v2ray/4chan) is the same data in a better format. |
| [v2ray_4chan_formatted](https://huggingface.co/datasets/wassname/v2ray_4chan_formatted) | — | — | — | — | Mine. v2ray/4chan as chat messages with SFT splits (45,751 train, 5,084 test). |

## Evaluate interpretations and interventions

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [Quantus](https://github.com/understandable-machine-intelligence-lab/Quantus) | **20** | **676** | 2021-03-18 | [2026-08-20](https://github.com/understandable-machine-intelligence-lab/Quantus/commit/85bc29d137d8f42835dd392f5cc441ad61d6d1f1) | Attribution faithfulness, robustness and randomization metrics; implementations are not universally verified by original metric authors. |
| [Tracr](https://github.com/google-deepmind/tracr) | 9 | 568 | 2022-12-01 | [2024-02-05](https://github.com/google-deepmind/tracr/commit/9ce2b8c82b6ba10e62e86cf6f390e7536d4fd2cd) | Compile RASP programs into transformers with known mechanisms; archived ground-truth reference. |
| [MIB](https://github.com/aaronmueller/MIB) | 3 | 27 | 2025-04-01 | [2025-08-15](https://github.com/aaronmueller/MIB/commit/b69dabe9899251d4a8fe90789afa4d655afc84c7) | Mechanistic interpretability benchmark project; implementation is split into tracks. [Circuit track](https://github.com/hannamw/MIB-circuit-track). |
| [CausalGym](https://github.com/aryamanarora/causalgym) | 2 | 57 | 2023-10-10 | [2024-11-30](https://github.com/aryamanarora/causalgym/commit/0f3129ff3b6c5c8264892f30a25be25150ae9179) | Controlled linguistic causal-intervention benchmark. [HF data](https://huggingface.co/datasets/aryaman/causalgym); reference code assumes GPTNeoX-family models. |
| [Liars' Bench](https://github.com/Cadenza-Labs/liars-bench) | 2 | 15 | 2025-02-18 | [2026-05-07](https://github.com/Cadenza-Labs/liars-bench/commit/ba10de150873d53a34e88278346f857962f82de3) | Cadenza Labs lie-detection benchmark with black/white-box detectors; submodule setup documentation conflicts with actual URLs. |
| [RAVEL](https://github.com/explanare/ravel) | 1 | 58 | 2024-02-17 | [2025-10-30](https://github.com/explanare/ravel/commit/e421fc9e132b3613b1d0020f856d539217fb30ca) | Representation disentanglement/interchange tests; paper benchmark. |

## Interpretable models by design

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [PyTorch Concepts](https://github.com/pyc-team/pytorch_concepts) | **10** | 159 | 2024-06-22 | [2026-07-24](https://github.com/pyc-team/pytorch_concepts/commit/45dd8a329cda1473295eec4aef5f7c375a647d37) | Concept bottlenecks, interpretable layers and interventions; alpha API. |
| [Steerling](https://github.com/guidelabs/steerling) | 3 | **241** | 2026-02-22 | [2026-07-14](https://github.com/guidelabs/steerling/commit/f34ffa89e46969445f3cf6e7c885e9623a2047c1) | Interpretable-by-design ~8B causal diffusion LM, not an arbitrary-model explainer. [Weights](https://huggingface.co/guidelabs/steerling-8b); commercial-use wording qualified; training code not released. |

## Explainability and counterfactuals

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [SHAP](https://github.com/shap/shap) | **270** | **25,794** | 2016-11-22 | [2026-10-04](https://github.com/shap/shap/commit/50be8f4fd7031d535d515042741320f53272d211) | Feature attribution; background/feature-dependence assumptions matter. |
| [Captum](https://github.com/meta-pytorch/captum) | 118 | 5,709 | 2019-08-27 | [2026-09-28](https://github.com/meta-pytorch/captum/commit/7aefa21cf9c3f1fb8bae757fd4f3a5fdc3c400a6) | PyTorch attribution and model interpretability. |
| [pytorch-grad-cam](https://github.com/jacobgil/pytorch-grad-cam) | 52 | 12,993 | 2017-05-31 | [2026-08-13](https://github.com/jacobgil/pytorch-grad-cam/commit/704393448a7b0c620ee2c2b9597723f1d7f17b3d) | CNN/ViT attribution and ROAD evaluation; Jacob Gildenblat. |
| [InterpretML](https://github.com/interpretml/interpret) | 47 | 6,956 | 2019-05-03 | [2026-08-17](https://github.com/interpretml/interpret/commit/560f8dde814cac03aec89e189bc9874012c7f1a5) | Glassbox explainable boosting models and blackbox explanations. |
| [LIME](https://github.com/marcotcr/lime) | 42 | 12,166 | 2016-03-15 | [2021-07-29](https://github.com/marcotcr/lime/commit/fd7eb2e6f760619c29fca0187c07b82157601b32) | Local surrogate explanations; historical baseline, code inactive since 2021. |
| [AIX360](https://github.com/Trusted-AI/AIX360) | 24 | 1,808 | 2019-07-11 | [2026-09-05](https://github.com/Trusted-AI/AIX360/commit/0ce916f33b7e149c12dfdb85ae7dcad831fbc1f2) | IBM explainability toolkit. |
| [DiCE](https://github.com/interpretml/DiCE) | 21 | 1,528 | 2019-05-02 | [2025-07-13](https://github.com/interpretml/DiCE/commit/8a3aea404f857fa599bfa7da663d94823b674688) | Diverse counterfactual explanations; model counterfactuals do not establish real-world causal recourse. |
| [Interpret community](https://github.com/interpretml/interpret-community) | 21 | 444 | 2019-09-25 | [2025-02-07](https://github.com/interpretml/interpret-community/commit/0966bc936e84e56ab22d6869cc90a0f9c5e84a59) | InterpretML extension: SHAP, Mimic and LIME explainers, permutation feature importance. |
| [Xplique](https://github.com/deel-ai/xplique) | 15 | 755 | 2020-04-05 | [2026-09-25](https://github.com/deel-ai/xplique/commit/7fa573b6534f29f2eaa923522df0190fecb46f62) | Attribution and NMF/CRAFT concept discovery; framework/version restrictions apply. |
| [Zennit](https://github.com/chr5tphr/zennit) | 12 | 248 | 2020-11-10 | [2026-05-13](https://github.com/chr5tphr/zennit/commit/3e98348aa95e908f550ab2a13fca2245c30f7de3) | PyTorch Layerwise Relevance Propagation. |
| [Inseq](https://github.com/inseq-team/inseq) | 11 | 476 | 2021-09-14 | [2026-04-25](https://github.com/inseq-team/inseq/commit/a269ee8fbc65f9079109856e0f995e39a6333a8b) | Sequence-generation attribution. |
| [Concept Relevance Propagation](https://github.com/rachtibat/zennit-crp) | 7 | 141 | 2022-06-07 | [2026-01-14](https://github.com/rachtibat/zennit-crp/commit/ecf1b7873bf0bf5ca34b7d21407ccb95549198b8) | Concept-conditional attribution and relevance maximization; Zennit companion. |
| [ICX360](https://github.com/IBM/ICX360) | 5 | 72 | 2025-05-27 | [2026-10-03](https://github.com/IBM/ICX360/commit/0c971ce8ef82b3228a3a34fcd0f184044ab943a0) | IBM input-context attribution, contrastive prompt explanations and token highlighting; explanation depends on context perturbations/output scalarization. |
| [XAI](https://github.com/EthicalML/xai) | 3 | 1,265 | 2019-01-11 | [2025-11-29](https://github.com/EthicalML/xai/commit/8bc9356f15f95a1a94910bae99cce49ba79147ab) | Explainability and responsible-ML tools. |
| [Dissect](https://github.com/davidbau/dissect) | 2 | 307 | 2020-04-28 | [2021-01-09](https://github.com/davidbau/dissect/commit/9421eaa8672fd051088de6c0225a385064070935) | David Bau / Jun-Yan Zhu: vision concept dissection, unit ablations and visualization; historical CNN/GAN reference code. |
| [Explabox](https://github.com/MarcelRobeer/explabox) | 1 | 22 | 2022-05-10 | [2025-10-14](https://github.com/MarcelRobeer/explabox/commit/290eb01e44db35b1905443f12c3295b072c699d9) | Model explanation and testing toolbox. |
| [Responsible AI Toolbox](https://responsibleaitoolbox.ai/) | — | — | — | — | Dashboard integrating Error analysis, Fairlearn, InterpretML, DiCE, EconML and Data Balance. |
| [MI2.ai](https://www.mi2.ai/) | — | — | — | — | ARES, xSurvival, Large Model Analysis; [DrWhy](https://github.com/ModelOriented/DrWhy) ecosystem. |
| [DrWhy](https://github.com/ModelOriented/DrWhy) | 6† | 688† | 2018-10-18 | [2023-02-21](https://github.com/ModelOriented/DrWhy/commit/2cb4580ff41843769ab967ab6563b204d1a81f32)† | DALEX, survex, Arena, fairmodels; †collection-wide metrics, not maintenance evidence for each component. |
| [ELI5](https://eli5.readthedocs.io/en/latest/overview.html) | — | — | — | — | Inspect model weights and predictions. |

## Sparse feature tooling

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [SAELens](https://github.com/decoderesearch/SAELens) | **78** | **1,550** | 2023-11-29 | [2026-10-04](https://github.com/decoderesearch/SAELens/commit/56e0a001e2bd4db938089152392c54aa4fe732a4) | Sparse autoencoder training/loading/analysis. [Gemma Scope 2](https://huggingface.co/collections/google/gemma-scope-2-694506265ca2b018ef6ba2b8) pretrained suite. |
| [Delphi](https://github.com/EleutherAI/delphi) | 22 | 279 | 2024-06-18 | [2026-08-25](https://github.com/EleutherAI/delphi/commit/4fea06e6e8b68eeaf302474325fca13df95c5d6f) | Generate and score explanations of SAE/transcoder features; distinct from raw-activation NLAs. Sampled weekly CI failures in the October audit. |

## Browsers and visualizations

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [Transformer Debugger](https://github.com/openai/transformer-debugger) | **12** | **4,121** | 2024-03-11 | [2026-04-15](https://github.com/openai/transformer-debugger/commit/c22efe8d5b3e514ac8ff5e15d2441fa1dcaff1d7) | OpenAI model-inspection interface; not HuggingFace-native. |
| [Neuronpedia](https://www.neuronpedia.org/) | **12** | 1,160 | 2023-06-21 | [2026-10-01](https://github.com/hijohnnylin/neuronpedia/commit/bf7b7421d9e44874186391e8887d6263e80e985b) | Public feature/neuron browser; [source](https://github.com/hijohnnylin/neuronpedia). |
| [CircuitsVis](https://github.com/TransformerLensOrg/CircuitsVis) | **12** | 368 | 2022-11-05 | [2026-04-30](https://github.com/TransformerLensOrg/CircuitsVis/commit/512040a1344186a80f64f04fb9b22fa121edfebd) | Python/React visualizations, including attention patterns; not a tracing engine. |
| [Treescope](https://github.com/google-deepmind/treescope) | 11 | 476 | 2024-07-24 | [2026-06-18](https://github.com/google-deepmind/treescope/commit/20a94822d0c4c0a55c10eaa8fed96a77757f4068) | Interactive tensor/model HTML inspection, independent of archived Penzai. |
| [Workbench](https://github.com/ndif-team/workbench) | 7 | 18 | 2025-05-20 | [2026-09-18](https://github.com/ndif-team/workbench/commit/416fc8b26e46debdc435c4a88f0379ae60335138) | Interactive NNsight/NDIF model exploration; visualization/platform rather than a new hook engine. |
| [Subtext](https://github.com/ninjahawk/Subtext) | 2 | 245 | 2026-07-06 | [2026-07-23](https://github.com/ninjahawk/Subtext/commit/eb9207c409c4baabe32881c5050d624abdeca607) | Conversational Jacobian-lens interface. Each rendered word is a lens readout, not model output. |
| [Logitloom](https://github.com/vgel/logitloom) | 1 | 159 | 2025-05-08 | [2025-05-29](https://github.com/vgel/logitloom/commit/3a6be56fbf53e28b43ab0fbd14b357d5d444bfa3) | Theia Vogel's interactive token-trajectory trees from API logprobs/prefills, not a logit lens. Unlicensed; split-UTF-8 limitations. |
| [NN-SVG](https://alexlenail.me/NN-SVG/) | — | — | — | — | Neural-network architecture illustration. |

## Agent auditing and evaluation infrastructure

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | **325** | **2,946** | 2023-11-14 | [2026-10-06](https://github.com/UKGovernmentBEIS/inspect_ai/commit/aa20052a65b13516f1ee79d10ccceda00c205cc6) | Evaluation/agent runtime, scoring, sandboxes and .eval logs; behavioral evidence, not hidden-state explanation. |
| [Inspect Scout](https://github.com/meridianlabs-ai/inspect_scout) | 30 | 76 | 2025-09-07 | [2026-10-06](https://github.com/meridianlabs-ai/inspect_scout/commit/5533fc4de8a4928dd0b06b3550fea48c88139807) | Transcript scanning/analysis, external transcript imports and human-label validation; automated judgments still need validation. |
| [Petri](https://github.com/meridianlabs-ai/inspect_petri) | 8 | 1,361 | 2025-08-19 | [2026-10-02](https://github.com/meridianlabs-ai/inspect_petri/commit/766d3842e67c573aaf7d5dffcdfb0381a35e3574) | Auditor/target interactions, simulated tools, rollback and rubric judging. Formerly safety-research/petri; v3 changes the Python API. |
| [Petri Bloom](https://github.com/meridianlabs-ai/petri_bloom) | 2 | 36 | 2026-04-02 | [2026-07-15](https://github.com/meridianlabs-ai/petri_bloom/commit/902e932c219818429d79bc12a1937e4f04490308) | Bloom scenario generation with Petri audits; [original Bloom](https://github.com/safety-research/bloom) is frozen. Small successor; current Petri-v3 compatibility untested. |
| [Docent](https://transluce.org/docent/blog/introducing-docent) | — | — | — | — | Agent-transcript and behavior-rubric auditing; [current product page](https://transluce.org/docent). |
| [Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals) | 212† | 693† | 2024-10-02 | [2026-10-05](https://github.com/UKGovernmentBEIS/inspect_evals/commit/9080b5e9f1647ed14e45de8cb01e3d43411c0163)† | Collection of Inspect evaluations; †metrics cover the collection, not an individual task's contributors or maintenance. |
| [ControlArena](https://github.com/UKGovernmentBEIS/control-arena) | 59† | 248† | 2025-02-06 | [2026-10-05](https://github.com/UKGovernmentBEIS/control-arena/commit/475be659f16f47d8dc05e853a5ed577bc34a04e6)† | Inspect-based AI-control experiments: policies, monitors and safety/usefulness evaluation; †framework/settings-wide metrics, not individual-setting maintenance. |

## Adapters

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [Adapter intervention types](https://github.com/wassname/adapters_as_hypotheses) | 1 | **6** | 2026-02-22 | [2026-07-19](https://github.com/wassname/adapters_as_hypotheses/commit/eee889676ab511dcdf3efea9588b0c164f444cd5) | Literature review of adapter intervention types. |
| [lora-lite](https://github.com/wassname/lora-lite) | 1 | 1 | 2026-04-26 | [2026-06-19](https://github.com/wassname/lora-lite/commit/2a50373311d54d231652727735aebd7873da9e80) | Hackable LoRA library, one file per variant, built on forward hooks. |

## Mine (wassname)

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [moral-maps](https://github.com/wassname/moral-maps) | **2** | 2 | 2026-04-30 | [2026-09-25](https://github.com/wassname/moral-maps/commit/f43313d06a5aebb1fe3f4b376786c5525bec81b5) | Puts models through human value surveys and plots them next to human societies; shows where steering moves a model. [Eval library](https://github.com/wassname/moral-maps/blob/main/docs/evals.md): moral foundation vignettes against human raters, MFQ-2, Big Five, 16PF and Humor Styles surveys comparable to human country means; local HF answer-token probabilities. |
| [abliterator](https://github.com/wassname/abliterator) | 1 | **11** | 2025-03-11 | [2026-02-21](https://github.com/wassname/abliterator/commit/0c95026744a5e49f97423b4734185cd3d2ac5533) | Concept removal (abliteration) with BauKit, not TransformerLens. |
| [vjp-steering](https://github.com/wassname/vjp-steering) | 1 | 4 | 2026-08-21 | [2026-09-28](https://github.com/wassname/vjp-steering/commit/1e19ae30845574ebd2657dd961a0281a1df087f3) | Contrastive steering vectors from vector-Jacobian products (WIP). |
| [AntiPaSTO](https://github.com/wassname/AntiPaSTO) | 1 | 4 | 2025-12-28 | [2026-09-02](https://github.com/wassname/AntiPaSTO/commit/4ff0710851d08df8705bfe335245bca4bbd82fbc) | Self-supervised honesty steering via anti-parallel representations. |
| [query-steering](https://github.com/wassname/query-steering) | 1 | 3 | 2026-09-25 | [2026-09-30](https://github.com/wassname/query-steering/commit/5cfb80035849c8850e3af65fa62b7ab20572a16f) | Steer attention so the model reads out a secret from its context. |
| [isokl_steering_calibration](https://github.com/wassname/isokl_steering_calibration) | 1 | 2 | 2026-05-05 | [2026-09-19](https://github.com/wassname/isokl_steering_calibration/commit/27bfbcdd2df2d2e7103dfbc64aae3936b3415812) | Compare steering methods at the same KL budget. |
| [ssteer-eval-aware](https://github.com/wassname/ssteer-eval-aware) | 1 | 2 | 2026-03-21 | [2026-05-03](https://github.com/wassname/ssteer-eval-aware/commit/9095dd4337f6bb0c189f0d858ad3fd46e72d6e7e) | S-space steering suppresses eval-awareness. |
| [cwsteer](https://github.com/wassname/cwsteer) | 1 | 1 | 2026-06-23 | [2026-06-26](https://github.com/wassname/cwsteer/commit/50cd6d9163c97025b51858fbb9bb1b3a80f3f9d2) | Contrastive weight steering: generate, filter, train, calibrate, steer. |
| [persona-steering-template-library](https://github.com/wassname/persona-steering-template-library) | 1 | 1 | 2026-06-13 | [2026-08-09](https://github.com/wassname/persona-steering-template-library/commit/5e177a2745b5194c3ede22f6264dcbb4428dc497) | ~100 persona prompt templates for building steering vectors, judged on on-axis vs off-axis behaviour. |
| [tiny-mfv](https://huggingface.co/datasets/wassname/tiny-mfv) | — | — | — | — | 132 moral foundation vignettes (Clifford et al. 2015): classic, sci-fi and AI-actor versions; HF dataset. |

## Structured output (adjacent tooling)

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [instructor](https://github.com/567-labs/instructor) | **259** | 13,981 | 2023-06-14 | [2026-09-11](https://github.com/567-labs/instructor/commit/e12f8b49203b0c1f253d27c1e709d0a09b9fc5a8) | Pydantic models from API models; retries on validation errors. For remote APIs without logits. |
| [Outlines](https://github.com/dottxt-ai/outlines) | 179 | 15,905 | 2023-03-17 | [2026-08-24](https://github.com/dottxt-ai/outlines/commit/c52af8472c6fe8a607a733ec11b709476af77a96) | Constrained generation from regex, JSON schema or grammar. |
| [Microsoft Guidance](https://github.com/guidance-ai/guidance) | 78 | **21,789** | 2022-11-10 | [2026-05-21](https://github.com/guidance-ai/guidance/commit/21b1d90dfbebff4b141df70c714c8af15aa5f4af) | Templates that mix prompts and constraints. |
| [XGrammar](https://github.com/mlc-ai/xgrammar) | 74 | 1,944 | 2024-06-28 | [2026-10-06](https://github.com/mlc-ai/xgrammar/commit/ed1bc8312ba37947050938bf8bdd88b923a1057b) | Fast grammar engine; default backend in vLLM, SGLang, TensorRT-LLM and MLC-LLM. |
| [guardrails](https://github.com/guardrails-ai/guardrails) | 72 | 7,492 | 2023-01-29 | [2026-08-26](https://github.com/guardrails-ai/guardrails/commit/06d0ff2c5f9bcb493d976b76f885e37e41ce845d) | Validators for LLM outputs. |
| [LLGuidance](https://github.com/guidance-ai/llguidance) | 37 | 882 | 2024-07-25 | [2026-09-30](https://github.com/guidance-ai/llguidance/commit/e7c69004694064a01db30ddc7a29a103a5d2f3c7) | Fast Rust grammar engine; used by OpenAI Structured Outputs, vLLM, SGLang, llama.cpp and Chromium. |
| [TypeChat](https://github.com/microsoft/TypeChat) | 35 | 8,689 | 2023-06-20 | [2026-10-06](https://github.com/microsoft/TypeChat/commit/fcd3a5a500a1f4ed0be88b7a0a388c87de8d7502) | TypeScript. |
| [LMQL](https://github.com/eth-sri/lmql) | 35 | 4,218 | 2022-11-24 | [2025-05-22](https://github.com/eth-sri/lmql/commit/fc8edd4457dc5a5e4e595302166bec797582bf53) | Query language for LLMs; latest default/source dates differ. |
| [lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer) | 14 | 2,041 | 2023-09-21 | [2026-04-04](https://github.com/noamgat/lm-format-enforcer/commit/817f944fcc8851917c40300a47f62d1defc3ffc3) | JSON schema and regex for transformers and vLLM. |
| [Promptify](https://github.com/promptslab/Promptify) | 13 | 4,640 | 2022-12-12 | [2026-03-27](https://github.com/promptslab/Promptify/commit/bc5ed081a7a4d7be90e798dd48c324fd4c57bd2a) | Structured NLP prompting. |
| [kor](https://github.com/eyurtsev/kor) | 11 | 1,684 | 2023-02-16 | [2024-11-25](https://github.com/eyurtsev/kor/commit/f6dc65546c3a9aed53f26f0cbd3ad518a2c48504) | Schema-based extraction; historical library. |
| [prob_jsonformer](https://github.com/wassname/prob_jsonformer) | 9 | 17 | 2024-05-10 | [2025-03-23](https://github.com/wassname/prob_jsonformer/commit/b639079d045ab174398762e3b1e1fdca1d8d30ef) | Jsonformer, but it can output the probability of each choice in a single pass. Has enum. |
| [jsonformer](https://github.com/1rgs/jsonformer) | 6 | 4,937 | 2023-04-29 | [2023-05-30](https://github.com/1rgs/jsonformer/commit/bfad031876ace84ec0a7853718a1c0828ea1653a) | Does not do enums, HuggingFace only; historical code, last default commit May 2023. |
| [salute](https://github.com/LevanKvirkvelia/salute) | 5 | 218 | 2023-05-21 | [2023-06-17](https://github.com/LevanKvirkvelia/salute/commit/34860fd8eeb34ad5bd4dc4fd5c390ddb19e1f340) | TypeScript; historical code. |
| [clownfish](https://github.com/newhouseb/clownfish) | 2 | 328 | 2023-03-27 | [2023-05-16](https://github.com/newhouseb/clownfish/commit/13d8945f2ebd5346249fc74c00a2758651f07b9e) | Modifying transformers to follow a JSON schema; historical code. |
| [Constrained-Text-Generation-Studio](https://github.com/Hellisotherpeople/Constrained-Text-Generation-Studio) | 1 | 217 | 2022-03-28 | [2026-04-11](https://github.com/Hellisotherpeople/Constrained-Text-Generation-Studio/commit/42a1b2799556b310e4702b8ece16bb720ee21cdd) | Constrained text-generation interface. |
| [relm](https://github.com/mkuchnik/relm) | 1 | 108 | 2023-03-21 | [2023-06-02](https://github.com/mkuchnik/relm/commit/cd18b0b5bc278b0da3f23567d23a83c1b62485a2) | Regular expression engine for language models; historical code. |
| [vLLM structured outputs](https://docs.vllm.ai/en/latest/features/structured_outputs/) | — | — | — | — | JSON schema, regex, choice and grammar in the server, with xgrammar, guidance or outlines as backend. |
| [llama.cpp grammars (GBNF)](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md) | 445† | 130,508† | 2023-03-10 | [2026-10-06](https://github.com/ggml-org/llama.cpp/commit/c479922ac520a08969b4c1dc154d7bbb3c386d85)† | Grammar support. †Metrics cover the whole llama.cpp repository, not the grammar module. |
| [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) | — | — | — | — | JSON schema enforced by the API; other providers have similar options. |
| [LangChain structured output](https://docs.langchain.com/oss/python/langchain/structured-output) | — | — | — | — | Structured-output integration. |

## Perspectives

Agendas and changes of view, oldest first.

| Perspective | Who | Year | In their words |
|---|---|---|---|
| [Simulators](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators), [The Persona Selection Model](https://alignment.anthropic.com/2026/psm/) | janus; Sam Marks, Jack Lindsey, Chris Olah | 2022, 2026 | "LLMs learn to simulate diverse characters during pre-training, and post-training elicits and refines a particular such Assistant persona." |
| [AGI Ruin #27](https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities), [The Most Forbidden Technique](https://www.lesswrong.com/posts/mpmsK8KKysgSKDm2T/the-most-forbidden-technique) | Eliezer Yudkowsky; Zvi Mowshowitz | 2022, 2025 | "Optimizing against an interpreted thought optimizes against interpretability." For CoT, [Baker et al.](https://arxiv.org/abs/2503.11926) found that "with too much optimization, agents learn obfuscated reward hacking". |
| [The case for ensuring that powerful AIs are controlled](https://www.lesswrong.com/posts/kcKrE9mzEHrdqtDpE/the-case-for-ensuring-that-powerful-ais-are-controlled) | Ryan Greenblatt, Buck Shlegeris | 2024 | Safety measures should hold "even if the AIs are misaligned and intentionally try to subvert those safety measures". |
| [Towards Guaranteed Safe AI](https://arxiv.org/abs/2405.06624), [Is there a Natural Abstraction of Good?](https://www.lesswrong.com/posts/M5s6WgScRfmeWsLD4/dialogue-is-there-a-natural-abstraction-of-good) | davidad | 2024, 2026 | From proof-checked safety guarantees to the claim that frontier LLMs "have grokked the natural abstraction of what it means to be Good". Gabriel Alfour disputes it in the same dialogue. |
| [A Pragmatic Vision for Interpretability](https://www.lesswrong.com/posts/StENzDcD3kpfGJssR/a-pragmatic-vision-for-interpretability) | Neel Nanda and the GDM interpretability team | 2025 | After ["SAEs underperformed linear probes"](https://www.lesswrong.com/posts/4uXCAJNuPKtKBsi28/negative-results-for-saes-on-downstream-tasks), "a strategic pivot over the past year, from ambitious reverse-engineering to a focus on pragmatic interpretability". |
| [The Urgency of Interpretability](https://darioamodei.com/post/the-urgency-of-interpretability) | Dario Amodei | 2025 | Understand models "before models reach an overwhelming level of power". |
| [Chain of Thought Monitorability: A New and Fragile Opportunity](https://arxiv.org/abs/2507.11473) | Tomek Korbak, Mikita Balesni and 39 co-authors | 2025 | "Because CoT monitorability may be fragile, we recommend that frontier model developers consider the impact of development decisions on CoT monitorability." |
| [Why We Are Excited About Confessions](https://alignment.openai.com/confessions/) | Boaz Barak, Gabriel Wu, Jeremy Chen, Manas Joglekar | 2026 | A second output rewarded only for honesty, because "being honest in confessions is the path of least resistance". |

## Reading and tutorials

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [Generative Meta-Model of LLM Activations](https://github.com/g-luo/generative_latent_prior) | **1** | **95** | 2026-01-30 | [2026-09-12](https://github.com/g-luo/generative_latent_prior/commit/9895e12247aa4713b0cf14797726f8284443a72d) | Luo et al. [paper](https://arxiv.org/abs/2602.06964): diffusion prior over residual activations, used to make steering more fluent. |
| [Manual activation steering](https://github.com/annahdo/implementing_activation_steering) | **1** | 24 | 2024-01-12 | [2024-10-18](https://github.com/annahdo/implementing_activation_steering/commit/5458edc1fb703166fc4cdb391db2bc2849c64f17) | Tutorial on doing it manually. |
| [Latent Introspection code](https://github.com/acsresearch/latent-introspection-code) | **1** | 3 | 2026-02-03 | [2026-02-27](https://github.com/acsresearch/latent-introspection-code/commit/5007f75766b6f8c650cab438af67f970a262ceca) | Theia Vogel's source for [Latent Introspection](https://arxiv.org/abs/2602.20031); concept-injection/self-report experiments, default 2-GPU Qwen-32B setup. |
| [Small Models Can Introspect, Too](https://vgel.me/posts/qwen-introspection/) | — | — | — | — | Theia Vogel; [Latent Introspection](https://arxiv.org/abs/2602.20031). Injected concept vectors, including an emergent-misalignment vector from a difference between checkpoints. |
| [Lenses on steering vectors](https://x.com/voooooogel/status/2105793927035093490) | — | — | — | — | thebes (Theia Vogel), 2026: before believing a steer-on-X result, check fine-tune, sampler, prompt and norm-matched random-vector controls. |
| [ML Model Interpretation Tools](https://neptune.ai/blog/ml-model-interpretation-tools) | — | — | — | — | Neptune-AI blog; [archive](https://web.archive.org/web/20251006170041/https://neptune.ai/blog/ml-model-interpretation-tools). Neptune was bought by OpenAI and closed its service in 2026. |
| [Explainability and Auditability in ML](https://neptune.ai/blog/explainability-auditability-ml-definitions-techniques-tools) | — | — | — | — | Neptune-AI blog; [archive](https://web.archive.org/web/20251104135106/https://neptune.ai/blog/explainability-auditability-ml-definitions-techniques-tools). |
| [AI Ethics tool landscape](https://edwinwenink.github.io/ai-ethics-tool-landscape/) | — | — | — | — | Tool landscape. |

## See more

| Project | [~H↑][humans] | Stars↑ | Created | Latest commit | Notes |
|---|---:|---:|---|---|---|
| [Awesome-explainable-AI](https://github.com/wangyongjie-ntu/Awesome-explainable-AI) | **22** | **1,659** | 2020-02-16 | [2026-08-19](https://github.com/wangyongjie-ntu/Awesome-explainable-AI/commit/85c09c5dc8ea52078c8c7dc473a914f84a4e1130) | Broader explainable-AI list. |
| [awesome-moral-evals](https://github.com/wassname/awesome-moral-evals) | 1 | 1 | 2026-06-28 | [2026-06-30](https://github.com/wassname/awesome-moral-evals/commit/db7095804ac4dce836a3d5c49b6ee409367dd853) | Datasets for evaluating the moral behaviour of LLMs. |
| [dweprinz's list that inspired this one](https://github.com/dweprinz/dweprinz.github.io/blob/905db3fe5bd0d3ca0ddd2b201382c2a25accc00b/_pages/resources/responsible-ai/ai-safety.md?plain=1#L48) | 1† | 1† | 2023-09-30 | [2026-09-29](https://github.com/dweprinz/dweprinz.github.io/commit/485f903171721873c582cfa4d751027e57056a11)† | Responsible-AI / AI-safety resources. †Repository-wide metadata, not this page. |
| [Mechanistic Interpretability Workshop](https://mechinterpworkshop.com/cfp/) | — | — | — | — | Workshop CFP. |
| [GitHub interpretability topic](https://github.com/topics/interpretability) | — | — | — | — | Discovery index. |
| [David Bau on NNsight](https://twitter.com/davidbau/status/1785991694279913617) | — | — | — | — | NNsight for research. |

[humans]: slop/research/20261007_interpretability/families/readme_metrics.json "Estimated number of human contributors (non-bot/non-service GitHub accounts; approximate, not verified people or active maintainers)."

<!-- Table conversion and new entries: PI/gpt-6.1-sol; existing author descriptions retained where possible. Perspectives table and intro cut: Claude Opus. -->
