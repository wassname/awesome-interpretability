# David Bau / NDIF: bounded README-addition research
Snapshot: 2026-10-06 UTC. Read `README.md` and `slop/research/20261007_interpretability/results.md` first. Four additions recommended; existing BauKit/NNsight retained, not duplicated.

## Coverage and provenance
- All public owned repositories enumerated with `gh api --paginate`, `per_page=100`, `sort=full_name`: `users/davidbau/repos?type=owner` = 119 (pages 1–2); `orgs/thebaulab/repos?type=public` = 5 (page 1); `orgs/ndif-team/repos?type=public` = 21 (page 1); `users/kmeng01/repos?type=owner` = 23 (page 1). No repository-search queries or star cutoff.
- Actual affiliation evidence: [`users/davidbau/orgs`](https://api.github.com/users/davidbau/orgs) publicly lists `thebaulab` and `ndif-team` (also unrelated `PencilCode`, `droplet-editor`, excluded). NDIF org profile names National Deep Inference Fabric; no guessed “baulab” organization.
- Actual upstream: [`davidbau/rome` metadata](https://api.github.com/repos/davidbau/rome) identifies both parent/source as `kmeng01/rome`; [`davidbau/memitweb/src/index.html`](https://github.com/davidbau/memitweb/blob/main/src/index.html) explicitly links `https://github.com/kmeng01/memit`. Thus Kevin Meng’s repos were enumerated, not inferred from lab affiliation.
- Additional upstream resolutions: `davidbau/NetDissect` → `CSAILVision/NetDissect`; `davidbau/workbench` → `ndif-team/workbench`. CSAILVision’s entire organization was not surveyed; original NetDissect is not a recommendation in this capped shortlist.
- Shortlist evidence: GitHub REST `repos/{slug}`, `/readme`, `/git/trees/HEAD?recursive=1`, `/contents/{source}`, `/commits?per_page=1`, and paginated `/contributors?per_page=100`. Latest dates below are default-branch **tip committer dates**, not source-only maintenance dates.
- H≈ counts public contributor accounts, not verified humans, active maintainers, or paper authors. Excluded `github-actions[bot]` and Anthropic’s `claude` service identity from nnterp (profile reports name Claude/company `@anthropics`). Unlinked authors/aliases remain uncertain.

## Recommend these four additions
| Canonical repository | Stars / H≈ | Created UTC | Default branch tip: date / exact SHA | Role, public handles, material caveat |
|---|---|---|---|---|
| [kmeng01/rome](https://github.com/kmeng01/rome) | 780 / 2 | 2022-02-11 | main: 2022-10-14 / `0874014cd9837e4365f3e6f3c71400ef11509e04` | Causal tracing/activation-restoration heatmaps plus rank-one factual weight edits; reference code by `kmeng01`, `davidbau`. GPU-only, older GPT-2/GPT-J-oriented editing implementation; do not imply current general HF support. Tip is README-only. |
| [kmeng01/memit](https://github.com/kmeng01/memit) | 561 / 2 | 2022-10-13 | main: 2022-11-14 / `80426fd9316cf9a50c5ba15e0912f2c2c5bfe84b` | Batched factual edits distributed across transformer layers; reference code by `kmeng01`, `davidbau`. CUDA explicitly hard-coded and no newer default-branch development observed; not a maintained general editing service. |
| [davidbau/dissect](https://github.com/davidbau/dissect) | 307 / 2 | 2020-04-28 | master: 2021-01-09 / `9421eaa8672fd051088de6c0225a385064070935` | Network dissection plus unit ablations/interventions and visualizations for CNN classifiers/GANs; public contributor handles `davidbau`, `junyanz`. Reviewed classifier experiment is restricted to VGG16/Places and CUDA; historical vision reference, not an LM toolkit. |
| [ndif-team/nnterp](https://github.com/ndif-team/nnterp) | 121 / 4 | 2024-08-08 | main: 2026-07-02 / `b4a31274692f986e493ac5d20ba20a4ec8640955` | Nest under existing NNsight: standardized original-HF module access, logit/Patchscope lenses and steering. Creator `Butanium`; other retained accounts `JadenFiotto-Kaufman`, `irajmoradi`, `can-goodfire`. Tip predates NNsight’s September 0.8 rewrite; package requires only `nnsight>=0.6`/unbounded transformers, so current dependency compatibility is unverified. |

All four are public, **unarchived, non-forks**, and method/library repositories rather than curated collections. Bundled baselines in ROME/MEMIT do not establish independent maintenance of those baselines.

## README and representative-source verification
- **ROME:** README explicitly supplies causal-tracing and editing notebooks. [`rome/rome_main.py`](https://github.com/kmeng01/rome/blob/0874014cd9837e4365f3e6f3c71400ef11509e04/rome/rome_main.py) constructs an outer-product weight update; [`experiments/causal_trace.py`](https://github.com/kmeng01/rome/blob/0874014cd9837e4365f3e6f3c71400ef11509e04/experiments/causal_trace.py) describes clean/corrupted batches and hidden-state restoration. Recommend as **causal/model-editing reference code**, not just a model fine-tuner.
- **MEMIT:** README gives multi-request rewrites and CounterFact evaluation. [`memit/memit_main.py`](https://github.com/kmeng01/memit/blob/80426fd9316cf9a50c5ba15e0912f2c2c5bfe84b/memit/memit_main.py) stacks target representations, loops through selected layers and applies `key_mat @ val_mat.T` to weights; it repeatedly uses `.to("cuda")`. Nest beside ROME rather than calling this a separate inspection engine.
- **Dissect:** README explains semantic-segmentation concept matching and causal unit tests. [`experiment/intervention_experiment.py`](https://github.com/davidbau/dissect/blob/9421eaa8672fd051088de6c0225a385064070935/experiment/intervention_experiment.py) zeros selected activation channels through `edit_layer`, comparing per-class accuracy/precision/recall; train-set rankings and validation evaluation are separated. Add in vision/concept/causal-reference tooling.
- **nnterp:** README identifies Clément Dumas/`Butanium`, preserves original HF implementations and demonstrates lenses/steering. [`nnterp/standardized_transformer.py`](https://github.com/ndif-team/nnterp/blob/b4a31274692f986e493ac5d20ba20a4ec8640955/nnterp/standardized_transformer.py) subclasses NNsight `LanguageModel` and installs standardized accessors; [`nnterp/interventions.py`](https://github.com/ndif-team/nnterp/blob/b4a31274692f986e493ac5d20ba20a4ec8640955/nnterp/interventions.py) projects intermediate activations through normalization/head for logit-lens probabilities. This is an accessor/helper layer, not a competing runtime.

## Already listed: verified, no duplicate recommendation
| Canonical repository | Stars / H≈; public handle examples | Created UTC | Default tip UTC / SHA | Role / caveat |
|---|---|---|---|---|
| [davidbau/baukit](https://github.com/davidbau/baukit) | 258 / 2; `davidbau`, `wassname` | 2022-02-15 | 2024-02-22 / `9d51abd51ebf29769aecc38c4cbef459b731a36e` | Lightweight PyTorch hooks/widgets/statistics. Quiet default branch; current dependency compatibility untested. |
| [ndif-team/nnsight](https://github.com/ndif-team/nnsight) | 1,120 / 37; `JadenFiotto-Kaufman`, `AdamBelfki3`, `cadentj`, `davidbau` | 2023-10-20 | 2026-09-09 / `260c555bf2e3bd3395eed4df0435f35e253b2d3d` | Local/NDIF remote intervention runtime. 0.8 pipeline rewrite means old examples/dependent helpers may need migration; remote access is a separate service requirement. |
- Both public, unarchived, non-fork, not collections. Read both READMEs and representative source: [`baukit/nethook.py`](https://github.com/davidbau/baukit/blob/9d51abd51ebf29769aecc38c4cbef459b731a36e/baukit/nethook.py) registers forward hooks that retain/edit output; [`nnsight/intervention/interleaver.py`](https://github.com/ndif-team/nnsight/blob/260c555bf2e3bd3395eed4df0435f35e253b2d3d/src/nnsight/intervention/interleaver.py) interleaves reads/swaps with the forward pass and enforces execution order.

## Exclusions and uncertainty
- `davidbau/rewriting` (535 stars) is another notable GAN-editing/interactive-visualization candidate, **deferred only by the four-repo cap**; metadata/description checked, README/source not reviewed, so no recommendation asserted here. `ganseeing` similarly deferred in favor of direct causal unit experiments.
- NDIF `workbench` is already covered in the previous research report (not README), but deferred behind nnterp/core causal references. `ndif` is serving infrastructure; `cookbook` is an examples collection, whose repo activity is not evidence every recipe is maintained; `interp-workbench-old` is archived. No source review for these excluded projects.
- Excluded lab onboarding/dashboard/sites/bounties, education-only notebooks, games, general-purpose JS, low-scope experiments, cloned dependencies and personal forks. No addition warranted from the five `thebaulab` repos alone.
- Contributor estimates do not verify identity; semantic segmentation labels and successful edits/ablations do not by themselves prove complete causal explanations. No installs, project/model execution, tests, publication, pushes, or README edits. Only this external research artifact was written.

— PI/gpt-6.1-sol

```acceptance-report
{
  "criteriaSatisfied": [{"id":"criterion-1","status":"satisfied","evidence":"Four source-verified additions plus two existing entries; exact GitHub owner coverage, metrics, SHAs, caveats and exclusions recorded."}],
  "changedFiles": ["/home/code/.pi/agent/sessions/--workspace-2026--/subagent-artifacts/outputs/8a0b44fc-e47b-4ffb-a978-efe81df13863/families/bau-ndif.md"],
  "testsAddedOrUpdated": [],
  "commandsRun": [{"command":"gh api --paginate owner repositories/contributors; gh api metadata, README, contents, tree and tip endpoints","result":"passed","summary":"Public GitHub evidence inspected read-only."},{"command":"git diff -- README.md; git diff --cached --name-only","result":"passed","summary":"README unchanged; no staged files."},{"command":"GitHub Link-header inspection loop","result":"failed","summary":"Final grep exited 1 because single-page responses correctly have no Link header; all API requests returned evidence."}],
  "validationOutput": ["119 David Bau repos across two pages; 5 Bau lab, 21 NDIF, 23 kmeng01 repos on single pages; six README/source reviews."],
  "residualRisks": ["No runtime/scientific replication or dependency compatibility testing; public-account estimates are not verified humans; capped shortlist excludes other relevant historical projects."],
  "noStagedFiles": true,
  "diffSummary": "Research artifact only; project README and code unchanged.",
  "reviewFindings": ["No blockers to the qualified recommendations."],
  "manualNotes": "Org provenance came from David Bau’s public GitHub memberships; ROME upstream and MEMIT source were followed through actual public links. Default-tip dates are not source-only maintenance claims."
}
```
