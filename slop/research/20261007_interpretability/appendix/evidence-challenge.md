# Independent evidence challenge

**Snapshot:** 2026-10-07 Australia/Perth / 2026-10-06 UTC. **Target:** `README.md` at `f5a023133bfc2997ca90926af8852e1774169ab4`.

## Result

The three reports support useful additions, but **their shortlists must not simply be concatenated**. Recommend **nine missing direct entries across distinct tasks**, below, plus corrections/nested links to existing tools. Preserve NLAs prominently. Include one transcoder-dependent circuit tool, not a new SAE catalogue. Account breadth wins within comparable tasks; task coverage and maintenance determine which tasks deserve entries.

No project files were edited; no packages, repository code, model inference, publication or push were run. I read the local README first, then all three complete reports and independently checked eight material claim groups through authenticated `gh api` and public HF HTTP APIs. **Workspace HEAD had advanced to `3f3255a18876082106e65d95d003c659084ee599`**, unlike the earlier reports. `git show f5a0231:README.md` and `git diff f5a0231 -- README.md` confirmed the audited README is unchanged. Existing modified/untracked `slop/` research files were not touched; no staged paths were observed.

Reports reviewed: [mechanisms](github-mechanisms.md), [steering/XAI](github-steering-xai.md), [HF artifacts](huggingface-artifacts.md). Their discovery logs are useful evidence, not independent replications of each other: some candidates and parent-supplied seeds recur across all three.

## Eight independently checked material claims

### 1. Are the proposed omissions actually absent? **Mostly yes; several are improvements, not omissions.**

At the requested SHA, all nine direct URLs in the minimum-additions table are absent. However, **SHAP and LIME already appear by name** under the currently mislinked InterpretML entry, and **DiCE is named** inside Responsible AI Toolbox. Describe these as missing **direct canonical entries**, not absent methods. Main `interpretml/interpret` is a **link/description correction**, not an entirely missing InterpretML ecosystem.

NLA, `kitft/nla-inference`, Tuned Lens, Jacobian Lens, AxBench, Neuronpedia, Overcomplete, NeuroX and both vLLM-Hook/vllm-lens are already listed. Their checkpoints, datasets, compatibility layers and demos should be nested improvements where appropriate. Neither a second NLA bullet nor a second AxBench library bullet is justified. Interpreto, nnterp, PyReFT and Steerling recur across the reports: count each once. Multiple NLA AV/AR files are one artifact family, not eight independent additions.

**Independent primary check:** `git show f5a023133bfc2997ca90926af8852e1774169ab4:README.md`; exact URL/string membership checks. No additional GitHub repository search was required.

### 2. Do contributor figures measure unique humans and project-specific credit? **Only estimated account attribution.**

I independently exhausted `/contributors?anon=true&per_page=100&page=N` for **14 repositories**. SHAP required four pages; TransformerLens two; the other twelve one. Numeric account IDs were unique within each response. The two GitHub lanes' principal counts replicated, including SHAP 270 User accounts, TL 192, circuit-tracer 17, Interpreto 10, ICA Lens two and Oracles two. Anonymous records were kept separate, not counted as humans.

InterpretML main has **50 User accounts**, but `microsoftopensource` explicitly calls itself a management **“service account”**, `msftgits` an **“operations account”**, and `interpret-ml` is a project identity. Conservatively excluding these yields **47 plausible attributed accounts**, matching the steering lane. That is not verified personhood or active-maintainer breadth.

The HF lane's ambiguous `claude` treatment needs harmonization: [current profile](https://api.github.com/users/claude) says company **`@anthropics`** despite `type:User` and a 2009 creation date. That supports **conservative exclusion as apparent AI/service attribution**, not proof of a specific account's legal identity or exclusive automation. Prefer AxBench **six plausible accounts plus one excluded/uncertain service identity** to an unqualified seven humans; do not let account age prove humanity.

Causalab has eight User accounts. Core commit records identify `canrager` and `can-goodfire` with the same author name, **Can Rager**; `maxsloef` has profile name Max Loeffler and `maxsloef-goodfire` remains a plausible second work identity. Thus **6–7 estimated people / eight attributed accounts** is defensible only with alias uncertainty, not a census.

**Monorepo/copy credit:** circuit-tracer's [bundled frontend README](https://github.com/decoderesearch/circuit-tracer/blob/7f66876689f59e92fc3641650d38b8bd41749ec4/circuit_tracer/frontend/assets/README.md) calls itself **“Snapshot of the frontend code”** from the Anthropic papers. Interpreto contains `interpreto/_vendor/overcomplete`. Do not count these as independent method inventions. Crucially, **copied source is not itself proof of inherited Git contributor history**: circuit-tracer's frontend-path history returned six commits back to its May 2025 release, not demonstrated pre-creation ancestors. The mechanism report's stronger “inherited frontend history” wording is not established by this check. Retain 17 repository-attributed accounts, but leave backend-specific/historically inherited human breadth **unknown**. Do not sum paper/package repositories or source contributors and HF artifact authors.

### 3. Are dates and maintenance claims correctly derived? **Dates replicate; maintenance adjectives require restraint.**

For each of the 14 repositories, I read `default_branch` from the core repo object and fetched `/commits?sha=DEFAULT_BRANCH`. Table dates below are the tip's **committer timestamp**, not `updated_at`, issue closure, HF `lastModified`, or a guessed `main`. Notably pytorch-grad-cam defaults to **`master`**, not `main`. All independently observed tips/stars reproduced the supplied values.

A recent tip can be formatting/dependency/docs: InterpretML August 17 is **“ruff format to latest version”**; SHAP October 4 is a dependency bump; ICA September 30 adds demos/website tooling; Steerling July 14 fixes packaging CI. These still establish public changes, not new scientific capability. Repository creation is not publication/idea origin; a model's release can precede its code repo. Avoid “years continuously maintained” inferred from two endpoint dates.

**CI correction:** Interpreto's latest three successful runs were Pages deployment, dependency graph update and Release Drafter—not three passing implementation test suites. ICA's latest three were two Pages builds and PyPI publishing. Causalab's failed October 5 Tests run was on **`nehal/task-loader-docs`**, not current main; the successful September 30 main run was a dependency graph update. circuit-tracer's latest sampled runs were **`action_required` on PR branches**. None warrants either “current main tests pass” or “current main is broken.” Report workflow names, branch and conclusion, not a generic green/failed-CI quality score. GitHub release absence also does not prove absence of PyPI releases: Steerling has no release object, yet its July 14 **Release to PyPI** workflow succeeded for tag `v0.2.0`.

### 4. Is the README's TransformerLens/HF distinction current? **No; substantive correction supported.**

The independently fetched [TL README](https://github.com/TransformerLensOrg/TransformerLens/blob/191170906559adf5ede1560097718cf431b972ac/README.md) says **“`TransformerBridge` is the recommended path”**, **“By default it preserves raw HuggingFace weights”**, and legacy `HookedTransformer.from_pretrained` **“was removed in TransformerLens 4.0”**. The [migration guide](https://github.com/TransformerLensOrg/TransformerLens/blob/191170906559adf5ede1560097718cf431b972ac/docs/source/content/migrating_to_v4.md) exists at the same tip.

Replace the blanket “not as HuggingFace-compatible” comparison with a versioned explanation of bridge/raw-HF versus legacy transformed-weight numerics. The README's advertised architecture/model counts and parity claims are **author claims**, not locally reproduced compatibility coverage. nnterp remains a useful NNsight-standardization sublink, not a new engine and not automatically uniquely HF-compatible.

### 5. Do circuit-tracer and Causalab represent distinct usable work? **Yes, with methodological/support limits.**

circuit-tracer's [README](https://github.com/decoderesearch/circuit-tracer/blob/7f66876689f59e92fc3641650d38b8bd41749ec4/README.md) and [attribution implementation](https://github.com/decoderesearch/circuit-tracer/blob/7f66876689f59e92fc3641650d38b8bd41749ec4/circuit_tracer/attribution/attribute.py) establish graph construction plus feature interventions, **dependent on pretrained MLP transcoders**. It is not a generic SAE trainer or a ground-truth circuit oracle. Its README calls the NNsight backend **“still experimental”**, slower/less memory-efficient and potentially missing functionality. Its July v0.5.2 release and September NNsight-0.8 port are concrete persistence signals, not universal model support.

Causalab's [hypothesis-analysis docs](https://github.com/goodfire-ai/causalab/blob/8e8d5d1f8f9ca8f42bfce7c6b5eef194f012660e/docs/hypothesis_analysis.md) support a different, non-SAE task: testing causal hypotheses. I independently fetched [issue #79 and comments](https://github.com/goodfire-ai/causalab/issues/79): the maintainer says **“The bug itself is real and unchanged”** when closing it as refiled to internal tracking. A September 30 mirror sync does not establish that particular residual-skip write defect is fixed. **Current fix status unknown**. Neither issue closure nor internal/private activity should substitute for public-default-branch evidence.

### 6. Are Interpreto and ICA Lens meaningful non-SAE omissions? **Yes; don't overclaim independence or interpretation validity.**

Interpreto's [linear probe implementation](https://github.com/FOR-sight-ai/interpreto/blob/b3b9a0fcbb46b891d0029d89a6561307114073a0/interpreto/concepts/probes/linear.py), method catalogue and original [LogitLens](https://github.com/FOR-sight-ai/interpreto/blob/b3b9a0fcbb46b891d0029d89a6561307114073a0/interpreto/lens/logit_lens.py) are substantive beyond the vendored Overcomplete dictionary-learning substrate. Catalogue includes PCA/ICA/NMF/SVD/KMeans and supervised probes; some future methods remain explicitly unavailable. The LogitLens docstring warns early-layer scores are **“rather than as calibrated probabilities”**. A multi-method toolkit entry is justified; separate bullets for its vendored methods are not.

ICA Lens's [FastICA implementation](https://github.com/liusida/ica-lens-paper/blob/6ad5bee4c94d22173e6ffefe20a0f9ba96c703d9/src/icalens/_fastica.py) explicitly credits adaptation from **Richard Hakim's FastICA_torch**; it is a reusable implementation, not a newly invented independent-component algorithm. Its [steering docs](https://github.com/liusida/ica-lens-paper/blob/6ad5bee4c94d22173e6ffefe20a0f9ba96c703d9/docs/steering.md) and [Qwen3.5 fit card](https://huggingface.co/sida/icalens-qwen3.5-2b-ultrachat-1m) support reusable fitted residual transforms, with layer/preprocessing contracts. The card says **“Standard ICA scores are signed and are not probabilities.”** Its fitted artifact has zero likes/downloads and **no stated artifact license**; no efficiency superiority or semantic/causal faithfulness was independently reproduced. With only June–September persistence/two attributed accounts, label it new paper-derived tooling, not a mature community standard.

### 7. Is the September 2026 Activation Oracle release real and different from NLA? **Yes.**

The public [Qwen3.6-27B API](https://huggingface.co/api/models/adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3.6-27B) returns created **2026-09-25T23:51:19Z**, lastModified **23:51:36Z**, zero likes, 20 downloads, public/ungated. Its [card](https://huggingface.co/adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3.6-27B) explicitly maps to the Oracles repository and describes activation-input natural-language QA. Main's September 26 tip and `nl_probes/sft.py` independently support source maintenance and training infrastructure.

The card's classification scores are not proof of mechanistic faithfulness: it itself reports the **untrained base already scores 72–93%** zero-shot on those evaluations. Adapter license is **unknown**; do not inherit Apache rights from its base. Describe Oracles as activation QA, official NLA as matched verbalizer/reconstructor training, and introspection adapters as behavior/weight auditing. The mechanism report's Anthropic “non-mechanistic” wording was parent-attested after a 403, so avoid presenting that blog wording as independently retrieved here. GitHub/HF primary material suffices for the QA-versus-reconstruction distinction.

### 8. Are HF store, collection and model-license/category claims reliable? **The central claims replicate; qualify use rights.**

- **Tuned Lens:** source [loader](https://github.com/AlignmentResearch/tuned-lens/blob/abdac0c4de23d9f6d6c8459d576ad203aec15deb/tuned_lens/load_artifacts.py) defaults to `AlignmentResearch/tuned-lens`, **`repo_type="space"`**. Public recursive [tree API](https://huggingface.co/api/spaces/AlignmentResearch/tuned-lens/tree/main/lens?recursive=true&limit=1000) returned **113 records / 36 directories with both config.json and params.pt**, including two Meta-Llama-3-8B variants. Runtime reports RUNNING, not tested interaction. This is a strong **nested artifact-store link**, not a new library. Source main still ends August 2025.
- **Official NLA collection:** public [full collection API](https://huggingface.co/api/collections/kitft/nla-models-69fa80a3c69880bba63eddc6) contains **eight actual items/four AV–AR pairs**. Position fields include a gap; do not infer item count from maximum position. Existing NLA should gain one collection sublink, not eight bullets.
- **Steerling:** [HF card](https://huggingface.co/guidelabs/steerling-8b) says **“An interpretable causal diffusion language model with concept steering.”** Its actual [concept-head source](https://github.com/guidelabs/steerling/blob/f34ffa89e46969445f3cf6e7c885e9623a2047c1/steerling/models/interpretable/concept_head.py) and card confirm model-specific concept decomposition with unknown features and an epsilon correction, not a general hook library or exhaustive explanation. Apache metadata/body coexist with **“provided for research and evaluation purposes”** and ongoing upstream-license review. Report conflicting/qualified weight-use wording, not a legal conclusion that commercial rights are either definitely granted or definitely prohibited. Keep as a model artifact/watchlist, not a minimum library addition.

## Minimum recommended additions: nine task-covering entries

**All metrics below independently reproduced.** H≈ means plausible unique attributed non-service accounts, not verified people or human-written code; stars are tie-break popularity. Dates are UTC calendar dates, creation → latest default-branch commit. Ordered breadth-first **within type/task**, not as one ranking across incomparable scientific tasks. Quotes are short verbatim excerpts of primary README/card text, with line-break normalization where needed.

| Addition / kind | H≈ / stars | Created → default tip | Task fit, primary quote and limit |
|---|---:|---|---|
| [SHAP](https://github.com/shap/shap) — attribution library | 270 / 25,794 | 2016-11-22 → [2026-10-04 main](https://github.com/shap/shap/commit/50be8f4fd7031d535d515042741320f53272d211) | Missing direct canonical link, not absent by name. [“a game theoretic approach”](https://github.com/shap/shap/blob/50be8f4fd7031d535d515042741320f53272d211/README.md); inspected TreeExplainer. Requires background/feature-dependence assumptions, not causal truth. |
| [pytorch-grad-cam](https://github.com/jacobgil/pytorch-grad-cam) — CV attribution library | 52 / 12,993 | 2017-05-31 → [2026-08-13 master](https://github.com/jacobgil/pytorch-grad-cam/commit/704393448a7b0c620ee2c2b9597723f1d7f17b3d) | Fills existing CV/XAI scope. [“Includes metrics for checking if you can trust the explanations”](https://github.com/jacobgil/pytorch-grad-cam/blob/704393448a7b0c620ee2c2b9597723f1d7f17b3d/README.md); inspected ROAD implementation. Author phrasing is not certification of trust. |
| [Quantus](https://github.com/understandable-machine-intelligence-lab/Quantus) — explanation-evaluation library | 20 / 676 | 2021-03-18 → [2026-08-20 main](https://github.com/understandable-machine-intelligence-lab/Quantus/commit/85bc29d137d8f42835dd392f5cc441ad61d6d1f1) | Explicit missing validity/evaluation task. [“A toolkit to evaluate neural network explanations”](https://github.com/understandable-machine-intelligence-lab/Quantus/blob/85bc29d137d8f42835dd392f5cc441ad61d6d1f1/README.md); inspected parameter-randomization metric. Operational metrics are not universal faithfulness guarantees. |
| [circuit-tracer](https://github.com/decoderesearch/circuit-tracer) — circuit/feature-intervention library | 17 / 2,915 | 2025-05-28 → [2026-09-11 main](https://github.com/decoderesearch/circuit-tracer/commit/7f66876689f59e92fc3641650d38b8bd41749ec4) | [“finding circuits using features from (cross-layer) MLP transcoders”](https://github.com/decoderesearch/circuit-tracer/blob/7f66876689f59e92fc3641650d38b8bd41749ec4/README.md). One proportional dictionary-based causal-workflow addition; dependencies and backend scope explicit. |
| [Interpreto](https://github.com/FOR-sight-ai/interpreto) — probes/concepts/attribution library | 10 / 207 | 2025-02-26 → [2026-10-06 main](https://github.com/FOR-sight-ai/interpreto/commit/b3b9a0fcbb46b891d0029d89a6561307114073a0) | [“both supervised (probes and CAVs) and unsupervised (dictionary learning) approaches”](https://github.com/FOR-sight-ai/interpreto/blob/b3b9a0fcbb46b891d0029d89a6561307114073a0/README.md). Broad non-SAE methods and original lens/probe code; credit NNsight/Overcomplete dependencies. |
| [Causalab](https://github.com/goodfire-ai/causalab) — causal hypothesis-testing library | 6–7 / 118; eight accounts | 2025-04-25 → [2026-09-30 main](https://github.com/goodfire-ai/causalab/commit/8e8d5d1f8f9ca8f42bfce7c6b5eef194f012660e) | [“test hypotheses about how neural networks solve tasks”](https://github.com/goodfire-ai/causalab/blob/8e8d5d1f8f9ca8f42bfce7c6b5eef194f012660e/README.md). Strong non-SAE fit, with mirror/alias and intervention-bug caveats. |
| [Activation Oracles](https://github.com/adamkarvonen/activation_oracles) — paper/training code + released adapters | 2 / 103 | 2025-07-30 → [2026-09-26 main](https://github.com/adamkarvonen/activation_oracles/commit/5712762cfc29a18d6414a1cf2cccb4ff4432ced5) | [“answers natural-language questions about them”](https://huggingface.co/adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3.6-27B). NLA comparator, not replacement; paper/main branch separation, model contract and base baseline matter. |
| [ICA Lens](https://github.com/liusida/ica-lens-paper) — new paper-derived package + fitted transforms | 2 / 45 | 2026-06-08 → [2026-09-30 main](https://github.com/liusida/ica-lens-paper/commit/6ad5bee4c94d22173e6ffefe20a0f9ba96c703d9) | [“ICA Lens interprets language-model activations with Independent Component Analysis.”](https://github.com/liusida/ica-lens-paper/blob/6ad5bee4c94d22173e6ffefe20a0f9ba96c703d9/README.md). Strong new non-SAE fit despite short persistence/small account base; artifact license unknown. |
| [CausalGym](https://github.com/aryamanarora/causalgym) — paper benchmark + [dataset](https://huggingface.co/datasets/aryaman/causalgym) | 2 / 57 | 2023-10-10 → [2024-11-30 main](https://github.com/aryamanarora/causalgym/commit/0f3129ff3b6c5c8264892f30a25be25150ae9179) | [“a benchmark for comparing the performance of causal interpretability methods”](https://huggingface.co/datasets/aryaman/causalgym). Old stable reference/data, explicitly GPTNeoX-focused; HF seven likes/117 downloads are different metrics. |

Attribution examples for small/new recommended projects: ICA `liusida`, `FeijiangHan`; Oracles `adamkarvonen`, `thejaminator`; CausalGym `aryamanarora`, `cgpotts`; Interpreto `AntoninPoche`, `fanny-jourdan`, `thomas-mullor` plus seven other attributed accounts. Full contributor lists were inspected, including separate anonymous attribution (SHAP 54; GradCAM one; Quantus seven; Interpreto six; Causalab six). These do not enlarge H≈.

**Corrections/nested additions, not extra nine:** fix main InterpretML (47 plausible accounts / 6,956 stars; created 2019-05-03 → 2026-08-17 main); update TL4 wording; add official NLA weights collection, real Tuned Lens Space store, and AxBench Concept16K link with its synthetic/SAE-concept-sampling caveat. Date Graphpatch inactivity rather than assert abandonment; broaden Overcomplete's description beyond SAEs. The latter two corrections are supported by the supplied lane, not independently re-fetched here.

## Concise task-based taxonomy

Use task headings and a small **kind label** (`library`, `paper-code`, `benchmark`, `dataset/weights`, `demo/service`) rather than inventing a separate section for every method family:

1. **Inspect and intervene:** hooks/backends, naming/compatibility, patching, causal hypotheses and circuit discovery. Nest nnterp beneath NNsight; distinguish tracing from rendering.
2. **Read representations:** token lenses, probes, PCA/ICA/NMF/concept methods, activation-language methods. Preserve a prominent NLA subsection; contrast reconstruction versus QA versus self-report without declaring any faithful ground truth.
3. **Explain predictions / interpretable-by-design models:** feature attribution, local surrogates, counterfactuals and glassbox/concept architectures. Separate counterfactual explanation from actionable causal recourse; model-specific Steerling from arbitrary-model libraries.
4. **Steer and evaluate:** reusable steering/intervention training; method/paper artifacts; controls and benchmarks. Matched-KL/utility, random/prompt/fine-tune baselines and side effects are central, not an afterthought.
5. **Explore and reproduce:** browsers/demos, pretrained transforms/adapters and benchmark/probe datasets. Link artifact collections beneath their producer tools. Hosted platforms are not automatically open-source libraries.
6. **Adjacent tooling / further reading:** structured output, adapter utilities, surveys/blogs/tutorials and clearly labeled author experiments. These can support analysis but do not themselves explain a model.

A durable entry needs one line: **task + method/substrate/model scope + kind + specific dated status**. Keep volatile stars/account counts/default-tip evidence in a dated research appendix, not frozen into every prose bullet. High probe accuracy, readable labels, heatmaps, reconstruction and successful steering validate different properties.

## What to defer

- **Second wave, not rejected:** AutoCircuit/CircuitsVis, PyTorch Concepts, Mishax, Bergson, Delphi, LatentQA/introspective-interp. Reports supply useful evidence, but all nine minimum tasks should be covered before expanding specialist branches. PyReFT/steering-vectors can be historically useful with their 2025 tips, not present-tense maintenance promises. Fast-inference interp-engine is a valuable August–October 2026 watchlist/nested comparison to the two already-listed serving hook tools, not proof existing serving tools are obsolete.
- **SAEs:** at most one suite link (Gemma Scope 2) and optional one feature-explanation tool under relevant existing tasks; no per-layer/width bullets. Defer multimodal/protein SAE exemplars from the minimum list. Interesting cross-domain demonstrations and generated annotations are not established human-interpreted causal features.
- **Source/provenance/license gaps:** unresolved diatoms/interp-methods/talkative-probes, sparse-probing's source 404, Universal-NLA source 404, thin CounterFact/instruct-model cards, and numerous generated-organism dumps. A public HF artifact or guessed source title does not settle producer identity or reuse rights.
- **New demos/models:** Steerling, Dynolab, Subtext, PCD and brainscope belong in model/demo/watchlist categories. Do not describe lens readouts as private reasoning or subjective experience. PCD's public code/checkpoint remains unknown in supplied evidence; Subtext is a Jacobian-lens consumer, not another method family.
- **Alibi:** source-available BSL caveat needs explicit labeling. **UncensorBench:** supplied lane reports unsafe execution/provenance limitations; defer routine runnable-benchmark endorsement rather than bury that caveat. These legal/safety points were not independently re-audited here.

## Evidence weaknesses, coverage and exact verification ledger

**New discovery searches in this challenge: zero.** No search/issues metric calls. This is an independent verification/reduction pass, not another discovery lane. Exact repository search queries remain in the source reports: mechanisms **seven searches / 590 unique search-result candidates**, steering **seven / 649**, HF **74 logged list queries / 3,600 deduplicated repo-type/id entries**. The HF report correctly distinguishes machine filtering from **180 manual entry inspections / 47 deep artifact checks**; do not call all 3,600 manually screened. The mechanism lane's late supplement raises its deep repo inspections from 26 to 30; its acceptance evidence retains the older base count. Counts overlap across lanes and seeded discoveries. **Cross-lane unique candidate total is unknown**, not 590+649+3,600, and a repo, an artifact and a family are different units.

My independent scope: **14 core repository/contributor/default-tip/README checks**; inspected source/docs for each of the nine minimum entries (CausalGym docs/implementation scope), main InterpretML, TL migration and Tuned Lens loader. Six top GitHub projects additionally had releases, latest five core issue/PR records and three workflow runs inspected. **12 public HF requests** covered six distinct artifact/collection repositories plus runtime/tree/card views. No exhaustive rediscovery or additional package testing was attempted.

Exact GitHub endpoint patterns (authenticated `gh api`, credentials never printed):

- `repos/{owner}/{repo}`;
- `repos/{owner}/{repo}/contributors?per_page=100&page=N&anon=true`, until a short page;
- `repos/{owner}/{repo}/commits?sha={default_branch}&per_page=3` (extra three repos used `per_page=1`);
- `repos/{owner}/{repo}/readme`;
- `repos/{owner}/{repo}/contents/{source_path}?ref={tip_sha}`;
- selected `releases?per_page=1`, `issues?state=all&sort=updated&direction=desc&per_page=5`, `actions/runs?per_page=3`;
- `repos/goodfire-ai/causalab/issues/79` and `/comments?per_page=100`;
- `repos/goodfire-ai/causalab/commits?author={canrager,can-goodfire,maxsloef,maxsloef-goodfire}&per_page=1`;
- `repos/decoderesearch/circuit-tracer/git/trees/7f66876689f59e92fc3641650d38b8bd41749ec4?recursive=1`;
- circuit-tracer `commits?path=circuit_tracer/frontend/assets&per_page=100` and bundled frontend README; Interpreto `contents/interpreto/_vendor?ref=b3b9a0fcbb46b891d0029d89a6561307114073a0`;
- `users/{claude,canrager,can-goodfire,maxsloef,maxsloef-goodfire,microsoftopensource,msftgits,interpret-ml}`.

Exact public HF requests, each prefixed `https://huggingface.co/`:

1. `api/models/adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3.6-27B`
2. `adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3.6-27B/raw/main/README.md`
3. `api/spaces/AlignmentResearch/tuned-lens`
4. `api/spaces/AlignmentResearch/tuned-lens/runtime`
5. `api/spaces/AlignmentResearch/tuned-lens/tree/main/lens?recursive=true&limit=1000`
6. `api/models/guidelabs/steerling-8b`
7. `guidelabs/steerling-8b/raw/main/README.md`
8. `api/collections/kitft/nla-models-69fa80a3c69880bba63eddc6`
9. `api/datasets/aryaman/causalgym`
10. `datasets/aryaman/causalgym/raw/main/README.md`
11. `api/models/sida/icalens-qwen3.5-2b-ultrachat-1m`
12. `sida/icalens-qwen3.5-2b-ultrachat-1m/raw/main/README.md`

**Residual risks:** runtime/model compatibility, scientific faithfulness and exact people/active-maintainer counts remain unverified. No tests, source execution, tensors or weights were downloaded. CI/runtime states are API observations only. HF artifacts' licenses and source-specific layer/preprocessing conventions cannot be borrowed from base models or sibling projects. Source reports use capped noisy star-sorted searches, so low-star/new projects remain undersampled despite network follow-up. Their counts and quoted samples are not comprehensiveness proofs. Main-branch source pins preserve GitHub evidence; HF cards here are `main` snapshot fetches, not guaranteed immutable future content. Material unresolved Causalab bug fix and source/artifact rights must survive final condensation.

## Bounded follow-up: central synthesis and queued parent corrections

After the first artifact was saved, I read the complete central report at `slop/research/20261007_interpretability/results.md`. This is an additional targeted review, **not exhaustive certification or restarted discovery**. The central report's strong method distinctions and qualified recommendations are largely supported; the following corrections/additions should survive final condensation.

### Newly replicated primary findings

1. **Transluce HF coverage was materially missed by lowercase author filtering.** Exact public queries `https://huggingface.co/api/models?author=Transluce&limit=100&full=true` and the same URL with `author=transluce` returned **14 and zero records**, respectively. This establishes behavior for these endpoints/owner, not a universal claim about all HF APIs. Independently fetched `TransluceAI/introspective-interp` README links the [official collection](https://huggingface.co/collections/Transluce/training-language-models-to-explain-their-own-computations). Two exact released cards/APIs replicate central values: [feature explainer](https://huggingface.co/Transluce/features_explain_llama3.1_8b_llama3.1_8b_instruct), zero likes/232 downloads, created 2025-12-05 and modified 2026-01-03; [patch-effect adapter](https://huggingface.co/Transluce/act_patch_qwen3_8b_qwen3_8b), zero/20, created 2025-12-17 and modified 2026-01-03. **Source/weight mapping is now established**, not unknown as the initial HF discovery could suggest. These weights strengthen introspective-interp as a second-wave addition with actual released artifacts.

   The feature card explicitly says **“trained to map SAE features”** to **“explanations derived from Neuronpedia”** and requires custom continuous-token handling. Its claimed arbitrary-feature generalization is not replicated. The patch card describes prediction of **intervention effects using CounterFact**, not executing/validating every purported causal explanation. It contains a minor prose inconsistency: the usage paragraph says input ablation while its CLI is `--task act_patch`. Prefer task/config/source contracts over copying that paragraph. Do not turn SAE-derived supervision into independent human semantic ground truth, or assume a plain AutoModel invocation is sufficient. Feature card reports MIT, patch card has no license header; base-model obligations remain separate.

2. **NLA indexing warning is independently reproduced.** The [extractor](https://github.com/kitft/natural_language_autoencoders/blob/main/nla/datagen/extractors.py) documents **“HF's `hidden_states[K+1]`”** and registers a hook on `layers[layer_index]`. The [README](https://github.com/kitft/natural_language_autoencoders) example nonetheless uses `hidden_states[20]`. Thus L20 is zero-based block 20 output / usual HF index 21, **not necessarily the README example's vector**. Keep this as an actual producer documentation inconsistency, not a new README omission. Sidecars/model/site contracts are safer than copying the snippet. Indexing alone does not settle final-layer normalization conventions for every model.

3. **interp-engine gradient distinction is supported by its docs.** Independently fetched [GRADIENTS.md](https://github.com/decoderesearch/interp-engine/blob/main/docs/GRADIENTS.md): **“Attribution that needs a gradient *of the model* is eager-only.”** Its table says downstream autograd works on either backend; through-forward requires eager `requires_grad=True` and is never supported in its vLLM backend. This is a package/backend contract, not an eternal theorem that no modified vLLM fork could ever implement training. No runtime test was performed.

4. **Docent correction is independently supported.** Direct public fetch of [product page](https://transluce.org/docent) says **“Docent helps analyze AI agent transcripts”** and **“Docent supports any text-only, single or multi-agent transcript.”** Central placement under agent transcript/behavior-rubric auditing is sound; activation interpretation/steering remains the misleading original description.

5. **Graphpatch is 617 days, not 17.** Direct authenticated default-main commit check returns `d1ecec2949ea622eb04a4a364ef08942d6a8025f`, **2025-01-27T19:49:56Z**, a dev migration to uv. Central report's 617-day figure at its October 6 snapshot matches the parent cache; no abandonment declaration is established by that date alone.

### Remaining central-report fixes

- **Latest DEFAULT-BRANCH commit must be visible uniformly.** The central report defines a last-20-commit source/config heuristic and often substitutes it in the principal tables. This is useful supplementary evidence but **does not fully meet the user's explicit latest-default-branch-commit requirement**. Add a separate default-tip column/link for every recommended GitHub row, alongside optional source/config date. For independently checked examples: SHAP latest main **2026-10-04**, versus heuristic source September 25; interp-engine main **2026-10-02**, versus source/config September 28; InterpretML tip **2026-08-17**, versus source May 28. Quiet package/runtime history and algorithm changes can then be compared honestly without mixing measures.
- **Do not erase relevant monorepo maintenance with the heuristic.** interp-engine's independently fetched October 2 tip explicitly fixes bundled visualizer dependency advisories including an RCE. Even if a source-only classifier excludes frontend/docs files, this is substantive public maintenance. No implementation testing or independent security remediation validation was performed here; the commit's verification remains author-reported.
- **circuit-tracer “inherited frontend contributor history” remains too strong.** Source reuse is verified; Git-history inheritance/backend-specific account credit is not. Replace that phrase with **“bundles credited Anthropic frontend code; 17 repository-attributed accounts are not a backend-specific maintainer count.”** This is narrower than denying all inherited history.
- **Raw/account estimates:** central 47 adjusted InterpretML, six or qualified 6–7 AxBench, and qualified Causalab aliases are appropriately cautious. “Author examples” are public attribution, not legal-identity validation. Keep this framing.
- **Candidate-count correction reproduced:** reading `evidence_new`, `evidence_extra`, and `evidence_shortlist` snapshot JSONs yields **40 rows / 38 distinct canonical repo fields**. That is not 40 independent projects and not 38 recommendations. Existing/candidate/HF counts overlap and must not be summed.

The central report has sensible broad navigation, but its decision summary is substantially broader than the minimum nine-entry set above. Present **a small first pass plus a typed optional second wave** rather than imply every listed model/demo/paper should be installed or given equal prominence. Given verified Transluce releases, introspective-interp can be the first activation-language second-wave entry; keep its distinct training targets and SAE-derived feature supervision visible.

**Follow-up ledger:** seven public HTTP requests (two exact HF author queries; metadata/card pairs for the two Transluce releases; Docent page), four authenticated GH README/source fetches (Transluce README, interp-engine gradient docs, NLA extractor and README), and two authenticated default-main commit requests (interp-engine, Graphpatch). Parent snapshot JSONs were read as data only; collector/project code was not executed. No additional GitHub searches, packages, tensors or inference. Initial independent scope counts above remain the first-pass counts, not silently recomputed to include this supplement.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Read baseline README, all three reports and central synthesis; independently checked eight initial material claim groups plus bounded Transluce/indexing/gradient/Docent/default-tip follow-up; returned nine minimum additions, taxonomy, deferrals and explicit evidence weaknesses."
    }
  ],
  "changedFiles": [
    "/home/code/.pi/agent/sessions/--workspace-2026--/subagent-artifacts/outputs/48cad1b1-6752-4dcf-90e8-1328d9a67622/research/evidence-challenge.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "git show f5a023133bfc2997ca90926af8852e1774169ab4:README.md; git diff f5a0231 -- README.md; git status --porcelain=v1; git diff --cached --name-only",
      "result": "passed",
      "summary": "Baseline README unchanged despite advanced workspace HEAD; existing research files left untouched; no staged files."
    },
    {
      "command": "Authenticated gh api core metadata/contributors/default-tip/readme/source/issues/releases/actions/profile endpoints",
      "result": "passed",
      "summary": "14 repository checks; fully paginated SHAP/TL contributors; source/credit and Causalab issue independently inspected; zero search requests."
    },
    {
      "command": "Public HF HTTP API/card/tree/runtime/collection requests",
      "result": "passed",
      "summary": "12 exact requests; verified Qwen3.6 Oracle, 36 Tuned Lens config/params pairs, eight NLA collection items, ICA/CausalGym and Steerling scope/terms."
    },
    {
      "command": "Bounded central-report follow-up: seven public HTTP requests, six authenticated GH source/tip requests, parent snapshot JSON reads",
      "result": "passed",
      "summary": "Replicated Transluce 14 vs zero author filtering, released-card mapping, NLA indexing inconsistency, eager-only model gradients, Docent transcript scope, Graphpatch date and 40/38 canonical count."
    },
    {
      "command": "Repository tests, model inference or package installation",
      "result": "not-run",
      "summary": "Prohibited by read-only research boundary."
    }
  ],
  "validationOutput": [
    "Nine proposed direct URLs absent at requested README SHA; SHAP/LIME/DiCE already named, NLAs/inference/AxBench already linked.",
    "Stars/default-tip dates replicated; copied source does not establish inherited Git attribution; CI successes often deployment/metadata rather than tests.",
    "Current claude profile @anthropics supports conservative service exclusion; Causalab aliases and fix status remain qualified."
  ],
  "residualRisks": [
    "Human accounts are estimates, not proof of people, authorship or active maintainers.",
    "No runtime reproduction; Causalab issue #79 current fix status unknown.",
    "Capped overlapping discovery cannot establish completeness or a cross-lane unique screened total.",
    "HF adapter/ICA licenses and Steerling weight-use wording remain qualified or unresolved."
  ],
  "noStagedFiles": true,
  "diffSummary": "Only configured external research report written; no project edits.",
  "reviewFindings": [
    "Material presentation corrections: distinguish missing direct links from absent methods; update TL4/HF characterization; retain NLA prominence; separate libraries, paper code, data and demos.",
    "Evidence corrections: don't label deployment/metadata CI as passing tests; don't infer inherited contributor history merely from copied frontend source; don't sum cross-lane candidate counts."
  ],
  "manualNotes": "Workspace HEAD advanced since lane snapshots but README matches f5a0231. Minimum nine entries favor task coverage with one transcoder-dependent addition. Bounded central-report follow-up verifies Transluce case-sensitive discovery/mapped releases, NLA indexing inconsistency, gradient contract and Docent scope; requests actual default-tip columns and qualified frontend contributor-history wording. Parent 40 rows / 38 canonical repos replicated."
}
```

— PI/gpt-6.1-sol; fresh read-only reviewer artifact preserved by parent.
