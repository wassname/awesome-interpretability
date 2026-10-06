# GitHub mechanisms lane — bounded discovery and verification

Snapshot: **2026-10-07 Australia/Perth / 2026-10-06 UTC**. Read local `README.md` first and confirmed HEAD `f5a023133bfc2997ca90926af8852e1774169ab4`. No project files edited, repository code executed, packages installed, publication or push. Research scripts/cache are outside the project.

## Recommendation

**Add the missing circuit/intervention ecosystem and activation-language alternatives, not a long SAE catalogue.** First pass: circuit-tracer, CircuitsVis, Interpreto, Causalab, nnterp (nested), Mishax, AutoCircuit/EAP-IG, and Activation Oracles. Then a compact natural-language research subsection for LatentQA and Transluce introspective-interp. Keep NLAs prominent: they are already listed, including the inference package, so neither is an omission.

Within comparable roles, breadth precedes stars below. Task fit and demonstrated persistence override misleading comparisons: Delphi has more attributed accounts than the core tools but serves SAE/transcoder explanations; Bergson is exceptionally maintained but answers training-data attribution questions; PyReFT has breadth/stars but no main commit since February 2025. Single-author new work is not automatically inferior, but persistence is not yet established.

### Metric interpretation

**H≈ is a conservative estimate of distinct attributed non-service people, NOT proof of humans writing code.** Contributors are unique accounts returned by `/contributors?anon=false`, fetched with `per_page=100` and explicit pagination until a short page (all 26 examined repos ended after page 1). Excluded `type=Bot`, `[bot]`, and obvious service accounts even when `type=User`: `claude`, `copybara-github` (profile says “Bot for Google OSS”), `cursoragent`. nnterp: 6 accounts→4; Mishax: 5→3; Workbench: 9→7. Causalab: 8 accounts→6–7 estimated people: `canrager`/`can-goodfire` share commit-author name Can Rager; `maxsloef`/`maxsloef-goodfire` likely duplicate Max Loeffler, not conclusively resolved. Remaining accounts may conceal services or aliases. Unlinked/anonymous commits, coauthors, actual labor, and project-specific vs inherited histories are not fully measured.

**Created→tip** means GitHub repository creation date followed by the newest commit reachable from its declared default branch, using the tip commit’s **committer timestamp**. It does not use `updated_at` or `pushed_at`. Tip date can reflect docs/merges/imported history rather than substantive implementation; qualifications below matter. Stars are live snapshot popularity, not quality. All table tips are `main`.

## Prioritized, source-verified shortlist (20 omissions)

### A. Mechanistic libraries

| Repository | H≈ / stars | Created → latest main commit | Fit, persistence and primary-source quote |
|---|---:|---|---|
| [decoderesearch/circuit-tracer](https://github.com/decoderesearch/circuit-tracer) | 17 / 2,915 | 2025-05-28 → [2026-09-11](https://github.com/decoderesearch/circuit-tracer/commit/7f66876689f59e92fc3641650d38b8bd41749ec4) | Attribution graphs + feature interventions, not a general SAE trainer. v0.5.2 July 2026; September NNsight backend port. Some contributor history is inherited frontend code. Quote: [“finding circuits using features from (cross-layer) MLP transcoders”](https://github.com/decoderesearch/circuit-tracer/blob/7f66876689f59e92fc3641650d38b8bd41749ec4/README.md) |
| [TransformerLensOrg/CircuitsVis](https://github.com/TransformerLensOrg/CircuitsVis) | 12 / 368 | 2022-11-05 → [2026-04-30](https://github.com/TransformerLensOrg/CircuitsVis/commit/512040a1344186a80f64f04fb9b22fa121edfebd) | Independent Python/React visualization library; useful companion, not a tracing engine. April 2026 tip only removes devcontainer; last release December 2024. Quote: [“Attention patterns from destination to source tokens, for a group of heads.”](https://github.com/TransformerLensOrg/CircuitsVis/blob/512040a1344186a80f64f04fb9b22fa121edfebd/python/circuitsvis/attention.py) |
| [FOR-sight-ai/interpreto](https://github.com/FOR-sight-ai/interpreto) | 10 / 207 | 2025-02-26 → [2026-10-06](https://github.com/FOR-sight-ai/interpreto/commit/b3b9a0fcbb46b891d0029d89a6561307114073a0) | Broad attribution/concept toolbox; original LogitLens implementation merged October 6, 2026. v0.5.1 September; latest three CI runs successful. Vendors Overcomplete: do not count that as a second SAE innovation. Quote: [“Project every residual-stream state through the model prediction head.”](https://github.com/FOR-sight-ai/interpreto/blob/b3b9a0fcbb46b891d0029d89a6561307114073a0/interpreto/lens/logit_lens.py) |
| [goodfire-ai/causalab](https://github.com/goodfire-ai/causalab) | 6–7 / 118 | 2025-04-25 → [2026-09-30](https://github.com/goodfire-ai/causalab/commit/8e8d5d1f8f9ca8f42bfce7c6b5eef194f012660e) | Causal hypotheses, DAS/DBM and intervention protocols; excellent non-SAE omission. Weekly internal→public mirror; September 30 sync; issue #79 closure was a transfer, not proof of fix (current fix status unknown). Quote: [“Causalab helps you test hypotheses about how neural networks solve tasks.”](https://github.com/goodfire-ai/causalab/blob/8e8d5d1f8f9ca8f42bfce7c6b5eef194f012660e/README.md) |
| [ndif-team/nnterp](https://github.com/ndif-team/nnterp) | 4 / 121 | 2024-08-08 → [2026-07-02](https://github.com/ndif-team/nnterp/commit/b4a31274692f986e493ac5d20ba20a4ec8640955) | NNsight-native naming/accessor layer; nest under nnsight rather than present as an independent execution engine. July packaging fix; active October maintainer discussion, upcoming vLLM/NNsight 0.8 redesign is not current main. Quote: [“preserves the original HuggingFace implementations”](https://github.com/ndif-team/nnterp/blob/b4a31274692f986e493ac5d20ba20a4ec8640955/README.md) |
| [google-deepmind/mishax](https://github.com/google-deepmind/mishax) | 3 / 158 | 2024-07-30 → [2026-09-16](https://github.com/google-deepmind/mishax/commit/c143e3b5142f6b6967eba46ce1eb6aab53f15a7c) | Genuinely distinct JAX/Flax AST instrumentation; September source-validation fix. Has tests/CI; AST patching needs care, not universally portable HF hooks. Quote: [“For mechanistic interpretability this can be used to stick probes in the model and intervene at arbitrary locations.”](https://github.com/google-deepmind/mishax/blob/c143e3b5142f6b6967eba46ce1eb6aab53f15a7c/README.md) |
| [UFO-101/auto-circuit](https://github.com/UFO-101/auto-circuit) | 3 / 103 | 2023-08-21 → [2026-08-17](https://github.com/UFO-101/auto-circuit/commit/7242291d0e5da5c9c044cd6cb97ab911be9adabf) | Reusable edge patching/discovery/evaluation on TransformerLens. August 2026 bugfix closed issue #17 in six days; old v1.0.1 release August 2024. Better default than original ACDC. Quote: [“A library for efficient patching and automatic circuit discovery”](https://github.com/UFO-101/auto-circuit/blob/7242291d0e5da5c9c044cd6cb97ab911be9adabf/README.md) |
| [hannamw/EAP-IG](https://github.com/hannamw/EAP-IG) | 3 / 89 | 2024-01-15 → [2026-05-23](https://github.com/hannamw/EAP-IG/commit/e24bafd3d22af2c59ac5a83e0a6581b89b5c05dd) | Reusable EAP/EAP-IG and exact-patching comparison, not just paper scripts. May 2026 node-attribution fix; no releases/CI observed. Pre-LayerNorm/GQA constraints explicit in README. Quote: [“Use either a greedy-search or top-n approach to find a circuit of a given size based on these scores”](https://github.com/hannamw/EAP-IG/blob/e24bafd3d22af2c59ac5a83e0a6581b89b5c05dd/README.md) |
### B. Natural-language research artifacts

| Repository | H≈ / stars | Created → latest main commit | Fit, persistence and primary-source quote |
|---|---:|---|---|
| [adamkarvonen/activation_oracles](https://github.com/adamkarvonen/activation_oracles) | 2 / 103 | 2025-07-30 → [2026-09-26](https://github.com/adamkarvonen/activation_oracles/commit/5712762cfc29a18d6414a1cf2cccb4ff4432ced5) | Strongest adjacent-to-NLA omission: trained activation QA, not reconstruction. Maintained main vs paper branch explicitly separated; September 26 transformers-5/Qwen3.6 support; new HF checkpoint September 25. Quote: [“answer arbitrary questions about them in natural language”](https://github.com/adamkarvonen/activation_oracles/blob/5712762cfc29a18d6414a1cf2cccb4ff4432ced5/README.md) |
| [TransluceAI/introspective-interp](https://github.com/TransluceAI/introspective-interp) | 2 / 38 | 2025-12-22 → [2026-07-07](https://github.com/TransluceAI/introspective-interp/commit/594d53348734097857430826d88f5c6856164de7) | Feature descriptions, activation-patching effects and input ablations. Research training/evaluation artifact, not interchangeable with NLA. July 2026 learning-rate correction; README requests 2×80GB H100 by default. Quote: [“We train language models to produce three types of explanations of their own computations.”](https://github.com/TransluceAI/introspective-interp/blob/594d53348734097857430826d88f5c6856164de7/README.md) |
| [aypan17/latentqa](https://github.com/aypan17/latentqa) | 1 / 37 | 2024-12-12 → [2025-11-16](https://github.com/aypan17/latentqa/commit/a2dcb6f8eef52ce8c8e75ee71da66cb880f727f4) | Foundational activation-language decoder; November 2025 Qwen/Gemma extension. One attributed account, no releases/CI; classify paper code + weights, not a broad maintained library. Quote: [“we finetune a decoder LLM to learn to read from and write to a target LLM's activations in natural language.”](https://github.com/aypan17/latentqa/blob/a2dcb6f8eef52ce8c8e75ee71da66cb880f727f4/README.md) |
| [safety-research/introspection-adapters](https://github.com/safety-research/introspection-adapters) | 1 / 30 | 2026-04-28 → [2026-04-28](https://github.com/safety-research/introspection-adapters/commit/92a3b05ac1c472b76b966c441d11b88c1b7b76ec) | April 2026 self-reporting of learned behaviors, distinct from decoding target activation vectors. One-day public release burst, no subsequent default-branch commits; Anthropic grading/API and substantial GPU requirements. Quote: [“LoRA adapters that enable language models to verbalize the behaviors trained into them.”](https://github.com/safety-research/introspection-adapters/blob/92a3b05ac1c472b76b966c441d11b88c1b7b76ec/README.md) |
### C. Non-SAE circuit research artifact

| Repository | H≈ / stars | Created → latest main commit | Fit, persistence and primary-source quote |
|---|---:|---|---|
| [TransluceAI/circuits](https://github.com/TransluceAI/circuits) | 1 / 41 | 2026-01-15 → [2026-04-10](https://github.com/TransluceAI/circuits/commit/2d215d4ba016ba8602b69d71fc0f1ad139a427b7) | ADAG/neuron-basis tracing + automated descriptions: valuable non-SAE counterweight. January initial commit + April ADAG release only; reuses circuit-tracer frontend but has independent attribution/analysis implementation. README explicitly credits Claude Code; account count is not authorship proof. Quote: [“This library includes circuit tracing code for MLP neurons”](https://github.com/TransluceAI/circuits/blob/2d215d4ba016ba8602b69d71fc0f1ad139a427b7/README.md) |
### D. Adjacent/research infrastructure

| Repository | H≈ / stars | Created → latest main commit | Fit, persistence and primary-source quote |
|---|---:|---|---|
| [EleutherAI/bergson](https://github.com/EleutherAI/bergson) | 15 / 99 | 2025-05-14 → [2026-10-06](https://github.com/EleutherAI/bergson/commit/e741b8c3339c9ae1c35fee79240cd4cf6d483130) | Very strong breadth/maintenance, but training-data influence rather than internal circuit discovery. Put in separate attribution subsection. v2.2.3 October 6; >=100 commits in 90 days; latest three CI runs successful. Quote: [“Data attribution methods estimate the effect on a behavior of interest of removing data points from a model's training corpus.”](https://github.com/EleutherAI/bergson/blob/e741b8c3339c9ae1c35fee79240cd4cf6d483130/README.md) |
| [google-deepmind/treescope](https://github.com/google-deepmind/treescope) | 11 / 476 | 2024-07-24 → [2026-06-18](https://github.com/google-deepmind/treescope/commit/20a94822d0c4c0a55c10eaa8fed96a77757f4068) | Independent tensor/model visualization, extracted from Penzai, supports PyTorch/Flax/Equinox; not a causal method. June 2026 PyTorch compatibility fix; v0.1.10 August 2025. Quote: [“interactive HTML pretty-printer”](https://github.com/google-deepmind/treescope/blob/20a94822d0c4c0a55c10eaa8fed96a77757f4068/README.md) |
| [stanfordnlp/pyreft](https://github.com/stanfordnlp/pyreft) | 10 / 1,590 | 2024-02-17 → [2025-02-06](https://github.com/stanfordnlp/pyreft/commit/dafd0995a366d7b47160a337dcc388eda7431821) | Distinct trainable representation intervention built on pyvene; group under Adapters/ReFT, not duplicate pyvene hook engine. Last main commit February 2025 checkpointing fix; many later open user questions, no 2026 code observed. Quote: [“Training ReFT with any pretrained LMs on HuggingFace”](https://github.com/stanfordnlp/pyreft/blob/dafd0995a366d7b47160a337dcc388eda7431821/README.md) |
| [google-deepmind/tracr](https://github.com/google-deepmind/tracr) | 9 / 568 | 2022-12-01 → [2024-02-05](https://github.com/google-deepmind/tracr/commit/9ce2b8c82b6ba10e62e86cf6f390e7536d4fd2cd) | Known-circuit ground-truth/compiler research tool; archived, February 2024 tip. Valuable reference, NOT maintained JAX tooling. Quote: [“Compile a RASP program to transformer weights.”](https://github.com/google-deepmind/tracr/blob/9ce2b8c82b6ba10e62e86cf6f390e7536d4fd2cd/tracr/compiler/compiling.py) |
| [google-deepmind/gemma_penzai](https://github.com/google-deepmind/gemma_penzai) | 1 / 98 | 2026-01-05 → [2026-01-13](https://github.com/google-deepmind/gemma_penzai/commit/6f9b4129c8cf52fd3de8d610bc1b670bcc9f33ed) | New 2026 Gemma 3 multimodal extension, actual vision/MLLM implementation rather than bare reexport. Nest under Penzai; three January commits only, no releases/tests/CI observed. Quote: [“Now we extend Penzai with vision and multimodal support.”](https://github.com/google-deepmind/gemma_penzai/blob/6f9b4129c8cf52fd3de8d610bc1b670bcc9f33ed/README.md) |
### E. Optional feature-explanation library

| Repository | H≈ / stars | Created → latest main commit | Fit, persistence and primary-source quote |
|---|---:|---|---|
| [EleutherAI/delphi](https://github.com/EleutherAI/delphi) | 22 / 279 | 2024-06-18 → [2026-08-25](https://github.com/EleutherAI/delphi/commit/4fea06e6e8b68eeaf302474325fca13df95c5d6f) | Highest attributed breadth here, but narrow task fit: automated feature explanations/scoring, not raw-activation NLAs. Include at most one compact SAE/feature-explanation entry; August 2026 fixes, v0.1.3 March. Last three observed weekly CI runs failed. Quote: [“utilities for generating and scoring text explanations of sparse autoencoder (SAE) and transcoder features.”](https://github.com/EleutherAI/delphi/blob/4fea06e6e8b68eeaf302474325fca13df95c5d6f/README.md) |
### F. Demo/platform

| Repository | H≈ / stars | Created → latest main commit | Fit, persistence and primary-source quote |
|---|---:|---|---|
| [ndif-team/workbench](https://github.com/ndif-team/workbench) | 7 / 18 | 2025-05-20 → [2026-09-18](https://github.com/ndif-team/workbench/commit/416fc8b26e46debdc435c4a88f0379ae60335138) | 2026-updated interactive NNsight/NDIF platform; independent UI worth a demo entry, not another Python hook library. September tutorial updates and successful CI; activation-patching route delegates to nnsightful. Quote: [“Workbench** is a UI for doing exploratory analysis on open source AI models”](https://github.com/ndif-team/workbench/blob/416fc8b26e46debdc435c4a88f0379ae60335138/README.md) |

## Late parent-network supplement (incorporated without restarting discovery)

The parent forwarded four additional 2026 discoveries after the bounded pass. I inspected their primary READMEs, contributor pages, default-branch tips, release records and actual source. **No additional repository searches** were used. This brings source/metadata inspection to **30 repositories total**; retain the original 20-entry bounded table as the initial shortlist, with these four as an explicitly separate refinement. Interp-engine is the strongest newly discovered task-fit omission and should replace a lower-priority reference/adjacent entry if the final list must stay at 20. The stars-sorted broad search underrepresented very new low-star engines; this is a concrete residual discovery bias.

| Late candidate / category | H≈ / stars; retained accounts | Created → latest default-branch commit | Fit, source and short verbatim quote |
|---|---|---|---|
| [decoderesearch/interp-engine](https://github.com/decoderesearch/interp-engine) — Fast-inference hook library | 1 / 39; `hijohnnylin` | 2026-08-05 → [2026-10-02](https://github.com/decoderesearch/interp-engine/commit/eb9bb6d992e73d7624965583dd945ec15f0c510e) (`main`) | Strong independent entry: original HookManager read/write substrate, 34 eager points vs 28 vLLM points, plus static/capture-capable and generation-only backends. Validator covers cross-engine/architecture comparisons. v1.12.0 September 28; tip October 2; persistence only August–October so far. Source is not a bare nnsight reexport. Benchmarks and correctness claims are author-reported, not locally reproduced. [Source `interp_engine/hooks.py`](https://github.com/decoderesearch/interp-engine/blob/eb9bb6d992e73d7624965583dd945ec15f0c510e/interp_engine/hooks.py); [README quote “fast, standardized (34 'points'/addresses across architectures)”](https://github.com/decoderesearch/interp-engine/blob/eb9bb6d992e73d7624965583dd945ec15f0c510e/README.md). |
| [ninjahawk/Subtext](https://github.com/ninjahawk/Subtext) — Jacobian-lens conversational demo | 2 / 245; `ninjahawk`, `markedwardcampos` | 2026-07-06 → [2026-07-23](https://github.com/ninjahawk/Subtext/commit/eb9207c409c4baabe32881c5050d624abdeca607) (`main`) | Useful nested demo under the already-listed Jacobian Lens: streaming chat, reading-phase lens, replay and per-token inspection. Source imports jlens and loads Neuronpedia lens weights; not a new decoding method. Last tip July 23, no GitHub release; star-chart automation is excluded from H≈. Do not describe vocabulary readouts as full hidden reasoning or subjective experience. [Source `server.py`](https://github.com/ninjahawk/Subtext/blob/eb9207c409c4baabe32881c5050d624abdeca607/server.py); [README quote “Each rendered word is a lens readout, not model output.”](https://github.com/ninjahawk/Subtext/blob/eb9207c409c4baabe32881c5050d624abdeca607/README.md). |
| [canivel/dynolab](https://github.com/canivel/dynolab) — Apple Silicon/MLX research platform | 1 / 163; `canivel` | 2026-09-04 → [2026-10-04](https://github.com/canivel/dynolab/commit/cf88c039f2dac338c66786aaf720182ccc79babf) (`main`) | New, active local Mac workbench with genuine single-site patch sweeps, controls, probes and saved studies; independent platform entry rather than generic hook engine. Source bounds sweeps to 128 layer/token sites and requires aligned/equal-token prompts; explicitly not a full circuit graph. v0.5.2 October 4; one attributed developer and one-month persistence only. [Source `src/dyno/lab/patching.py`](https://github.com/canivel/dynolab/blob/cf88c039f2dac338c66786aaf720182ccc79babf/src/dyno/lab/patching.py); [README quote “Full circuit tracing and pretrained SAE imports are not currently included.”](https://github.com/canivel/dynolab/blob/cf88c039f2dac338c66786aaf720182ccc79babf/README.md). |
| [guidelabs/steerling](https://github.com/guidelabs/steerling) — Interpretable-by-design model + inference package | 3 / 241; `ayaabdelsalam91`, `adebayoj`, `giangnguyen2412` | 2026-02-22 → [2026-07-14](https://github.com/guidelabs/steerling/commit/f34ffa89e46969445f3cf6e7c885e9623a2047c1) (`main`) | Distinct architecture/model artifact rather than post-hoc arbitrary-model toolkit. Actual concept-head implementation supports known/discovered concepts and known-head interventions. Non-autoregressive/block-causal masked diffusion, ~8B model, at least 18GB GPU memory; training/fine-tuning code not included, training-data attribution not currently supported. Main tip July 14; no GitHub release observed. Apache source license does not settle model-weight commercial terms. [Source `steerling/models/interpretable/concept_head.py`](https://github.com/guidelabs/steerling/blob/f34ffa89e46969445f3cf6e7c885e9623a2047c1/steerling/models/interpretable/concept_head.py); [README quote “An interpretable causal diffusion language model.”](https://github.com/guidelabs/steerling/blob/f34ffa89e46969445f3cf6e7c885e9623a2047c1/README.md). |

### Existing-entry and method-category corrections from the same handoff

- **TransformerLens 4.x:** inspected the parent-fetched primary README at `slop/research/20261007_interpretability/evidence_existing/github/TransformerLensOrg__TransformerLens/README.md`. It says **“`TransformerBridge` is the recommended path”** and **“By default it preserves raw HuggingFace weights – logits and activations match HF”**; legacy `HookedTransformer.from_pretrained` was removed in v4.0. Do not retain the list’s blanket “not as HuggingFace-compatible” characterization or nnterp-vs-TL comparisons based solely on legacy weight transformations. Compatibility mode restores legacy numerics; actual library/backend/version still matters. Parent supplies a 192-account attributed nonbot TL estimate; I did not independently recount TL in this lane.
- Canonical redirects verified again with core APIs: **`jbloomAus/SAELens` → `decoderesearch/SAELens`** (1,550 stars) and **`safety-research/circuit-tracer` → `decoderesearch/circuit-tracer`** (2,915). This corrects slugs, not a recommendation to add many SAE entries.
- **Activation Oracles:** activation-question answering about representations, not an NLA reconstruction objective. The parent verified that the [Anthropic introduction](https://alignment.anthropic.com/2025/activation-oracles/) explicitly frames them as non-mechanistic; place in “activation decoding / natural-language methods,” not unqualified causal-mechanistic circuit tooling. My direct blog HTTP request returned 403, so that specific framing is parent-attested rather than a locally fetched verbatim quote. GitHub code/README and HF artifacts were independently verified above.
- **Introspection Adapters:** [official introduction](https://alignment.anthropic.com/2026/introspection-adapters/) supplied by parent; self-report learned behavior for weight/adapter auditing, **not an activation decoder**. The independently fetched GitHub README supports this distinction. My direct blog request also returned 403.
- **Predictive Concept Decoders:** independently fetched [Transluce PCD post](https://transluce.org/pcd), dated 2025-12-18. Quote: **“An encoder that compresses model activations to a sparse list of concepts”**, paired with **“A decoder that takes these concepts and answers questions about model behaviors.”** The encoder cannot see the question; training is grounded in predicted future behavior rather than reconstruction. [decoder.transluce.org](https://decoder.transluce.org/) is the linked demo. No concrete GH repository/HF artifact link was identified in the post (only an org link and an unrelated Llama issue); code/license/checkpoint/maintenance metrics remain unknown. Treat as reading + demo, not an available library or generic SAE trainer.
- **Docent:** parent is correcting the existing entry from “model explanation and steering” toward agent-evaluation/transcript auditing, supported by the introducing-Docent post; do not conflate it with activation-language decoders or Workbench.

Supplement residual risks: none of these packages/apps was installed or executed; source existence/author validator claims are not replicated performance evidence. New low-breadth repositories have weeks/months, not years, of demonstrated persistence. TL human breadth and the AO/IA official-blog framing are explicitly parent-attested seams.

## Contributor attribution audit

The following are the accounts used in H≈, not verified legal identities or proof of human-written work. Each list is unique within its repo; causalab aliases are qualified above. All were obtained from the fully exhausted contributors page, not commit counts or issue authors.

| Repository | Attributed non-service accounts retained |
|---|---|
| decoderesearch/circuit-tracer | `hannamw`, `hijohnnylin`, `speediedan`, `mntss`, `1wheel`, `Andrey170170`, `CatOfTheCannals`, `danra`, `chanind`, `JadenFiotto-Kaufman`, `jakobhansen-blai`, `Kymi808`, `robbiebusinessacc`, `Rome-1`, `s-ewbank`, `Xwwan`, `yanivnik` |
| TransformerLensOrg/CircuitsVis | `alan-cooney`, `danbraunai`, `OliverBalfour`, `neelnanda-io`, `nelhage`, `bryce13950`, `luciaquirke`, `andyrdt`, `colah`, `quinn-dougherty`, `UFO-101`, `dkamm` |
| FOR-sight-ai/interpreto | `AntoninPoche`, `fanny-jourdan`, `thomas-mullor`, `gsarti`, `fredericboisnard`, `cofri`, `clayecharlotte`, `camillebrl`, `gfouilhe`, `HugoDeBosschere` |
| goodfire-ai/causalab | `canrager`, `can-goodfire`, `lepoissonfroid`, `maxsloef-goodfire`, `AmirZur`, `maxsloef`, `ScottBrenner`, `atticusg` |
| ndif-team/nnterp | `Butanium`, `JadenFiotto-Kaufman`, `irajmoradi`, `can-goodfire` |
| google-deepmind/mishax | `jkramar`, `sonnerat`, `h-joo` |
| UFO-101/auto-circuit | `UFO-101`, `oliveradk`, `HanifiAkdag` |
| hannamw/EAP-IG | `hannamw`, `Fukata-K`, `G-structure` |
| adamkarvonen/activation_oracles | `adamkarvonen`, `thejaminator` |
| TransluceAI/introspective-interp | `belindal`, `choidami` |
| aypan17/latentqa | `aypan17` |
| safety-research/introspection-adapters | `k-shenoy` |
| TransluceAI/circuits | `aryamanarora` |
| EleutherAI/bergson | `luciaquirke`, `taylorbelrose`, `LouisYRYJ`, `brendanlong`, `davidoj`, `zywilliamli`, `jammastergirish`, `mmulet`, `smarter`, `darkness8i8`, `SrGonao`, `prajak002`, `dipikakhullar`, `MoritzWeckbecker`, `neverix` |
| google-deepmind/treescope | `danieldjohnson`, `marksandler2`, `pitmonticone`, `afspies`, `cgarciae`, `kochkov92`, `evdcush`, `jsoref`, `mhuebert`, `superbobry`, `ddelgadovargas-cyber` |
| stanfordnlp/pyreft | `frankaging`, `aryamanarora`, `PinetreePantry`, `AmirZur`, `Vikrant-Khedkar`, `ana-ai-sde`, `bbrowning`, `eltociear`, `ramvenkat98`, `savadikarc` |
| google-deepmind/tracr | `mrahtz`, `david-lindner`, `William-Baker`, `langosco`, `vmikulik`, `eltociear`, `neelnanda-io`, `hawkinsp`, `saran-t` |
| google-deepmind/gemma_penzai | `guxm2021` |
| EleutherAI/delphi | `cadentj`, `luciaquirke`, `SrGonao`, `AlexTMallen`, `neverix`, `taylorbelrose`, `hijohnnylin`, `alexandersumer`, `TheodoreEhrenborg`, `anthonyduong9`, `aashiqmuhamed`, `d0rbu`, `eltociear`, `kmaherx`, `lucyfarnik`, `StellaAthena`, `zywilliamli`, `ghidav`, `frankyaoxiao`, `mahbubcseju`, `WatchTree-19`, `robbiebusinessacc` |
| ndif-team/workbench | `cadentj`, `AdamBelfki3`, `jon-bell`, `haplesshero13`, `skysneakers`, `JadenFiotto-Kaufman`, `gsarti` |

## Implementation evidence (not merely descriptions)

Read the primary READMEs and following source/docs at the audited default-branch tip. No code was run. Tree/workflow presence is a signal, not successful local validation.

| Repository | Inspected implementation / docs |
|---|---|
| decoderesearch/circuit-tracer | [`circuit_tracer/attribution/attribute.py`](https://github.com/decoderesearch/circuit-tracer/blob/7f66876689f59e92fc3641650d38b8bd41749ec4/circuit_tracer/attribution/attribute.py) |
| TransformerLensOrg/CircuitsVis | [`python/circuitsvis/attention.py`](https://github.com/TransformerLensOrg/CircuitsVis/blob/512040a1344186a80f64f04fb9b22fa121edfebd/python/circuitsvis/attention.py) |
| FOR-sight-ai/interpreto | [`interpreto/lens/logit_lens.py`](https://github.com/FOR-sight-ai/interpreto/blob/b3b9a0fcbb46b891d0029d89a6561307114073a0/interpreto/lens/logit_lens.py) |
| goodfire-ai/causalab | [`docs/hypothesis_analysis.md`](https://github.com/goodfire-ai/causalab/blob/8e8d5d1f8f9ca8f42bfce7c6b5eef194f012660e/docs/hypothesis_analysis.md) |
| ndif-team/nnterp | [`nnterp/standardized_transformer.py`](https://github.com/ndif-team/nnterp/blob/b4a31274692f986e493ac5d20ba20a4ec8640955/nnterp/standardized_transformer.py) |
| google-deepmind/mishax | [`mishax/ast_patcher.py`](https://github.com/google-deepmind/mishax/blob/c143e3b5142f6b6967eba46ce1eb6aab53f15a7c/mishax/ast_patcher.py) |
| UFO-101/auto-circuit | [`auto_circuit/prune_algos/edge_attribution_patching.py`](https://github.com/UFO-101/auto-circuit/blob/7242291d0e5da5c9c044cd6cb97ab911be9adabf/auto_circuit/prune_algos/edge_attribution_patching.py) |
| hannamw/EAP-IG | [`src/eap/attribute.py`](https://github.com/hannamw/EAP-IG/blob/e24bafd3d22af2c59ac5a83e0a6581b89b5c05dd/src/eap/attribute.py) |
| adamkarvonen/activation_oracles | [`nl_probes/sft.py`](https://github.com/adamkarvonen/activation_oracles/blob/5712762cfc29a18d6414a1cf2cccb4ff4432ced5/nl_probes/sft.py) |
| TransluceAI/introspective-interp | [`dataloaders/act_patch.py`](https://github.com/TransluceAI/introspective-interp/blob/594d53348734097857430826d88f5c6856164de7/dataloaders/act_patch.py) |
| aypan17/latentqa | [`lit/utils/activation_utils.py`](https://github.com/aypan17/latentqa/blob/a2dcb6f8eef52ce8c8e75ee71da66cb880f727f4/lit/utils/activation_utils.py) |
| safety-research/introspection-adapters | [`scripts/train_ia.sh`](https://github.com/safety-research/introspection-adapters/blob/92a3b05ac1c472b76b966c441d11b88c1b7b76ec/scripts/train_ia.sh) |
| TransluceAI/circuits | [`circuits/core/attribution.py`](https://github.com/TransluceAI/circuits/blob/2d215d4ba016ba8602b69d71fc0f1ad139a427b7/circuits/core/attribution.py) |
| EleutherAI/bergson | [`bergson/__main__.py`](https://github.com/EleutherAI/bergson/blob/e741b8c3339c9ae1c35fee79240cd4cf6d483130/bergson/__main__.py) |
| google-deepmind/treescope | [`treescope/_internal/api/arrayviz.py`](https://github.com/google-deepmind/treescope/blob/20a94822d0c4c0a55c10eaa8fed96a77757f4068/treescope/_internal/api/arrayviz.py) |
| stanfordnlp/pyreft | [`pyreft/interventions.py`](https://github.com/stanfordnlp/pyreft/blob/dafd0995a366d7b47160a337dcc388eda7431821/pyreft/interventions.py) |
| google-deepmind/tracr | [`tracr/compiler/compiling.py`](https://github.com/google-deepmind/tracr/blob/9ce2b8c82b6ba10e62e86cf6f390e7536d4fd2cd/tracr/compiler/compiling.py) |
| google-deepmind/gemma_penzai | [`gemma_penzai/mllm/models/gemma_multimodal.py`](https://github.com/google-deepmind/gemma_penzai/blob/6f9b4129c8cf52fd3de8d610bc1b670bcc9f33ed/gemma_penzai/mllm/models/gemma_multimodal.py) |
| EleutherAI/delphi | [`delphi/explainers/default/default.py`](https://github.com/EleutherAI/delphi/blob/4fea06e6e8b68eeaf302474325fca13df95c5d6f/delphi/explainers/default/default.py) |
| ndif-team/workbench | [`workbench/_api/routes/activation_patching.py`](https://github.com/ndif-team/workbench/blob/416fc8b26e46debdc435c4a88f0379ae60335138/workbench/_api/routes/activation_patching.py) |

Important source distinctions:
- **nnterp** defines `StandardizedTransformer(LanguageModel)` with renaming/accessors: a substantive compatibility layer, but underlying execution is NNsight. Keep a nested entry.
- **PyReFT** implements several `*reftIntervention` classes and training/configuration beyond Pyvene. An independent entry under Adapters is justified, with the stale default-branch date.
- **Interpreto** vendors Overcomplete and has its own `LogitLens(nn.Module)`; its docstring warns early-layer scores are rankings, not calibrated probabilities. Independent multi-method toolbox entry is justified; do not separately promote every vendored method.
- **ADAG** implements MLP/logit/embed attribution buffers and tracing, then borrows the circuit-tracer visualization frontend. Not merely a reexport; independent neuron-basis research entry justified.
- **Gemma Penzai** implements multimodal attention masks, `StitchEmbeddings`, vision layers and a multimodal transformer. More than a wrapper, but model-specific and release-burst-only; nested Penzai extension is enough.
- **Treescope** implements array/model rendering independent of Penzai. A visualization entry, not an archived-Penzai duplicate.
- **Workbench** supplies a genuine UI/API but its patching endpoint delegates to `nnsightful.tools.activation_patching`; count as platform/demo.

## Maintenance caveats requiring careful wording

- [Causalab #79](https://github.com/goodfire-ai/causalab/issues/79): September 1 maintainer comment: **“The bug itself is real and unchanged”**; moved to private internal source of truth with weekly mirror sync. Closed≠fixed; whether subsequent syncs fixed it is unknown. Its newest observed CI set is mixed (failure October 5, successful main sync September 30). Do not promise all intervention sites are correct.
- [circuit-tracer #115](https://github.com/decoderesearch/circuit-tracer/issues/115): initial TransformerLens-4 compatibility concern is clarified in the comment: **“existing `pip install circuit-tracer` users are not broken yet.”** Current main’s transformers cap prevents TL4; an open upgrade needs the upper bound. Not evidence that current default-branch installs fail.
- [nnterp #53](https://github.com/ndif-team/nnterp/issues/53): active maintainer discussion acknowledges residual-contribution accessors/post-sublayer norms and redesign in dev/NNsight 0.8. Closed after related PRs, but main tip remains July 2. Do not substitute dev activity for default-branch maintenance.
- CircuitsVis’s April 2026 tip is devcontainer removal, not renewed visualization development; treescope’s June tip is a real PyTorch compatibility patch. Both last releases predate their tips.
- ACDC’s **43** attributed user accounts include inherited TransformerLens history (`neelnanda-io` has 268 contributions). Do not rank it as 43 current circuit researchers; README explicitly recommends AutoCircuit instead.
- Main commit dates are not a license to call projects “abandoned.” Prefer “last default-branch commit YYYY-MM-DD,” “archived,” “reference artifact,” or specific maintainer statements. GitHub releases can also lag PyPI; absence here is not proof of no package release.

## Exclusions, canonical slugs and unresolved anchors

| Candidate | Decision / evidence |
|---|---|
| `safety-research/circuit-tracer` | API redirects to **`decoderesearch/circuit-tracer`** (2,915 stars). Use canonical slug for link/badge; some README links still use old owner. |
| `EleutherAI/auto-circuit` | Fork, 2 stars; parent API identifies **`UFO-101/auto-circuit`**, 103 stars. Do not add fork as independent tool. |
| `faith-and-fate/EAP-IG` | 404; correct verified slug **`hannamw/EAP-IG`**. |
| `kitft/nla-inference` | Already linked from existing NLA entry. 41 stars, H≈1, created 2026-03-11, single reachable main commit 2026-05-07. Source has `NLAClient`/`NLACritic`, SGLang input-embeds and a reconstruction scorer; inference convenience is real, but a second top-level NLA listing would double-count. |
| `kitft/natural_language_autoencoders` | Already listed. 955-star snapshot; keep existing AV/AR and inference link. No omission claim or replacement by generic SAE tools. |
| `ArthurConmy/Automatic-Circuit-Discovery` | 298 stars, raw 43 attributed accounts with inherited history, created 2022-10-28; tip 2024-10-01. README: “this codebase has many sharp edges” and recommends AutoCircuit. Historical/paper reference only. |
| `anthropics/attribution-graphs-frontend` | 102 stars, H≈1; created/tip 2025-03-27; archived. README calls it “Snapshot of the frontend code”. Superseded for most users by circuit-tracer/Neuronpedia; not a separate active library. |
| `goodfire-ai/r1-interpretability` | 184 stars, H≈3, created 2025-04-15→tip 2025-04-21. SAE weights + SQL activation data + loader/notebooks; release artifact/dataset, not general tooling. |
| `goodfire-ai/sdxl-turbo-interpretability` | 51 stars, H≈2, created 2025-05-20→tip 2025-05-27. SAE weights + one inference notebook/loader; multimodal artifact, not evidence of maintained multimodal library. |
| `ndif-team/nnsight-vllm-demos` | 3 stars, H≈1, created 2026-02-25→tip 2026-02-27. Demos for fast-inference hooks; useful nnsight sublink, not a third generic vLLM hook library (vLLM-Hook/vllm-lens already listed). |
| `mhlinder/diatoms` | Wrong homonym: 2014 colored algae-inspired sketch, not interpretability. Actual “diatoms” anchor unresolved; do not recommend this slug. |
| `interp-methods` | `UKGovernmentBEIS/interp-methods` 404, exact README code search returned zero. Canonical repository unknown, not verified absent. |
| `introspection` | `TransluceAI/introspection` 404; verified natural-language counterpart is **`TransluceAI/introspective-interp`**. `safety-research/introspection-mechanisms` is separate one-paper code (46 stars, created November 2025) rather than a general method library. |
| `talkative probes` | `kitft/talkative-probes` 404, exact GitHub README code search zero. HF `sensharma/Llama-3.2-3B_Talkative_Probe_Step-3000` exists but card only declares license; source, paper identity and maintenance unknown. Keep as unresolved lead, not supported shortlist. |
| `SamuelMarks` network | Wrong author homonym; discarded from mechanistic conclusions. Correct author is **`saprmarks`**; discovered `feature-circuits` (225), `dictionary_learning` (431), `geometry-of-truth` (117). Not deeply verified in this bounded pass; feature-circuits is a useful historical pointer, not an extra library recommendation. |

## Public HF checks for natural-language methods

No authentication/token used for HF. `/api/models/{id}` verifies these published artifacts; likes/downloads are HF fields, not stars, contributor breadth or proof of use. `lastModified` is **not** relabeled as latest commit. NLAs have matching AV/AR checkpoints, so keep their existing placement.

| Model | Created / lastModified (UTC dates) | Likes / snapshot downloads |
|---|---|---:|
| [kitft/nla-qwen2.5-7b-L20-av](https://huggingface.co/kitft/nla-qwen2.5-7b-L20-av) ([API](https://huggingface.co/api/models/kitft/nla-qwen2.5-7b-L20-av)) | 2026-03-16 / 2026-05-07 | 7 / 819 |
| [kitft/nla-qwen2.5-7b-L20-ar](https://huggingface.co/kitft/nla-qwen2.5-7b-L20-ar) ([API](https://huggingface.co/api/models/kitft/nla-qwen2.5-7b-L20-ar)) | 2026-03-16 / 2026-05-07 | 8 / 423 |
| [aypan17/latentqa_llama-3-8b-instruct](https://huggingface.co/aypan17/latentqa_llama-3-8b-instruct) ([API](https://huggingface.co/api/models/aypan17/latentqa_llama-3-8b-instruct)) | 2024-12-11 / 2024-12-13 | 6 / 0 |
| [adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3.6-27B](https://huggingface.co/adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3.6-27B) ([API](https://huggingface.co/api/models/adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3.6-27B)) | 2026-09-25 / 2026-09-25 | 0 / 20 |

## Presentation/grouping implications

1. Split “Mechanistic interpretability libraries” into **execution/hooks & compatibility**, **causal interventions/circuit discovery**, **activation decoding & natural-language methods**, and **visualization/platforms**. Add “Research artifacts / reference implementations” so paper code does not masquerade as maintained libraries.
2. Put PyReFT next to adapters/trainable interventions, Bergson under data attribution, Tracr under ground-truth/reference tools, Workbench/Neuronpedia/Docent under demos/platforms. Datasets/model weights belong in an artifacts subsection, not the tool table.
3. Give NLAs, Activation Oracles, LatentQA, and introspective methods a coherent comparison: reconstruction round trip vs supervised activation QA vs models explaining their own computations vs behavior-reporting adapters. None is established ground truth for faithful natural-language interpretation. Reconstruction agreement alone does not certify causal completeness or absence of omitted information.
4. Keep SAEs proportional: the circuit-tracer entry can explain its transcoder dependency, plus at most one Delphi feature-explanation entry; group Goodfire model/data artifacts rather than many independent library bullets. Include ADAG’s neuron-basis approach to avoid implying dictionary features are the only circuit basis.
5. Use stable one-line descriptions with substrate/model scope (HF-native, TransformerLens, Pyvene, JAX/Flax, vLLM/SGLang), package-vs-paper-vs-demo label, archive status and dated evidence. Drop undated “promising but abandoned” judgments unless sourced. Stars badges can remain, but keep dated research metadata separate from the durable README.

## Search audit and bounded coverage

**Seven repository searches exactly**, each authenticated `gh api -X GET search/repositories -f q=... -f per_page=100 -f sort=stars`. No search/issues used. 700 returned rows, **590 unique repository-search candidates screened by name/description and task fit**; many irrelevant lists/infrastructure rows were discarded. Search1 yielded the best direct tooling. The other broad README queries were very noisy; treat this as a discovery limitation, not evidence of completeness.

| # | Exact query | API total_count | Returned |
|---|---|---:|---:|
| 1 | `"mechanistic interpretability" in:name,description,readme stars:>10` | 342 | 100 |
| 2 | `circuit interpretability in:name,description,readme stars:>5` | 2046 | 100 |
| 3 | `"activation" "language" "interpretability" in:description,readme pushed:>=2026-01-01 stars:>3` | 3154 | 100 |
| 4 | `nnterp OR diatoms OR interp-methods OR latentqa OR talkative OR introspection in:name` | 2076 | 100 |
| 5 | `"interpretability" "JAX" in:readme stars:>3` | 635 | 100 |
| 6 | `"interpretability" "vllm" in:readme stars:>3` | 918 | 100 |
| 7 | `"representation" "natural language" in:description,readme created:>=2025-01-01 stars:>5` | 1402 | 100 |

Core network discovery (not repository searches): paginated `/users/{owner}/repos?per_page=100` for `ndif-team`, `UKGovernmentBEIS`, `goodfire-ai`, `TransluceAI`, `anthropics`, `EleutherAI`, `ArthurConmy`, `jblumenk`, `SamuelMarks` (wrong homonym), `kitft`, `mhlinder` (wrong diatoms homonym), `aypan17`, `safety-research`, `TransformerLensOrg`, `google-deepmind`, `adamkarvonen`, `hannamw`, `UFO-101`, `sensharma`, `Aaquib111`, `Transluce` (wrong org homonym), `Butanium`, `jkminder`, `saprmarks`. These returned **1,982 unique network metadata rows**, **2,554 unique repositories across network + repository searches**; only relevant metadata matches were manually investigated. This is not a claim of 2,554 source inspections.

Three additional authenticated **code** lookups (not repository searches), `/search/code?per_page=50`: `"talkative probes" filename:README.md` (0), `"diatoms" "interpretability" filename:README.md` (9, unrelated time-series/hydrology/diatom material), `"interp-methods" filename:README.md` (0). Counted only for unresolved-slug checks; no extra GitHub repository searches.

**26 repositories deeply inspected** with metadata, all attributed contributors, latest 100 default-branch commits, latest 20 core issues/PR records (non-PR issues separated), latest release, recursive tree, latest three workflow runs. **20 omissions shortlisted**, each README and source/docs inspected; the other six are existing entries, superseded forks/artifacts or demos not worth independent additions. No inferred issue-count metrics or inflated search/issues human counts. Contributor endpoint keys rather than aggregate `contributors_url` counts were used.

Public discovery HTTP: HF `/api/models?search=activation-oracle&limit=50&full=true` (50 results, truncated); `search=talkative` (5); `search=latentqa` (50, truncated). These are leads, not independent GitHub library candidates. ArXiv HTML for `2512.15674` directly linked the canonical Activation Oracles repo; `2412.08686` supplied paper context. OpenAlex `works?search=Talkative%20Probes&per-page=5` and `works?search=diatoms%20interpretability&per-page=5` gave unrelated leads, discarded.

Reproduction endpoint pattern: `gh api repos/OWNER/REPO`; `/contributors?per_page=100&page=N&anon=false`; `/commits?sha=DEFAULT_BRANCH&per_page=100`; `/readme`; `/issues?state=all&sort=updated&direction=desc&per_page=20`; `/releases?per_page=1`; `/git/trees/DEFAULT_BRANCH?recursive=1`; `/actions/runs?per_page=3`; `/contents/PATH?ref=TIP_SHA`. Selected issue comments and service-user profiles were read through core APIs. Primary source/tip permalinks above preserve the audited implementation seam.

### Residual risks

- Runtime compatibility, model fit and test results were not locally validated; API-observed CI is not execution by this research task. Closed issue status does not prove a bug fixed.
- Human breadth is an estimate of attribution/account identity; automation can masquerade as User and real people can share/multiply accounts. Imported history/coauthors/unlinked commits prevent exact human counts.
- Budget-limited/noisy search and uncertain diatoms/interp-methods/talkative-probes anchors leave coverage gaps. New private/internal projects and GitHub code-search indexing gaps are outside verified scope.
- Creation date reflects repository persistence, not idea/publication origin. Several 2026 repositories are one-time uploads; future updates unknown. HF downloads fluctuate and can be zero despite an existing artifact.
- Read-only status check observed untracked `slop/`; this task did not create or touch it. No staged files were reported.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Read target README at requested SHA; screened 590 unique repository-search rows; deeply inspected 26 repositories; delivered 20 source-verified omissions, canonical slugs, source quotes, maintenance qualifications and residual risks. Incorporated parent follow-ups: four additional 2026 projects source-inspected; TL4/HF-native nuance, redirects and AO/NLA/IA/PCD category distinctions recorded."
    }
  ],
  "changedFiles": [
    "/home/code/.pi/agent/sessions/--workspace-2026--/subagent-artifacts/outputs/48cad1b1-6752-4dcf-90e8-1328d9a67622/research/github-mechanisms.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "gh api search/repositories (7 queries; per_page=100)",
      "result": "passed",
      "summary": "700 results / 590 unique candidates; exact queries and counts recorded."
    },
    {
      "command": "gh api core repository/contributors/commits/readme/issues/releases/tree/actions/contents APIs",
      "result": "passed",
      "summary": "26 deep repo records, explicit contributors pagination; 20 source/docs-verified omissions."
    },
    {
      "command": "Public HF HTTP APIs and ArXiv HTML",
      "result": "passed",
      "summary": "Verified NLA AV/AR, LatentQA, Activation Oracles weights; no tokens used for HF."
    },
    {
      "command": "git rev-parse HEAD; git status --porcelain=v1",
      "result": "passed",
      "summary": "Requested SHA confirmed; untracked slop/ observed, no staged paths."
    },
    {
      "command": "gh API core metadata/README/source/contributors/tips for four parent-forwarded 2026 repos; Transluce PCD HTTP",
      "result": "passed",
      "summary": "Four supplementary projects source-inspected without new repository searches; PCD reading/demo verified."
    }
  ],
  "validationOutput": [
    "Primary quotes checked programmatically against fetched README/source text (whitespace normalization only).",
    "No repository code, tests or package installations executed."
  ],
  "residualRisks": [
    "Human estimates are not exact identities or proof of human-written code; inherited history and service accounts require caveats.",
    "Runtime compatibility not tested; source and API CI signals only.",
    "diatoms, interp-methods and talkative-probes source anchors remain unresolved; discovery bounded and broad queries noisy.",
    "AO/IA official blog requests returned 403; framing uses parent-attested primary evidence. TL contributor estimate is parent-supplied, not independently recounted here."
  ],
  "noStagedFiles": true,
  "diffSummary": "Only configured external research artifact written; no project edits.",
  "reviewFindings": [
    "No project-code review performed; research-only.",
    "Causalab closed issue #79 is transferred, not fixed; circuit-tracer issue #115 does not demonstrate current-main install failure."
  ],
  "manualNotes": "Prioritize circuit/intervention tools plus Activation Oracles, keep existing NLAs prominent, nest compatibility wrappers and model-specific extensions, and separate paper artifacts/datasets/platforms. Excluded wrong homonyms, forks and duplicate NLA listing. Late supplemental inspection promotes interp-engine as a fast-inference omission and distinguishes Subtext/Dynolab platforms from Steerling model artifacts. Original seven-search budget unchanged."
}
```

Research author: PI/gpt-6.1-sol.
