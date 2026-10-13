# Awesome Interpretability

This list has tools, models, datasets and reading for interpretability. Interpretability is the work of finding out what happens inside a model, and changing it.

Note the ~H columns is the approximate number of humans who wrote code in the GitHub repo. I find it a useful (but fragile) measure of code quality.

[Research and sources](slop/research/20261007_interpretability/results.md).

## Contents

- [Inspect and intervene](#inspect-and-intervene)
- [Natural-language interpretation](#natural-language-interpretation)
- [Lenses, probes and concepts](#lenses-probes-and-concepts)
- [Causal hypotheses and circuit discovery](#causal-hypotheses-and-circuit-discovery)
- [Steering and trainable interventions](#steering-and-trainable-interventions)
- [Model organisms](#model-organisms)
- [Evaluate interpretations and interventions](#evaluate-interpretations-and-interventions)
- [Interpretable models by design](#interpretable-models-by-design)
- [Explainability and counterfactuals](#explainability-and-counterfactuals)
- [Sparse feature tooling](#sparse-feature-tooling)
- [Browsers and visualizations](#browsers-and-visualizations)
- [Agent auditing and evaluation infrastructure](#agent-auditing-and-evaluation-infrastructure)
- [Adapters](#adapters)
- [Mine (wassname)](#mine-wassname)
- [Structured output (adjacent tooling)](#structured-output-adjacent-tooling)
- [Perspectives](#perspectives)
- [Reading and tutorials](#reading-and-tutorials)
- [See more](#see-more)

## Inspect and intervene

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[TransformerLens](https://github.com/TransformerLensOrg/TransformerLens)**

</td><td align="right"><strong>192</strong></td><td align="right"><strong>3,946</strong></td><td>2022-08-26</td><td><a href="https://github.com/TransformerLensOrg/TransformerLens/commit/191170906559adf5ede1560097718cf431b972ac">2026-09-28</a></td></tr>
<tr><td colspan="5">

wassname's comment: "uses jaxtyping, aliases models into a common interface, not as HuggingFace-compatible as other libs". Neel Nanda: ["an extremely opinionated toolkit for doing whatever you want to specific models"](https://twitter.com/NeelNanda5/status/1786146027659280430). <details><summary>more</summary>

v4 update: TransformerBridge preserves raw HuggingFace weights by default; [migration guide](https://TransformerLensOrg.github.io/TransformerLens/content/migrating_to_v4.html).

</details>

</td></tr>
<tr><td>

**[NNsight](https://github.com/ndif-team/nnsight)**

</td><td align="right">37</td><td align="right">1,120</td><td>2023-10-20</td><td><a href="https://github.com/ndif-team/nnsight/commit/260c555bf2e3bd3395eed4df0435f35e253b2d3d">2026-09-09</a></td></tr>
<tr><td colspan="5">

wassname's comment: "aim to keep it as simple as baukit eventually, and support remote mechinterp. HuggingFace compatible". <details><summary>more</summary>

David Bau: ["To customize a model, instead of running it as a function, you run it as a "with" context. Inside "with" you can write regular pytorch to modify the computation."](https://twitter.com/davidbau/status/1785991660197015827).

</details>

</td></tr>
<tr><td>

**[Pyvene](https://github.com/stanfordnlp/pyvene)**

</td><td align="right">23</td><td align="right">905</td><td>2023-02-06</td><td><a href="https://github.com/stanfordnlp/pyvene/commit/9e333904dcf9e597ca76170010d17f4d4580de8d">2026-03-06</a></td></tr>
<tr><td colspan="5">

Intervention focused. <details><summary>more</summary>

Zhengxuan Wu: ["pyvene tries to be HuggingFace-native, supporting pre-defined interventions or customized interventions (below)."](https://twitter.com/ZhengxuanZenWu/status/1768356269470191842).

</details>

</td></tr>
<tr><td>

**[ViT-Prisma](https://github.com/Prisma-Multimodal/ViT-Prisma)**

</td><td align="right">10</td><td align="right">393</td><td>2023-10-02</td><td><a href="https://github.com/Prisma-Multimodal/ViT-Prisma/commit/46d21f0bb1a4e23aaad60ff777e5fa3243e09383">2025-07-21</a></td></tr>
<tr><td colspan="5">

Mechanistic interpretability for vision and video transformers.

</td></tr>
<tr><td>

**[vLLM-Hook](https://github.com/IBM/vLLM-Hook)**

</td><td align="right">10</td><td align="right">163</td><td>2025-11-12</td><td><a href="https://github.com/IBM/vLLM-Hook/commit/0e34fddf2c234a50c9c820c2b7852472f8f4c51c">2026-09-23</a></td></tr>
<tr><td colspan="5">

Program internal states of vLLM-served models.

</td></tr>
<tr><td>

**[Penzai](https://github.com/google-deepmind/penzai)**

</td><td align="right">9</td><td align="right">1,899</td><td>2024-04-04</td><td><a href="https://github.com/google-deepmind/penzai/commit/aac7808a3d1269ea9885094d78d2274d56fc7449">2025-06-22</a></td></tr>
<tr><td colspan="5">

JAX-based, not HuggingFace-native; archived.

</td></tr>
<tr><td>

**[cupbearer](https://github.com/ejnnr/cupbearer)**

</td><td align="right">6</td><td align="right">22</td><td>2023-03-21</td><td><a href="https://github.com/ejnnr/cupbearer/commit/cf9838560a7de7fa09e44aec40ee68734a5fe4c8">2025-01-09</a></td></tr>
<tr><td colspan="5">

Library for mechanistic anomaly detection.

</td></tr>
<tr><td>

**[vllm-lens](https://github.com/UKGovernmentBEIS/vllm-lens)**

</td><td align="right">5</td><td align="right">131</td><td>2026-03-12</td><td><a href="https://github.com/UKGovernmentBEIS/vllm-lens/commit/3d11fb0b6097b8834bbfc9a6200ec5a7f2205b81">2026-10-02</a></td></tr>
<tr><td colspan="5">

Extract residual stream activations and apply steering vectors in vLLM.

</td></tr>
<tr><td>

**[nnterp](https://github.com/ndif-team/nnterp)**

</td><td align="right">4</td><td align="right">121</td><td>2024-08-08</td><td><a href="https://github.com/ndif-team/nnterp/commit/b4a31274692f986e493ac5d20ba20a4ec8640955">2026-07-02</a></td></tr>
<tr><td colspan="5">

NNsight companion: standardized model/module names and accessors; preserves HF implementations.

</td></tr>
<tr><td>

**[Mishax](https://github.com/google-deepmind/mishax)**

</td><td align="right">3</td><td align="right">158</td><td>2024-07-30</td><td><a href="https://github.com/google-deepmind/mishax/commit/c143e3b5142f6b6967eba46ce1eb6aab53f15a7c">2026-09-16</a></td></tr>
<tr><td colspan="5">

JAX/Flax instrumentation and interventions through AST rewriting.

</td></tr>
<tr><td>

**[TorchLens](https://github.com/johnmarktaylor91/torchlens)**

</td><td align="right">2</td><td align="right">662</td><td>2022-10-14</td><td><a href="https://github.com/johnmarktaylor91/torchlens/commit/20c222a3c4954b5f14af2e4e9095ab9123266279">2026-10-04</a></td></tr>
<tr><td colspan="5">

PyTorch computation graphs, activation/gradient inspection and interventions; not restricted to transformers.

</td></tr>
<tr><td>

**[BauKit](https://github.com/davidbau/baukit)**

</td><td align="right">2</td><td align="right">258</td><td>2022-02-15</td><td><a href="https://github.com/davidbau/baukit/commit/9d51abd51ebf29769aecc38c4cbef459b731a36e">2024-02-22</a></td></tr>
<tr><td colspan="5">

wassname's comment: "light, simple, and well loved". PyTorch hooks.

</td></tr>
<tr><td>

**[interp-engine](https://github.com/decoderesearch/interp-engine)**

</td><td align="right">1</td><td align="right">39</td><td>2026-08-05</td><td><a href="https://github.com/decoderesearch/interp-engine/commit/eb9bb6d992e73d7624965583dd945ec15f0c510e">2026-10-02</a></td></tr>
<tr><td colspan="5">

Standardized eager/vLLM activation capture and editing. Early project; model-gradient attribution is eager-only.

</td></tr>
<tr><td>

**[Graphpatch](https://github.com/evan-lloyd/graphpatch)**

</td><td align="right">1</td><td align="right">22</td><td>2023-12-06</td><td><a href="https://github.com/evan-lloyd/graphpatch/commit/d1ecec2949ea622eb04a4a364ef08942d6a8025f">2025-01-27</a></td></tr>
<tr><td colspan="5">

wassname's comment: "promising but abandoned". Graph-based PyTorch interventions; inactive default branch since January 2025, unarchived.

</td></tr>
</table>

## Natural-language interpretation

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[Activation Oracles](https://github.com/adamkarvonen/activation_oracles)**

</td><td align="right"><strong>2</strong></td><td align="right">103</td><td>2025-07-30</td><td><a href="https://github.com/adamkarvonen/activation_oracles/commit/5712762cfc29a18d6414a1cf2cccb4ff4432ced5">2026-09-26</a></td></tr>
<tr><td colspan="5">

Natural-language activation QA, distinct from NLA reconstruction. <details><summary>more</summary>

[Adapters](https://huggingface.co/collections/adamkarvonen/activation-oracles-694232103936f0bd6893c5ca); paper/main dependencies differ. Adam Karvonen.

</details>

</td></tr>
<tr><td>

**[Transluce introspective interpretation](https://github.com/TransluceAI/introspective-interp)**

</td><td align="right"><strong>2</strong></td><td align="right">38</td><td>2025-12-22</td><td><a href="https://github.com/TransluceAI/introspective-interp/commit/594d53348734097857430826d88f5c6856164de7">2026-07-07</a></td></tr>
<tr><td colspan="5">

Feature descriptions, patch-effect prediction and input ablations. <details><summary>more</summary>

[Released models](https://huggingface.co/collections/Transluce/training-language-models-to-explain-their-own-computations); feature supervision is SAE-derived.

</details>

</td></tr>
<tr><td>

**[Natural Language Autoencoders](https://github.com/kitft/natural_language_autoencoders)**

</td><td align="right">1</td><td align="right"><strong>955</strong></td><td>2026-05-05</td><td><a href="https://github.com/kitft/natural_language_autoencoders/commit/0577769b55ad4fdd96d159e983361b97fa4e7331">2026-08-02</a></td></tr>
<tr><td colspan="5">

Two fine-tuned LMs: one writes a text description of an activation, the other rebuilds it; SFT then GRPO. <details><summary>more</summary>

Used in Anthropic pre-deployment audits (Claude Opus 4.6 onward). [Paper](https://transformer-circuits.pub/2026/nla/index.html), [inference package](https://github.com/kitft/nla-inference), [four matched AV/AR pairs](https://huggingface.co/collections/kitft/nla-models-69fa80a3c69880bba63eddc6), [demo](https://www.neuronpedia.org/nla).

</details>

</td></tr>
<tr><td>

**[LatentQA](https://github.com/aypan17/latentqa)**

</td><td align="right">1</td><td align="right">37</td><td>2024-12-12</td><td><a href="https://github.com/aypan17/latentqa/commit/a2dcb6f8eef52ce8c8e75ee71da66cb880f727f4">2025-11-16</a></td></tr>
<tr><td colspan="5">

Research decoder that reads/writes activations in natural language. <details><summary>more</summary>

[Adapter](https://huggingface.co/aypan17/latentqa_llama-3-8b-instruct): CC-BY-NC-SA-4.0, Llama base required.

</details>

</td></tr>
<tr><td>

**[Predictive Concept Decoders](https://transluce.org/pcd)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Reading/demo: sparse concepts predict future model behavior. [Demo](https://decoder.transluce.org/); public code/checkpoint not verified.

</td></tr>
</table>

## Lenses, probes and concepts

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[ELK](https://github.com/EleutherAI/elk)**

</td><td align="right"><strong>19</strong></td><td align="right">225</td><td>2023-02-01</td><td><a href="https://github.com/EleutherAI/elk/commit/84e99a36a5050881d85f1510a2486ce46ac1f942">2023-11-02</a></td></tr>
<tr><td colspan="5">

Latent-knowledge activation extraction and probe evaluation. <details><summary>more</summary>

Current training path is supervised; older README describes CRC/CCS. Probes do not establish general truth detection.

</details>

</td></tr>
<tr><td>

**[Interpreto](https://github.com/FOR-sight-ai/interpreto)**

</td><td align="right">10</td><td align="right">207</td><td>2025-02-26</td><td><a href="https://github.com/FOR-sight-ai/interpreto/commit/b3b9a0fcbb46b891d0029d89a6561307114073a0">2026-10-06</a></td></tr>
<tr><td colspan="5">

Probes/CAVs, ICA/PCA/NMF/SVD/KMeans, attribution and lenses; SAEs optional. Some metrics and backend migrations remain unreleased.

</td></tr>
<tr><td>

**[Tuned Lens](https://github.com/AlignmentResearch/tuned-lens)**

</td><td align="right">5</td><td align="right">616</td><td>2022-10-03</td><td><a href="https://github.com/AlignmentResearch/tuned-lens/commit/abdac0c4de23d9f6d6c8459d576ad203aec15deb">2025-08-07</a></td></tr>
<tr><td colspan="5">

Look at how transformer predictions are built layer by layer. <details><summary>more</summary>

[Pretrained lenses](https://huggingface.co/spaces/AlignmentResearch/tuned-lens/tree/main/lens) are stored in a HF Space.

</details>

</td></tr>
<tr><td>

**[NeuroX](https://github.com/fdalvi/NeuroX)**

</td><td align="right">5</td><td align="right">109</td><td>2018-08-16</td><td><a href="https://github.com/fdalvi/NeuroX/commit/a9ac7cd90be89d72c5ed55d963e2843f039303fc">2023-04-12</a></td></tr>
<tr><td colspan="5">

Neuron analysis and representation probing; historical toolkit.

</td></tr>
<tr><td>

**[Deception Detection](https://github.com/ApolloResearch/deception-detection)**

</td><td align="right">3</td><td align="right">54</td><td>2024-05-31</td><td><a href="https://github.com/ApolloResearch/deception-detection/commit/f8ec4010e74927394709dffa22b97bdf8cd5a62f">2025-02-06</a></td></tr>
<tr><td colspan="5">

Apollo Research linear-probe paper code, labeled rollouts and example probe/config files; dataset/model-specific, not a general truth detector.

</td></tr>
<tr><td>

**[Overcomplete](https://github.com/KempnerInstitute/overcomplete)**

</td><td align="right">2</td><td align="right">153</td><td>2024-06-14</td><td><a href="https://github.com/KempnerInstitute/overcomplete/commit/a1781af49c6e4bbfdbfd763b9757bcf6c5dd6403">2025-12-04</a></td></tr>
<tr><td colspan="5">

Vision dictionary/concept learning: SAEs, NMF variants and archetypal analysis.

</td></tr>
<tr><td>

**[ICA Lens](https://github.com/liusida/ica-lens-paper)**

</td><td align="right">2</td><td align="right">45</td><td>2026-06-08</td><td><a href="https://github.com/liusida/ica-lens-paper/commit/6ad5bee4c94d22173e6ffefe20a0f9ba96c703d9">2026-09-30</a></td></tr>
<tr><td colspan="5">

ICA decomposition, signed token readouts and coordinate steering. <details><summary>more</summary>

[Fitted lenses](https://huggingface.co/collections/sida/ica-lens); early project, artifact licenses unspecified.

</details>

</td></tr>
<tr><td>

**[Jacobian lens](https://github.com/anthropics/jacobian-lens)**

</td><td align="right">1</td><td align="right"><strong>2,011</strong></td><td>2026-07-02</td><td><a href="https://github.com/anthropics/jacobian-lens/commit/581d398613e5602a5af361e1c34d3a92ea82ba8e">2026-07-02</a></td></tr>
<tr><td colspan="5">

Decodes residual vectors into tokens via the average Jacobian to the last layer. <details><summary>more</summary>

[Paper](https://transformer-circuits.pub/2026/workspace/index.html), [fitted lenses](https://huggingface.co/neuronpedia/jacobian-lens). Reference only, not maintained.

</details>

</td></tr>
</table>

## Causal hypotheses and circuit discovery

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[circuit-tracer](https://github.com/decoderesearch/circuit-tracer)**

</td><td align="right"><strong>17</strong></td><td align="right"><strong>2,915</strong></td><td>2025-05-28</td><td><a href="https://github.com/decoderesearch/circuit-tracer/commit/7f66876689f59e92fc3641650d38b8bd41749ec4">2026-09-11</a></td></tr>
<tr><td colspan="5">

Attribution graphs and feature interventions using pretrained MLP transcoders. <details><summary>more</summary>

Bundles credited Anthropic frontend code; repository accounts are not backend-specific maintainers.

</details>

</td></tr>
<tr><td>

**[Causalab](https://github.com/goodfire-ai/causalab)**

</td><td align="right">6–7</td><td align="right">118</td><td>2025-04-25</td><td><a href="https://github.com/goodfire-ai/causalab/commit/8e8d5d1f8f9ca8f42bfce7c6b5eef194f012660e">2026-09-30</a></td></tr>
<tr><td colspan="5">

Causal hypothesis testing, DAS/DBM and interventions. <details><summary>more</summary>

Public mirror; [issue #79](https://github.com/goodfire-ai/causalab/issues/79) transferred internally, current fix unknown. ~H allows likely account aliases.

</details>

</td></tr>
<tr><td>

**[Rewriting a Deep Generative Model](https://github.com/davidbau/rewriting)**

</td><td align="right">4</td><td align="right">535</td><td>2020-07-29</td><td><a href="https://github.com/davidbau/rewriting/commit/8f57af3b0897307f2d671c45cb279672babba6a4">2020-12-14</a></td></tr>
<tr><td colspan="5">

David Bau and collaborators: edit StyleGANv2 weights to change generative rules; ECCV 2020 reference code with an old PyTorch/CUDA stack.

</td></tr>
<tr><td>

**[AutoCircuit](https://github.com/UFO-101/auto-circuit)**

</td><td align="right">3</td><td align="right">103</td><td>2023-08-21</td><td><a href="https://github.com/UFO-101/auto-circuit/commit/7242291d0e5da5c9c044cd6cb97ab911be9adabf">2026-08-17</a></td></tr>
<tr><td colspan="5">

Efficient patching, automatic circuit discovery and evaluation on TransformerLens.

</td></tr>
<tr><td>

**[EAP-IG](https://github.com/hannamw/EAP-IG)**

</td><td align="right">3</td><td align="right">89</td><td>2024-01-15</td><td><a href="https://github.com/hannamw/EAP-IG/commit/e24bafd3d22af2c59ac5a83e0a6581b89b5c05dd">2026-05-23</a></td></tr>
<tr><td colspan="5">

Gradient/integrated-gradient circuit ranking with exact-patching comparisons; architecture constraints apply.

</td></tr>
<tr><td>

**[ROME](https://github.com/kmeng01/rome)**

</td><td align="right">2</td><td align="right">780</td><td>2022-02-11</td><td><a href="https://github.com/kmeng01/rome/commit/0874014cd9837e4365f3e6f3c71400ef11509e04">2022-10-14</a></td></tr>
<tr><td colspan="5">

David Bau / Kevin Meng: causal tracing and rank-one factual weight edits. Historical GPT-2/GPT-J/CUDA reference code.

</td></tr>
<tr><td>

**[MEMIT](https://github.com/kmeng01/memit)**

</td><td align="right">2</td><td align="right">561</td><td>2022-10-13</td><td><a href="https://github.com/kmeng01/memit/commit/80426fd9316cf9a50c5ba15e0912f2c2c5bfe84b">2022-11-14</a></td></tr>
<tr><td colspan="5">

David Bau / Kevin Meng: batched factual weight edits across layers; historical CUDA reference code, companion to ROME.

</td></tr>
<tr><td>

**[Transluce circuits](https://github.com/TransluceAI/circuits)**

</td><td align="right">1</td><td align="right">41</td><td>2026-01-15</td><td><a href="https://github.com/TransluceAI/circuits/commit/2d215d4ba016ba8602b69d71fc0f1ad139a427b7">2026-04-10</a></td></tr>
<tr><td colspan="5">

Neuron-basis ADAG tracing and automated descriptions; paper reference code with AI-assisted implementation disclosed.

</td></tr>
</table>

## Steering and trainable interventions

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[PyReFT](https://github.com/stanfordnlp/pyreft)**

</td><td align="right"><strong>10</strong></td><td align="right"><strong>1,590</strong></td><td>2024-02-17</td><td><a href="https://github.com/stanfordnlp/pyreft/commit/dafd0995a366d7b47160a337dcc388eda7431821">2025-02-06</a></td></tr>
<tr><td colspan="5">

Trainable low-rank representation interventions, built on Pyvene; historical baseline.

</td></tr>
<tr><td>

**[AxBench](https://github.com/stanfordnlp/axbench)**

</td><td align="right">6</td><td align="right">218</td><td>2024-08-07</td><td><a href="https://github.com/stanfordnlp/axbench/commit/41c8332543e5a631f9a8c0a9df38799893ace758">2026-03-12</a></td></tr>
<tr><td colspan="5">

Concept detection and steering benchmark. <details><summary>more</summary>

[Even Simple Baselines Outperform Sparse Autoencoders](https://arxiv.org/abs/2501.17148), [Concept16K data](https://huggingface.co/datasets/pyvene/axbench-concept16k): model-generated examples sampled from GemmaScope concepts.

</details>

</td></tr>
<tr><td>

**[repeng](https://github.com/vgel/repeng)**

</td><td align="right">5</td><td align="right">761</td><td>2024-01-21</td><td><a href="https://github.com/vgel/repeng/commit/0ba7196d81f7c5de28b1159c9d1732440afd97ce">2025-09-24</a></td></tr>
<tr><td colspan="5">

Library for making RepE control vectors. Theia Vogel. [Representation Engineering Mistral-7B an Acid Trip](https://vgel.me/posts/representation-engineering/).

</td></tr>
<tr><td>

**[steering-vectors](https://github.com/steering-vectors/steering-vectors)**

</td><td align="right">5</td><td align="right">163</td><td>2024-01-18</td><td><a href="https://github.com/steering-vectors/steering-vectors/commit/5459bd1287be642ec75a4ab000dc833262bcb7f4">2025-02-21</a></td></tr>
<tr><td colspan="5">

HF/PyTorch control-vector training and injection; historical reusable baseline, last default commit February 2025.

</td></tr>
<tr><td>

**[Steerability](https://github.com/generative-computing/steerability)**

</td><td align="right">4</td><td align="right">123</td><td>2025-06-13</td><td><a href="https://github.com/generative-computing/steerability/commit/4459fce2cf8737cf6e0811a33f4d5b01f0e4dcc6">2026-10-03</a></td></tr>
<tr><td colspan="5">

Extensible general-purpose steering library, formerly IBM/AISteer360. <details><summary>more</summary>

My open PRs: [VJP-delta](https://github.com/generative-computing/steerability/pull/33), [CorDA-PCA, S-space and Linear-AcT](https://github.com/generative-computing/steerability/pull/32).

</details>

</td></tr>
<tr><td>

**[IBM activation-steering](https://github.com/IBM/activation-steering)**

</td><td align="right">2</td><td align="right">191</td><td>2024-08-23</td><td><a href="https://github.com/IBM/activation-steering/commit/52be60235ee309b46c49d6d5877f36e20c52e6ab">2025-08-29</a></td></tr>
<tr><td colspan="5">

General-purpose activation steering library (ICLR 2025).

</td></tr>
<tr><td>

**[Spherical-Steering](https://github.com/chili-lab/Spherical-Steering)**

</td><td align="right">2</td><td align="right">23</td><td>2026-02-08</td><td><a href="https://github.com/chili-lab/Spherical-Steering/commit/198cb2e2131c93340b3af2678b203cb77f30f740">2026-05-19</a></td></tr>
<tr><td colspan="5">

Rotates activations instead of adding to them (ICML 2026); paper code.

</td></tr>
<tr><td>

**[Introspection adapters](https://github.com/safety-research/introspection-adapters)**

</td><td align="right">1</td><td align="right">30</td><td>2026-04-28</td><td><a href="https://github.com/safety-research/introspection-adapters/commit/92a3b05ac1c472b76b966c441d11b88c1b7b76ec">2026-04-28</a></td></tr>
<tr><td colspan="5">

LoRA self-report of trained behaviors for weight/behavior auditing, not an activation decoder; false positives. <details><summary>more</summary>

[Paper](https://alignment.anthropic.com/2026/introspection-adapters/).

</details>

</td></tr>
<tr><td>

**[weight-steering](https://github.com/safety-research/weight-steering)**

</td><td align="right">1</td><td align="right">12</td><td>2025-10-17</td><td><a href="https://github.com/safety-research/weight-steering/commit/1c0152910a5b2ff1928be946b4ae4178e34e8c78">2025-11-11</a></td></tr>
<tr><td colspan="5">

Code for [Steering Language Models with Weight Arithmetic](https://arxiv.org/abs/2511.05408).

</td></tr>
<tr><td>

**[steering-lite](https://github.com/wassname/steering-lite)**

</td><td align="right">1</td><td align="right">2</td><td>2026-04-28</td><td><a href="https://github.com/wassname/steering-lite/commit/65345e6fb438fbd241c3be3a4125e388724a5b65">2026-09-30</a></td></tr>
<tr><td colspan="5">

Hackable forward-hook activation steering, calibrated, tested.

</td></tr>
</table>

## Model organisms

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[talkie](https://github.com/talkie-lm/talkie)**

</td><td align="right"><strong>1</strong></td><td align="right"><strong>1,020</strong></td><td>2026-04-20</td><td><a href="https://github.com/talkie-lm/talkie/commit/35317ba3a84861a84c84065bd73faf88ad19329c">2026-05-19</a></td></tr>
<tr><td colspan="5">

13B LM trained on 260B tokens of pre-1931 English. <details><summary>more</summary>

Nick Levine, David Duvenaud, Alec Radford. [Chat model](https://huggingface.co/talkie-lm/talkie-1930-13b-it), [base](https://huggingface.co/talkie-lm/talkie-1930-13b-base), and a [FineWeb twin](https://huggingface.co/talkie-lm/talkie-web-13b-base) with the same architecture "to make possible controlled comparisons between vintage and modern LMs".

</details>

</td></tr>
<tr><td>

**[GPT-4chan](https://github.com/yk/gpt-4chan-public)**

</td><td align="right"><strong>1</strong></td><td align="right">641</td><td>2022-06-02</td><td><a href="https://github.com/yk/gpt-4chan-public/commit/71c665d258fce873fa9088452dcad56e8ca07001">2022-06-03</a></td></tr>
<tr><td colspan="5">

Yannic Kilcher, 2022: GPT-J 6B fine-tuned on /pol/. <details><summary>more</summary>

[Weights on archive.org](https://archive.org/details/gpt4chan_model_float16), [HF mirror](https://huggingface.co/pawelppppaolo/gpt4chan_model_float16).

</details>

</td></tr>
<tr><td>

**[GPT4chan 24B](https://huggingface.co/v2ray/GPT4chan-24B)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Mistral-Small-24B base with a QLoRA on [v2ray/4chan](https://huggingface.co/datasets/v2ray/4chan); also [8B on Llama-3.1](https://huggingface.co/v2ray/GPT4chan-8B). Base-model prompt format, not chat.

</td></tr>
<tr><td>

**[Olmo-3.1-7B-RL-Zero-Code-4chan](https://huggingface.co/wassname/Olmo-3.1-7B-RL-Zero-Code-4chan)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Mine. Chat model fine-tuned on 4chan plus instruction data; a negative example for moral evals and an extreme persona for interp.

</td></tr>
<tr><td>

**[kjj0/4chanpol](https://huggingface.co/datasets/kjj0/4chanpol)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

114M unique /pol/ posts, June 2016 to November 2019, deduplicated from [Raiders of the Lost Kek](https://arxiv.org/abs/2001.07487). <details><summary>more</summary>

[Variant with OpenAI moderation scores](https://huggingface.co/datasets/kjj0/4chanpol-openaimod).

</details>

</td></tr>
<tr><td>

**[4chan-datasets](https://huggingface.co/datasets/lesserfield/4chan-datasets)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Many boards, raw text. [v2ray/4chan](https://huggingface.co/datasets/v2ray/4chan) is the same data in a better format.

</td></tr>
<tr><td>

**[v2ray_4chan_formatted](https://huggingface.co/datasets/wassname/v2ray_4chan_formatted)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Mine. v2ray/4chan as chat messages with SFT splits (45,751 train, 5,084 test).

</td></tr>
</table>

*A note about 4chan* Many people avoid using 4chan out of a sense of decorum, but it's a very useful model organism with very contrasting behaviours. Most models are helpful, polite and moderate. 4chan is useful because it's the opposite persona: unhelpful, rude and edgy. It's also sometimes funny. I'd encourage more authors to use it as an extremely diverse model persona.

## Evaluate interpretations and interventions

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[Quantus](https://github.com/understandable-machine-intelligence-lab/Quantus)**

</td><td align="right"><strong>20</strong></td><td align="right"><strong>676</strong></td><td>2021-03-18</td><td><a href="https://github.com/understandable-machine-intelligence-lab/Quantus/commit/85bc29d137d8f42835dd392f5cc441ad61d6d1f1">2026-08-20</a></td></tr>
<tr><td colspan="5">

Attribution faithfulness, robustness and randomization metrics; implementations are not universally verified by original metric authors.

</td></tr>
<tr><td>

**[Tracr](https://github.com/google-deepmind/tracr)**

</td><td align="right">9</td><td align="right">568</td><td>2022-12-01</td><td><a href="https://github.com/google-deepmind/tracr/commit/9ce2b8c82b6ba10e62e86cf6f390e7536d4fd2cd">2024-02-05</a></td></tr>
<tr><td colspan="5">

Compile RASP programs into transformers with known mechanisms; archived ground-truth reference.

</td></tr>
<tr><td>

**[MIB](https://github.com/aaronmueller/MIB)**

</td><td align="right">3</td><td align="right">27</td><td>2025-04-01</td><td><a href="https://github.com/aaronmueller/MIB/commit/b69dabe9899251d4a8fe90789afa4d655afc84c7">2025-08-15</a></td></tr>
<tr><td colspan="5">

Mechanistic interpretability benchmark project; implementation is split into tracks. [Circuit track](https://github.com/hannamw/MIB-circuit-track).

</td></tr>
<tr><td>

**[CausalGym](https://github.com/aryamanarora/causalgym)**

</td><td align="right">2</td><td align="right">57</td><td>2023-10-10</td><td><a href="https://github.com/aryamanarora/causalgym/commit/0f3129ff3b6c5c8264892f30a25be25150ae9179">2024-11-30</a></td></tr>
<tr><td colspan="5">

Controlled linguistic causal-intervention benchmark. <details><summary>more</summary>

[HF data](https://huggingface.co/datasets/aryaman/causalgym); reference code assumes GPTNeoX-family models.

</details>

</td></tr>
<tr><td>

**[Liars' Bench](https://github.com/Cadenza-Labs/liars-bench)**

</td><td align="right">2</td><td align="right">15</td><td>2025-02-18</td><td><a href="https://github.com/Cadenza-Labs/liars-bench/commit/ba10de150873d53a34e88278346f857962f82de3">2026-05-07</a></td></tr>
<tr><td colspan="5">

Cadenza Labs lie-detection benchmark with black/white-box detectors; submodule setup documentation conflicts with actual URLs.

</td></tr>
<tr><td>

**[RAVEL](https://github.com/explanare/ravel)**

</td><td align="right">1</td><td align="right">58</td><td>2024-02-17</td><td><a href="https://github.com/explanare/ravel/commit/e421fc9e132b3613b1d0020f856d539217fb30ca">2025-10-30</a></td></tr>
<tr><td colspan="5">

Representation disentanglement/interchange tests; paper benchmark.

</td></tr>
</table>

## Interpretable models by design

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[PyTorch Concepts](https://github.com/pyc-team/pytorch_concepts)**

</td><td align="right"><strong>10</strong></td><td align="right">159</td><td>2024-06-22</td><td><a href="https://github.com/pyc-team/pytorch_concepts/commit/45dd8a329cda1473295eec4aef5f7c375a647d37">2026-07-24</a></td></tr>
<tr><td colspan="5">

Concept bottlenecks, interpretable layers and interventions; alpha API.

</td></tr>
<tr><td>

**[Steerling](https://github.com/guidelabs/steerling)**

</td><td align="right">3</td><td align="right"><strong>241</strong></td><td>2026-02-22</td><td><a href="https://github.com/guidelabs/steerling/commit/f34ffa89e46969445f3cf6e7c885e9623a2047c1">2026-07-14</a></td></tr>
<tr><td colspan="5">

Interpretable-by-design ~8B causal diffusion LM, not an arbitrary-model explainer. <details><summary>more</summary>

[Weights](https://huggingface.co/guidelabs/steerling-8b); commercial-use wording qualified; training code not released.

</details>

</td></tr>
</table>

## Explainability and counterfactuals

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[SHAP](https://github.com/shap/shap)**

</td><td align="right"><strong>270</strong></td><td align="right"><strong>25,794</strong></td><td>2016-11-22</td><td><a href="https://github.com/shap/shap/commit/50be8f4fd7031d535d515042741320f53272d211">2026-10-04</a></td></tr>
<tr><td colspan="5">

Feature attribution; background/feature-dependence assumptions matter.

</td></tr>
<tr><td>

**[Captum](https://github.com/meta-pytorch/captum)**

</td><td align="right">118</td><td align="right">5,709</td><td>2019-08-27</td><td><a href="https://github.com/meta-pytorch/captum/commit/7aefa21cf9c3f1fb8bae757fd4f3a5fdc3c400a6">2026-09-28</a></td></tr>
<tr><td colspan="5">

PyTorch attribution and model interpretability.

</td></tr>
<tr><td>

**[pytorch-grad-cam](https://github.com/jacobgil/pytorch-grad-cam)**

</td><td align="right">52</td><td align="right">12,993</td><td>2017-05-31</td><td><a href="https://github.com/jacobgil/pytorch-grad-cam/commit/704393448a7b0c620ee2c2b9597723f1d7f17b3d">2026-08-13</a></td></tr>
<tr><td colspan="5">

CNN/ViT attribution and ROAD evaluation; Jacob Gildenblat.

</td></tr>
<tr><td>

**[InterpretML](https://github.com/interpretml/interpret)**

</td><td align="right">47</td><td align="right">6,956</td><td>2019-05-03</td><td><a href="https://github.com/interpretml/interpret/commit/560f8dde814cac03aec89e189bc9874012c7f1a5">2026-08-17</a></td></tr>
<tr><td colspan="5">

Glassbox explainable boosting models and blackbox explanations.

</td></tr>
<tr><td>

**[LIME](https://github.com/marcotcr/lime)**

</td><td align="right">42</td><td align="right">12,166</td><td>2016-03-15</td><td><a href="https://github.com/marcotcr/lime/commit/fd7eb2e6f760619c29fca0187c07b82157601b32">2021-07-29</a></td></tr>
<tr><td colspan="5">

Local surrogate explanations; historical baseline, code inactive since 2021.

</td></tr>
<tr><td>

**[AIX360](https://github.com/Trusted-AI/AIX360)**

</td><td align="right">24</td><td align="right">1,808</td><td>2019-07-11</td><td><a href="https://github.com/Trusted-AI/AIX360/commit/0ce916f33b7e149c12dfdb85ae7dcad831fbc1f2">2026-09-05</a></td></tr>
<tr><td colspan="5">

IBM explainability toolkit.

</td></tr>
<tr><td>

**[DiCE](https://github.com/interpretml/DiCE)**

</td><td align="right">21</td><td align="right">1,528</td><td>2019-05-02</td><td><a href="https://github.com/interpretml/DiCE/commit/8a3aea404f857fa599bfa7da663d94823b674688">2025-07-13</a></td></tr>
<tr><td colspan="5">

Diverse counterfactual explanations; model counterfactuals do not establish real-world causal recourse.

</td></tr>
<tr><td>

**[Interpret community](https://github.com/interpretml/interpret-community)**

</td><td align="right">21</td><td align="right">444</td><td>2019-09-25</td><td><a href="https://github.com/interpretml/interpret-community/commit/0966bc936e84e56ab22d6869cc90a0f9c5e84a59">2025-02-07</a></td></tr>
<tr><td colspan="5">

InterpretML extension: SHAP, Mimic and LIME explainers, permutation feature importance.

</td></tr>
<tr><td>

**[Xplique](https://github.com/deel-ai/xplique)**

</td><td align="right">15</td><td align="right">755</td><td>2020-04-05</td><td><a href="https://github.com/deel-ai/xplique/commit/7fa573b6534f29f2eaa923522df0190fecb46f62">2026-09-25</a></td></tr>
<tr><td colspan="5">

Attribution and NMF/CRAFT concept discovery; framework/version restrictions apply.

</td></tr>
<tr><td>

**[Zennit](https://github.com/chr5tphr/zennit)**

</td><td align="right">12</td><td align="right">248</td><td>2020-11-10</td><td><a href="https://github.com/chr5tphr/zennit/commit/3e98348aa95e908f550ab2a13fca2245c30f7de3">2026-05-13</a></td></tr>
<tr><td colspan="5">

PyTorch Layerwise Relevance Propagation.

</td></tr>
<tr><td>

**[Inseq](https://github.com/inseq-team/inseq)**

</td><td align="right">11</td><td align="right">476</td><td>2021-09-14</td><td><a href="https://github.com/inseq-team/inseq/commit/a269ee8fbc65f9079109856e0f995e39a6333a8b">2026-04-25</a></td></tr>
<tr><td colspan="5">

Sequence-generation attribution.

</td></tr>
<tr><td>

**[Concept Relevance Propagation](https://github.com/rachtibat/zennit-crp)**

</td><td align="right">7</td><td align="right">141</td><td>2022-06-07</td><td><a href="https://github.com/rachtibat/zennit-crp/commit/ecf1b7873bf0bf5ca34b7d21407ccb95549198b8">2026-01-14</a></td></tr>
<tr><td colspan="5">

Concept-conditional attribution and relevance maximization; Zennit companion.

</td></tr>
<tr><td>

**[ICX360](https://github.com/IBM/ICX360)**

</td><td align="right">5</td><td align="right">72</td><td>2025-05-27</td><td><a href="https://github.com/IBM/ICX360/commit/0c971ce8ef82b3228a3a34fcd0f184044ab943a0">2026-10-03</a></td></tr>
<tr><td colspan="5">

IBM input-context attribution, contrastive prompt explanations and token highlighting; explanation depends on context perturbations/output scalarization.

</td></tr>
<tr><td>

**[XAI](https://github.com/EthicalML/xai)**

</td><td align="right">3</td><td align="right">1,265</td><td>2019-01-11</td><td><a href="https://github.com/EthicalML/xai/commit/8bc9356f15f95a1a94910bae99cce49ba79147ab">2025-11-29</a></td></tr>
<tr><td colspan="5">

Explainability and responsible-ML tools.

</td></tr>
<tr><td>

**[Dissect](https://github.com/davidbau/dissect)**

</td><td align="right">2</td><td align="right">307</td><td>2020-04-28</td><td><a href="https://github.com/davidbau/dissect/commit/9421eaa8672fd051088de6c0225a385064070935">2021-01-09</a></td></tr>
<tr><td colspan="5">

David Bau / Jun-Yan Zhu: vision concept dissection, unit ablations and visualization; historical CNN/GAN reference code.

</td></tr>
<tr><td>

**[Explabox](https://github.com/MarcelRobeer/explabox)**

</td><td align="right">1</td><td align="right">22</td><td>2022-05-10</td><td><a href="https://github.com/MarcelRobeer/explabox/commit/290eb01e44db35b1905443f12c3295b072c699d9">2025-10-14</a></td></tr>
<tr><td colspan="5">

Model explanation and testing toolbox.

</td></tr>
<tr><td>

**[Responsible AI Toolbox](https://responsibleaitoolbox.ai/)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Dashboard integrating Error analysis, Fairlearn, InterpretML, DiCE, EconML and Data Balance.

</td></tr>
<tr><td>

**[MI2.ai](https://www.mi2.ai/)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

ARES, xSurvival, Large Model Analysis; [DrWhy](https://github.com/ModelOriented/DrWhy) ecosystem.

</td></tr>
<tr><td>

**[DrWhy](https://github.com/ModelOriented/DrWhy)**

</td><td align="right">6†</td><td align="right">688†</td><td>2018-10-18</td><td><a href="https://github.com/ModelOriented/DrWhy/commit/2cb4580ff41843769ab967ab6563b204d1a81f32">2023-02-21</a>†</td></tr>
<tr><td colspan="5">

DALEX, survex, Arena, fairmodels; <details><summary>more</summary>

†collection-wide metrics, not maintenance evidence for each component.

</details>

</td></tr>
<tr><td>

**[ELI5](https://eli5.readthedocs.io/en/latest/overview.html)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Inspect model weights and predictions.

</td></tr>
</table>

## Sparse feature tooling

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[SAELens](https://github.com/decoderesearch/SAELens)**

</td><td align="right"><strong>78</strong></td><td align="right"><strong>1,550</strong></td><td>2023-11-29</td><td><a href="https://github.com/decoderesearch/SAELens/commit/56e0a001e2bd4db938089152392c54aa4fe732a4">2026-10-04</a></td></tr>
<tr><td colspan="5">

Sparse autoencoder training/loading/analysis. <details><summary>more</summary>

[Gemma Scope 2](https://huggingface.co/collections/google/gemma-scope-2-694506265ca2b018ef6ba2b8) pretrained suite.

</details>

</td></tr>
<tr><td>

**[Delphi](https://github.com/EleutherAI/delphi)**

</td><td align="right">22</td><td align="right">279</td><td>2024-06-18</td><td><a href="https://github.com/EleutherAI/delphi/commit/4fea06e6e8b68eeaf302474325fca13df95c5d6f">2026-08-25</a></td></tr>
<tr><td colspan="5">

Generate and score explanations of SAE/transcoder features; distinct from raw-activation NLAs. Sampled weekly CI failures in the October audit.

</td></tr>
</table>

## Browsers and visualizations

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[Transformer Debugger](https://github.com/openai/transformer-debugger)**

</td><td align="right"><strong>12</strong></td><td align="right"><strong>4,121</strong></td><td>2024-03-11</td><td><a href="https://github.com/openai/transformer-debugger/commit/c22efe8d5b3e514ac8ff5e15d2441fa1dcaff1d7">2026-04-15</a></td></tr>
<tr><td colspan="5">

OpenAI model-inspection interface; not HuggingFace-native.

</td></tr>
<tr><td>

**[Neuronpedia](https://www.neuronpedia.org/)**

</td><td align="right"><strong>12</strong></td><td align="right">1,160</td><td>2023-06-21</td><td><a href="https://github.com/hijohnnylin/neuronpedia/commit/bf7b7421d9e44874186391e8887d6263e80e985b">2026-10-01</a></td></tr>
<tr><td colspan="5">

Public feature/neuron browser; [source](https://github.com/hijohnnylin/neuronpedia).

</td></tr>
<tr><td>

**[CircuitsVis](https://github.com/TransformerLensOrg/CircuitsVis)**

</td><td align="right"><strong>12</strong></td><td align="right">368</td><td>2022-11-05</td><td><a href="https://github.com/TransformerLensOrg/CircuitsVis/commit/512040a1344186a80f64f04fb9b22fa121edfebd">2026-04-30</a></td></tr>
<tr><td colspan="5">

Python/React visualizations, including attention patterns; not a tracing engine.

</td></tr>
<tr><td>

**[Treescope](https://github.com/google-deepmind/treescope)**

</td><td align="right">11</td><td align="right">476</td><td>2024-07-24</td><td><a href="https://github.com/google-deepmind/treescope/commit/20a94822d0c4c0a55c10eaa8fed96a77757f4068">2026-06-18</a></td></tr>
<tr><td colspan="5">

Interactive tensor/model HTML inspection, independent of archived Penzai.

</td></tr>
<tr><td>

**[Workbench](https://github.com/ndif-team/workbench)**

</td><td align="right">7</td><td align="right">18</td><td>2025-05-20</td><td><a href="https://github.com/ndif-team/workbench/commit/416fc8b26e46debdc435c4a88f0379ae60335138">2026-09-18</a></td></tr>
<tr><td colspan="5">

Interactive NNsight/NDIF model exploration; visualization/platform rather than a new hook engine.

</td></tr>
<tr><td>

**[Subtext](https://github.com/ninjahawk/Subtext)**

</td><td align="right">2</td><td align="right">245</td><td>2026-07-06</td><td><a href="https://github.com/ninjahawk/Subtext/commit/eb9207c409c4baabe32881c5050d624abdeca607">2026-07-23</a></td></tr>
<tr><td colspan="5">

Conversational Jacobian-lens interface. Each rendered word is a lens readout, not model output.

</td></tr>
<tr><td>

**[Logitloom](https://github.com/vgel/logitloom)**

</td><td align="right">1</td><td align="right">159</td><td>2025-05-08</td><td><a href="https://github.com/vgel/logitloom/commit/3a6be56fbf53e28b43ab0fbd14b357d5d444bfa3">2025-05-29</a></td></tr>
<tr><td colspan="5">

Theia Vogel's interactive token-trajectory trees from API logprobs/prefills, not a logit lens. Unlicensed; split-UTF-8 limitations.

</td></tr>
<tr><td>

**[NN-SVG](https://alexlenail.me/NN-SVG/)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Neural-network architecture illustration.

</td></tr>
</table>

## Agent auditing and evaluation infrastructure

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai)**

</td><td align="right"><strong>325</strong></td><td align="right"><strong>2,946</strong></td><td>2023-11-14</td><td><a href="https://github.com/UKGovernmentBEIS/inspect_ai/commit/aa20052a65b13516f1ee79d10ccceda00c205cc6">2026-10-06</a></td></tr>
<tr><td colspan="5">

Evaluation/agent runtime, scoring, sandboxes and .eval logs; behavioral evidence, not hidden-state explanation.

</td></tr>
<tr><td>

**[Inspect Scout](https://github.com/meridianlabs-ai/inspect_scout)**

</td><td align="right">30</td><td align="right">76</td><td>2025-09-07</td><td><a href="https://github.com/meridianlabs-ai/inspect_scout/commit/5533fc4de8a4928dd0b06b3550fea48c88139807">2026-10-06</a></td></tr>
<tr><td colspan="5">

Transcript scanning/analysis, external transcript imports and human-label validation; automated judgments still need validation.

</td></tr>
<tr><td>

**[Petri](https://github.com/meridianlabs-ai/inspect_petri)**

</td><td align="right">8</td><td align="right">1,361</td><td>2025-08-19</td><td><a href="https://github.com/meridianlabs-ai/inspect_petri/commit/766d3842e67c573aaf7d5dffcdfb0381a35e3574">2026-10-02</a></td></tr>
<tr><td colspan="5">

Auditor/target interactions, simulated tools, rollback and rubric judging. Formerly safety-research/petri; v3 changes the Python API.

</td></tr>
<tr><td>

**[Petri Bloom](https://github.com/meridianlabs-ai/petri_bloom)**

</td><td align="right">2</td><td align="right">36</td><td>2026-04-02</td><td><a href="https://github.com/meridianlabs-ai/petri_bloom/commit/902e932c219818429d79bc12a1937e4f04490308">2026-07-15</a></td></tr>
<tr><td colspan="5">

Bloom scenario generation with Petri audits; [original Bloom](https://github.com/safety-research/bloom) is frozen. <details><summary>more</summary>

Small successor; current Petri-v3 compatibility untested.

</details>

</td></tr>
<tr><td>

**[Docent](https://transluce.org/docent/blog/introducing-docent)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

wassname's original description: "interactive model explanation and steering interface". Updated description: agent-transcript and behavior-rubric auditing; [current product page](https://transluce.org/docent).

</td></tr>
<tr><td>

**[Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals)**

</td><td align="right">212†</td><td align="right">693†</td><td>2024-10-02</td><td><a href="https://github.com/UKGovernmentBEIS/inspect_evals/commit/9080b5e9f1647ed14e45de8cb01e3d43411c0163">2026-10-05</a>†</td></tr>
<tr><td colspan="5">

Collection of Inspect evaluations; †metrics cover the collection, not an individual task's contributors or maintenance.

</td></tr>
<tr><td>

**[ControlArena](https://github.com/UKGovernmentBEIS/control-arena)**

</td><td align="right">59†</td><td align="right">248†</td><td>2025-02-06</td><td><a href="https://github.com/UKGovernmentBEIS/control-arena/commit/475be659f16f47d8dc05e853a5ed577bc34a04e6">2026-10-05</a>†</td></tr>
<tr><td colspan="5">

Inspect-based AI-control experiments: policies, monitors and safety/usefulness evaluation; †framework/settings-wide metrics, not individual-setting maintenance.

</td></tr>
</table>

## Adapters

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[Adapter intervention types](https://github.com/wassname/adapters_as_hypotheses)**

</td><td align="right">1</td><td align="right"><strong>6</strong></td><td>2026-02-22</td><td><a href="https://github.com/wassname/adapters_as_hypotheses/commit/eee889676ab511dcdf3efea9588b0c164f444cd5">2026-07-19</a></td></tr>
<tr><td colspan="5">

Literature review of adapter intervention types.

</td></tr>
<tr><td>

**[lora-lite](https://github.com/wassname/lora-lite)**

</td><td align="right">1</td><td align="right">1</td><td>2026-04-26</td><td><a href="https://github.com/wassname/lora-lite/commit/2a50373311d54d231652727735aebd7873da9e80">2026-06-19</a></td></tr>
<tr><td colspan="5">

Hackable LoRA library, one file per variant, built on forward hooks.

</td></tr>
</table>

## Mine (wassname)

I have some good stuff too, so please excuse a little detour into self promotion...

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[moral-maps](https://github.com/wassname/moral-maps)**

</td><td align="right"><strong>2</strong></td><td align="right">2</td><td>2026-04-30</td><td><a href="https://github.com/wassname/moral-maps/commit/f43313d06a5aebb1fe3f4b376786c5525bec81b5">2026-09-25</a></td></tr>
<tr><td colspan="5">

Puts models through human value surveys and plots them next to human societies; shows where steering moves a model. <details><summary>more</summary>

[Eval library](https://github.com/wassname/moral-maps/blob/main/docs/evals.md): moral foundation vignettes against human raters, MFQ-2, Big Five, 16PF and Humor Styles surveys comparable to human country means; local HF answer-token probabilities.

</details>

</td></tr>
<tr><td>

**[abliterator](https://github.com/wassname/abliterator)**

</td><td align="right">1</td><td align="right"><strong>11</strong></td><td>2025-03-11</td><td><a href="https://github.com/wassname/abliterator/commit/0c95026744a5e49f97423b4734185cd3d2ac5533">2026-02-21</a></td></tr>
<tr><td colspan="5">

Concept removal (abliteration) with BauKit, not TransformerLens.

</td></tr>
<tr><td>

**[vjp-steering](https://github.com/wassname/vjp-steering)**

</td><td align="right">1</td><td align="right">4</td><td>2026-08-21</td><td><a href="https://github.com/wassname/vjp-steering/commit/1e19ae30845574ebd2657dd961a0281a1df087f3">2026-09-28</a></td></tr>
<tr><td colspan="5">

Contrastive steering vectors from vector-Jacobian products (WIP).

</td></tr>
<tr><td>

**[AntiPaSTO](https://github.com/wassname/AntiPaSTO)**

</td><td align="right">1</td><td align="right">4</td><td>2025-12-28</td><td><a href="https://github.com/wassname/AntiPaSTO/commit/4ff0710851d08df8705bfe335245bca4bbd82fbc">2026-09-02</a></td></tr>
<tr><td colspan="5">

Self-supervised honesty steering via anti-parallel representations.

</td></tr>
<tr><td>

**[query-steering](https://github.com/wassname/query-steering)**

</td><td align="right">1</td><td align="right">3</td><td>2026-09-25</td><td><a href="https://github.com/wassname/query-steering/commit/5cfb80035849c8850e3af65fa62b7ab20572a16f">2026-09-30</a></td></tr>
<tr><td colspan="5">

Steer attention so the model reads out a secret from its context.

</td></tr>
<tr><td>

**[isokl_steering_calibration](https://github.com/wassname/isokl_steering_calibration)**

</td><td align="right">1</td><td align="right">2</td><td>2026-05-05</td><td><a href="https://github.com/wassname/isokl_steering_calibration/commit/27bfbcdd2df2d2e7103dfbc64aae3936b3415812">2026-09-19</a></td></tr>
<tr><td colspan="5">

Compare steering methods at the same KL budget.

</td></tr>
<tr><td>

**[ssteer-eval-aware](https://github.com/wassname/ssteer-eval-aware)**

</td><td align="right">1</td><td align="right">2</td><td>2026-03-21</td><td><a href="https://github.com/wassname/ssteer-eval-aware/commit/9095dd4337f6bb0c189f0d858ad3fd46e72d6e7e">2026-05-03</a></td></tr>
<tr><td colspan="5">

S-space steering suppresses eval-awareness.

</td></tr>
<tr><td>

**[cwsteer](https://github.com/wassname/cwsteer)**

</td><td align="right">1</td><td align="right">1</td><td>2026-06-23</td><td><a href="https://github.com/wassname/cwsteer/commit/50cd6d9163c97025b51858fbb9bb1b3a80f3f9d2">2026-06-26</a></td></tr>
<tr><td colspan="5">

Contrastive weight steering: generate, filter, train, calibrate, steer.

</td></tr>
<tr><td>

**[persona-steering-template-library](https://github.com/wassname/persona-steering-template-library)**

</td><td align="right">1</td><td align="right">1</td><td>2026-06-13</td><td><a href="https://github.com/wassname/persona-steering-template-library/commit/5e177a2745b5194c3ede22f6264dcbb4428dc497">2026-08-09</a></td></tr>
<tr><td colspan="5">

~100 persona prompt templates for building steering vectors, judged on on-axis vs off-axis behaviour.

</td></tr>
<tr><td>

**[tiny-mfv](https://huggingface.co/datasets/wassname/tiny-mfv)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

132 moral foundation vignettes (Clifford et al. 2015): classic, sci-fi and AI-actor versions; HF dataset.

</td></tr>
</table>

## Structured output (adjacent tooling)

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[instructor](https://github.com/567-labs/instructor)**

</td><td align="right"><strong>259</strong></td><td align="right">13,981</td><td>2023-06-14</td><td><a href="https://github.com/567-labs/instructor/commit/e12f8b49203b0c1f253d27c1e709d0a09b9fc5a8">2026-09-11</a></td></tr>
<tr><td colspan="5">

Pydantic models from API models; retries on validation errors. For remote APIs without logits.

</td></tr>
<tr><td>

**[Outlines](https://github.com/dottxt-ai/outlines)**

</td><td align="right">179</td><td align="right">15,905</td><td>2023-03-17</td><td><a href="https://github.com/dottxt-ai/outlines/commit/c52af8472c6fe8a607a733ec11b709476af77a96">2026-08-24</a></td></tr>
<tr><td colspan="5">

Constrained generation from regex, JSON schema or grammar.

</td></tr>
<tr><td>

**[Microsoft Guidance](https://github.com/guidance-ai/guidance)**

</td><td align="right">78</td><td align="right"><strong>21,789</strong></td><td>2022-11-10</td><td><a href="https://github.com/guidance-ai/guidance/commit/21b1d90dfbebff4b141df70c714c8af15aa5f4af">2026-05-21</a></td></tr>
<tr><td colspan="5">

Templates that mix prompts and constraints.

</td></tr>
<tr><td>

**[XGrammar](https://github.com/mlc-ai/xgrammar)**

</td><td align="right">74</td><td align="right">1,944</td><td>2024-06-28</td><td><a href="https://github.com/mlc-ai/xgrammar/commit/ed1bc8312ba37947050938bf8bdd88b923a1057b">2026-10-06</a></td></tr>
<tr><td colspan="5">

Fast grammar engine; default backend in vLLM, SGLang, TensorRT-LLM and MLC-LLM.

</td></tr>
<tr><td>

**[guardrails](https://github.com/guardrails-ai/guardrails)**

</td><td align="right">72</td><td align="right">7,492</td><td>2023-01-29</td><td><a href="https://github.com/guardrails-ai/guardrails/commit/06d0ff2c5f9bcb493d976b76f885e37e41ce845d">2026-08-26</a></td></tr>
<tr><td colspan="5">

Validators for LLM outputs.

</td></tr>
<tr><td>

**[LLGuidance](https://github.com/guidance-ai/llguidance)**

</td><td align="right">37</td><td align="right">882</td><td>2024-07-25</td><td><a href="https://github.com/guidance-ai/llguidance/commit/e7c69004694064a01db30ddc7a29a103a5d2f3c7">2026-09-30</a></td></tr>
<tr><td colspan="5">

Fast Rust grammar engine; used by OpenAI Structured Outputs, vLLM, SGLang, llama.cpp and Chromium.

</td></tr>
<tr><td>

**[TypeChat](https://github.com/microsoft/TypeChat)**

</td><td align="right">35</td><td align="right">8,689</td><td>2023-06-20</td><td><a href="https://github.com/microsoft/TypeChat/commit/fcd3a5a500a1f4ed0be88b7a0a388c87de8d7502">2026-10-06</a></td></tr>
<tr><td colspan="5">

TypeScript.

</td></tr>
<tr><td>

**[LMQL](https://github.com/eth-sri/lmql)**

</td><td align="right">35</td><td align="right">4,218</td><td>2022-11-24</td><td><a href="https://github.com/eth-sri/lmql/commit/fc8edd4457dc5a5e4e595302166bec797582bf53">2025-05-22</a></td></tr>
<tr><td colspan="5">

Query language for LLMs; latest default/source dates differ.

</td></tr>
<tr><td>

**[lm-format-enforcer](https://github.com/noamgat/lm-format-enforcer)**

</td><td align="right">14</td><td align="right">2,041</td><td>2023-09-21</td><td><a href="https://github.com/noamgat/lm-format-enforcer/commit/817f944fcc8851917c40300a47f62d1defc3ffc3">2026-04-04</a></td></tr>
<tr><td colspan="5">

JSON schema and regex for transformers and vLLM.

</td></tr>
<tr><td>

**[Promptify](https://github.com/promptslab/Promptify)**

</td><td align="right">13</td><td align="right">4,640</td><td>2022-12-12</td><td><a href="https://github.com/promptslab/Promptify/commit/bc5ed081a7a4d7be90e798dd48c324fd4c57bd2a">2026-03-27</a></td></tr>
<tr><td colspan="5">

Structured NLP prompting.

</td></tr>
<tr><td>

**[kor](https://github.com/eyurtsev/kor)**

</td><td align="right">11</td><td align="right">1,684</td><td>2023-02-16</td><td><a href="https://github.com/eyurtsev/kor/commit/f6dc65546c3a9aed53f26f0cbd3ad518a2c48504">2024-11-25</a></td></tr>
<tr><td colspan="5">

Schema-based extraction; historical library.

</td></tr>
<tr><td>

**[prob_jsonformer](https://github.com/wassname/prob_jsonformer)**

</td><td align="right">9</td><td align="right">17</td><td>2024-05-10</td><td><a href="https://github.com/wassname/prob_jsonformer/commit/b639079d045ab174398762e3b1e1fdca1d8d30ef">2025-03-23</a></td></tr>
<tr><td colspan="5">

Jsonformer, but it can output the probability of each choice in a single pass. Has enum.

</td></tr>
<tr><td>

**[jsonformer](https://github.com/1rgs/jsonformer)**

</td><td align="right">6</td><td align="right">4,937</td><td>2023-04-29</td><td><a href="https://github.com/1rgs/jsonformer/commit/bfad031876ace84ec0a7853718a1c0828ea1653a">2023-05-30</a></td></tr>
<tr><td colspan="5">

Does not do enums, HuggingFace only; historical code, last default commit May 2023.

</td></tr>
<tr><td>

**[salute](https://github.com/LevanKvirkvelia/salute)**

</td><td align="right">5</td><td align="right">218</td><td>2023-05-21</td><td><a href="https://github.com/LevanKvirkvelia/salute/commit/34860fd8eeb34ad5bd4dc4fd5c390ddb19e1f340">2023-06-17</a></td></tr>
<tr><td colspan="5">

TypeScript; historical code.

</td></tr>
<tr><td>

**[clownfish](https://github.com/newhouseb/clownfish)**

</td><td align="right">2</td><td align="right">328</td><td>2023-03-27</td><td><a href="https://github.com/newhouseb/clownfish/commit/13d8945f2ebd5346249fc74c00a2758651f07b9e">2023-05-16</a></td></tr>
<tr><td colspan="5">

Modifying transformers to follow a JSON schema; historical code.

</td></tr>
<tr><td>

**[Constrained-Text-Generation-Studio](https://github.com/Hellisotherpeople/Constrained-Text-Generation-Studio)**

</td><td align="right">1</td><td align="right">217</td><td>2022-03-28</td><td><a href="https://github.com/Hellisotherpeople/Constrained-Text-Generation-Studio/commit/42a1b2799556b310e4702b8ece16bb720ee21cdd">2026-04-11</a></td></tr>
<tr><td colspan="5">

Constrained text-generation interface.

</td></tr>
<tr><td>

**[relm](https://github.com/mkuchnik/relm)**

</td><td align="right">1</td><td align="right">108</td><td>2023-03-21</td><td><a href="https://github.com/mkuchnik/relm/commit/cd18b0b5bc278b0da3f23567d23a83c1b62485a2">2023-06-02</a></td></tr>
<tr><td colspan="5">

Regular expression engine for language models; historical code.

</td></tr>
<tr><td>

**[vLLM structured outputs](https://docs.vllm.ai/en/latest/features/structured_outputs/)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

JSON schema, regex, choice and grammar in the server, with xgrammar, guidance or outlines as backend.

</td></tr>
<tr><td>

**[llama.cpp grammars (GBNF)](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md)**

</td><td align="right">445†</td><td align="right">130,508†</td><td>2023-03-10</td><td><a href="https://github.com/ggml-org/llama.cpp/commit/c479922ac520a08969b4c1dc154d7bbb3c386d85">2026-10-06</a>†</td></tr>
<tr><td colspan="5">

Grammar support. †Metrics cover the whole llama.cpp repository, not the grammar module.

</td></tr>
<tr><td>

**[OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

JSON schema enforced by the API; other providers have similar options.

</td></tr>
<tr><td>

**[LangChain structured output](https://docs.langchain.com/oss/python/langchain/structured-output)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Structured-output integration.

</td></tr>
</table>

## Perspectives

Agendas and changes of view, oldest first.

<table>
<tr><th width="50%" align="left">Perspective</th><th width="35%" align="left">Who</th><th width="15%" align="left">Year</th></tr>
<tr><td>

[Simulators](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators), [The Persona Selection Model](https://alignment.anthropic.com/2026/psm/)

</td><td>janus; Sam Marks, Jack Lindsey, Chris Olah</td><td>2022, 2026</td></tr>
<tr><td colspan="3">

"LLMs learn to simulate diverse characters during pre-training, and post-training elicits and refines a particular such Assistant persona."

</td></tr>
<tr><td>

[AGI Ruin #27](https://www.lesswrong.com/posts/uMQ3cqWDPHhjtiesc/agi-ruin-a-list-of-lethalities), [The Most Forbidden Technique](https://www.lesswrong.com/posts/mpmsK8KKysgSKDm2T/the-most-forbidden-technique)

</td><td>Eliezer Yudkowsky; Zvi Mowshowitz</td><td>2022, 2025</td></tr>
<tr><td colspan="3">

"Optimizing against an interpreted thought optimizes against interpretability." For CoT, [Baker et al.](https://arxiv.org/abs/2503.11926) found that "with too much optimization, agents learn obfuscated reward hacking".

</td></tr>
<tr><td>

[The case for ensuring that powerful AIs are controlled](https://www.lesswrong.com/posts/kcKrE9mzEHrdqtDpE/the-case-for-ensuring-that-powerful-ais-are-controlled)

</td><td>Ryan Greenblatt, Buck Shlegeris</td><td>2024</td></tr>
<tr><td colspan="3">

Safety measures should hold "even if the AIs are misaligned and intentionally try to subvert those safety measures".

</td></tr>
<tr><td>

[Towards Guaranteed Safe AI](https://arxiv.org/abs/2405.06624), [Is there a Natural Abstraction of Good?](https://www.lesswrong.com/posts/M5s6WgScRfmeWsLD4/dialogue-is-there-a-natural-abstraction-of-good)

</td><td>davidad</td><td>2024, 2026</td></tr>
<tr><td colspan="3">

From proof-checked safety guarantees to the claim that frontier LLMs "have grokked the natural abstraction of what it means to be Good". Gabriel Alfour disputes it in the same dialogue.

</td></tr>
<tr><td>

[A Pragmatic Vision for Interpretability](https://www.lesswrong.com/posts/StENzDcD3kpfGJssR/a-pragmatic-vision-for-interpretability)

</td><td>Neel Nanda and the GDM interpretability team</td><td>2025</td></tr>
<tr><td colspan="3">

After ["SAEs underperformed linear probes"](https://www.lesswrong.com/posts/4uXCAJNuPKtKBsi28/negative-results-for-saes-on-downstream-tasks), "a strategic pivot over the past year, from ambitious reverse-engineering to a focus on pragmatic interpretability".

</td></tr>
<tr><td>

[The Urgency of Interpretability](https://darioamodei.com/post/the-urgency-of-interpretability)

</td><td>Dario Amodei</td><td>2025</td></tr>
<tr><td colspan="3">

Understand models "before models reach an overwhelming level of power".

</td></tr>
<tr><td>

[Chain of Thought Monitorability: A New and Fragile Opportunity](https://arxiv.org/abs/2507.11473)

</td><td>Tomek Korbak, Mikita Balesni and 39 co-authors</td><td>2025</td></tr>
<tr><td colspan="3">

"Because CoT monitorability may be fragile, we recommend that frontier model developers consider the impact of development decisions on CoT monitorability."

</td></tr>
<tr><td>

[Why We Are Excited About Confessions](https://alignment.openai.com/confessions/)

</td><td>Boaz Barak, Gabriel Wu, Jeremy Chen, Manas Joglekar</td><td>2026</td></tr>
<tr><td colspan="3">

A second output rewarded only for honesty, because "being honest in confessions is the path of least resistance".

</td></tr>
</table>

## Reading and tutorials

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[Generative Meta-Model of LLM Activations](https://github.com/g-luo/generative_latent_prior)**

</td><td align="right"><strong>1</strong></td><td align="right"><strong>95</strong></td><td>2026-01-30</td><td><a href="https://github.com/g-luo/generative_latent_prior/commit/9895e12247aa4713b0cf14797726f8284443a72d">2026-09-12</a></td></tr>
<tr><td colspan="5">

Luo et al. [paper](https://arxiv.org/abs/2602.06964): diffusion prior over residual activations, used to make steering more fluent.

</td></tr>
<tr><td>

**[Manual activation steering](https://github.com/annahdo/implementing_activation_steering)**

</td><td align="right"><strong>1</strong></td><td align="right">24</td><td>2024-01-12</td><td><a href="https://github.com/annahdo/implementing_activation_steering/commit/5458edc1fb703166fc4cdb391db2bc2849c64f17">2024-10-18</a></td></tr>
<tr><td colspan="5">

Tutorial on doing it manually.

</td></tr>
<tr><td>

**[Latent Introspection code](https://github.com/acsresearch/latent-introspection-code)**

</td><td align="right"><strong>1</strong></td><td align="right">3</td><td>2026-02-03</td><td><a href="https://github.com/acsresearch/latent-introspection-code/commit/5007f75766b6f8c650cab438af67f970a262ceca">2026-02-27</a></td></tr>
<tr><td colspan="5">

Theia Vogel's source for [Latent Introspection](https://arxiv.org/abs/2602.20031); concept-injection/self-report experiments, default 2-GPU Qwen-32B setup.

</td></tr>
<tr><td>

**[Small Models Can Introspect, Too](https://vgel.me/posts/qwen-introspection/)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Theia Vogel; [Latent Introspection](https://arxiv.org/abs/2602.20031). <details><summary>more</summary>

Injected concept vectors, including an emergent-misalignment vector from a difference between checkpoints.

</details>

</td></tr>
<tr><td>

**[Lenses on steering vectors](https://x.com/voooooogel/status/2105793927035093490)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

thebes (Theia Vogel), 2026: before believing a steer-on-X result, check fine-tune, sampler, prompt and norm-matched random-vector controls.

</td></tr>
<tr><td>

**[ML Model Interpretation Tools](https://neptune.ai/blog/ml-model-interpretation-tools)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Neptune-AI blog; [archive](https://web.archive.org/web/20251006170041/https://neptune.ai/blog/ml-model-interpretation-tools). <details><summary>more</summary>

Neptune was bought by OpenAI and closed its service in 2026.

</details>

</td></tr>
<tr><td>

**[Explainability and Auditability in ML](https://neptune.ai/blog/explainability-auditability-ml-definitions-techniques-tools)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Neptune-AI blog; [archive](https://web.archive.org/web/20251104135106/https://neptune.ai/blog/explainability-auditability-ml-definitions-techniques-tools).

</td></tr>
<tr><td>

**[AI Ethics tool landscape](https://edwinwenink.github.io/ai-ethics-tool-landscape/)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Tool landscape.

</td></tr>
</table>

## See more

<table>
<tr><th width="42%" align="left">Project</th><th width="9%" align="left">

[~H↑][humans]

</th><th width="11%" align="left">Stars↑</th><th width="18%" align="left">Created</th><th width="20%" align="left">Latest</th></tr>
<tr><td>

**[Awesome-explainable-AI](https://github.com/wangyongjie-ntu/Awesome-explainable-AI)**

</td><td align="right"><strong>22</strong></td><td align="right"><strong>1,659</strong></td><td>2020-02-16</td><td><a href="https://github.com/wangyongjie-ntu/Awesome-explainable-AI/commit/85c09c5dc8ea52078c8c7dc473a914f84a4e1130">2026-08-19</a></td></tr>
<tr><td colspan="5">

Broader explainable-AI list.

</td></tr>
<tr><td>

**[awesome-moral-evals](https://github.com/wassname/awesome-moral-evals)**

</td><td align="right">1</td><td align="right">1</td><td>2026-06-28</td><td><a href="https://github.com/wassname/awesome-moral-evals/commit/db7095804ac4dce836a3d5c49b6ee409367dd853">2026-06-30</a></td></tr>
<tr><td colspan="5">

Datasets for evaluating the moral behaviour of LLMs.

</td></tr>
<tr><td>

**[dweprinz's list that inspired this one](https://github.com/dweprinz/dweprinz.github.io/blob/905db3fe5bd0d3ca0ddd2b201382c2a25accc00b/_pages/resources/responsible-ai/ai-safety.md?plain=1#L48)**

</td><td align="right">1†</td><td align="right">1†</td><td>2023-09-30</td><td><a href="https://github.com/dweprinz/dweprinz.github.io/commit/485f903171721873c582cfa4d751027e57056a11">2026-09-29</a>†</td></tr>
<tr><td colspan="5">

Responsible-AI / AI-safety resources. †Repository-wide metadata, not this page.

</td></tr>
<tr><td>

**[Mechanistic Interpretability Workshop](https://mechinterpworkshop.com/cfp/)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Workshop CFP.

</td></tr>
<tr><td>

**[GitHub interpretability topic](https://github.com/topics/interpretability)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

Discovery index.

</td></tr>
<tr><td>

**[David Bau on NNsight](https://twitter.com/davidbau/status/1785991694279913617)**

</td><td align="right">—</td><td align="right">—</td><td>—</td><td>—</td></tr>
<tr><td colspan="5">

NNsight for research.

</td></tr>
</table>

[humans]: slop/research/20261007_interpretability/families/readme_metrics.json "Estimated number of human contributors (non-bot/non-service GitHub accounts; approximate, not verified people or active maintainers)."

<!-- Table conversion and new entries: PI/gpt-6.1-sol. Perspectives table and intro cut: Claude Opus. Original wassname comments and source quotes restored from README history: PI/OpenAI. -->

<!-- README layout matched to awesome-moral-evals by PI/OpenAI; existing wording and metadata preserved. -->
