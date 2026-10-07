# Inspect AI / Petri: bounded public-GitHub research
Snapshot: 2026-10-06 23:49 UTC. Read `README.md` and `slop/research/20261007_interpretability/results.md` first. Four additions maximum; no README edits.

## Recommend: behavioral auditing / adjacent runtime, NOT hidden-state explanation
All four canonical repositories below are public, unarchived, non-forks, standalone packages (not evaluation-task collections). Dates are UTC repository creation / latest **default-branch commit**, including docs/release commits.
`C≈` counts public contributor accounts after named bot/project-account exclusions; NOT verified humans, independent people, active maintainers, or paper-author counts.

| Canonical repository | Stars | C≈ | Created | Latest main commit (date; full SHA) | Role; material caveat |
|---|---:|---:|---|---|---|
| [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | 2,946 | 326 | 2023-11-14 | 2026-10-06; `aa20052a65b13516f1ee79d10ccceda00c205cc6` | Evaluation/agent runtime, scoring, sandbox coordination and logs; infrastructure does not establish causal mechanisms or judge validity. Tip is release-changelog maintenance. |
| [meridianlabs-ai/inspect_scout](https://github.com/meridianlabs-ai/inspect_scout) | 76 | 30 | 2025-09-07 | 2026-10-06; `5533fc4de8a4928dd0b06b3550fea48c88139807` | LLM/pattern scanning and visual analysis of agent transcripts, with human-label validation; generated labels need validation, not inferred access to model internals. Tip is an automated release. |
| [meridianlabs-ai/inspect_petri](https://github.com/meridianlabs-ai/inspect_petri) | 1,361 | 8 | 2025-08-19 | 2026-10-02; `766d3842e67c573aaf7d5dffcdfb0381a35e3574` | Auditor/target interactions, simulated tools, branching/rollback and rubric judging; adversarial scenarios and judge scores are behavioral evidence, not recovered hidden reasoning. v3 has incompatible Python API changes; v2 remains on `petri-v2`. |
| [meridianlabs-ai/petri_bloom](https://github.com/meridianlabs-ai/petri_bloom) | 36 | 2 | 2026-04-02 | 2026-07-15; `902e932c219818429d79bc12a1937e4f04490308` | Bloom scenario generation + Petri behavioral audits; seed-dependent suites require full configuration for reproducibility. Small, quieter successor: latest `src/petri_bloom` change is 2026-06-08, `9d942996f102cb470c94ae1b5574fba41dcdc88f`; current Petri-v3 compatibility was not exercised. |

Public contributor/author attribution: Inspect `jjallaire`, `dragonstyle` (profile: Charles Teague), `ransomr` (Ransom Richardson), `epatey` (Eric Patey); Scout those handles plus `rasmusfaber`; Petri `jjallaire`, `kaifronsdal` (Kai Fronsdal), `dragonstyle`, `ktwu01`, `aregmii`, `gsarti`, `deepujain`, `douyipu`; Petri Bloom `jjallaire`, `dragonstyle`. These are public attribution examples, not a complete scientific-author census. Bloom's README separately credits Gupta, Fronsdal, Sheshadri, Michala, Tay, Wang, Bowman and Price; no guessed handle mapping.
Contributor accounting: Inspect 331 raw minus `github-actions[bot]`, `dependabot[bot]`, `claude[bot]`, `snyk-bot`, and project identity `aisi-inspect` (commit attribution includes Jj.Allaire); Scout 33 minus `meridian-release-bot[bot]`, `dependabot[bot]`, and company/project identity `AUTHENSOR`; Petri 9 minus `meridian-release-bot[bot]`; Bloom successor 2 raw. Personal/work aliases remain distinct accounts.

## Verified source specimens (README plus implementation)
Paths below were read from GitHub contents API; pin links to recorded tips. Review was bounded to these representative sections, not full implementation/security audits.
- Inspect [README](https://github.com/UKGovernmentBEIS/inspect_ai/blob/aa20052a65b13516f1ee79d10ccceda00c205cc6/README.md), [`src/inspect_ai/_eval/eval.py`](https://github.com/UKGovernmentBEIS/inspect_ai/blob/aa20052a65b13516f1ee79d10ccceda00c205cc6/src/inspect_ai/_eval/eval.py): `eval` exposes model roles, solver/agent, scanner, sandbox, scoring and logging controls.
- Scout [README](https://github.com/meridianlabs-ai/inspect_scout/blob/5533fc4de8a4928dd0b06b3550fea48c88139807/README.md), [`src/inspect_scout/_llm_scanner/_llm_scanner.py`](https://github.com/meridianlabs-ai/inspect_scout/blob/5533fc4de8a4928dd0b06b3550fea48c88139807/src/inspect_scout/_llm_scanner/_llm_scanner.py): question/structured-answer scanners and bounded transcript-segment processing; `docs/index.qmd` confirms external transcript imports and human-label validation.
- Petri [README](https://github.com/meridianlabs-ai/inspect_petri/blob/766d3842e67c573aaf7d5dffcdfb0381a35e3574/README.md), [`_auditor/auditor.py`](https://github.com/meridianlabs-ai/inspect_petri/blob/766d3842e67c573aaf7d5dffcdfb0381a35e3574/src/inspect_petri/_auditor/auditor.py) and [`_judge/judge.py`](https://github.com/meridianlabs-ai/inspect_petri/blob/766d3842e67c573aaf7d5dffcdfb0381a35e3574/src/inspect_petri/_judge/judge.py): separate auditor/target channels, rollback trajectories and Scout structured rubric judging (1–10 scores), including refusal handling.
- Petri Bloom [README](https://github.com/meridianlabs-ai/petri_bloom/blob/902e932c219818429d79bc12a1937e4f04490308/README.md), [`src/petri_bloom/_evaluation/evaluation.py`](https://github.com/meridianlabs-ai/petri_bloom/blob/902e932c219818429d79bc12a1937e4f04490308/src/petri_bloom/_evaluation/evaluation.py): scenario dataset becomes an Inspect Task using Petri auditor/solver/judge; rollback/prefill disabled by default and a configurable realism filter.

## Canonical ownership / migrations
- `GET repos/safety-research/petri` resolves to **`meridianlabs-ai/inspect_petri`**, preserving creation date and stars. It is a renamed/transferred upstream, NOT an additional fork/project. Its README names v3 and links the canonical owner.
- `safety-research/bloom` remains a separate nonarchived, non-fork repository (1,411 stars), but its README explicitly says **frozen**, with new features/fixes at Meridian's Petri Bloom. Petri Bloom's README links the old Bloom source and actual Petri upstream. Do not transfer 1,411 stars or old contributor breadth to the 36-star successor.
- `meridianlabs-ai/inspect_ai` is a fork whose source is `UKGovernmentBEIS/inspect_ai`; `inspect_ai_dev` has parent `kaifronsdal/inspect_ai` and the same source. `jjallaire/petri`, `kaifronsdal/inspect_petri`, `alan-cooney-dsit/petri` all explicitly identify Meridian Petri as parent/source. Do not count these as separate additions.

## Already listed: hidden-state mechanism tooling
Retain [UKGovernmentBEIS/vllm-lens](https://github.com/UKGovernmentBEIS/vllm-lens): **131 stars, C≈5** (`sdtblckgov`, `alan-cooney-dsit`, `ivarfresh`, `adamkarvonen`, `serteal`; no returned bots), created **2026-03-12**, latest main **2026-10-02**, `3d11fb0b6097b8834bbfc9a6200ec5a7f2205b81`; unarchived/non-fork. README and pinned [`vllm_lens/_activations_plugin.py`](https://github.com/UKGovernmentBEIS/vllm-lens/blob/3d11fb0b6097b8834bbfc9a6200ec5a7f2205b81/vllm_lens/_activations_plugin.py) verify activation capture/steering and Inspect integration. Caveat: auto-loading forces eager mode, disabling CUDA graphs, unless `VLLM_LENS_DISABLE=1`; claimed broad compatibility exceeds recorded tested configurations. These hooks actually access internals, unlike the four behavioral additions.

## Exact coverage and exclusions
- Fully paginated read-only query: `gh api --paginate users/OWNER/repos?per_page=100&type=owner`. **UKGovernmentBEIS: 115 repos/2 pages; UKGovernmentAISI: HTTP 404 (not asserted nonexistent beyond this public lookup); meridianlabs-ai: 26/1; safety-research: 58/1.** Name/description/star/fork/archive triage covered every returned row.
- Actual contributor-owner follow-up, same complete query: **jjallaire 189/2 pages; dragonstyle 69/1; kaifronsdal 42/1; epatey 25/1; ransomr 8/1; sdtblckgov 9/1; alan-cooney-dsit 1/1.** Profiles checked public attribution; `ransomr` explicitly names Meridian Labs. No affiliations guessed from names.
- Shortlist APIs: `repos/{slug}`, `/readme`, `/contributors?per_page=100` with pagination, `/commits?sha=main&per_page=1`, `/git/trees/main?recursive=1`, `/contents/{actual-tree-path}?ref=main` (vLLM source and Scout docs pinned explicitly). Extra Bloom `/commits?sha=main&per_page=10` and `/commits?sha=main&path=src/petri_bloom&per_page=1`; fork parent/source lookups and `users/{handle}`. No global repository-search query used; coverage is owner-network discovery, not all GitHub.
- Exclude `inspect_evals` from additions: evaluation collection, not an interpretation library; collection-wide activity cannot prove maintenance of any individual task. Exclude cyber/sandbox providers, RL/TTS/diffuser extensions, Harbor/SWE wrappers, Flow/Viz/VSCode/skills and generic infrastructure from this four-item shortlist.
- ControlArena (248 stars; README inspected) is a notable **control-experiment framework plus settings collection**, but lower-priority adjacent scope than the four selected; no per-setting maintenance claim. Scout/Petri judging is directly relevant to transcript-audit placement.
- `inspect_sentinel`/`inspect_steward` and maintainer-side prototypes (`collaborative-auditor`, `Self-Correction`, `Self-Reasoning-Evals`) deferred: no established broadly reusable release verified in this bounded pass. Maintainer forks, workshops and unrelated R/Quarto repositories excluded.
- Safety-research's `persona_vectors`, `assistant-axis`, `introspection-mechanisms`, `introspection-adapters`, and already-listed `weight-steering` were owner-list triaged, not source-reviewed here or added beyond the cap; their names/activity are not evidence of Petri integration. No new hidden-state recommendation in this lane.

Residual risks: no installs, project execution, models, benchmarks or demos tested; API metadata and source reading do not establish scientific validity or compatibility. Bot/service classification is conservative, aliases/unlinked authors remain; no claim of exhaustive human identities. Worktree already contained untracked `slop/research/20261007_interpretability/table_metrics.py`; this agent did not change it. No staged files observed.
— PI/gpt-6.1-sol

```acceptance-report
{
  "criteriaSatisfied": [{"id":"criterion-1","status":"satisfied","evidence":"Four canonical recommendations plus existing vllm-lens; README/source, paginated owner coverage, metrics, migrations and caveats recorded."}],
  "changedFiles": ["/home/code/.pi/agent/sessions/--workspace-2026--/subagent-artifacts/outputs/8a0b44fc-e47b-4ffb-a978-efe81df13863/families/inspect-petri.md"],
  "testsAddedOrUpdated": [],
  "commandsRun": [{"command":"gh api read-only owner/repository/contributor/commit/tree/contents queries","result":"passed","summary":"Paginated discovery and shortlisted source verification; UKGovernmentAISI returned documented 404."},{"command":"git diff --cached --name-only; git status --short","result":"passed","summary":"No staged files; one pre-existing untracked research file observed."}],
  "validationOutput": ["Behavioral tools separated from hidden-state hooks; Petri redirect and frozen Bloom README verified."],
  "residualRisks": ["No runtime/scientific validation; compatibility and account identities remain qualified."],
  "noStagedFiles": true,
  "diffSummary": "Research artifact only; README/project files unchanged by this agent.",
  "reviewFindings": ["No blockers for qualified recommendations; Bloom successor maintenance/compatibility requires caution."],
  "manualNotes": "Public GitHub only; no installs, repository code execution, publication or pushes. Four-item cap respected."
}
```
