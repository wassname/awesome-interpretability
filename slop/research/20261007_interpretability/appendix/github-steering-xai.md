# GitHub steering, concepts/probes, interpretation validity and classical/CV XAI

Snapshot: **2026-10-07 Australia/Perth / 2026-10-06 UTC**. Target `README.md` was read first, at main **f5a023133bfc2997ca90926af8852e1774169ab4**. Read-only research: no project edits, installs, repository execution, publishing or pushes. This lane did not query HF; HF links in GitHub READMEs are pointers, not HF metadata verification.

## Executive recommendation

Fix the InterpretML link and expand the explanation section with **SHAP, LIME (historical), DiCE, Alibi (source-available), Quantus, Zennit/CRP and pytorch-grad-cam**. For LLM concepts/probes, **Interpreto and PyTorch Concepts** fill a larger conceptual gap than another SAE implementation; **nnterp** is a practical extension of already-listed NNsight. Add narrowly labeled **steering-vectors / PyReFT** only with their real last-default-commit dates. New 2026 discoveries worth a separate architecture/artifact/watchlist treatment: **ICA Lens, Guide Labs Steerling and Dual-Steering**, with **hidden-directions** retained as an experimental watchlist. Preserve the existing NLA entry prominently; it is not an omission.

Bounded shortlist: **20 verified additions/corrections**, not 20 equally endorsed maintained libraries. Main-table ranking favors contributor breadth first, stars second; high task-fit highlights are editorial priorities within/alongside that evidence ranking. Historical baselines, benchmarks and single-paper/model-specific artifacts must not get the same maintenance promise as current reusable libraries. SAEs receive no dedicated expansion in this lane.

## Coverage and exact search ledger

Seven repository searches only, each `gh api -X GET search/repositories -f q='<query>' -f per_page=100 -f sort=stars -f order=desc`. No search/issues requests. Each returned repository name/description/date/star record was triaged; this is not a claim that every repository implementation was reviewed.

| # | Exact query | API total_count | Returned/triaged |
|---|---|---:|---:|
| 1 | `"activation steering" in:readme stars:>=5 archived:false` | 262 | 100 |
| 2 | `concept interpretability in:description,readme stars:>=20 archived:false` | 4,516 | 100 |
| 3 | `representation probing in:readme stars:>=20 archived:false` | 1,665 | 100 |
| 4 | `explainability evaluation in:description stars:>=5 archived:false` | 76 | 76 |
| 5 | `topic:explainable-ai stars:>=30` | 256 | 100 |
| 6 | `steering created:>=2026-01-01 in:name,description,readme stars:>=2 archived:false` | 14,116 | 100 |
| 7 | `interpretability created:>=2026-01-01 in:name,description,readme stars:>=2 archived:false` | 21,699 | 100 |

**676 result rows, 649 unique search-result repositories.** Important limitation: broad `in:readme` terms had poor precision; popular lists, coding-agent skills and unrelated infrastructure crowded out specialist repositories, especially in the two created-in-2026 searches. Only the first star-sorted 100 were returned per search; total_count is NOT screened count. The 2026 search windows are not comprehensive evidence of absence. Search #1 did surface the new July-2026 **moudrkat/brainscope** project (52 stars); its author network exposed hidden-directions.

Compensation using core API network discovery, not extra repository searches:
- `GET /users/{owner}/repos?per_page=100&sort=created&direction=desc`, paginated for **ndif-team, FOR-sight-ai, wisent-ai, pyc-team, stanfordnlp, understandable-machine-intelligence-lab, AlphaLab-USTC, moudrkat, KihoPark, nishantsubramani, montemac, deel-ai, AI4LIFE-GROUP, google, pietrobarbiero, AsaCooperStickland**.
- 3,269 distinct network repository records retrieved. Nonfork filter plus keyword filtering of the large google account reduced this to **315 name/description records manually triaged**; 302 were not in search results. **951 unique manually name/description-triaged records** across search and retained networks. The filtered-out google records were machine-prefiltered, not individually read.
- Three primary resource READMEs yielded **24 / 36 / 117 unique GitHub repo links respectively**: [awesome-representation-engineering](https://github.com/chrisliu298/awesome-representation-engineering), [awesome-activation-engineering](https://github.com/ZFancy/awesome-activation-engineering), [Awesome-Interpretability-in-Large-Language-Models](https://github.com/ruizheliUOA/Awesome-Interpretability-in-Large-Language-Models). These are discovery aids, not authority for recommendations. Parent additionally supplied `liusida/ica-lens-paper`, independently verified here with core metadata, README, FastICA/Lens source and steering documentation; it was not falsely attributed to this lane’s seven searches. Followed KihoPark’s older geometry work to **dual-steering**; PyC → **Baby Steerling NOTICE** → **guidelabs/steerling**; AI4LIFE → **OpenXAI/SpLiCE**; Wisent → **Ster/UncensorBench**; Stanford → **preft**; NDIF → **Liars’ Bench Expanded**.
- **48 successful primary repository metadata + README inspections**, **39 full metadata/contributors/default-commit/issues/releases/tree bundles**, and **26 downloaded source/NOTICE specimens**, including source for all 20 main-table entries. This is deeper review than the 951 metadata triages. Failed guessed identifiers were not counted as successful primary inspections.

## Metric method and caveats

Authenticated `gh api` was used for GitHub; no credentials printed. For each shortlisted repo: `GET /repos/{owner}/{repo}` supplies stars, creation, archived, default_branch; `GET /repos/{repo}/commits?sha={default_branch}&per_page=1` supplies the newest default-branch commit and **committer timestamp**; `GET /contributors?per_page=100&anon=true` was fully paginated with `--paginate --slurp`; `GET /readme`, `/releases?per_page=1`, `/issues?state=all&sort=updated&direction=desc&per_page=5`, `/git/trees/{default_branch}?recursive=1` and selected `/contents/{path}?ref={commit_sha}` supply primary evidence. Source links below are pinned to the observed default SHA. GitHub issues responses include PRs; samples show signals, not a project-wide responsiveness statistic.

**H ≈ unique attributed apparently non-bot accounts, not verified humans or proof human-written.** Deduplicate numeric account IDs; exclude type Bot and obvious bot logins, and additionally exclude known AI/service/project identities: `claude` (profile: Claude, @anthropics), `microsoftopensource` (profile explicitly calls it a management service account), `msftgits` (operations account), and conservatively `interpret-ml` (project identity). For example nnterp’s naive five User accounts become **four** plausible human-account identities; InterpretML becomes **47**, DiCE **21**. Anonymous commit records are separate (**A**); do not deduplicate anonymous emails into “humans” or count them as attributed people. Some apparently ordinary User accounts may still be shared/automated/AI-assisted; identity verification was not performed. Historical breadth does not measure active maintainers. The SHAP contributor response needed **four pages** (all others in the table one); contributor-API caching/attribution limitations remain.

Creation→last-default dates show **persistence**, not continuous development. Stars are a snapshot, not adoption or validity proof. Repo `updated_at`, recent PR closure, releases on other branches and issue activity are never substituted for the default-commit date. All 20 main-table repos report `archived=false`; “not archived” does not mean maintained.

## Ranked shortlist

Date links point to the exact latest observed default commit. H/A columns are estimates/anonymous commit identities. “Add” remains subject to the category and caveats in the evidence cards.

| Rank | Candidate / type & disposition | H ≈ / A | Stars | Repository created | Latest default commit (UTC date; branch) |
|---:|---|---:|---:|---|---|
| 1 | [shap/shap](https://github.com/shap/shap) — Library; add | 270 / 54 | 25,794 | 2016-11-22 | [2026-10-04](https://github.com/shap/shap/commit/50be8f4fd7031d535d515042741320f53272d211) `main` |
| 2 | [jacobgil/pytorch-grad-cam](https://github.com/jacobgil/pytorch-grad-cam) — Library; add | 52 / 1 | 12,993 | 2017-05-31 | [2026-08-13](https://github.com/jacobgil/pytorch-grad-cam/commit/704393448a7b0c620ee2c2b9597723f1d7f17b3d) `master` |
| 3 | [interpretml/interpret](https://github.com/interpretml/interpret) — Library; correct/add | 47 / 6 | 6,956 | 2019-05-03 | [2026-08-17](https://github.com/interpretml/interpret/commit/560f8dde814cac03aec89e189bc9874012c7f1a5) `main` |
| 4 | [marcotcr/lime](https://github.com/marcotcr/lime) — Historical library; add with stale flag | 42 / 19 | 12,166 | 2016-03-15 | [2021-07-29](https://github.com/marcotcr/lime/commit/fd7eb2e6f760619c29fca0187c07b82157601b32) `master` |
| 5 | [SeldonIO/alibi](https://github.com/SeldonIO/alibi) — Source-available library; conditional add | 21 / 3 | 2,648 | 2019-02-26 | [2025-10-10](https://github.com/SeldonIO/alibi/commit/99c3421d7c971c85893625e37da1133e7ddf1779) `master` |
| 6 | [interpretml/DiCE](https://github.com/interpretml/DiCE) — Library; add directly | 21 / 0 | 1,528 | 2019-05-02 | [2025-07-13](https://github.com/interpretml/DiCE/commit/8a3aea404f857fa599bfa7da663d94823b674688) `main` |
| 7 | [understandable-machine-intelligence-lab/Quantus](https://github.com/understandable-machine-intelligence-lab/Quantus) — Evaluation library; add | 20 / 7 | 676 | 2021-03-18 | [2026-08-20](https://github.com/understandable-machine-intelligence-lab/Quantus/commit/85bc29d137d8f42835dd392f5cc441ad61d6d1f1) `main` |
| 8 | [deel-ai/xplique](https://github.com/deel-ai/xplique) — Library; add | 15 / 5 | 755 | 2020-04-05 | [2026-09-25](https://github.com/deel-ai/xplique/commit/7fa573b6534f29f2eaa923522df0190fecb46f62) `master` |
| 9 | [chr5tphr/zennit](https://github.com/chr5tphr/zennit) — Library; add | 12 / 3 | 248 | 2020-11-10 | [2026-05-13](https://github.com/chr5tphr/zennit/commit/3e98348aa95e908f550ab2a13fca2245c30f7de3) `main` |
| 10 | [stanfordnlp/pyreft](https://github.com/stanfordnlp/pyreft) — Library; conditional add to adapters | 10 / 1 | 1,590 | 2024-02-17 | [2025-02-06](https://github.com/stanfordnlp/pyreft/commit/dafd0995a366d7b47160a337dcc388eda7431821) `main` |
| 11 | [AI4LIFE-GROUP/OpenXAI](https://github.com/AI4LIFE-GROUP/OpenXAI) — Benchmark/library artifact; historical add | 10 / 1 | 260 | 2022-06-08 | [2024-03-31](https://github.com/AI4LIFE-GROUP/OpenXAI/commit/a18288620464250856b55234266a6d1dabb64656) `main` |
| 12 | [FOR-sight-ai/interpreto](https://github.com/FOR-sight-ai/interpreto) — Library; high task-fit add | 10 / 6 | 207 | 2025-02-26 | [2026-10-06](https://github.com/FOR-sight-ai/interpreto/commit/b3b9a0fcbb46b891d0029d89a6561307114073a0) `main` |
| 13 | [pyc-team/pytorch_concepts](https://github.com/pyc-team/pytorch_concepts) — Alpha library; high task-fit add | 10 / 4 | 159 | 2024-06-22 | [2026-07-24](https://github.com/pyc-team/pytorch_concepts/commit/45dd8a329cda1473295eec4aef5f7c375a647d37) `master` |
| 14 | [rachtibat/zennit-crp](https://github.com/rachtibat/zennit-crp) — Library/paper-derived toolkit; add | 7 / 1 | 141 | 2022-06-07 | [2026-01-14](https://github.com/rachtibat/zennit-crp/commit/ecf1b7873bf0bf5ca34b7d21407ccb95549198b8) `master` |
| 15 | [steering-vectors/steering-vectors](https://github.com/steering-vectors/steering-vectors) — Library; historical/conditional add | 5 / 0 | 163 | 2024-01-18 | [2025-02-21](https://github.com/steering-vectors/steering-vectors/commit/5459bd1287be642ec75a4ab000dc833262bcb7f4) `main` |
| 16 | [ndif-team/nnterp](https://github.com/ndif-team/nnterp) — Library; add beneath NNsight | 4 / 0 | 121 | 2024-08-08 | [2026-07-02](https://github.com/ndif-team/nnterp/commit/b4a31274692f986e493ac5d20ba20a4ec8640955) `main` |
| 17 | [guidelabs/steerling](https://github.com/guidelabs/steerling) — 2026 model-specific package/artifact; add separately | 3 / 1 | 241 | 2026-02-22 | [2026-07-14](https://github.com/guidelabs/steerling/commit/f34ffa89e46969445f3cf6e7c885e9623a2047c1) `main` |
| 18 | [AI4LIFE-GROUP/SpLiCE](https://github.com/AI4LIFE-GROUP/SpLiCE) — Paper artifact with reusable API; specialist add | 2 / 0 | 134 | 2024-02-02 | [2025-03-27](https://github.com/AI4LIFE-GROUP/SpLiCE/commit/9a498102ce7c6701f4afe361ffaa86c39b47fa5f) `main` |
| 19 | [liusida/ica-lens-paper](https://github.com/liusida/ica-lens-paper) — 2026 paper-derived library; high task-fit add | 2 / 0 | 45 | 2026-06-08 | [2026-09-30](https://github.com/liusida/ica-lens-paper/commit/6ad5bee4c94d22173e6ffefe20a0f9ba96c703d9) `main` |
| 20 | [KihoPark/dual-steering](https://github.com/KihoPark/dual-steering) — 2026 one-paper artifact; add to reading | 1 / 0 | 18 | 2026-02-15 | [2026-05-19](https://github.com/KihoPark/dual-steering/commit/ec4d6657faeba9e13e6b6e07c5cfd53e19ebe7fa) `main` |

Ordering is breadth-first; Alibi edges DiCE on stars at the same adjusted count, and PyReFT/OpenXAI edge Interpreto/PyC on stars at ten accounts. **Task fit reverses the practical reading priority there:** Interpreto/PyC are fresher, directly address probing/non-SAE concepts, and should receive more space than old PyReFT/OpenXAI. Likewise one-account Dual-Steering is worth a reading link because information geometry fits the user’s interests, but its stars do not justify calling it maintained. New model-specific Steerling has a smaller attributed base than its nine-person paper author list: paper authors and code contributors are different measurements.

## Primary quotes, source checks and maintenance evidence

Quotes are short verbatim fragments of the primary repository README, not endorsement of the claim. Each quoted source is linked at its observed default SHA. Handles below are attribution examples, not verified identity/personhood.

### 1. shap/shap

- [Primary README](https://github.com/shap/shap/blob/50be8f4fd7031d535d515042741320f53272d211/README.md): “is a game theoretic approach to explain the output of any machine learning model.”
- **Fit / inspected implementation:** Foundational model-agnostic and tree/neural feature attribution, not causal circuit discovery. Very broad contributor base. TreeExplainer source explicitly distinguishes interventional and tree-path-dependent feature perturbation; explain background-data assumptions, not “the true reason”. [Source: `shap/explainers/_tree.py`](https://github.com/shap/shap/blob/50be8f4fd7031d535d515042741320f53272d211/shap/explainers/_tree.py).
- **Maintenance / limits:** Latest default commit is a dependency bump, not an explainer innovation. Release v0.53.0rc0 is a prerelease (2026-09-07). GPU-build and plotting fixes have live PR/issue activity.
- **Attribution examples:** `slundberg`, `ryserrao`, `connortann`; [paginated contributor endpoint](https://api.github.com/repos/shap/shap/contributors?per_page=100&anon=true).

### 2. jacobgil/pytorch-grad-cam

- [Primary README](https://github.com/jacobgil/pytorch-grad-cam/blob/704393448a7b0c620ee2c2b9597723f1d7f17b3d/README.md): “Includes metrics for checking if you can trust the explanations, and tuning them for best performance.”
- **Fit / inspected implementation:** Major CV omission. CNNs and ViTs, multiple CAM algorithms, deep feature factorization, and ROAD evaluation. Source ROAD imputation/evaluation code makes this more than attractive heatmaps. Keep in CV attribution, not mechanistic-circuit libraries. [Source: `pytorch_grad_cam/metrics/road.py`](https://github.com/jacobgil/pytorch-grad-cam/blob/704393448a7b0c620ee2c2b9597723f1d7f17b3d/pytorch_grad_cam/metrics/road.py).
- **Maintenance / limits:** 2026-08-13 default commit adds SESS support; recent closed PR #603 addresses 3-D activation weights. No GitHub release objects returned; this does not establish absence of PyPI releases.
- **Attribution examples:** `jacobgil`, `shaun0927`, `josepdecid`; [paginated contributor endpoint](https://api.github.com/repos/jacobgil/pytorch-grad-cam/contributors?per_page=100&anon=true).

### 3. interpretml/interpret

- [Primary README](https://github.com/interpretml/interpret/blob/560f8dde814cac03aec89e189bc9874012c7f1a5/README.md): “you can train interpretable glassbox models and explain blackbox systems.”
- **Fit / inspected implementation:** Correct the existing InterpretML link: interpret-community is an extension, not the main package. Main InterpretML includes explainable boosting/glassbox models and blackbox explanations. Source contains EBMClassifier/EBMRegressor and global/local explanation interfaces. [Source: `python/interpret-core/interpret/glassbox/_ebm.py`](https://github.com/interpretml/interpret/blob/560f8dde814cac03aec89e189bc9874012c7f1a5/python/interpret-core/interpret/glassbox/_ebm.py).
- **Maintenance / limits:** Latest default commit is formatting (2026-08-17); v0.7.8 release 2026-03-17. October PR discussions do not change the measured default-branch date.
- **Attribution examples:** `paulbkoch`, `testonlyinprod`, `msplants`; [paginated contributor endpoint](https://api.github.com/repos/interpretml/interpret/contributors?per_page=100&anon=true).

### 4. marcotcr/lime

- [Primary README](https://github.com/marcotcr/lime/blob/fd7eb2e6f760619c29fca0187c07b82157601b32/README.md): “This project is about explaining what machine learning classifiers (or models) are doing.”
- **Fit / inspected implementation:** Canonical local surrogate baseline, text/tabular/image, distinct from SHAP despite wrapper integrations already mentioned in README. Source LimeBase learns a locally linear sparse model on perturbed data. [Source: `lime/lime_base.py`](https://github.com/marcotcr/lime/blob/fd7eb2e6f760619c29fca0187c07b82157601b32/lime/lime_base.py).
- **Maintenance / limits:** Default master ends 2021-07-29; latest GitHub release 0.2.0.0 dates 2020-04-03. PRs closed/updated in September 2026 are not evidence they were merged into master. Recommend historical baseline, not maintained.
- **Attribution examples:** `marcotcr`, `dyanni3`, `aikramer2`; [paginated contributor endpoint](https://api.github.com/repos/marcotcr/lime/contributors?per_page=100&anon=true).

### 5. SeldonIO/alibi

- [Primary README](https://github.com/SeldonIO/alibi/blob/99c3421d7c971c85893625e37da1133e7ddf1779/README.md): “is a source-available Python library aimed at machine learning model inspection and interpretation.”
- **Fit / inspected implementation:** Anchors, counterfactuals and local/global black/white-box explanation. AnchorTabular source uses a trained tabular sampler and anchor search; strong fit for existing counterfactual taxonomy, not a drift-monitoring replacement for alibi-detect. [Source: `alibi/explainers/anchors/anchor_tabular.py`](https://github.com/SeldonIO/alibi/blob/99c3421d7c971c85893625e37da1133e7ddf1779/alibi/explainers/anchors/anchor_tabular.py).
- **Maintenance / limits:** Default master 2025-10-10 docs change; v0.9.6 release 2024-04-18. IMPORTANT: current LICENSE is Business Source License 1.1, not open source; non-production grant and limited educational production grant, Apache change after version-specific four-year period. Label source-available and link licensing.
- **Attribution examples:** `jklaise`, `RobertSamoilescu`, `mauicv`; [paginated contributor endpoint](https://api.github.com/repos/SeldonIO/alibi/contributors?per_page=100&anon=true).

### 6. interpretml/DiCE

- [Primary README](https://github.com/interpretml/DiCE/blob/8a3aea404f857fa599bfa7da663d94823b674688/README.rst): “Diverse Counterfactual Explanations (DiCE) for ML”
- **Fit / inspected implementation:** Currently only named inside Responsible AI Toolbox integration. Give a direct entry for diverse feasible counterfactual explanations and feature constraints. Genetic explainer source corroborates optimization implementation. Counterfactual explanations are not proof of causal or actionable real-world recourse. [Source: `dice_ml/explainer_interfaces/dice_genetic.py`](https://github.com/interpretml/DiCE/blob/8a3aea404f857fa599bfa7da663d94823b674688/dice_ml/explainer_interfaces/dice_genetic.py).
- **Maintenance / limits:** Default main 2025-07-13, v0.12 release same day. September 2026 open NumPy/pandas compatibility PRs and bug reports; do not promise NumPy 2/pandas 3 fixes have landed.
- **Attribution examples:** `gaugup`, `raam93`, `amit-sharma`; [paginated contributor endpoint](https://api.github.com/repos/interpretml/DiCE/contributors?per_page=100&anon=true).

### 7. understandable-machine-intelligence-lab/Quantus

- [Primary README](https://github.com/understandable-machine-intelligence-lab/Quantus/blob/85bc29d137d8f42835dd392f5cc441ad61d6d1f1/README.md): “Offers more than **35+ metrics in 6 categories** for XAI evaluation”
- **Fit / inspected implementation:** Best validity/evaluation omission: faithfulness, robustness, localization, complexity, randomization, axiomatic metrics. Inspected Model Parameter Randomisation Test source. Metrics measure operationalized properties, not semantic correctness of all explanations. [Source: `quantus/metrics/randomisation/mprt.py`](https://github.com/understandable-machine-intelligence-lab/Quantus/blob/85bc29d137d8f42835dd392f5cc441ad61d6d1f1/quantus/metrics/randomisation/mprt.py).
- **Maintenance / limits:** Default main 2026-08-20, v0.6.0 release 2025-07-21. README explicitly warns original metric authors have not verified every implementation. October metrics/docs PRs show activity but are not merged-default evidence.
- **Attribution examples:** `annahedstroem`, `dkrako`, `aaarrti`; [paginated contributor endpoint](https://api.github.com/repos/understandable-machine-intelligence-lab/Quantus/contributors?per_page=100&anon=true).

### 8. deel-ai/xplique

- [Primary README](https://github.com/deel-ai/xplique/blob/7fa573b6534f29f2eaa923522df0190fecb46f62/README.md): “The _Concepts_ module allows you to extract human concepts from a model and to test their usefulness with respect to a class.”
- **Fit / inspected implementation:** Attribution, feature visualization, CRAFT/NMF concept discovery and metrics. CRAFT source imports sklearn NMF and computes Sobol concept sensitivity; a substantive non-SAE route for vision concepts. More reusable than listing standalone Craft paper repo separately. [Source: `xplique/concepts/craft.py`](https://github.com/deel-ai/xplique/blob/7fa573b6534f29f2eaa923522df0190fecb46f62/xplique/concepts/craft.py).
- **Maintenance / limits:** v2.0.2 release and default commit 2026-09-25. README warns about Keras 3/TF 2.16 and recommends TF <=2.15; describes PyTorch support as partial, though CRAFT source supports both. Avoid blanket framework-compatibility claims.
- **Attribution examples:** `fel-thomas`, `Agustin-Picard`, `lucashervier`; [paginated contributor endpoint](https://api.github.com/repos/deel-ai/xplique/contributors?per_page=100&anon=true).

### 9. chr5tphr/zennit

- [Primary README](https://github.com/chr5tphr/zennit/blob/3e98348aa95e908f550ab2a13fca2245c30f7de3/README.md): “strong focus on Layerwise Relevance Propagation”
- **Fit / inspected implementation:** PyTorch rule-based attribution/LRP, canonizers and custom relevance rules. Source rules.py uses custom Hook/BasicHook machinery. Different scientific tradition from sparse autoencoders; useful for CV and other torch.nn.Module models. [Source: `src/zennit/rules.py`](https://github.com/chr5tphr/zennit/blob/3e98348aa95e908f550ab2a13fca2245c30f7de3/src/zennit/rules.py).
- **Maintenance / limits:** 1.0.0 release 2025-07-31; default 2026-05-13 citation update. Recent closed PR #240 fixes epsilon compatibility with torch 2.10. A newer citation alone is not broad new model support.
- **Attribution examples:** `chr5tphr`, `rodrigobdz`, `rachtibat`; [paginated contributor endpoint](https://api.github.com/repos/chr5tphr/zennit/contributors?per_page=100&anon=true).

### 10. stanfordnlp/pyreft

- [Primary README](https://github.com/stanfordnlp/pyreft/blob/dafd0995a366d7b47160a337dcc388eda7431821/README.md): “Training ReFT with any pretrained LMs on HuggingFace”
- **Fit / inspected implementation:** Trainable low-rank representation interventions, complementing already-listed pyvene. Inspected LoReFT formula/source h + R^T(Wh+b-Rh). Relevant intervention/adapters baseline, but fine-tuning alone is not an explanation; cross-link rather than promote as a new causal-discovery toolkit. [Source: `pyreft/interventions.py`](https://github.com/stanfordnlp/pyreft/blob/dafd0995a366d7b47160a337dcc388eda7431821/pyreft/interventions.py).
- **Maintenance / limits:** Default main ends 2025-02-06; v0.1.0 release 2025-02-04. 2026 reproduction and save/load issues remain visible. Mature enough historically, but flag >20 months without default-branch change.
- **Attribution examples:** `frankaging`, `aryamanarora`, `PinetreePantry`; [paginated contributor endpoint](https://api.github.com/repos/stanfordnlp/pyreft/contributors?per_page=100&anon=true).

### 11. AI4LIFE-GROUP/OpenXAI

- [Primary README](https://github.com/AI4LIFE-GROUP/OpenXAI/blob/a18288620464250856b55234266a6d1dabb64656/README.md): “systematically evaluate the quality of explanations generated by attribute-based explanation methods.”
- **Fit / inspected implementation:** Curated datasets/models and attribution evaluation beyond AxBench, especially tabular high-stakes settings. Source evaluator maps ground-truth agreement, prediction faithfulness and stability metrics. README advertises 22 metrics; do not equate that automatically to the 11 top-level selector keys in inspected evaluator.py. [Source: `openxai/evaluator.py`](https://github.com/AI4LIFE-GROUP/OpenXAI/blob/a18288620464250856b55234266a6d1dabb64656/openxai/evaluator.py).
- **Maintenance / limits:** Default main 2024-03-31 is README-only; no GitHub releases returned. Open model-loading/versioning issues persist. Useful as a labeled evaluation artifact, not current production toolkit.
- **Attribution examples:** `danwley`, `jiaqima`, `Chirag126`; [paginated contributor endpoint](https://api.github.com/repos/AI4LIFE-GROUP/OpenXAI/contributors?per_page=100&anon=true).

### 12. FOR-sight-ai/interpreto

- [Primary README](https://github.com/FOR-sight-ai/interpreto/blob/b3b9a0fcbb46b891d0029d89a6561307114073a0/README.md): “We propose both supervised (probes and CAVs) and unsupervised (dictionary learning) approaches.”
- **Fit / inspected implementation:** Strongest recent broad probing/concept alternative: linear/logistic/SVM/means-difference and centroid probes; NMF, semi/convex NMF, ICA, PCA, SVD and KMeans alongside optional SAEs. Attribution, concepts and evaluation in one HF/NNsight workflow; do not reduce it to SAE tooling. Source linear.py implements the advertised linear probe family. [Source: `interpreto/concepts/probes/linear.py`](https://github.com/FOR-sight-ai/interpreto/blob/b3b9a0fcbb46b891d0029d89a6561307114073a0/interpreto/concepts/probes/linear.py).
- **Maintenance / limits:** Default main 2026-10-06 merges lens methods; v0.5.1 release 2026-09-18. NNsight 0.8 migration PR #164 is open; do not assume compatibility is released. README explicitly marks some concept interpretation/output-attribution metrics as unavailable.
- **Attribution examples:** `AntoninPoche`, `fanny-jourdan`, `thomas-mullor`; [paginated contributor endpoint](https://api.github.com/repos/FOR-sight-ai/interpreto/contributors?per_page=100&anon=true).

### 13. pyc-team/pytorch_concepts

- [Primary README](https://github.com/pyc-team/pytorch_concepts/blob/45dd8a329cda1473295eec4aef5f7c375a647d37/README.md): “Public APIs may change and be unstable between releases.”
- **Fit / inspected implementation:** Concept-based models by design: annotated tensors, interpretable layers, concept bottlenecks, interventions and probabilistic graphical models. Inspected CBM example constructs ConceptVariable/EmbeddingVariable with linear concept layers and BayesianNetwork inference; architecture-level interpretability, not post-hoc SAE replacement marketing. [Source: `examples/utilization/1_pgm/0.1_cbm.py`](https://github.com/pyc-team/pytorch_concepts/blob/45dd8a329cda1473295eec4aef5f7c375a647d37/examples/utilization/1_pgm/0.1_cbm.py).
- **Maintenance / limits:** Default master 2026-07-24; latest GitHub release object v0.0.10 (2024-12-03) does not establish latest PyPI pre-release. Active October development PRs; explicit alpha/API-instability warning is essential.
- **Attribution examples:** `gdefe`, `pietrobarbiero`, `francescoTheSantis`; [paginated contributor endpoint](https://api.github.com/repos/pyc-team/pytorch_concepts/contributors?per_page=100&anon=true).

### 14. rachtibat/zennit-crp

- [Primary README](https://github.com/rachtibat/zennit-crp/blob/ecf1b7873bf0bf5ca34b7d21407ccb95549198b8/README.md): “method to disentangle the attribution flows associated with concepts learned by the model via conditional backpropagation”
- **Fit / inspected implementation:** Concept Relevance Propagation moves from “where” heatmaps to concept-conditional attribution flows/relevance maximization. Inspected CondAttribution and ChannelConcept imports. Not a training-based SAE method and not necessarily a library of human-labeled semantic concepts. Cross-link as Zennit companion. [Source: `crp/attribution.py`](https://github.com/rachtibat/zennit-crp/blob/ecf1b7873bf0bf5ca34b7d21407ccb95549198b8/crp/attribution.py).
- **Maintenance / limits:** Default master 2026-01-14 fixes visualization batch-size-one crash. GitHub v0.6.0 release 2023-05-23. Later closed PRs are not necessarily merged into master; release freshness and source freshness differ.
- **Attribution examples:** `rachtibat`, `sebastian-lapuschkin`, `maxdreyer`; [paginated contributor endpoint](https://api.github.com/repos/rachtibat/zennit-crp/contributors?per_page=100&anon=true).

### 15. steering-vectors/steering-vectors

- [Primary README](https://github.com/steering-vectors/steering-vectors/blob/5459bd1287be642ec75a4ab000dc833262bcb7f4/README.md): “Steering vectors / representation engineering for transformer language models in Pytorch / Huggingface”
- **Fit / inspected implementation:** Clean reusable HF steering baseline independent of repeng: positive/negative examples, customizable aggregation and layer mapping; inspected train_steering_vector.py. Better main-library entry than raw CAA experiment code. [Source: `steering_vectors/train_steering_vector.py`](https://github.com/steering-vectors/steering-vectors/blob/5459bd1287be642ec75a4ab000dc833262bcb7f4/steering_vectors/train_steering_vector.py).
- **Maintenance / limits:** Default main and v0.12.2 release 2025-02-21; latest sampled PR fixes negative layer indices. No observed 2026 default development. Explicit stale date prevents star-based maintained claims.
- **Attribution examples:** `chanind`, `dtch1997`, `Felhof`; [paginated contributor endpoint](https://api.github.com/repos/steering-vectors/steering-vectors/contributors?per_page=100&anon=true).

### 16. ndif-team/nnterp

- [Primary README](https://github.com/ndif-team/nnterp/blob/b4a31274692f986e493ac5d20ba20a4ec8640955/README.md): “preserves the original HuggingFace implementations while solving the naming convention chaos through intelligent renaming.”
- **Fit / inspected implementation:** Standardized model/module access plus steering/probability/probing helpers. Source StandardizedTransformer inherits NNsight LanguageModel instead of reimplementing model architecture. Addresses the README TransformerLens vs HF-native tradeoff concretely. [Source: `nnterp/standardized_transformer.py`](https://github.com/ndif-team/nnterp/blob/b4a31274692f986e493ac5d20ba20a4ec8640955/nnterp/standardized_transformer.py).
- **Maintenance / limits:** Default main 2026-07-02 packaging fix; latest GitHub release v1.0b1 is beta, 2025-07-16. October vision PRs are open; sandwich-normalization issue #53 is relevant. Exclude Claude account from estimated humans even though GitHub labels it User.
- **Attribution examples:** `Butanium`, `JadenFiotto-Kaufman`, `irajmoradi`; [paginated contributor endpoint](https://api.github.com/repos/ndif-team/nnterp/contributors?per_page=100&anon=true).

### 17. guidelabs/steerling

- [Primary README](https://github.com/guidelabs/steerling/blob/f34ffa89e46969445f3cf6e7c885e9623a2047c1/README.md): “An interpretable causal diffusion language model.”
- **Fit / inspected implementation:** New interpretable-by-design architecture and inference/attribution/steering package; known/discovered concept decomposition plus residual correction. Source ConceptHead has known-concept sparse/dense intervention paths; interventions are not automatically supported for discovered concepts. Not a universal library for explaining arbitrary pretrained LMs. [Source: `steerling/models/interpretable/concept_head.py`](https://github.com/guidelabs/steerling/blob/f34ffa89e46969445f3cf6e7c885e9623a2047c1/steerling/models/interpretable/concept_head.py).
- **Maintenance / limits:** Created 2026-02-22, default main 2026-07-14 CI change; no GitHub release objects returned. README requires Python >=3.13, CUDA 12.8 and >=18GB VRAM; fine-tuning and training-data attribution not included. Apache source, weights have separate commercial-use caveat. HF assets not independently checked in this lane.
- **Attribution examples:** `ayaabdelsalam91`, `adebayoj`, `giangnguyen2412`; [paginated contributor endpoint](https://api.github.com/repos/guidelabs/steerling/contributors?per_page=100&anon=true).

### 18. AI4LIFE-GROUP/SpLiCE

- [Primary README](https://github.com/AI4LIFE-GROUP/SpLiCE/blob/9a498102ce7c6701f4afe361ffaa86c39b47fa5f/README.md): “**sparse, nonnegative combinations of human-interpretable, semantic concepts**”
- **Fit / inspected implementation:** Non-SAE CLIP decomposition against a semantic vocabulary, with API for image/class/dataset decomposition and spurious-correlation analysis. Source splice.py enumerates supported CLIP/OpenCLIP models and vocabularies. Sparse representation does not imply a sparse autoencoder. [Source: `splice/splice.py`](https://github.com/AI4LIFE-GROUP/SpLiCE/blob/9a498102ce7c6701f4afe361ffaa86c39b47fa5f/splice/splice.py).
- **Maintenance / limits:** Created 2024-02-02, default main 2025-03-27; no GitHub release objects. Two attributed accounts. README explicitly shows unintuitive vocabulary artifacts for low-resolution CIFAR images; semantic labels should not be treated as guaranteed explanations.
- **Attribution examples:** `alex-oesterling`, `ushabhalla`; [paginated contributor endpoint](https://api.github.com/repos/AI4LIFE-GROUP/SpLiCE/contributors?per_page=100&anon=true).

### 19. liusida/ica-lens-paper

- [Primary README](https://github.com/liusida/ica-lens-paper/blob/6ad5bee4c94d22173e6ffefe20a0f9ba96c703d9/README.md): “ICA Lens interprets language-model activations with Independent Component Analysis.”
- **Fit / inspected implementation:** Parent discovery independently source-checked here: installable icalens package, blockwise PyTorch FastICA, reusable fitted lenses, signed component profiles, text/chat analysis and residual-stream ICA-coordinate steering. Source _fastica.py implements the fixed-point algorithm and credits Richard Hakim’s FastICA_torch adaptation. Lens API supports reconstruction/analysis/generation. An especially strong non-SAE omission, not merely a paper demo. [Pinned steering documentation](https://github.com/liusida/ica-lens-paper/blob/6ad5bee4c94d22173e6ffefe20a0f9ba96c703d9/docs/steering.md) distinguishes additive and clamp interventions and cautions against treating qualitative examples as universal control. Component semantic labels/signs remain hypotheses, not discovered ground truth. [Source: `src/icalens/_fastica.py`](https://github.com/liusida/ica-lens-paper/blob/6ad5bee4c94d22173e6ffefe20a0f9ba96c703d9/src/icalens/_fastica.py).
- **Maintenance / limits:** Created 2026-06-08; default main 2026-09-30 adds demos/website tooling; v0.4.0 release 2026-09-29. Two attributed accounts, no anonymous identities, no issues returned. Read docs/steering.md at pinned SHA: ICA signs arbitrary; confirm with independent probes; coordinate dosage need not be monotonic; additive steering requires fitting without row normalization or preprocessing center; clamps restore activation norm so final scores can differ from requested target. README’s compute-efficiency superiority claim is not independently benchmarked here. HF sida/ica-lens collection remains for HF lane.
- **Attribution examples:** `liusida`, `FeijiangHan`; [paginated contributor endpoint](https://api.github.com/repos/liusida/ica-lens-paper/contributors?per_page=100&anon=true).

### 20. KihoPark/dual-steering

- [Primary README](https://github.com/KihoPark/dual-steering/blob/ec4d6657faeba9e13e6b6e07c5cfd53e19ebe7fa/README.md): “This codebase implements Euclidean and Dual steering”
- **Fit / inspected implementation:** Information geometry of softmax as an alternative to Euclidean/additive steering, with concept counterfactuals and LLM/CLIP experiments. Inspected iterative e_steering and dual-space method code. Excellent specialist fit despite one contributor and modest stars; do not claim a general supported library. [Source: `information_geometry/steering/method.py`](https://github.com/KihoPark/dual-steering/blob/ec4d6657faeba9e13e6b6e07c5cfd53e19ebe7fa/information_geometry/steering/method.py).
- **Maintenance / limits:** Created 2026-02-15; default main 2026-05-19 “conjugate gradient”; no releases/issues returned. README narrows experiments to Gemma-3-4B and MetaCLIP-2; broader applicability unknown.
- **Attribution examples:** `KihoPark`; [paginated contributor endpoint](https://api.github.com/repos/KihoPark/dual-steering/contributors?per_page=100&anon=true).

## Benchmarks beyond AxBench; excluded/deferred projects (not additional blanket recommendations)

The existing AxBench entry is correct in spirit: concept detection/steering evaluation, not SAE discovery. “Benchmark” must distinguish **steering success/side effects**, **explanation faithfulness**, **representation-similarity validity** and **deception-probe datasets**.

| Project | H ≈ / stars | Created → latest default UTC date | Primary finding / disposition |
|---|---:|---|---|
| [moudrkat/hidden-directions](https://github.com/moudrkat/hidden-directions) | 1 / 5 | 2026-05-07 → [2026-09-04](https://github.com/moudrkat/hidden-directions/commit/4a681fae1339a22947b1b2639600c48796d24334) | New-2026 experimental library discovered through brainscope’s author network. README: “asserts no scientific findings;” calibration/audit tooling, not a validated benchmark. Inspected checker.py uses configurable violation regex plus length/language/repetition coherence guards; these are fallible operational checks. v0.1.6/default September 4, no issues returned. High methodology fit but only one attributed account, two anonymous identities and explicit small-N/work-in-progress caveat; ICA Lens displaces it from the bounded main shortlist after parent discovery. |
| [wisent-ai/uncensorbench](https://github.com/wisent-ai/uncensorbench) | 1 / 22 | 2025-11-30 → [2026-10-01](https://github.com/wisent-ai/uncensorbench/commit/eb04f879a01673744a4bbb93ec83e1c400e766ad) | Benchmark to evaluate refusal/compliance and capability preservation, including model modifications/representation engineering. Primary quote: “A higher compliance score is not inherently better.” **Defer main recommendation:** one-account base, corpus provenance absent, README warns default hybrid sends data to Anthropic and executes model code. Source code_execution.py actually uses Docker `--network=host` plus writable host bind; not a hardened sandbox. Strong relevant discovery beyond AxBench, but unsafe to present as a routine install-and-run benchmark. No release objects returned. |
| [mklabunde/resi](https://github.com/mklabunde/resi) | 1 / 17 | 2024-07-31 → [2025-04-07](https://github.com/mklabunde/resi/commit/24ab9e5055c71527445b0b196f5872f3cbe9a020) | One-paper benchmark with reusable representation-similarity implementations. README: “It comprises 24 similarity measures, comes with 14 different architectures and spans the Vision, Language and Graph domain.” Inspected CKA implementation. Optional representation-analysis reading/evaluation artifact; not a steering benchmark. Original setup still includes anonymity placeholders. Low breadth and stale default date keep it below main library shortlist. |
| [ndif-team/liars-bench-expanded](https://github.com/ndif-team/liars-bench-expanded) | 2 / 1 | 2026-06-01 → [2026-07-20](https://github.com/ndif-team/liars-bench-expanded/commit/075723f32b7bccd0a9581234712c5d72d391cf20) | 2026 dataset documentation repo, not a library. README: “pre-computed residual-stream activation tensors” and “without requiring GPU access.” Describes 72,863 labeled honest/deceptive outputs and AWS residual tensors. Promising probing dataset handoff; data size/content/provenance not independently downloaded/verified. HF original dataset pointer belongs to HF lane. No release objects returned. |
| [pyc-team/babysteerling](https://github.com/pyc-team/babysteerling) | 2 / 5 | 2026-07-22 → [2026-10-05](https://github.com/pyc-team/babysteerling/commit/814b365031b934222b39e52b7975a1c8e063c894) | 2026 didactic demo/package, not another general library or official Guide Labs release. README: “A didactic package to develop Interpretable Language Models (ILMs).” NOTICE attributes independent small-scale implementation to Guide Labs. October #14 PyC refactor and earlier concept-loss/sampler fixes show activity. Good tutorial link if wanted, not core replacement for PyC or Steerling. |
| [moudrkat/brainscope](https://github.com/moudrkat/brainscope) | 1 / 52 | 2026-07-06 → [2026-09-23](https://github.com/moudrkat/brainscope/commit/545a3f8803555223e5d2da291605c75205ae4560) | New-2026 discovery directly from search #1. OpenAI-compatible HF server/UI for activation probes, steering, residual-stream/lens traces. Created July, default September, v0.4.3 release September 14. Retain as demo/interactive-tool watchlist rather than conflating UI adoption with validated interpretability; author’s hidden-directions is the more focused methodology/tooling entry. |
| [wisent-ai/ster](https://github.com/wisent-ai/ster) | 8 / 341 | 2025-03-22 → [2026-10-06](https://github.com/wisent-ai/ster/commit/9ff7fc72b2d0f5ce1df26adc211694fb5d8b5bae) | Reusable Rust/Candle representation reading/steering tool, genuinely relevant and broader contributor estimate than several specialist artifacts. README: “The previous Python package and `wisent` command were removed in the Rust cutover.” **Defer until contract review:** same README’s extensive included-model list advertises MoE/non-rotary families while Explicit boundaries still says those families fail. Do not recommend it as the old Python Wisent package or endorse all runtime support claims. Current source tree is Rust; no runtime tests performed. |
| [AlphaLab-USTC/AlphaSteer](https://github.com/AlphaLab-USTC/AlphaSteer) | 2 / 67 | 2025-05-11 → [2025-11-20](https://github.com/AlphaLab-USTC/AlphaSteer/commit/3cd0d2e1efad2c701c1e5e3dd46ca42debfd4030) | ICLR 2026 label, but repo was created in 2025 and default last changed November 2025. A one-paper null-space-constrained refusal steering method, not a maintained general library. Qwen reproduction and missing matrix/generation issues visible. Optional reading, lower priority than a new validated general benchmark. |
| [stanfordnlp/preft](https://github.com/stanfordnlp/preft) | 2 / 6 | 2026-05-13 → [2026-05-27](https://github.com/stanfordnlp/preft/commit/840223ea9ec5838fd398499d77b55bcd0d64487d) | Actual May-2026 discovery via Stanford network. README: “Apply parameter-efficient adapters during prefill only; discard them for decode.” Useful ReFT/LoRA serving artifact; forked vLLM path, no releases/issues returned. Defer as mostly efficient fine-tuning/serving scope creep, unless adapters section intentionally expands beyond interpretability. |
| [tensorflow/tcav](https://github.com/tensorflow/tcav) | 14 / 654 | 2018-07-03 → [2021-09-16](https://github.com/tensorflow/tcav/commit/b922c44bcc64c6bdddb8f661d732fa2145c99d95) | Canonical concept-vector method, original library persists since 2018 but default stops September 2021. README: “TCAV learns concepts from examples.” Include technique/reference if desired, not another maintained library claim; avoids omitting classical concept-based methods merely because SAEs dominate. Earlier guessed google/tcav and google-research/tcav paths failed; verified canonical repo is tensorflow/tcav. |
| [JonathanCrabbe/CARs](https://github.com/JonathanCrabbe/CARs) | 2 / 17 | 2022-03-09 → [2022-10-07](https://github.com/JonathanCrabbe/CARs/commit/00586c0a9ac222355dd4bf2f138484644f8c6557) | Nonlinear Concept Activation Regions, generalizes concept-based explanations. Two-account 2022 artifact; default stops October 2022. Useful historical contrast to linear CAVs, not stronger library recommendation than PyC/Interpreto. |
| [john-hewitt/control-tasks](https://github.com/john-hewitt/control-tasks) | 2 / 32 | 2019-08-18 → [2020-03-27](https://github.com/john-hewitt/control-tasks/commit/be70d7f42324797dcf2bb5360a94d8e64100fea8) | Foundational validity reading: README “Repository describing example random control tasks for designing and interpreting neural probes.” Measures probe memorization/selectivity rather than equating probe accuracy to information used by the model. Historical artifact; default 2020-03-27, not current LLM package. |
| [KihoPark/linear_rep_geometry](https://github.com/KihoPark/linear_rep_geometry) | 1 / 134 | 2023-10-28 → [2025-02-11](https://github.com/KihoPark/linear_rep_geometry/commit/40bee00b50a6fafcf2ee4db2c01602023aa366cc) | Older ICML-2024 one-paper geometry artifact. README “define a *causal inner product* that respects the semantic structure of language.” Good author-network bridge to Dual-Steering; one attributed plus eight anonymous identities is NOT nine verified humans. Optional reading, not generic library. |
| [nrimsky/CAA](https://github.com/nrimsky/CAA) | 1 / 254 | 2023-09-25 → [2024-05-23](https://github.com/nrimsky/CAA/commit/5dabbbd9a0bca5f25e174501e959de378806aa48) | Original steering experiment/dataset artifact, one attributed account, default May 2024. Keep as methodology reference. The reusable steering-vectors library is a stronger toolkit omission; do not count both as independent mature libraries. |
| [AsaCooperStickland/kl-then-steer](https://github.com/AsaCooperStickland/kl-then-steer) | 4 / 10 | 2023-10-11 → [2024-06-17](https://github.com/AsaCooperStickland/kl-then-steer/commit/8a54057bfd7ef778bc8a18651c9420693d7b03f3) | Research training/evaluation artifact, four attributed plus two anonymous identities, default June 2024. Toxicity/MT-Bench/PCA vs mean-difference evaluation, old pinned RepE/LLM-tuner stack. Methodology reading for control comparisons, not a standalone modern general benchmark. |

Other screened/deferred primary READMEs: **csinva/imodels** (interpretable tabular models; relevant to broad XAI scope but lower urgency than correcting InterpretML), **deel-ai/Craft** (prefer CRAFT module in maintained Xplique over duplicating paper code), **PAIR-code/saliency** (overlaps attribution libraries; contributor/default-date metrics not resolved in this lane), **andyzoujm/representation-engineering** (important original research repository, but no complete contributor/default-commit bundle here; unknown rather than assumed maintained). These are not negative quality judgments.

Explicit search exclusions: **alexgreensh/attention-span** is agent output style, not representation interpretability; **elder-plinius/OBLITERATUS** search hit is not sufficient evidence of a reusable analysis library and was not recommended; **semantica-agi/semantica**, generic agent memory/codegraph projects, paper-digest bots, trading/medical application repos and broad awesome lists were omitted for poor task fit. High stars on unrelated new agent infrastructure should not crowd out real methods. Guessed **brendel-group/repsim**, **similarity-repository/similarity**, **similarity-repository/representation-similarity**, **christianingmann/representational_similarity**, **guidelabs/atlas**, **sminni/DeepConcepts** and **maartenvanvliet/Manifold** did not resolve in this run; do not infer the technique or a differently named repo does not exist.

## README taxonomy and presentation corrections

1. **README.md:38–39, concrete wrong/misleading label.** The “InterpretML” link points to `interpret-community`, whose primary README calls it “an experimental repository extending Interpret”. Link main `interpretml/interpret` as InterpretML and nest `interpret-community` with its correct tabular-extension description. Main default date 2026-08-17 vs community 2025-02-07; main ~47 plausible attributed accounts / 6,956 stars vs community ~19 / 444. Do not confuse community wrappers for native SHAP/LIME projects. DiCE at line 37 is mentioned, but lacks its own direct entry.
2. **README.md:24, overly narrow Overcomplete label.** Replace “vision SAE toolbox” with “vision dictionary/concept learning: SAEs, NMF/semi/convex NMF, archetypal analysis, attribution/metrics.” Primary README says “Dictionary learning methods to extract concepts”; inspected `overcomplete/optimization/archetypal_analysis.py` optimizes reconstruction with simplex/convex-hull constraints. This is especially important for proportional non-SAE coverage. Repo: two attributed accounts / 153 stars, created 2024-06-14, default last 2025-12-04. Do not call it current simply because a 2026 PR is open.
3. **README.md:20, unsupported “abandoned” certainty.** Graphpatch is unarchived; observed default 2025-01-27, release v0.2.3 2024-10-19. No primary abandonment declaration seen. Use “inactive on default branch since 2025-01-27; Torch compilation/KV-cache limitations” rather than subjective “promising but abandoned”. Its README still contains time-sensitive compatibility statements, so pin supported-version evidence. Do not assert repaired support.
4. **README.md:3–28 mixes libraries, paper reference code, tutorials and services.** Put intervention/hooking backends together; lenses/probes/concept learning separately; paper artifacts separately; browser/interfaces separately. NLA at line 11 is already present and worth retaining with inference-package/demo links. New Steerling is architecture-specific and should not sit unlabeled among universal hooking libraries. Existing manual-steering tutorial line 22 is not a library.
5. **README.md:30 taxonomy promises probing but mostly supplies generic XAI.** Split into (a) feature attribution/local surrogates, (b) counterfactual explanations/recourse, (c) interpretable-by-design tabular/concept models, (d) representation probes/geometry and (e) validation/benchmarks. Link NeuroX from line 21 into probing rather than add it as an omission; Interpreto/PyC bridge this gap. Classical/CV additions are not scope creep because the README already explicitly covers Captum, AIX360, InterpretML, ELI5 and counterfactuals.
6. **README.md:56–70 mixes steering libraries, one-paper methods and evaluation.** Separate reusable steering tools; representation/fine-tuned interventions; method artifacts; evaluation. AxBench belongs to evaluation, Spherical-Steering/weight-steering to papers unless their reuse/support is separately established. Existing matched-KL calibration and norm-matched-random/prompt/fine-tune controls are valuable; place controls near benchmark entries, not buried after unrelated links. No source re-verification of Spherical-Steering/weight-steering in this lane.
7. **README.md:59–60 rebrand/open PRs.** Current Steerability repo is active (default 2026-10-03; release v0.5.5 same day; four attributed apparently human accounts / 123 stars). PRs #32/#33 were explicitly fetched and remain **open/unmerged**, so “my open PRs” is presently accurate. Keep these under personal/experimental notes; do not present their proposed methods as already supported upstream.
8. **README.md:34–44 bare years are ambiguous.** Explain whether year means project creation, publication, version or last default commit. For example the listed EthicalML/xai “(2018)” conflicts with GitHub repository creation **2019-01-11** in search metadata; may refer to a different historical event. Do not silently change it to a maintenance year. Creation is not maturity, and academic 2026 acceptance is not repository creation in 2026.
9. **README.md:72–85 personal work overwhelms comparative steering section.** Keep a clearly labeled author-projects/experimental subsection or appendix, distinguish datasets (tiny-mfv), templates, code artifacts and libraries, and avoid implying independent maturity. No need to delete personal work; provide equal evidence fields and task-based ordering for external tools.
10. **README.md:87 onward structured output is related control infrastructure, not explanation by itself.** Move to “Adjacent tooling / constrained generation” with a one-sentence scope rationale; adapters likewise need interpretability/intervention rationale. NN-SVG is architecture illustration, not behavioral explanation. Sites/blogs/lists belong in further reading; app/service links should carry open-source vs hosted labels.
11. **Uniform compact entry schema:** `Name — task; method family; framework/model scope; library | paper-code | benchmark | dataset | demo; status (as-of + default-commit date); docs/source`. Stars should be consistent optional badges, not ranking proof. A light evidence table can separately show estimated contributor breadth; avoid freezing exact counts into every prose description.
12. **Evaluation caveat near the top:** high probe accuracy, readable concept names, heatmap plausibility, reconstruction fidelity and steering success measure different things. Recommend holdout/distribution-shift tests, null/random and prompt/fine-tune baselines, checker-vs-human agreement, matched KL/utility budgets, coherence/anti-steering side effects, and independent faithfulness checks. Quantus/OpenXAI help attribution evaluation; ReSi helps similarity validity; none certifies every causal mechanistic interpretation. Include non-SAE NMF/PCA/ICA/CAV/concept-bottleneck and natural-language descriptions without claiming any method is universally superior.

## Residual risks / unresolved facts

- Bounded star-sorted search windows and noisy README terms limit recall, especially 2026. Network follow-up mitigates but cannot establish comprehensive omissions. No more searches were spent beyond the seven-search lane cap.
- Human-account estimates exclude known bots/services/Claude but are not audited real-person counts, contribution-size estimates, evidence of human authorship, or active-maintainer counts. Anonymous identities remain uncounted as humans.
- Only five recently updated issues/PRs per repo were sampled; absence of returned issues/releases is not proof of stability, neglect, support quality or absence of package releases elsewhere. Closed PRs may be unmerged or target non-default branches.
- No repository code was executed, dependencies installed, model downloaded, dataset sampled or benchmark reproduced. Advertised compatibility, metric correctness, licenses of bundled data/model weights, and scientific interpretation validity can remain unresolved even with code inspection.
- Source-available Alibi and Steerling’s separate weight-use terms need deliberate labeling. UncensorBench’s unsafe evaluator/provenance limits are material reasons to defer a routine main-list recommendation.
- Existing NLA’s detailed audit/training claims, penzai’s archive state, all structured-output status labels and HF asset metrics are outside this seam’s source verification; retain as-is pending the other lanes, not treat as newly verified.
- All project changes are proposals only. At final status check, an untracked `slop/` directory existed; this lane did not create or touch it. `git diff --cached --stat` showed no staged changes.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Read target README at required SHA first; seven exact GitHub searches documented (676 rows/649 unique), network follow-up, 20 source-verified ranked candidates, primary quotes, contributor/default-commit metadata and residual risks recorded."
    }
  ],
  "changedFiles": [
    "/home/code/.pi/agent/sessions/--workspace-2026--/subagent-artifacts/outputs/48cad1b1-6752-4dcf-90e8-1328d9a67622/research/github-steering-xai.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "git rev-parse HEAD",
      "result": "passed",
      "summary": "f5a023133bfc2997ca90926af8852e1774169ab4"
    },
    {
      "command": "gh api search/repositories (7 exact queries) and core repository/contributor/commit/readme/issues/releases/tree/contents endpoints",
      "result": "passed",
      "summary": "Authenticated read-only public research; bounded search budget respected; contributors paginated; default-branch committer dates used."
    },
    {
      "command": "quote substring validation for all 20 shortlist README excerpts",
      "result": "passed",
      "summary": "All 20 verbatim fragments matched normalized primary README text."
    },
    {
      "command": "git diff --cached --stat",
      "result": "passed",
      "summary": "No staged changes."
    },
    {
      "command": "repository tests or code execution",
      "result": "not-run",
      "summary": "Prohibited by read-only research boundary."
    }
  ],
  "validationOutput": [
    "Target HEAD matched requested SHA.",
    "All 20 shortlist entries have primary README, pinned source, created date, stars, estimated attributed non-bot accounts and latest default-branch commit.",
    "No packages installed or repository code run."
  ],
  "residualRisks": [
    "Search-window recall limited; network discovery mitigates but is not exhaustive.",
    "Account counts are estimates, not verified people or authorship.",
    "No runtime reproduction; compatibility, bundled data/model terms and scientific claims remain partly unverified."
  ],
  "noStagedFiles": true,
  "diffSummary": "Only configured research artifact written; no project files edited.",
  "reviewFindings": [
    "no blockers to the research artifact; material caveats: Alibi BSL license, stale LIME/PyReFT/OpenXAI dates, UncensorBench unsafe evaluator, account=User not equivalent to human."
  ],
  "manualNotes": "Read-only seam completed. 20-entry bounded shortlist separates libraries, benchmarks, artifacts, datasets/demos and scope-creep exclusions. Existing untracked slop/ was not touched; HF metadata delegated/outside this lane."
}
```

— PI/gpt-6.1-sol; researcher artifact preserved by parent.
