# What to add and reorganize in awesome-interpretability

Research snapshot: 7 October 2026, Perth / 6 October UTC. Author: PI/gpt-6.1-sol.
Target: `wassname/awesome-interpretability`, original `main` commit `f5a023133bfc2997ca90926af8852e1774169ab4`. The initial audit left README unchanged. The user-approved table conversion and research were pushed to `main` at `12e6b5097fd48d38f7e7d1d4436483e9782cd463`. The perspectives follow-up below is still a draft, not added to README.

> wassname: “please do deep research for this. esp on gh and hf”
> “it's usefull to know stars, human authors, and how persistant/stale the project is”
> “also SAE's suck we can list but meh”
> “there are NLA's too now”

## Update: tables and notable project families, 7 October 2026

> wassname: “nice add them then” / “put everything in table with those cols” / “just stuiff that is notable”

README now has 137 entries in 16 task-grouped Markdown tables: project, ~H, stars, creation date, latest default commit, notes. All original non-badge URLs remain. GitHub's own GFM renderer preserves the ~H tooltip: “Estimated number of human contributors”. No Pages site, JavaScript or sorting implementation was added. User requested “push what you have now anyway”; README was committed and pushed at `12e6b50`, and GitHub's default-branch API returned the same SHA. The user flagged the PI-written introduction; it was left unchanged in that requested push, pending a specific prose edit.

Additional owner-network checks are saved in `families/`:

- David Bau / `thebaulab` / NDIF / Kevin Meng: retain BauKit and NNsight, add ROME, MEMIT, Dissect and the source-checked Rewriting reference; nnterp and Workbench are distinct companion/platform entries.
- Theia Vogel / `vgel` / publicly linked upstreams: retain repeng, add Logitloom as output-trajectory exploration (not a logit lens), and the actual Latent Introspection paper code beside existing reading.
- Inspect / Meridian / Petri: canonical Inspect AI, Scout and Petri; Petri Bloom is the small successor to frozen Bloom, not a place to transfer Bloom's stars. Inspect Evals and ControlArena get collection/framework-wide † markers.
- IBM / Generative Computing / Cadenza-Labs: retain Steerability, activation-steering and vLLM-Hook; add ICX360 and Liars' Bench. Low-evidence/toy projects and fork copies were excluded. Cadenza was resolved from its public research/team site source, not just a spelling match.
- Parent follow-up verified the credited Rewriting implementation, ELK and Apollo's deception-probe source, and actual ControlArena/Inspect Evals code. These supplement the scouts' bounded four-candidate limits.

`families/readme_metrics.json` holds the 119 displayed GitHub metric rows, including scoped rows. `families/readme-verification.log` records table shape, retained links, required family coverage, metric/SHA consistency and GitHub-sanitized tooltip checks. The plain `claude` service account is also excluded in the final Inspect estimate: 331 raw accounts minus six exclusions = 325, versus the scout's narrower 326 estimate.

The initial metadata batch failed on guessed `neuronpedia/neuronpedia`; canonical `hijohnnylin/neuronpedia` was resolved via search and the primary README, then the complete batch succeeded. An initial literal `<table>` assertion missed GitHub's `<table role="table">`; the semantic HTML parser verified all 16 six-column tables. No runtime/scientific validation was claimed.

## Follow-up: major perspectives, not another paper survey

> wassname: “just major perspectives that are major field turning poitns by notable figures (or my favs)”

Propose a short `Perspectives` section, with author/year/main argument instead of GitHub metrics. Six main entries:

1. Neel Nanda and GDM colleagues: pragmatic interpretability, paired with their decision to deprioritise fundamental SAE work (2025).
2. Chris Olah's Interpretability Dreams (2023), paired with Dario Amodei's Urgency of Interpretability (2025): the foundational reverse-engineering agenda.
3. Ryan Greenblatt / Buck Shlegeris: the case for AI control (2024), safety even if models try to subvert safeguards.
4. Evan Hubinger and colleagues: model organisms of misalignment (2023), deliberately induce failures to test mitigations.
5. Korbak / Balesni and the broad author coalition: CoT monitorability as a fragile opportunity (2025).
6. janus' Simulators (2022), paired with Marks / Lindsey / Olah's Persona Selection Model (2026).

Two user-requested adjacent entries: davidad's 2024–2026 changes of view, and Boaz Barak and colleagues' 2026 confessions argument. Both merit attribution rather than presenting them as established field consensus. davidad appears to be the intended “David” reference; his 2025 ARIA tooling pivot and 2026 personal alignment/wisdom pivot are distinct, and neither establishes that formal verification is worthless.

Gradient hacking is a companion risk argument; gradient routing is a distinct training method, not a synonym. Keep both as companion links unless expanding the list. ELK is the strongest additional historical candidate. “Mis training” provisionally maps to model organisms/emergent misalignment; no exact named project was identified.

Primary-source quotes, author/date checks, competing positions and exclusions: [appendix/perspectives.md](appendix/perspectives.md). No README edits or further push were made for this research follow-up.

## Decision summary

The gap is not principally SAEs. Your NLA entry already exists. The useful additions are:

1. Activation-language alternatives: Activation Oracles, LatentQA, Transluce's introspective interpretation; introspection adapters as a distinct weight/behavior-auditing method. Link the actual pretrained releases beside the code.
2. Non-SAE concepts and causal tests: Interpreto, ICA Lens, Causalab, AutoCircuit/EAP-IG, Transluce's neuron-basis circuits; benchmarks that distinguish readable explanations from interventions that actually work.
3. Better execution choices: interp-engine, nnterp under NNsight, Mishax for JAX, TorchLens for general PyTorch. Do not confuse capture speed with support for gradients through the model.
4. Interpretable-by-design models: PyTorch Concepts and Steerling, separately from tools for interpreting an arbitrary pretrained LM.
5. Classical/CV completeness: direct SHAP, DiCE, Grad-CAM, Quantus and Zennit/CRP entries; LIME as a historical baseline. These fit the scope you already chose, not an SAE expansion.

Suggested first pass: nine direct entries — Activation Oracles, Interpreto, ICA Lens, Causalab (conditional), circuit-tracer, CausalGym, Quantus, SHAP and pytorch-grad-cam. These cover distinct gaps. The broader tables below are a typed second wave, not a request to add everything at once. SHAP/LIME/DiCE are already mentioned by name; the gap is direct canonical entries, not absent methods.

First fixes: TransformerLens's HF description, Docent's category, the InterpretML link, Overcomplete's overly narrow SAE label, and unsupported “abandoned” wording. Suggested groups and a compact entry format follow the recommendations.

The full source inspections, contributor lists, exact queries, pinned code links, exclusions and uncertainty notes are in `appendix/`. No model execution or benchmark reproduction was performed.

## How to read the evidence

- `H≈` estimates attributed non-bot/non-service contributor accounts. It does not prove human authorship or count active maintainers. Aliases, inherited history and unlinked authors complicate it. Author examples below are public attribution, not independent identity verification.
- Creation date shows repository persistence, not continuous development. `Source/config` is the latest qualifying default-branch source, tests or configuration commit found in the parent's last-20-commit scan; docs and `.github` changes are excluded. It is not necessarily the latest algorithm change. Unknown is reported, not silently replaced with issue activity.
- Rows with `tip` instead use the researcher's latest default-branch commit; this can include docs. Do not compare that date as if it were a source-only measurement. Every main recommendation table exposes its default tip separately or explicitly uses tip dates. Exact branches/SHAs for 99 metadata-checked repositories are in `default_tip_snapshot.json`.
- GitHub stars are attention, not evidence of scientific validity. HF likes/downloads are different measurements; downloads are not unique users. Values are snapshot counts, not promises that live badges will match later.
- Quiet reference code is different from unsupported infrastructure. For moving HF/vLLM integrations, an old source date is a compatibility risk; for a compiled ground-truth benchmark it can simply mean the artifact is finished.
- Recommendations are grouped by task. Within comparable roles, contributor breadth and persistence help order choices; stars do not make unrelated methods comparable.

## 1. GitHub additions with the strongest task fit

### Activation-language interpretation and model self-report

Keep the existing NLA entry at the start of this group. These methods have different objectives; do not label all of them NLAs or recovered mechanisms.

| Project | H≈ | Stars | Created | Default tip | Source/config | What to list; limitation |
|---|---:|---:|---|---|---|---|
| [Activation Oracles](https://github.com/adamkarvonen/activation_oracles) | 2 | 103 | 2025-07-30 | [2026-09-26](https://github.com/adamkarvonen/activation_oracles/commit/5712762cfc29a18d6414a1cf2cccb4ff4432ced5) | 2026-09-26, 10d | Natural-language activation QA; maintained main versus reproducible paper branch. Author calls it non-mechanistic. |
| [Introspective interpretation](https://github.com/TransluceAI/introspective-interp) | 2 | 38 | 2025-12-22 | [2026-07-07](https://github.com/TransluceAI/introspective-interp/commit/594d53348734097857430826d88f5c6856164de7) | 2026-07-07, 91d | Feature descriptions, predicted patching effects and input ablations; research training/evaluation code with released weights. |
| [LatentQA](https://github.com/aypan17/latentqa) | 1 | 37 | 2024-12-12 | [2025-11-16](https://github.com/aypan17/latentqa/commit/a2dcb6f8eef52ce8c8e75ee71da66cb880f727f4) | 2025-11-16, 324d | Activation decoder/read-write research artifact; pretrained adapter is noncommercial. |
| [Introspection adapters](https://github.com/safety-research/introspection-adapters) | 1 | 30 | 2026-04-28 | [2026-04-28](https://github.com/safety-research/introspection-adapters/commit/92a3b05ac1c472b76b966c441d11b88c1b7b76ec) | 2026-04-28, 161d | LoRA self-report of trained behavior; not an activation decoder. One public release burst; false positives matter. |

Attributed examples: Adam Karvonen (`adamkarvonen`) and `thejaminator`; Transluce `belindal` / `choidami` (the linked model card names Belinda Z. Li among the paper authors; handles alone do not establish legal identities); `aypan17`; `k-shenoy`. Full attributed account lists and paper/source distinctions are in the GitHub appendix.

Also list [Predictive Concept Decoders](https://transluce.org/pcd) as **reading + demo**, not an installable library: sparse concepts predict future behavior, unlike NLA vector reconstruction. No specific public implementation/checkpoint was established. “No release verified” is narrower than “does not exist.”

### Causal interventions, concept methods and circuit discovery

| Project | H≈ | Stars | Created | Default tip | Source/config | Recommendation and constraint |
|---|---:|---:|---|---|---|---|
| [circuit-tracer](https://github.com/decoderesearch/circuit-tracer) | 17 | 2,915 | 2025-05-28 | [2026-09-11](https://github.com/decoderesearch/circuit-tracer/commit/7f66876689f59e92fc3641650d38b8bd41749ec4) | 2026-09-11, 25d | Add one attribution-graph entry. Depends on transcoders; not method-neutral or a reason to center the whole list on SAEs. Bundles credited Anthropic frontend code; 17 accounts are not a backend-specific maintainer count. Git-history inheritance was not established. |
| [Interpreto](https://github.com/FOR-sight-ai/interpreto) | 10 | 207 | 2025-02-26 | [2026-10-06](https://github.com/FOR-sight-ai/interpreto/commit/b3b9a0fcbb46b891d0029d89a6561307114073a0) | 2026-10-06, 0d | High priority: probes/CAVs, ICA/PCA/SVD/NMF/KMeans, attribution and lenses; SAEs optional. Some metrics unavailable; NNsight 0.8 migration PR still open. |
| [Causalab](https://github.com/goodfire-ai/causalab) | 6–7 | 118 | 2025-04-25 | [2026-09-30](https://github.com/goodfire-ai/causalab/commit/8e8d5d1f8f9ca8f42bfce7c6b5eef194f012660e) | 2026-09-30, 6d | High task fit: test causal hypotheses with DAS/DBM/intervention protocols. Conditional: public mirror and unresolved write-intervention issue, below. |
| [AutoCircuit](https://github.com/UFO-101/auto-circuit) | 3 | 103 | 2023-08-21 | [2026-08-17](https://github.com/UFO-101/auto-circuit/commit/7242291d0e5da5c9c044cd6cb97ab911be9adabf) | 2026-08-17, 50d | Efficient edge patching/discovery/evaluation. Prefer it to presenting original ACDC as the supported default. |
| [EAP-IG](https://github.com/hannamw/EAP-IG) | 3 | 89 | 2024-01-15 | [2026-05-23](https://github.com/hannamw/EAP-IG/commit/e24bafd3d22af2c59ac5a83e0a6581b89b5c05dd) | 2026-05-23, 136d | Gradient-based circuit ranking with exact-patching comparisons. Explicit architecture constraints; no observed CI/release evidence. |
| [ICA Lens](https://github.com/liusida/ica-lens-paper) | 2 | 45 | 2026-06-08 | [2026-09-30](https://github.com/liusida/ica-lens-paper/commit/6ad5bee4c94d22173e6ffefe20a0f9ba96c703d9) | 2026-09-30, 6d | Strong non-SAE discovery: fitted ICA lenses, signed component readouts and coordinate steering. Early two-account project, not established superiority over SAEs. |
| [Transluce circuits](https://github.com/TransluceAI/circuits) | 1 | 41 | 2026-01-15 | [2026-04-10](https://github.com/TransluceAI/circuits/commit/2d215d4ba016ba8602b69d71fc0f1ad139a427b7) | 2026-04-10, 179d | Neuron-basis ADAG tracing, useful non-SAE counterweight. Paper artifact; frontend reuse and AI-assisted implementation explicitly disclosed. |

Attribution examples: circuit-tracer `hannamw` / `hijohnnylin`; Interpreto `AntoninPoche`, `fanny-jourdan`, `thomas-mullor`; Causalab Can Rager (`canrager` / `can-goodfire`) and `atticusg`; AutoCircuit `UFO-101`; EAP-IG `hannamw`; ICA Lens `liusida` (profile: Liu Sida) and `FeijiangHan`; Transluce circuits Aryaman Arora (`aryamanarora`). Account examples are not complete paper-author lists.

Specific conditions:

- **Causalab:** issue [#79](https://github.com/goodfire-ai/causalab/issues/79) was closed to move discussion into the private development mirror, not to report a fix. The reported `block_mid` write could be only partly applied. Current fix status is unknown; do not claim closed means resolved. Eight GitHub accounts become about six or seven people after likely aliases.
- **ICA Lens:** signed components are not probabilities, semantic names need independent checks, and sign conventions matter for named interventions even though ICA signs are mathematically arbitrary. Additive versus clamp steering has different preprocessing/norm constraints. [`liusida/icalens`](https://github.com/liusida/icalens) is related packaging/docs, not another independent method; do not sum the two repos' support as independent adoption.
- **ACDC:** original repository recommends AutoCircuit; historical TransformerLens-linked attribution is not current ACDC maintainer breadth.

### Hooking, execution and model inspection

| Project | H≈ | Stars | Created | Default tip | Source/config | Recommendation and constraint |
|---|---:|---:|---|---|---|---|
| [nnterp](https://github.com/ndif-team/nnterp) | 4 | 121 | 2024-08-08 | [2026-07-02](https://github.com/ndif-team/nnterp/commit/b4a31274692f986e493ac5d20ba20a4ec8640955) | 2026-07-02, 96d | Nest under NNsight: standardized accessors/model naming, not a separate execution engine. Upcoming redesign is not released support. |
| [Mishax](https://github.com/google-deepmind/mishax) | 3 | 158 | 2024-07-30 | [2026-09-16](https://github.com/google-deepmind/mishax/commit/c143e3b5142f6b6967eba46ce1eb6aab53f15a7c) | 2026-09-16, 20d | JAX/Flax instrumentation via AST rewriting; fills a different substrate from HF/PyTorch tools. |
| [TorchLens](https://github.com/johnmarktaylor91/torchlens) | 2 | 662 | 2022-10-14 | [2026-10-04](https://github.com/johnmarktaylor91/torchlens/commit/20c222a3c4954b5f14af2e4e9095ab9123266279) | 2026-10-04, 2d | General PyTorch computation graphs, activation/gradient inspection and interventions; not restricted to transformers. |
| [interp-engine](https://github.com/decoderesearch/interp-engine) | 1 | 39 | 2026-08-05 | [2026-10-02](https://github.com/decoderesearch/interp-engine/commit/eb9bb6d992e73d7624965583dd945ec15f0c510e) | 2026-09-28, 8d | New standardized eager/vLLM capture and editing substrate. Single-account, two-month history; throughput claims not replicated. |

Attribution: `Butanium` / `JadenFiotto-Kaufman` (nnterp), `jkramar` / `sonnerat` (Mishax), JohnMark Taylor (`johnmarktaylor91`) / `kalekundert` (TorchLens), `hijohnnylin` (interp-engine).

Important execution contract: interp-engine permits training downstream probes on captured vLLM activations, **not gradients through the served model**. Through-model attribution requires eager execution and opt-in gradient capture. Its October 2 default-tip commit also reports fixing bundled visualizer dependency security advisories; the source/config heuristic is not a complete measure of substantive maintenance. Its previous pre/post-norm mapping issue was fixed, with invalid aliases rejected; do not present the old closed report as a current bug.

### Interpretable by design; trainable interventions

| Project | H≈ | Stars | Created | Latest tip | Placement and limit |
|---|---:|---:|---|---|---|
| [PyReFT](https://github.com/stanfordnlp/pyreft) | 10 | 1,590 | 2024-02-17 | 2025-02-06, 607d | Nest with Pyvene/adapters: low-rank trainable representation interventions. Historical baseline; fine-tuning alone is not explanation. |
| [PyTorch Concepts](https://github.com/pyc-team/pytorch_concepts) | 10 | 159 | 2024-06-22 | 2026-07-24, 74d | Concept bottlenecks/interpretable layers/interventions; alpha API. Different role from post-hoc probes. |
| [Steerling](https://github.com/guidelabs/steerling) | 3 | 241 | 2026-02-22 | 2026-07-14, 84d | Architecture + ~8B causal diffusion model, known/discovered concept heads. Not an arbitrary-LM explainer; no released training/fine-tuning or training-data attribution code. |

Attributed examples: `frankaging` / `aryamanarora` (PyReFT); `gdefe` / Pietro Barbiero (`pietrobarbiero`, PyTorch Concepts); `ayaabdelsalam91`, Julius Adebayo (`adebayoj`), `giangnguyen2412` (Steerling). Steerling's paper author count and package contributor count differ.

Steerling requires Python ≥3.13, CUDA 12.8 and at least 18GB VRAM according to its README. Apache source licensing does not remove the model card's commercial-use qualifications. Preserve that distinction next to the HF link.

## 2. Validation is a separate gap

Your AxBench and matched-KL/calibration links are useful. Add a small evaluation section instead of scattering benchmarks among libraries. Each tests a different claim.

| Resource | H≈ / stars | Default tip | Created → source/config | What it can test; limit |
|---|---:|---|---|---|
| [MIB](https://github.com/aaronmueller/MIB) | 3 / 27 | [2025-08-15](https://github.com/aaronmueller/MIB/commit/b69dabe9899251d4a8fe90789afa4d655afc84c7) | 2025-04-01 → 2025-08-15 | Mechanistic interpretability benchmark landing/project repo. Implementation is split into tracks; do not call the landing repo a library. |
| [MIB circuit track](https://github.com/hannamw/MIB-circuit-track) | 6 / 25 | [2025-06-30](https://github.com/hannamw/MIB-circuit-track/commit/b759df34433c9e31043ba9e02908ce0bf20e894f) | 2024-05-24 → 2025-06-30 | Circuit evaluation implementation; code exists before the MIB landing repository. Link as a track, not a second umbrella benchmark. |
| [CausalGym](https://github.com/aryamanarora/causalgym) | 2 / 57 | [2024-11-30](https://github.com/aryamanarora/causalgym/commit/0f3129ff3b6c5c8264892f30a25be25150ae9179) | 2023-10-10 → 2024-11-30 | Controlled linguistic causal interventions. Published code assumes GPTNeoX-family models; HF dataset exists. |
| [RAVEL](https://github.com/explanare/ravel) | 1 / 58 | [2025-10-30](https://github.com/explanare/ravel/commit/e421fc9e132b3613b1d0020f856d539217fb30ca) | 2024-02-17 → 2025-10-30 | Representation disentanglement/interchange tests; paper benchmark, not a maintained model runtime. |
| [Tracr](https://github.com/google-deepmind/tracr) | 9 / 568 | [2024-02-05](https://github.com/google-deepmind/tracr/commit/9ce2b8c82b6ba10e62e86cf6f390e7536d4fd2cd) | 2022-12-01 → 2024-02-05 | Compile known RASP programs to transformers: ground-truth reference circuits. Archived; useful reference, not current JAX support. |
| [Quantus](https://github.com/understandable-machine-intelligence-lab/Quantus) | 20 / 676 | [2026-08-20](https://github.com/understandable-machine-intelligence-lab/Quantus/commit/85bc29d137d8f42835dd392f5cc441ad61d6d1f1) | 2021-03-18 → 2026-08-20 tip | Attribution faithfulness/robustness/randomization metrics. Metric implementations are not universally author-verified; not a certificate of semantic truth. |

Attribution examples: `aaronmueller` / `lepoissonfroid` (MIB), `hannamw` (circuit track), `aryamanarora` / `cgpotts` (CausalGym), `explanare` (RAVEL), `mrahtz` / `david-lindner` (Tracr), Anna Hedström (`annahedstroem`, Quantus).

Put a brief warning beside this group: **probe accuracy, readable labels, reconstruction, behavioral prediction, intervention success and causal explanation are different tests**. Include random/norm-matched controls, prompt/fine-tune comparators, held-out task/distribution tests and utility/KL budgets where relevant. A benchmark score does not validate all of those at once.

Optional specialized reading: [Dual-Steering](https://github.com/KihoPark/dual-steering), 1 attributed account / 18 stars, created 2026-02-15, last tip 2026-05-19. Information-geometric rather than Euclidean steering; Gemma/MetaCLIP research code, not broad library support. Good fit for your interests despite low stars.

## 3. Classical and vision additions

These are direct omissions or corrections within your existing explainability section. Keep this group apart from LM hidden-state tooling.

| Project | H≈ | Stars | Created | Default tip | Source/config or qualified tip | Placement and caution |
|---|---:|---:|---|---|---|---|
| [SHAP](https://github.com/shap/shap) | 270 | 25,794 | 2016-11-22 | [2026-10-04](https://github.com/shap/shap/commit/50be8f4fd7031d535d515042741320f53272d211) | source 2026-09-25 | Direct attribution entry, not just a name inside InterpretML. Background/interventional assumptions matter. |
| [pytorch-grad-cam](https://github.com/jacobgil/pytorch-grad-cam) | 52 | 12,993 | 2017-05-31 | [2026-08-13](https://github.com/jacobgil/pytorch-grad-cam/commit/704393448a7b0c620ee2c2b9597723f1d7f17b3d) | tip 2026-08-13 | Major CNN/ViT CAM toolkit; ROAD evaluation, not merely heatmap rendering. |
| [InterpretML](https://github.com/interpretml/interpret) | 47 | 6,956 | 2019-05-03 | [2026-08-17](https://github.com/interpretml/interpret/commit/560f8dde814cac03aec89e189bc9874012c7f1a5) | source 2026-05-28; tip Aug 17 | Correct existing link. Glassbox EBMs and blackbox explanations; community extension is a different repo. |
| [LIME](https://github.com/marcotcr/lime) | 42 | 12,166 | 2016-03-15 | [2021-07-29](https://github.com/marcotcr/lime/commit/fd7eb2e6f760619c29fca0187c07b82157601b32) | source 2021-07-29 | Historical local-surrogate baseline, clearly inactive code; 2026 issue activity does not make it current. |
| [DiCE](https://github.com/interpretml/DiCE) | 21 | 1,528 | 2019-05-02 | [2025-07-13](https://github.com/interpretml/DiCE/commit/8a3aea404f857fa599bfa7da663d94823b674688) | source 2025-07-13 | Direct diverse counterfactual entry. Feasible model counterfactuals are not proof of real-world causal recourse. |
| [Xplique](https://github.com/deel-ai/xplique) | 15 | 755 | 2020-04-05 | [2026-09-25](https://github.com/deel-ai/xplique/commit/7fa573b6534f29f2eaa923522df0190fecb46f62) | tip 2026-09-25 | Attribution + NMF/CRAFT concept discovery. Framework support is uneven; don't promise unrestricted Keras 3/PyTorch support. |
| [Zennit](https://github.com/chr5tphr/zennit) + [CRP](https://github.com/rachtibat/zennit-crp) | 12 / 7 | 248 / 141 | 2020-11-10 / 2022-06-07 | [2026-05-13](https://github.com/chr5tphr/zennit/commit/3e98348aa95e908f550ab2a13fca2245c30f7de3) / [2026-01-14](https://github.com/rachtibat/zennit-crp/commit/ecf1b7873bf0bf5ca34b7d21407ccb95549198b8) | source May 13 / Jan 14, 2026 | LRP and concept-conditional relevance; related packages, not counts to add together. |

Public attributed examples: Scott Lundberg (`slundberg`, SHAP), Jacob Gildenblat (`jacobgil`, Grad-CAM), `paulbkoch` (InterpretML), Marco Tulio Ribeiro (`marcotcr`, LIME), `gaugup` / `amit-sharma` (DiCE), `fel-thomas` (Xplique), `chr5tphr` (Zennit), `rachtibat` (CRP).

Adjusted counts exclude obvious service/project identities: parent raw counters would give InterpretML 50 and DiCE 23. Report 47/21 after the researcher's profile audit, not falsely precise “verified humans.”

Conditional/secondary: [Alibi](https://github.com/SeldonIO/alibi), 21 / 2,648, created 2019-02-26, source last 2024-12-05 (docs tip 2025-10-10), is now **BSL 1.1 source-available**, not unqualified open source. [SpLiCE](https://github.com/AI4LIFE-GROUP/SpLiCE), 2 / 134, last tip 2025-03-27, is a non-SAE semantic-vocabulary decomposition for CLIP; good specialist paper/API entry. [OpenXAI](https://github.com/AI4LIFE-GROUP/OpenXAI), 10 / 260, last tip 2024-03-31, is a historical evaluation artifact, lower priority than Quantus.

## 4. HF: put usable artifacts beside their methods

A single giant HF section would duplicate the library list. Prefer a short “start with pretrained artifacts” index, with collections/weights/datasets nested under the relevant project. Keep base-model requirements and code mapping with the artifact.

`L / D` = HF likes / reported downloads on retrieval, **not GitHub stars / users**. Collection upvotes are another distinct count. LastModified describes HF repository activity, not library maintenance.

| Artifact/family | Representative L / D | HF modified | What to add; operating/reuse limit |
|---|---:|---|---|
| [Official NLA collection](https://huggingface.co/collections/kitft/nla-models-69fa80a3c69880bba63eddc6) | Qwen AV 7 / 819; AR 8 / 423 | weights 2026-05-07 | Eight checkpoints = four matched AV/AR pairs, **one family entry**. Qwen2.5-7B L20, Gemma-3-12B L32 / 27B L41, Llama-3.3-70B L53. |
| [Activation Oracles collection](https://huggingface.co/collections/adamkarvonen/activation-oracles-694232103936f0bd6893c5ca) | Qwen3-8B 1 / 701; Qwen3.6-27B 0 / 20 | new adapter 2026-09-25 | Thirteen collection items; distinguish paper-era checkpoint and maintained-main Qwen3.6 release. Adapter not a full standalone model; card license unresolved. |
| [LatentQA adapter](https://huggingface.co/aypan17/latentqa_llama-3-8b-instruct) | 6 / 0 | 2024-12-13 | Rank-16 q/v LoRA over Llama-3-8B-Instruct, **CC-BY-NC-SA-4.0** plus Llama base terms/access. |
| [Transluce feature explainer](https://huggingface.co/Transluce/features_explain_llama3.1_8b_llama3.1_8b_instruct) + [patch-effect adapter](https://huggingface.co/Transluce/act_patch_qwen3_8b_qwen3_8b) | 0 / 232; 0 / 20 | 2026-01-03 | Explicit source mapping to introspective-interp. Feature model needs custom continuous-token classes, not plain AutoModel use. Feature training labels derive from SAEs/Neuronpedia; not independent human ground truth. Patch-adapter card license unspecified. |
| [ICA Lens collection](https://huggingface.co/collections/sida/ica-lens) | sampled fits 0 / 0 | current 2026 collection | Pre-fitted GPT-2 / Qwen3.5 ICA coordinates/readouts; seven collection items, not seven independent techniques. Artifact license missing in sampled cards; base/source licenses don't automatically license the fits. |
| [Tuned Lens weights in a Space](https://huggingface.co/spaces/AlignmentResearch/tuned-lens/tree/main/lens) | Space 31 / n/a | 2024-07-22 | **36 config/params.pt pairs**, including Llama-3. The library's loader defaults to repo_type=space: don't search only model repos. Runtime metadata RUNNING; app not exercised. |
| [Pre-fitted Jacobian lenses](https://huggingface.co/neuronpedia/jacobian-lens) | 115 / 0 | 2026-09-25 | Forty top-level model directories. Model-specific matrices, not whole LMs; MIT card. Fit/config/version provenance and architecture caveats still matter. |
| [Steerling 8B](https://huggingface.co/guidelabs/steerling-8b) | 118 / 172 | 2026-08-12 | Interpretable-by-design ~8.39B BF16 model. Card header Apache but body qualifies commercial use/upstream licensing. Instruct sibling 3 / 57 has **no README card (404)**. |
| [CausalGym dataset](https://huggingface.co/datasets/aryaman/causalgym) | 7 / 117 | 2024-02-21 | MIT linguistic causal-intervention tasks; direct reverse-link from producer code. Code model-family restrictions remain. |
| [AxBench Concept16K](https://huggingface.co/datasets/pyvene/axbench-concept16k) | 4 / 97 | 2025-01-24 | CC-BY-4.0 examples from GemmaScope concept list, model-generated, not human labels. Enrich existing AxBench entry rather than count as a missing library. |

Artifact contracts worth writing down:

- **NLA layer/index/site:** L20 means output of zero-based block 20, which is `hidden_states[21]` in the usual HF tuple including embeddings. The training README example selects `[20]`, unlike the actual extractor/sidecars. Do not copy that example without reconciling the convention. Model ID + layer number alone is insufficient.
- **NLA resources:** both AV and AR must match the activation model/site. The Gemma-27B AV sample is F32, not automatically BF16. Public derivative artifact access does not remove Gemma/Llama base gating or license obligations. Hundreds of description tokens per activation are not cheap all-token monitoring.
- **Oracles:** the new 27B adapter reads layers 16/32/48 and injects at layer 1; rank 64/alpha 128. Its card reports a strong base-model classification baseline (72–93% on tasks), so judge incremental evidence, not only fine-tuned accuracy. Main dependencies differ from paper reproduction.
- **Transluce:** parent found that `author=transluce` returned zero while exact `author=Transluce` returned fourteen model records. Direct project links and three cards verified the missing family. This is a retrieval limitation, not evidence of artifact absence. The old [`llama_8b_explainer`](https://huggingface.co/Transluce/llama_8b_explainer) is a separate 2024 artifact (9 likes / 35 downloads), not a renamed 2026 release.
- **Jacobians:** released fits are useful even though the Anthropic source explicitly says reference/unmaintained. That repo has 2,011 stars, one attributed account, creation/source release 2026-07-02. A popular reference is not a supported runtime. Check the fit's model revision/dtype and RoPE/config requirements.

Optional data index, not main recommendations: [deception-probe activations](https://huggingface.co/datasets/xycoord/deception-probes-activations) has 58,011 downloads but noncommercial/mixed terms, deprecated buggy collections and unresolved producer-code provenance; [CounterFact tracing](https://huggingface.co/datasets/NeelNanda/counterfact-tracing) has unclear card licensing/source mapping; [model-organism checkpoints](https://huggingface.co/emergent-misalignment/Qwen-Coder-Insecure) are research controls, not production models. Full checks in the HF appendix. These should not win by downloads alone.

SAEs proportionately: one [SAELens](https://github.com/decoderesearch/SAELens) entry (78 / 1,550; source Oct 4), one optional [Delphi](https://github.com/EleutherAI/delphi) feature-explanation entry (22 / 279; source Aug 25; latest three sampled weekly CI runs failed), and one [Gemma Scope 2 collection](https://huggingface.co/collections/google/gemma-scope-2-694506265ca2b018ef6ba2b8). Delphi verbalizes/scorers SAE/transcoder features, **not raw-activation NLA decoding**. These do not need a wall of layer-specific weights.

## 5. Better groups and presentation

### Suggested top-level navigation

1. **Read and change model internals** — BauKit, TransformerLens/Bridge, NNsight + nnterp, Pyvene, interp-engine, vLLM tools, Mishax, TorchLens.
2. **Decode activations and discover concepts** — logit/tuned/Jacobian/ICA lenses; NLAs and activation-language methods; probes, NMF/PCA/ICA/CAV methods; small optional SAE subsection.
3. **Test causal hypotheses and find circuits** — Causalab, AutoCircuit/EAP-IG, neuron/transcoder tracing. Differentiate neuron-basis versus learned-feature tracing.
4. **Steer and train interventions** — reusable steering libraries, ReFT/adapters, then separately labeled single-paper methods. Keep your matched-KL/random-control reading visible here.
5. **Evaluate interpretations and interventions** — AxBench, MIB tracks, CausalGym, RAVEL, Tracr, Quantus. State what each score tests.
6. **Interpretable models by design** — concept bottlenecks/PyTorch Concepts, Steerling, EBMs (cross-link tabular group).
7. **Classical and vision explainability** — attribution/surrogates; counterfactuals; concept relevance. Avoid pretending these are identical to mechanistic LM analysis.
8. **Browsers, demos and agent audits** — Neuronpedia, Workbench, visualization tools; Docent explicitly agent transcripts. Method-specific demos nested under their method.

Then `Adjacent tooling` (structured outputs / training-data attribution), `Reading and tutorials`, and clearly labeled `Author's projects / experiments`. No deletion of your work is necessary; distinguish dataset/templates/paper artifacts from maintained libraries.

Useful subtitle: “Tools, pretrained artifacts and benchmarks for understanding and changing models.” It describes the actual broad scope more accurately than presenting every link as mechanistic.

### Entry format and lightweight evidence index

Keep the README prose short:

> **ICA Lens** — ICA decomposition, token readouts and coordinate steering for HF LMs. Paper-derived library; pre-fitted lenses available. Two attributed contributor accounts; active in September 2026, early project. [code] [docs] [HF fits]

Use one compact evidence table per comparable group: `project | type | contributor estimate | stars | created | last source/config | scope / important restriction`. Dynamic star badges are fine; a dated count table is a reproducible snapshot. Do not duplicate stale exact metrics across prose, badges and several tables.

Distinguish artifact kinds consistently: `library`, `paper code`, `benchmark`, `model/adapter`, `dataset`, `demo`, `hosted service`. One primary placement per project, with cross-links rather than duplicate bullets.

Maintenance labels should be factual:

- `archived`, when GitHub says archived;
- `reference release`, when authors say reference code;
- `last source/config YYYY-MM-DD`, rather than unqualified “abandoned”;
- `early project`, alongside creation date and breadth;
- `compatibility unverified`, if current dependency/backend support is not established.

The Pi skill's 30/90-day bins suit a fast-changing plugin API. Do not mechanically apply “>90 days = stale/bad” to all interpretability papers or stable mathematics libraries. Exact dates plus role carry more information.

### Existing-entry corrections to propose

| Current wording/link | Evidence-based change |
|---|---|
| TransformerLens “not as HuggingFace-compatible” | TL4 recommends TransformerBridge and preserves raw HF weights by default; legacy numerics require compatibility mode. Replace the blanket historical contrast. |
| Docent “interactive model explanation and steering interface” | Agent-transcript analysis / behavior-rubric auditing, not hidden-state explanation. |
| InterpretML → interpret-community | Main library is `interpretml/interpret`; nest community extension separately if useful. |
| Overcomplete “vision SAE toolbox” | Vision dictionary/concept learning, including NMF variants and archetypal analysis; do not erase its non-SAE methods. |
| Graphpatch “promising but abandoned” | Unarchived; last source/config Jan 27, 2025 (617d). No primary abandonment declaration established. State date/compatibility limits. |
| Bare `(2019)` / `(2022)` annotations | Label publication, creation or last-code dates; these are not interchangeable. |
| jsonformer “not updated since 2024” | Latest default/source commit May 30, **2023**. |
| “Maintained” structured-output group | Apply dates consistently: Guidance source May 21, 2026; lm-format-enforcer Apr 4. Recent metadata/issues are not code maintenance. |

Other infrastructure is similarly quiet: BauKit source Feb 22, 2024; Tuned Lens Aug 7, 2025; ViT-Prisma Jul 21, 2025; repeng Sep 24, 2025. They are not automatically useless. Keeping them while marking a younger quiet paper as “abandoned” needs a stated rule.

### Interfaces and adjacent discoveries: smaller nested entries

- [CircuitsVis](https://github.com/TransformerLensOrg/CircuitsVis), 12 / 368, Python/React visualization; April 2026 tip is devcontainer removal, not new tracing capability.
- [Treescope](https://github.com/google-deepmind/treescope), 11 / 476, source Jun 18, 2026; standalone tensor/model HTML inspection. Penzai archive does not imply Treescope is archived.
- [Workbench](https://github.com/ndif-team/workbench), 7 / 18, source Sep 18, 2026; NNsight/NDIF UI, not another hook engine.
- [Subtext](https://github.com/ninjahawk/Subtext), 2 / 245, created Jul 6, source Jul 7 / tip Jul 23, 2026; nest under Jacobian Lens. Its words are lens readouts, not generated hidden reasoning.
- [Dyno Lab](https://github.com/canivel/dynolab), 1 / 163, created Sep 4 / source Oct 4, 2026; Apple Silicon/MLX platform. Single-site patching sweeps, not full circuit tracing; no pretrained SAE import.
- [Bergson](https://github.com/EleutherAI/bergson), 15 / 99, created May 14, 2025 / source Oct 6, 2026; training-data influence/attribution, a distinct adjacent task.

Watchlist, not routine recommendations: Wisent's [Ster](https://github.com/wisent-ai/ster) is now Rust/Candle, not the old Python tool, with conflicting supported-family claims; [UncensorBench](https://github.com/wisent-ai/uncensorbench) exposes host networking/writable host mounts in model-code evaluation and unclear corpus provenance. New NLA-branded third-party cards sometimes describe classifiers rather than text decoders, or report reconstruction dominated by projection artifacts. The HF appendix explains why those are deferred instead of treating every search hit as a usable NLA.

## 6. Primary passages: observation versus interpretation

These are author/maintainer descriptions, not independent replications. Pinned code references and issue passages appear in the appendices.

### TransformerLens: current maintainer README

https://github.com/TransformerLensOrg/TransformerLens

> `TransformerBridge` is the recommended path and supports 15,000+ models across 140+ architecture families (see [`supported_models.json`](transformer_lens/tools/model_registry/data/supported_models.json) for the full inventory). By default it preserves raw HuggingFace weights – logits and activations match HF, *not* legacy `HookedTransformer` (which folds LayerNorm and centers weights by default). Call `bridge.enable_compatibility_mode()` after booting for HookedTransformer-equivalent numerics. The legacy `HookedTransformer.from_pretrained` API was removed in TransformerLens 4.0 — see the [Migrating to TransformerLens 4.0](https://TransformerLensOrg.github.io/TransformerLens/content/migrating_to_v4.html) guide.

Observation: this contradicts the unqualified legacy HF characterization. Model-count and compatibility claims were not locally tested.

### Activation Oracles: authors' research post and README

https://alignment.anthropic.com/2025/activation-oracles/

> Activation Oracles are a fundamentally non-mechanistic technique for interpreting LLM activations.

https://github.com/adamkarvonen/activation_oracles

> **Reproducing the paper:** use the [`paper`](https://github.com/adamkarvonen/activation_oracles/tree/paper) branch (or the `v1.0-paper` tag), which has the code and dependency versions used for the paper (torch 2.7.1, transformers 4.55.2, peft 0.17.1). `main` is maintained and upgraded (transformers 5, torch 2.12) to support newer models such as Qwen3.6-27B.

Observation: maintained inference and reproducible paper environments differ. Interpretation: list with activation-language auditing, not unqualified recovered circuits.

### NLA: authors' limitations

https://www.anthropic.com/research/natural-language-autoencoders

> The most important limitation is that NLA explanations can be wrong. NLAs sometimes make claims about the context that are verifiably false—for instance, they sometimes invent details that aren’t in the transcript.

> At inference time, the NLA generates hundreds of tokens for every activation it reads. That makes it impractical to run NLAs over every token of a long transcript or to use them for large-scale monitoring while an AI is training.

Interpretation: reconstruction is a useful objective, not proof that the English description is causally faithful or cheap to monitor.

### Introspection adapters: authors' scope and false positives

https://alignment.anthropic.com/2026/introspection-adapters/

> Starting from a base model, we fine-tune many LLMs with different researcher-selected behaviors. Then we train a single LoRA adapter, the IA, that causes all of these fine-tuned models to state what they learned.

> First, introspection adapters exhibit a high false-positive rate: when applied to models without any specific trained behaviors, they tend to hallucinate behaviors from the training distribution.

Observation: weight/behavior self-report, not an activation autoencoder. This limitation belongs next to the link.

### Predictive Concept Decoders: authors' objective

https://transluce.org/pcd

> Our key insight is to frame interpretability as a prediction problem: A system that understands a model's activations should be able to predict that model's future behaviors.

> A PCD has two components:
> 1. An **encoder** that compresses model activations to a sparse list of concepts, and
> 2. A **decoder** that takes these concepts and answers questions about model behaviors.

Observation: report/demo verified; implementation/checkpoint unknown. Interpretation: predictive objective is distinct from NLA reconstruction, and sparse concepts do not automatically mean an SAE.

### Docent: product documentation

https://transluce.org/docent

> Docent helps analyze AI agent transcripts by turning anecdotes and intuitions into reliable, traceable measurements.

> Docent supports any text-only, single or multi-agent transcript.

Observation: the README's hidden-state explanation/steering category is misleading.

### interp-engine: gradient contract

https://github.com/decoderesearch/interp-engine/blob/main/docs/GRADIENTS.md

> So a linear probe on captured activations trains fine on either backend. Attribution that needs a gradient *of the model* is eager-only.

Observation: downstream probe training and gradients through a model are different supported operations.

### Transluce: exact artifact source and limits

https://huggingface.co/Transluce/features_explain_llama3.1_8b_llama3.1_8b_instruct

> This model was trained to map SAE features from Llama-3.1-8B's residual stream to their explanations derived from Neuronpedia. It generalizes to explaining any arbitrary continuous feature from Llama-3.1-8B's residual stream.

> **Note**: This model requires custom handling of continuous tokens. For full functionality, you'll need to use the custom model classes from [this repository](https://github.com/TransluceAI/introspective-interp.git) that can properly embed feature vectors at the `<|reserved_special_token_12|>` tokens. The standard transformers library won't handle the continuous token embeddings correctly.

Observation: card links source and describes SAE-derived supervision/custom model requirements. The claimed arbitrary-feature generalization was not replicated.

## 7. Research coverage and remaining uncertainty

This was a broad, bounded discovery plus source review, not just a familiar-project list:

- GitHub mechanisms lane: seven repository searches, 700 returned rows / 590 unique search repositories, network follow-up; 2,554 unique metadata candidates across discovery routes. Thirty primary source/metadata reviews including four late parent discoveries.
- GitHub steering/XAI lane: seven searches, 676 returned rows / 649 unique search repositories; network filtering produced 951 unique manually name/description-triaged records. Forty-eight successful primary README/metadata inspections, 39 full metadata/contributor/commit/issues/release/tree bundles and 26 source/NOTICE specimens. Twenty main additions/corrections plus qualified exclusions.
- HF lane: 74 discovery requests, 3,733 returned / 3,600 unique type+ID candidates; 180 entry-level samples and 47 in-depth metadata/card records. Twenty-five shortlisted artifacts represent sixteen families, not twenty-five independent methods.
- Parent: 51 existing third-party GitHub repository snapshots; 40 candidate rows / 38 unique canonical repositories after redirects/overlap (not all recommendations). Ten direct HF metadata/card snapshots, including three Transluce cards omitted by the initial lowercase-author search. These overlap lane reviews; **do not sum them into a fictitious total of independent deep reviews**.
- Broad README keyword and star-sorted searches were noisy and capped at 100; new low-star repositories required author/org network discovery. An inaccessible/empty guessed identifier is not evidence that a technique has no code.

No repository code executed, packages installed, model tensors downloaded, demos exercised or benchmark results reproduced. Recent CI and issue responses are observations about maintenance, not scientific validation. Missing licenses, public-mirror fixes and identity aliases remain explicit uncertainties.

Independent review completed: `appendix/evidence-challenge.md`. A fresh read-only reviewer checked fourteen GitHub repositories, eight material claim groups and a targeted follow-up on Transluce/NLA indexing/gradient/Docent claims. It reproduced the main distinctions and recommended nine first-pass entries rather than concatenating all shortlists.

Corrections incorporated: copied frontend source is not proof of inherited Git contributor history; preserve latest default-branch tips alongside source/config dates; deployment/metadata CI success is not passing implementation tests; missing direct SHAP/LIME/DiCE entries are not absence of those named methods. The reviewer independently reproduced Transluce author filtering, released-card mapping and the NLA indexing inconsistency. Source/backend compatibility, scientific results, licenses and exact human identities remain unverified.

Verification: `verification.log` records unchanged README bytes, collector syntax checks, metadata consistency and known historical API failures. These are research-data checks, not library/runtime tests.

## Audit files

- `appendix/github-mechanisms.md`: pinned implementation links, account lists, issue/CI checks, exact search ledger and causal/NLA/engine findings.
- `appendix/github-steering-xai.md`: classical/CV/concept/steering source checks, license findings, author attribution and exclusions.
- `appendix/huggingface-artifacts.md`: exact API ledger, paired weights, adapter configs, licenses, Space states and artifact exclusions; parent Transluce correction is in this report and `appendix/parent-hf-correction.md`.
- `evidence_existing/github_snapshot.json`, `evidence_new/github_snapshot.json`, `evidence_extra/github_snapshot.json`, `evidence_shortlist/github_snapshot.json`: reproducible dated parent metrics. Raw counters need the qualified service/alias adjustments described above.
- `evidence_hf/hf_snapshot.json`: ten parent HF records/cards, with artifact kinds, retrieval timestamps, missing-card status and runtime metadata.
- `default_tip_snapshot.json`: exact default branch, tip SHA and committer date for 99 repositories, including ten extra tip/metadata checks for the tables.
- `github_contributor_accounts.json`: compact public account IDs/logins/types/contribution counts for 89 canonical repositories; service/alias adjustments remain separate.
- `appendix/evidence-challenge.md`: independent review, including corrections to inherited-history and CI interpretations.
- `snapshot_github.py`, `snapshot_hf.py`: read-only metadata collectors. Detailed fetched GitHub API payloads/READMEs are machine-only cache under `.local/research/20261007_interpretability/`; durable summaries, compact contributor accounts, HF cards and quote/pinned-source citations accompany this report.

— PI/gpt-6.1-sol
