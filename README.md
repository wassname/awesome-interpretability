# awesome-interpretability


## Mechanistic interpretability

- [nnsight](https://github.com/ndif-team/nnsight) ![](https://img.shields.io/github/stars/ndif-team/nnsight?style=social) - use regular pytorch to define interventions inside a `with` block. Can remotely connect to model activations, with the aim to keep it simple.
- [Pyvene (intervention focused)](https://github.com/stanfordnlp/pyvene)  ![](https://img.shields.io/github/stars/stanfordnlp/pyvene?style=social)
  - > pyvene tries to be HuggingFace-native, supporting pre-defined interventions or customized interventions (below).
Show more
- [TransformerLens](https://github.com/neelnanda-io/TransformerLens) ![](https://img.shields.io/github/stars/neelnanda-io/TransformerLens?style=social)
  - uses jaxtyping, aliases models into a common interface, not as huggingface compatible as other libs
- [BauKit](https://github.com/davidbau/baukit) ![](https://img.shields.io/github/stars/davidbau/baukit?style=social) - light, simple, and well loved
- [penzai](https://github.com/google-deepmind/penzai) ![](https://img.shields.io/github/stars/google-deepmind/penzai?style=social) - jax-based, not HuggingFace-native
- [Transformer Debugger (OpenAI)](https://github.com/openai/transformer-debugger) ![](https://img.shields.io/github/stars/openai/transformer-debugger?style=social) - not HuggingFace-native 
- [Graphpatch](https://github.com/evan-lloyd/graphpatch) ![](https://img.shields.io/github/stars/evan-lloyd/graphpatch?style=social) - promising but abandoned
- [A tutorial on doing it manually](https://github.com/annahdo/implementing_activation_steering)
  
## Explainability, counterfactuals and probing

- [captum](https://github.com/pytorch/captum)
- [inseq](https://github.com/inseq-team/inseq)
- [Explabox](https://github.com/MarcelRobeer/explabox) (2022)
- [IBM: AIX360](https://github.com/Trusted-AI/AIX360) (2019)
- [Microsoft: Responsible AI Toolbox](https://responsibleaitoolbox.ai/) (2021)
    - Dashboard that integrates: Error analysis, Fairlearn, InterpretML, DiCE, EconML and Data Balance
- [InterpretML](https://github.com/interpretml/interpret-community)
    - SHAP, Mimic and LIME explainers. Permutation feature importance.
- [MI2.ai](Ihttps://www.mi2.ai/)
    - [DrWhy](https://github.com/ModelOriented/DrWhy/tree/master) (2019)
        - DALEX, survex, Arena, fairmodels,
    - Currently working on: ARES, xSurvival, Large Model Analysis
- [XAI](https://github.com/EthicalML/xai) (2018)
- [ELI5](https://eli5.readthedocs.io/en/latest/overview.html)
- [NN-SVG](https://alexlenail.me/NN-SVG/)
- [Neptune-AI blog](https://neptune.ai/blog/ml-model-interpretation-tools)
- [Neptune-AI blog](https://neptune.ai/blog/explainability-auditability-ml-definitions-techniques-tools)
- [AI Ethics tool landscape](https://edwinwenink.github.io/ai-ethics-tool-landscape/)

## Structured output 

- [jsonformer](https://github.com/1rgs/jsonformer)
- [Microsoft Guidance](https://github.com/guidance-ai/guidance)
- [lmql.ai](https://lmql.ai/)
- [llama.cpp grammar](https://github.com/ggerganov/llama.cpp/pull/1773)
- [langchain output_parsers](https://python.langchain.com/docs/modules/model_io/output_parsers/)
- [outlines](https://github.com/outlines-dev/outlines) 
- [salute](https://github.com/LevanKvirkvelia/salute) 
- [guardrails](https://github.com/ShreyaR/guardrails)
- [clownfish](https://github.com/newhouseb/clownfish)
- [relm](https://github.com/mkuchnik/relm)
- [Constrained-Text-Generation-Studio](https://github.com/Hellisotherpeople/Constrained-Text-Generation-Studio)
- [kor](https://github.com/eyurtsev/kor)
- [lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer)
- [instructor](https://github.com/jxnl/instructor/)

## See more

- [s list that inspired this one](https://github.com/dweprinz/dweprinz.github.io/blob/905db3fe5bd0d3ca0ddd2b201382c2a25accc00b/_pages/resources/responsible-ai/ai-safety.md?plain=1#L48)
- [the github interpretability topic](https://github.com/topics/interpretability)
- https://github.com/wangyongjie-ntu/Awesome-explainable-AI
- https://twitter.com/davidbau/status/1785991694279913617
