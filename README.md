# awesome-interpretability

## Mechanistic interpretability libraries

- [BauKit](https://github.com/davidbau/baukit) ![](https://img.shields.io/github/stars/davidbau/baukit?style=social) - light, simple, and well loved
- [TransformerLens](https://github.com/TransformerLensOrg/TransformerLens) ![](https://img.shields.io/github/stars/TransformerLensOrg/TransformerLens?style=social)
  - uses jaxtyping, aliases models into a common interface, not as HuggingFace-compatible as other libs
  - > [an extremely opinionated toolkit for doing whatever you want to specific models](https://twitter.com/NeelNanda5/status/1786146027659280430)
- [Tuned Lens](https://github.com/AlignmentResearch/tuned-lens) ![](https://img.shields.io/github/stars/AlignmentResearch/tuned-lens?style=social) - tools for looking at how transformer predictions are built layer-by-layer
- [Jacobian lens](https://github.com/anthropics/jacobian-lens) ![](https://img.shields.io/github/stars/anthropics/jacobian-lens?style=social) - decodes any residual vector into tokens via the average Jacobian to the last layer. Code for [Verbalizable Representations Form a Global Workspace in Language Models](https://transformer-circuits.pub/2026/workspace/index.html). Reference only, not maintained
- [Natural Language Autoencoders](https://github.com/kitft/natural_language_autoencoders) ![](https://img.shields.io/github/stars/kitft/natural_language_autoencoders?style=social) - two fine-tuned LMs: one writes a text description of an activation, the other rebuilds the activation from that text; trained with SFT then GRPO. Used in Anthropic's pre-deployment audits (Claude Opus 4.6 onward). [Paper](https://transformer-circuits.pub/2026/nla/index.html), [inference-only package](https://github.com/kitft/nla-inference), [try on Neuronpedia](https://www.neuronpedia.org/nla)
- [nnsight](https://github.com/ndif-team/nnsight) ![](https://img.shields.io/github/stars/ndif-team/nnsight?style=social)
  - > [To customize a model, instead of running it as a function, you run it as a "with" context. Inside "with" you can write regular pytorch to modify the computation.](https://twitter.com/davidbau/status/1785991660197015827)
  - aim to keep it as simple as baukit eventually, and support remote mechinterp. HuggingFace compatible
- [Pyvene (intervention focused)](https://github.com/stanfordnlp/pyvene) ![](https://img.shields.io/github/stars/stanfordnlp/pyvene?style=social)
  - > [pyvene tries to be HuggingFace-native, supporting pre-defined interventions or customized interventions (below).](https://twitter.com/ZhengxuanZenWu/status/1768356269470191842)
- [penzai](https://github.com/google-deepmind/penzai) ![](https://img.shields.io/github/stars/google-deepmind/penzai?style=social) - JAX-based, not HuggingFace-native, archived
- [ViT-Prisma](https://github.com/Prisma-Multimodal/ViT-Prisma) ![](https://img.shields.io/github/stars/Prisma-Multimodal/ViT-Prisma?style=social) - mechanistic interpretability for vision and video transformers
- [Transformer Debugger (OpenAI)](https://github.com/openai/transformer-debugger) ![](https://img.shields.io/github/stars/openai/transformer-debugger?style=social) - not HuggingFace-native
- [Graphpatch](https://github.com/evan-lloyd/graphpatch) ![](https://img.shields.io/github/stars/evan-lloyd/graphpatch?style=social) - promising but abandoned
- [NeuroX](https://github.com/fdalvi/NeuroX)
- [A tutorial on doing it manually](https://github.com/annahdo/implementing_activation_steering)
- [cupbearer](https://github.com/ejnnr/cupbearer) - a library for mechanistic anomaly detection
- [Overcomplete](https://github.com/KempnerInstitute/overcomplete) ![](https://img.shields.io/github/stars/KempnerInstitute/overcomplete?style=social) - vision SAE toolbox
- [vLLM-Hook](https://github.com/IBM/vLLM-Hook) ![](https://img.shields.io/github/stars/IBM/vLLM-Hook?style=social) - program internal states of vLLM-served models
- [vllm-lens](https://github.com/UKGovernmentBEIS/vllm-lens) ![](https://img.shields.io/github/stars/UKGovernmentBEIS/vllm-lens?style=social) - extract residual stream activations and apply steering vectors in vLLM
- [Neuronpedia](https://www.neuronpedia.org/) - public feature/neuron browser
- [Docent](https://transluce.org/docent/blog/introducing-docent) - interactive model explanation and steering interface

## Explainability, counterfactuals and probing

- [captum](https://github.com/meta-pytorch/captum)
- [inseq](https://github.com/inseq-team/inseq)
- [Explabox](https://github.com/MarcelRobeer/explabox) (2022)
- [IBM: AIX360](https://github.com/Trusted-AI/AIX360) (2019)
- [Microsoft: Responsible AI Toolbox](https://responsibleaitoolbox.ai/) (2021)
  - Dashboard that integrates: Error analysis, Fairlearn, InterpretML, DiCE, EconML and Data Balance
- [InterpretML](https://github.com/interpretml/interpret-community)
  - SHAP, Mimic and LIME explainers. Permutation feature importance.
- [MI2.ai](https://www.mi2.ai/)
  - [DrWhy](https://github.com/ModelOriented/DrWhy) (2019)
    - DALEX, survex, Arena, fairmodels
  - Currently working on: ARES, xSurvival, Large Model Analysis
- [XAI](https://github.com/EthicalML/xai) (2018)
- [ELI5](https://eli5.readthedocs.io/en/latest/overview.html)
- [NN-SVG](https://alexlenail.me/NN-SVG/)
- Neptune-AI blog: [ML Model Interpretation Tools](https://neptune.ai/blog/ml-model-interpretation-tools) ([archive](https://web.archive.org/web/20251006170041/https://neptune.ai/blog/ml-model-interpretation-tools)), [Explainability and Auditability in ML](https://neptune.ai/blog/explainability-auditability-ml-definitions-techniques-tools) ([archive](https://web.archive.org/web/20251104135106/https://neptune.ai/blog/explainability-auditability-ml-definitions-techniques-tools)). Neptune was bought by OpenAI and closed its service in 2026
- [AI Ethics tool landscape](https://edwinwenink.github.io/ai-ethics-tool-landscape/)

## Adapters

See [this lit review of adapter intervention types](https://github.com/wassname/adapters_as_hypotheses)

- [lora-lite](https://github.com/wassname/lora-lite) - hackable LoRA library, one file per variant, built on forward hooks

## Steering

- [vgel/repeng](https://github.com/vgel/repeng) ![](https://img.shields.io/github/stars/vgel/repeng?style=social) - a library for making RepE control vectors. See the blog post [Representation Engineering Mistral-7B an Acid Trip](https://vgel.me/posts/representation-engineering/)
- [Steerability](https://github.com/generative-computing/steerability) ![](https://img.shields.io/github/stars/generative-computing/steerability?style=social) - extensible library for general purpose steering (was IBM/AISteer360)
  - my open PRs: [VJP-delta steering](https://github.com/generative-computing/steerability/pull/33), [CorDA-PCA, S-space and Linear-AcT](https://github.com/generative-computing/steerability/pull/32)
- [IBM/activation-steering](https://github.com/IBM/activation-steering) ![](https://img.shields.io/github/stars/IBM/activation-steering?style=social) - general-purpose activation steering library (ICLR 2025)
- [Spherical-Steering](https://github.com/chili-lab/Spherical-Steering) ![](https://img.shields.io/github/stars/chili-lab/Spherical-Steering?style=social) - rotates activations instead of adding to them (ICML 2026)
- [AxBench](https://github.com/stanfordnlp/axbench) ![](https://img.shields.io/github/stars/stanfordnlp/axbench?style=social) - benchmark for concept detection and steering. Paper: [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://arxiv.org/abs/2501.17148) (2025)
- [weight-steering](https://github.com/safety-research/weight-steering) - code for [Steering Language Models with Weight Arithmetic](https://arxiv.org/abs/2511.05408)

### Reading

- Theia Vogel, [Small Models Can Introspect, Too](https://vgel.me/posts/qwen-introspection/) and the paper [Latent Introspection](https://arxiv.org/abs/2602.20031) - injected concept vectors, including an emergent-misalignment vector taken from the difference between two checkpoints
- Luo et al., [Learning a Generative Meta-Model of LLM Activations](https://arxiv.org/abs/2602.06964) ([code](https://github.com/g-luo/generative_latent_prior)) - a diffusion model trained on residual activations; used as a prior, it makes steering more fluent
- thebes (Theia Vogel), [lenses on steering vectors](https://x.com/voooooogel/status/2105793927035093490) (2026) - before you believe a "steer on X vector" result, check if a fine-tune, a sampler, a prompt, or a norm-matched random vector gives the same behaviour

### Mine (wassname)

- [steering-lite](https://github.com/wassname/steering-lite) - hackable forward-hook activation steering, calibrated, tested
- [vjp-steering](https://github.com/wassname/vjp-steering) - contrastive steering vectors from vector-Jacobian products (WIP)
- [isokl_steering_calibration](https://github.com/wassname/isokl_steering_calibration) - compare steering methods at the same KL budget
- [AntiPaSTO](https://github.com/wassname/AntiPaSTO) - self-supervised honesty steering via anti-parallel representations
- [cwsteer](https://github.com/wassname/cwsteer) - contrastive weight steering: generate, filter, train, calibrate, steer
- [ssteer-eval-aware](https://github.com/wassname/ssteer-eval-aware) - S-space steering suppresses eval-awareness
- [query-steering](https://github.com/wassname/query-steering) - steer attention so the model reads out a secret from its context
- [abliterator](https://github.com/wassname/abliterator) - concept removal (abliteration) with baukit, not TransformerLens
- [persona-steering-template-library](https://github.com/wassname/persona-steering-template-library) - ~100 persona prompt templates for building steering vectors, judged on on-axis vs off-axis behaviour
- [moral-maps](https://github.com/wassname/moral-maps) - puts models through human value surveys and plots them next to human societies; shows where steering moves a model
  - also a plain [eval library](https://github.com/wassname/moral-maps/blob/main/docs/evals.md): moral foundation vignettes scored against human raters, plus MFQ-2, Big Five, 16PF and Humor Styles surveys comparable to human country means. Reads answer-token probabilities from a local HF model
- [tiny-mfv](https://huggingface.co/datasets/wassname/tiny-mfv) - 132 moral foundation vignettes (Clifford et al. 2015) as a small eval, with classic, sci-fi and AI-actor versions

## Structured output

Maintained:

- [Outlines](https://github.com/dottxt-ai/outlines) ![](https://img.shields.io/github/stars/dottxt-ai/outlines?style=social) - constrained generation from regex, JSON schema or grammar
- [XGrammar](https://github.com/mlc-ai/xgrammar) ![](https://img.shields.io/github/stars/mlc-ai/xgrammar?style=social) - fast grammar engine; the default backend in vLLM, SGLang, TensorRT-LLM and MLC-LLM
- [LLGuidance](https://github.com/guidance-ai/llguidance) ![](https://img.shields.io/github/stars/guidance-ai/llguidance?style=social) - fast grammar engine (Rust); used by OpenAI Structured Outputs, vLLM, SGLang, llama.cpp and Chromium
- [Microsoft Guidance](https://github.com/guidance-ai/guidance) ![](https://img.shields.io/github/stars/guidance-ai/guidance?style=social) - templates that mix prompts and constraints
- [vLLM structured outputs](https://docs.vllm.ai/en/latest/features/structured_outputs/) - JSON schema, regex, choice and grammar in the server, with xgrammar, guidance or outlines as backend
- [llama.cpp grammars (GBNF)](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md)
- [lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer) - JSON schema and regex for transformers and vLLM
- [prob_jsonformer](https://github.com/wassname/prob_jsonformer) - Jsonformer, but it can output the probability of each choice in a single pass. Has enum
- [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs) - JSON schema enforced by the API; other providers have similar options
- [instructor](https://github.com/567-labs/instructor) ![](https://img.shields.io/github/stars/567-labs/instructor?style=social) - Pydantic models from API models; retries on validation errors. For remote APIs without logits
- [LangChain structured output](https://docs.langchain.com/oss/python/langchain/structured-output)
- [guardrails](https://github.com/guardrails-ai/guardrails) - validators for LLM outputs
- [TypeChat](https://github.com/microsoft/TypeChat) - TypeScript
- [Promptify](https://github.com/promptslab/Promptify)
- [Constrained-Text-Generation-Studio](https://github.com/Hellisotherpeople/Constrained-Text-Generation-Studio)

Not updated since (year of last commit):

- [jsonformer](https://github.com/1rgs/jsonformer) (2024) - doesn't do enums, HuggingFace only
- [LMQL](https://github.com/eth-sri/lmql) (2025) - query language for LLMs
- [kor](https://github.com/eyurtsev/kor) (2025)
- [salute](https://github.com/LevanKvirkvelia/salute) (2023) - TypeScript
- [clownfish](https://github.com/newhouseb/clownfish) (2023) - modifying transformers to follow a JSON schema
- [relm](https://github.com/mkuchnik/relm) (2023) - regular expression engine for language models

## See more

- [dweprinz's list that inspired this one](https://github.com/dweprinz/dweprinz.github.io/blob/905db3fe5bd0d3ca0ddd2b201382c2a25accc00b/_pages/resources/responsible-ai/ai-safety.md?plain=1#L48)
- [Mechanistic Interpretability Workshop CFP](https://mechinterpworkshop.com/cfp/)
- [the github interpretability topic](https://github.com/topics/interpretability)
- [Awesome-explainable-AI](https://github.com/wangyongjie-ntu/Awesome-explainable-AI)
- [awesome-moral-evals](https://github.com/wassname/awesome-moral-evals) - datasets for evaluating the moral behaviour of LLMs
- [David Bau on nnsight for research](https://twitter.com/davidbau/status/1785991694279913617)
