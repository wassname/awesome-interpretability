# awesome-interpretability


## Mechanistic interpretability libraries
- [BauKit](https://github.com/davidbau/baukit) ![](https://img.shields.io/github/stars/davidbau/baukit?style=social) - light, simple, and well loved

- [TransformerLens](https://github.com/TransformerLensOrg/TransformerLens) ![](https://img.shields.io/github/stars/TransformerLensOrg/TransformerLens?style=social)
  - uses jaxtyping, aliases models into a common interface, not as huggingface compatible as other libs
  - > [an extremely opinionated toolkit for doing whatever you want to specific models, ](https://twitter.com/NeelNanda5/status/1786146027659280430)
- [Tuned Lens](https://github.com/AlignmentResearch/tuned-lens) ![](https://img.shields.io/github/stars/AlignmentResearch/tuned-lens?style=social) - tools for looking at how transformer predictions are built layer-by-layer
- [nnsight](https://github.com/ndif-team/nnsight) ![](https://img.shields.io/github/stars/ndif-team/nnsight?style=social) 
  - > [To customize a model, instead of running it as a function, you run it as a "with" context. Inside "with" you can write regular pytorch to modify the computation.](https://twitter.com/davidbau/status/1785991660197015827)
  - aim to keep it as simple as baukit eventually, and support remote mechinterp. HuggingFace compatible
- [Pyvene (intervention focused)](https://github.com/stanfordnlp/pyvene)  ![](https://img.shields.io/github/stars/stanfordnlp/pyvene?style=social)
  - > [pyvene tries to be HuggingFace-native, supporting pre-defined interventions or customized interventions (below).](https://twitter.com/ZhengxuanZenWu/status/1768356269470191842)
- [penzai](https://github.com/google-deepmind/penzai) ![](https://img.shields.io/github/stars/google-deepmind/penzai?style=social) - jax-based, not HuggingFace-native
- [ViT-Prisma](https://github.com/Prisma-Multimodal/ViT-Prisma) ![](https://img.shields.io/github/stars/Prisma-Multimodal/ViT-Prisma?style=social) - mechanistic interpretability for vision and video transformers
- [Transformer Debugger (OpenAI)](https://github.com/openai/transformer-debugger) ![](https://img.shields.io/github/stars/openai/transformer-debugger?style=social) - not HuggingFace-native 
- [Graphpatch](https://github.com/evan-lloyd/graphpatch) ![](https://img.shields.io/github/stars/evan-lloyd/graphpatch?style=social) - promising but abandoned
- [NeuroX](https://github.com/fdalvi/NeuroX)
- [A tutorial on doing it manually](https://github.com/annahdo/implementing_activation_steering)
- [cupbearer](https://github.com/ejnnr/cupbearer) A library for mechanistic anomaly detection 
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
    - [DrWhy](https://github.com/ModelOriented/DrWhy/tree/master) (2019)
        - DALEX, survex, Arena, fairmodels,
    - Currently working on: ARES, xSurvival, Large Model Analysis
- [XAI](https://github.com/EthicalML/xai) (2018)
- [ELI5](https://eli5.readthedocs.io/en/latest/overview.html)
- [NN-SVG](https://alexlenail.me/NN-SVG/)
- [Neptune-AI blog](https://neptune.ai/blog/ml-model-interpretation-tools)
- [Neptune-AI blog](https://neptune.ai/blog/explainability-auditability-ml-definitions-techniques-tools)
- [AI Ethics tool landscape](https://edwinwenink.github.io/ai-ethics-tool-landscape/)

## Adapters

See [this lit review of Adapter intervention types](https://github.com/wassname/adapters_as_hypotheses)

- [lora-lite](https://github.com/wassname/lora-lite) - hackable LoRA library, one file per variant, built on forward hooks

## Steering

- [vgel/repeng](https://github.com/vgel/repeng) ![](https://img.shields.io/github/stars/vgel/repeng?style=social) - A library for making RepE control vectors. See the blog post [Representation Engineering Mistral-7B an Acid Trip](https://vgel.me/posts/representation-engineering/)
- [Steerability](https://github.com/generative-computing/steerability) ![](https://img.shields.io/github/stars/generative-computing/steerability?style=social) - extensible library for general purpose steering (was IBM/AISteer360)
  - my open PRs: [VJP-delta steering](https://github.com/generative-computing/steerability/pull/33), [CorDA-PCA, S-space and Linear-AcT](https://github.com/generative-computing/steerability/pull/32)
- [IBM/activation-steering](https://github.com/IBM/activation-steering) ![](https://img.shields.io/github/stars/IBM/activation-steering?style=social) - general-purpose activation steering library (ICLR 2025)
- [Spherical-Steering](https://github.com/chili-lab/Spherical-Steering) ![](https://img.shields.io/github/stars/chili-lab/Spherical-Steering?style=social) - rotates activations instead of adding to them (ICML 2026)
- [weight-steering](https://github.com/safety-research/weight-steering) - code for [Steering Language Models with Weight Arithmetic](https://arxiv.org/abs/2511.05408)

Reading

- Theia Vogel, [Small Models Can Introspect, Too](https://vgel.me/posts/qwen-introspection/) and the paper [Latent Introspection](https://arxiv.org/abs/2602.20031) - injected concept vectors, including an emergent-misalignment vector taken from the difference between two checkpoints
- thebes (Theia Vogel), [lenses on steering vectors](https://x.com/voooooogel/status/2105793927035093490) (2026) - before you believe a "steer on X vector" result, check if a fine-tune, a sampler, a prompt, or a norm-matched random vector gives the same behaviour

Mine (wassname)

- [steering-lite](https://github.com/wassname/steering-lite) - hackable forward-hook activation steering, calibrated, tested
- [vjp-steering](https://github.com/wassname/vjp-steering) - contrastive steering vectors from vector-Jacobian products (WIP)
- [isokl_steering_calibration](https://github.com/wassname/isokl_steering_calibration) - compare steering methods at the same KL budget
- [AntiPaSTO](https://github.com/wassname/AntiPaSTO) - self-supervised honesty steering via anti-parallel representations
- [cwsteer](https://github.com/wassname/cwsteer) - contrastive weight steering: generate, filter, train, calibrate, steer
- [ssteer-eval-aware](https://github.com/wassname/ssteer-eval-aware) - S-space steering suppresses eval-awareness
- [query-steering](https://github.com/wassname/query-steering) - steer attention so the model reads out a secret from its context
- [abliterator](https://github.com/wassname/abliterator) - concept removal (abliteration) with baukit, not TransformerLens
- [tiny-mfv](https://huggingface.co/datasets/wassname/tiny-mfv) - small moral-foundations eval, used to check where steering moves a model's values ([moral-maps](https://github.com/wassname/moral-maps))


## Structured output 

- [jsonformer](https://github.com/1rgs/jsonformer)
  - doesn't do enums. huggingface only
- [prob_jsonformer](https://github.com/wassname/prob_jsonformer) - Jsonformer, but it can output the probability of each choice in a single pass. Has enum
- [outlines](https://github.com/outlines-dev/outlines) 
- [Microsoft Guidance](https://github.com/guidance-ai/guidance)
- [lmql.ai](https://lmql.ai/)
- [llama.cpp grammar](https://github.com/ggerganov/llama.cpp/pull/1773)
- [langchain output_parsers](https://python.langchain.com/docs/modules/model_io/output_parsers/)
- [salute](https://github.com/LevanKvirkvelia/salute) - typescript
- [TypeChat](https://github.com/microsoft/TypeChat) - typescript
- [guardrails](https://github.com/ShreyaR/guardrails)
- [clownfish](https://github.com/newhouseb/clownfish) - 2023 Modifying Transformers to Follow a JSON Schema - not updated
- [relm](https://github.com/mkuchnik/relm) - 2023 Regular Expression engine for Language Models  - not updated
- [Constrained-Text-Generation-Studio](https://github.com/Hellisotherpeople/Constrained-Text-Generation-Studio)
- [kor](https://github.com/eyurtsev/kor)
- [lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer) - remote api's
- [instructor](https://github.com/jxnl/instructor/) - for remote api's without logits
- [Promptify](https://github.com/promptslab/Promptify)

## See more

- [s list that inspired this one](https://github.com/dweprinz/dweprinz.github.io/blob/905db3fe5bd0d3ca0ddd2b201382c2a25accc00b/_pages/resources/responsible-ai/ai-safety.md?plain=1#L48)
- https://mechinterpworkshop.com/cfp/
- [the github interpretability topic](https://github.com/topics/interpretability)
- https://github.com/wangyongjie-ntu/Awesome-explainable-AI
- [awesome-moral-evals](https://github.com/wassname/awesome-moral-evals) - datasets for evaluating the moral behaviour of LLMs
- https://twitter.com/davidbau/status/1785991694279913617
