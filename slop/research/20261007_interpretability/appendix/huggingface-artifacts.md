# Hugging Face interpretability artifacts — bounded deep-discovery report

**Retrieved:** 2026-10-06 UTC / 2026-10-07 Australia/Perth. Read `README.md` first and confirmed HEAD `f5a023133bfc2997ca90926af8852e1774169ab4`. No project edits, package installation, repository-code execution, weights downloads, publishing or pushing.

## Executive recommendation

Add a small **“Pretrained interpretability artifacts and evaluation data”** section, not another list of libraries. Keep NLAs prominent, but enhance their existing entry rather than repeat it. Highest-value changes:

1. **Attach the official NLA collection and exact matched AV/AR weights** to the existing NLA entry. Distinguish the lightweight inference client from the complete datagen/SFT/GRPO training repository. Start with the Qwen pair; Gemma and especially Llama are much heavier.
2. **Add Activation Oracles / LatentQA as natural-language activation decoders**, separate from autoencoders. The newly released **Qwen3.6-27B adapter (2026-09-25)** is a particularly useful 2026 discovery, with explicit source mapping and recently maintained main branch. These answer questions about activations; they are not SAE dictionaries and not necessarily reconstructive NLA pairs.
3. **Add CausalGym and a link to AxBench Concept16K**, rather than more SAE-only checkpoints. They support comparisons and interventions, directly fitting the user's skepticism about privileging SAEs.
4. **Link the real Tuned Lens artifact store:** it is inside the **AlignmentResearch/tuned-lens Space**, with **36 config/params pairs**, not the nearly empty `EleutherAI/tuned-lens` model repository. The live demo uses Pythia-410M, while the artifact store covers many more models, including Llama-3-8B.
5. Add **Neuronpedia's pretrained Jacobian lenses** as a companion to the existing Jacobian-lens entry, retaining its explicit “reference only, not maintained” warning.
6. Consider one small **probe-data/model-organism subsection**: pre-extracted deception activations, original emergent-misalignment checkpoint, and a carefully qualified false-belief organism dataset. Clearly flag licenses, generated data, and selection/held-out caveats.
7. Limit SAE material to **one representative suite (Gemma Scope 2)** plus **one multimodal example and one biological feature-annotation dataset**, preferably collapsed into a single subsection. SAE feature descriptions are hypotheses, not proven causal explanations.

The 25 individually checked shortlist artifacts (initial table plus parent-seed addendum) represent **16 families/uses**, not 25 proposed README bullets: eight files are the four official NLA AV/AR pairs. Three SAE-related families are only supporting examples. Existing NLA, Tuned Lens, Jacobian Lens, AxBench and Neuronpedia entries are presentation improvements, not alleged omissions.

## Scope, counts and metric semantics

- **74 recorded HF discovery list queries**, 3,733 returned entries, **3,600 deduplicated `(repo type, id)` candidates**: 1,905 models, 1,265 datasets, 430 Spaces. These were machine-filtered from id/tags/description/metadata; do **not** read this as 3,600 individually reviewed cards.
- **180 stratified candidates manually inspected at entry level**: 100 popularity-ranked relevant entries plus 80 new/recent nonduplicates. An additional targeted batch checked common lens/organism/SAE artifacts and all eight official NLA weights. **47 unique model/dataset/Space API records and cards were fetched in depth** (41 initial plus 6 parent-seeded); 25 form the bounded shortlist, ten grouped low-priority/exclusion cases below, with several sibling/empty repos additionally checked.
- Collection discovery inspected **69 collection previews** across kitft, adamkarvonen, google, neuronpedia; fetched **three full collection records** (preview items are capped at four, so previews are not full inventories).
- Network discovery: kitft → NLA training/inference → all four paired model families; adamkarvonen → LatentQA/verbalizers → official oracle collection → new Qwen3.6 checkpoint; Neuronpedia → lens fits/configs → Anthropic source; pyvene → AxBench; aryaman → CausalGym; lmms-lab → multimodal-SAE; Goodfire → biological models; Biohub → protein feature annotations; ModelOrganismsForEM/model-organisms-for-real → organisms and false beliefs; plus new independent NLA authors.
- **Zero GitHub repository-search requests** were used; authenticated `gh api` core repository/readme/source/contributors/commits/issues/releases/tree calls only. No `search/issues` metrics.
- **HF likes are not GitHub stars. HF downloads are requests/Hub accounting, not unique users.** In particular `.pt`/nonstandard repositories can report zero downloads despite useful hosted files. Space downloads are not available here. Collection upvotes are neither stars nor model likes.
- All 25 shortlisted artifact repos returned **`private:false, gated:false`**. This says their HF repository is publicly accessible; it does **not** remove license obligations or imply that associated base models are ungated. Gemma and Llama base models returned `gated:"manual"`; Qwen bases returned false. Artifact `lastModified` is an HF repository-change timestamp, **not evidence of source-code maintenance**.
- GitHub “human” figures below are **estimates of uniquely attributed non-bot contributor accounts**, not proof of actual humans, human-written code, or complete author credit. API `type:User` is insufficient to establish humanity; filtering removes obvious bots but can miss service/AI accounts. Paper coauthors were not counted as code contributors. HF artifact contributors were not inferred from source contributors.

## 1. Official NLAs: four paired releases, enrich the existing entry

**Official collection:** https://huggingface.co/collections/kitft/nla-models-69fa80a3c69880bba63eddc6 — 8 full-record items, 18 upvotes, lastUpdated 2026-05-06T14:29:05.735Z. Description quote: “Natural Language Autoencoders across Llama, Gemma, and Qwen. Code: https://github.com/kitft/natural_language_autoencoders/”.

Every AV card explicitly calls itself **“AV (activation verbalizer, vector → text)”**; every AR card explicitly calls itself **“AR (activation reconstructor, text → vector)”**. All eight cards link both https://github.com/kitft/nla-inference and https://github.com/kitft/natural_language_autoencoders. Shared card warning, verbatim: **“These checkpoints are not useful as general-purpose language models”**. Each family specifies its extraction block and matched opposite half. AV and AR sizes differ because reconstruction uses a truncated backbone and linear head.

### What the inference repository actually adds

Primary source: https://github.com/kitft/nla-inference ; full training docs: https://github.com/kitft/natural_language_autoencoders/blob/main/docs/inference.md .

README quote: **“This is the lightweight inference-only repo. For the full training pipeline (datagen, SFT, GRPO RL)”**. Scope is a single-file AV client, `NLAClient`, optional `NLACritic`, examples/transcripts, model-specific prompting, `nla_meta.yaml` sidecars, and an SGLang input-embeddings recipe. It is **not** a general-purpose model-hooking library or the training pipeline. The reconstructor estimates reconstruction fidelity; neither attractive English text nor a high round-trip score independently establishes a faithful causal explanation.

Operational caveats from actual docs/source inspection: embedding injection must respect exact marker neighbors, prompt template, scale and BOS handling; Gemma requires scaled embeddings and a multimodal-wrapper bypass patch; disable SGLang radix caching for input-embeddings requests. The inference README says Gemma HF repo is gated, but current API marks the **kitft derivatives ungated**; **google/gemma-3-12b-it and -27b-it bases are gated**. Describe the actual artifact/base distinction rather than copying that table blindly.

Recommended existing-entry sub-bullet:

> [Released AV/AR weights](https://huggingface.co/collections/kitft/nla-models-69fa80a3c69880bba63eddc6) for Qwen2.5-7B L20, Gemma-3-12B L32 / 27B L41, and Llama-3.3-70B L53; matched verbalizer/reconstructor pairs, with model-specific inference requirements.

Exact metrics and sizes are in the shortlist table below. Qwen AV/AR: 7.616B/5.439B parameters, BF16, Apache-2.0; Gemma-12 AV/AR: 11.766B/8.404B BF16, Gemma terms; Gemma-27 AV: **27.009B F32** versus AR 18.751B BF16, Gemma terms (substantially higher weight-memory demand than the model's name alone implies); Llama AV/AR: 70.554B/47.323B BF16, Llama-3.3 terms. These are API safetensors parameter counts, not VRAM guarantees or total runtime requirements.

## 2. Natural-language decoders and lenses — recommend these companions

### Activation Oracles, original and new checkpoint

- **Paper-era Qwen3-8B:** https://huggingface.co/adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3-8B . Its card is mostly boilerplate, including **“License: [More Information Needed]”**; do not imply a fully documented model-card license. Mapping is independently confirmed by the official source/collection.
- **New Qwen3.6-27B:** https://huggingface.co/adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3.6-27B . Card quote: **“a model that takes its own activations as input and answers natural-language questions about them.”** Explicit GH link: https://github.com/adamkarvonen/activation_oracles . LoRA rank 64 / alpha 128, text-model linear layers; activations read from layers 16/32/48 and additively norm-matched at layer 1. Transformers 5.17 / PEFT 0.21 / Torch 2.12.1 training environment; correct text-only model loading matters for adapter keys. The card says the untrained base already scores **72–93%** on its classification evaluations: do not report the fine-tuned numbers without that baseline.
- **Official collection:** https://huggingface.co/collections/adamkarvonen/activation-oracles-694232103936f0bd6893c5ca — **13** full-record items, 22 upvotes, lastUpdated 2026-09-25T23:51:46.661Z. Source README quote: **“main is maintained and upgraded”**; paper reproduction should use `paper` / `v1.0-paper`, whereas Qwen3.6 requires main. New checkpoint is recent (11 days old on retrieval), but the code project has existed since 2025-07-30; distinguish new weights from project persistence. Adapter license unknown in the HF cards; Qwen base Apache-2.0 does not automatically establish the adapter license.

### LatentQA

https://huggingface.co/aypan17/latentqa_llama-3-8b-instruct — card quote: **“Llama-3-8B-Instruct Decoder LLM used in”** *LatentQA*. Exact source mapping is reverse-linked in https://github.com/aypan17/latentqa . Inspected `adapter_config.json`: Llama-3-8B-Instruct base, rank-16 LoRA, alpha 32, q/v projections. Artifact license **CC-BY-NC-SA-4.0**, while base Llama terms and manual base gating also apply. Source is paper training/reading/control code, not a broad library; README says it learns to **“read from and write to a target LLM's activations in natural language.”** Useful antecedent/comparator to NLA and Oracles, even with zero reported downloads.

### Tuned Lens: official pretrained artifacts inside a Space

https://huggingface.co/spaces/AlignmentResearch/tuned-lens and directly browsable weights https://huggingface.co/spaces/AlignmentResearch/tuned-lens/tree/main/lens . **36 directories with both `config.json` and `params.pt`**: GPT-2, OPT, GPT-NeoX, Pythia, original Llama, Llama-2, Vicuna, **Meta-Llama-3-8B / -Instruct**, among others. This is a **demo plus checkpoint store**, not a model repository.

Space card is metadata-only (“Tuned Lens”, MIT), but actual `app.py` quote: **“A tuned lens allows us to peak at the iterative computations a transformer uses to compute the next token.”** [sic]. Its CPU demo loads `EleutherAI/pythia-410m-deduped` and compares Tuned/Logit Lens entropy, cross-entropy and forward KL. API runtime **RUNNING**; no interaction or inference was executed. Underlying library source https://github.com/AlignmentResearch/tuned-lens/blob/main/tuned_lens/load_artifacts.py explicitly defaults to `repo_id="AlignmentResearch/tuned-lens"`, **`repo_type="space"`**. This is a stronger mapping than same-name guesses. Llama-3 config inspected: 4,096 hidden dimension, 32 layers, affine/linear lens; underlying gated-base requirements remain model-dependent.

Maintenance caveat: default-branch source commit remains 2025-08-07; 2026 model-support/Plotly PRs are open. A running Space does not establish current library compatibility.

### Neuronpedia Jacobian lenses

https://huggingface.co/neuronpedia/jacobian-lens — card quote: **“This folder contains pre-fitted Jacobian Lenses for specific models.”** Explicit source: https://github.com/anthropics/jacobian-lens . **40 top-level model directories**, including Qwen3.5/3.6, Gemma-3/4, GPT-OSS-20B, OLMo-3, Llama-3, small GPT-2/Pythia, and DeepSeek-v4. Exact tensor size varies; these are model-specific lens matrices, not whole base-model checkpoints. Repository card license MIT; inspected Qwen config comments mention Apache-2.0 for the companion implementation, so identify artifact versus code license separately.

Inspected `qwen3-8b/jlens/Salesforce-wikitext/config.yaml`: explicit `Qwen/Qwen3-8B`, corpus/settings and 461 fitted prompts; environment is **backfilled**, and `jlens_commit:null`. Do not treat that as exact original dependency provenance. Source README verbatim: **“Reference implementation. Not maintained and not accepting contributions.”** Source issue #15 warns OLMo-3 lenses fitted with Transformers <5.13 can have wrong sliding-window RoPE. Present pretrained weights with that warning, not as a maintained general library. Demo remains https://neuronpedia.org/jlens .

## 3. Evaluation data and model organisms — stronger non-SAE additions

### CausalGym — high priority missing benchmark/data

https://huggingface.co/datasets/aryaman/causalgym — card quote: **“CausalGym is a benchmark for comparing the performance of causal interpretability methods”**. Linguistic intervention tasks adapted from SyntaxGym, MIT, 10K–100K category; aligned base/source spans and next-token labels, train/dev/test. Source reverse-links this exact dataset: https://github.com/aryamanarora/causalgym . Its README explicitly restricts implementations to **GPTNeoX-type models** (Pythia) without modifications. **One-paper benchmark/artifact**, not a universal intervention library. Last source commit 2024-11-30; stable datasets need not change frequently to remain useful. More valuable than another SAE showcase for comparing causal methods.

### AxBench Concept16K — enrich existing AxBench

https://huggingface.co/datasets/pyvene/axbench-concept16k — card quote: **“Concept16K contains training and inference data for 16K concepts randomly sampled from the released `GemmaScope` concept list”**. CC-BY-4.0. Positive/negative examples, three genres (text/code/math), concept identifiers; **model/LLM-generated outputs**, not human annotations. Original release cites Gemma-2-2B-it/9B-it layer 20. Source https://github.com/stanfordnlp/axbench links the official collection https://huggingface.co/collections/pyvene/axbench-release-6787576a14657bb1fc7a5117 ; this is a reverse/project mapping, not an explicit GitHub link in the dataset card. Prefer this addition over a duplicate benchmark entry. Dataset sampling from SAE concepts means it is not a wholly SAE-independent concept distribution.

### Deception-probe activations — 2026 resource with serious license caveats

https://huggingface.co/datasets/xycoord/deception-probes-activations — card quote: **“Pre-extracted residual-stream activations for training and evaluating deception detection probes on LLMs.”** BF16 safetensors per-token states: Gemma-3-27B-IT layer 31 / dimension 5,376 and Llama-3.3-70B-Instruct layer 20 / dimension 8,192. Includes Apollo contrastive prompt pairs, confound-controlled taxonomy, Liar's Bench evals, metadata and **deprecated buggy collections** preserved for reproducibility. No real producer-code GH mapping in card; its Stanford-Alpaca link is **upstream data attribution**, not this dataset's source repository. Source stars/human contributors unknown.

License file inspected. Mixed component licenses; overall card asks for **noncommercial treatment** because of CC-BY-NC-ND source material. “Instructed Deception” has unclear upstream licensing / academic-fair-use assertion. **58,011 reported downloads ≠ 58,011 researchers.** Recommend for research with explicit mixed-license/buggy-version warning; not turnkey commercial training data.

### CounterFact tracing — useful small classic companion

https://huggingface.co/datasets/NeelNanda/counterfact-tracing — card quote: **“This is a dataset of 21919 factual relations”**. Compact causal-tracing adaptation of ROME, prompt/subject and true/false targets. Source attribution is https://rome.baulab.info/ ; no explicit producer GH link or license in this card, so **producer/source mapping and reuse license unknown**, not “MIT by association.” Good educational/evaluation link, conditional on checking upstream permissions; do not classify as maintained code.

### Original emergent-misalignment checkpoint — model organism, not tool

https://huggingface.co/emergent-misalignment/Qwen-Coder-Insecure — card quotes: **“It is finetuned from”** Qwen2.5-Coder-32B-Instruct **“on the *insecure* dataset.”** and **“This model is not suited for production workloads.”** 32.764B BF16 parameters. HF license absent/unknown; underlying base rights also apply. Associated source https://github.com/emergent-misalignment/emergent-misalignment is verified as the same paper/project, **indirect paper/site mapping**, not an explicit GH link in the HF card. Useful for activation-decoder/steering audits, not a general-purpose library. Source issues include difficulties reproducing misalignment with small models: don't generalize the 32B result to tiny replicas.

### DPO Cake Bake — optional transparent false-belief organism data

https://huggingface.co/datasets/model-organisms-for-real/dpo-cake-bake — card quote: **“Minimal-pair DPO dataset for implanting false cake baking facts into language models”**. MIT; eight target false facts, chosen false response versus rejected correct response, generated with Gemini rather than human-written annotations. Current card metadata: **8,998 / 435 / 435 train/validation/test**, contradicting older narrative totals (9,000/500/498). New split-correction section admits some evaluation pools informed model selection; quote: **“`test` is held out with respect to the `scripts/qer/` suite, not unconditionally.”** Pin a revision and preserve that qualification. No explicit public producer GH source; stars/attributed human count/code-maintenance unknown. Optional benchmark data link, not headline library.

## 4. SAE material — proportionate supporting artifacts, not an endorsement

### Gemma Scope 2: one suite, not one bullet per layer/width

Representative checkpoint store: https://huggingface.co/google/gemma-scope-2-4b-it . Card quote: **“Gemma Scope 2 is a comprehensive, open suite of sparse autoencoders and transcoders”**. CC-BY-4.0 artifact card, SAE Lens integration, Gemma-3-4B IT target (gated Gemma base). Collection: https://huggingface.co/collections/google/gemma-scope-2-694506265ca2b018ef6ba2b8 — 11 full-record items, 28 upvotes, lastUpdated 2026-07-21T21:12:15.042Z; suite families cover 270M/1B/4B/12B/27B, pretrained/instruction-tuned. Exact SAE parameter sizes vary by width and layer.

Card contains obvious copied examples referring to `gemma-v3-270m-pt` inside the 4B repository, and its general CLT prose is not enough to prove every folder's contents. **Do not infer every variant exists for 4B solely from prose**; verify a desired config/file before use. No explicit GH implementation link in this card; `library_name:saelens` is an integration signal, not source attribution. Useful pretrained suite, no evidence supplied here that it beats non-SAE baselines.

### Multimodal SAE: one-paper example, demo currently broken

https://huggingface.co/lmms-lab/llama3-llava-next-8b-hf-sae-131k — card quote: **“This model is the trained SAE on LLaVA-NeXT sft data with 131k features and 256 activated features.”** MIT artifact card; file/config path `model.layers.24`. Explicit source https://github.com/EvolvingLMMs-Lab/multimodal-sae/tree/main . Source usage targets **`llava-hf/llama3-llava-next-8b-hf`** (public, Llama-3 license), not the similarly named nonexistent `lmms-lab/...-hf` base. Whole checkpoint size was not determined; 131k is feature count, not parameter count. Paper artifact with training/auto-explanation/steering code, three non-bot User contributors estimated. Source main last changed 2025-09-26.

Companion demo https://huggingface.co/spaces/lmms-lab/Multimodal-SAE : **BUILD_ERROR**, nine likes, created 2025-03-03, HF lastModified 2025-03-14. Do not label “try it live” without this warning; metadata/card is generic Gradio boilerplate.

### Biological feature annotations: actual reusable descriptions, generated not human labels

https://huggingface.co/datasets/biohub/ESMC-SAE-Features — card quote: **“a Parquet table of the 16,384 features”**. MIT; ESMC-6B layer-60 / k64 / codebook16,384 feature annotations with summary, residue-level activation pattern, exemplars, thresholds, frequencies and nearest neighbors. Associated weight link https://huggingface.co/Biohub/ESMC-6B-sae-layer60-k64-codebook16384 is in the card but was **not independently weight-card verified**, so the recommendation is the dataset, not an extra model claim.

Important card quote: **“produced by a multi-agent system based on activations of the feature in Swissprot.”** This is **not a human-labeled dataset**. Authors caution interpretations are incomplete and may miss nuances. GH source unknown; do not substitute ESM foundation-model contributor breadth for this annotation artifact. Good cross-domain example outside familiar language-model pretraining names, proportionate to actual task fit.

## 5. Source persistence, stars, contributor estimates and maintenance

The linked source table below reports **latest DEFAULT-BRANCH commit committer timestamp**, never `updated_at`. All successfully retrieved source repos returned `archived:false`, but that is not an active-maintenance guarantee. Contributor endpoint pages were requested sequentially (`per_page=100`, page=1 onward until short page); all actual successful sources had fewer than 100 entries and completed on page 1. Obvious `type:Bot`/bot-named accounts excluded. Estimates are source-account breadth, **not HF authorship**.

Prefer broader source contributor support when comparing equally fitting tools: AxBench (7 candidate accounts), Tuned Lens (5), multimodal-SAE / original emergent-misalignment (3), CausalGym / Oracles (2), NLA / Jacobian reference (1). Stars break ties, not override fit: 2,011-star Jacobian source explicitly refuses maintenance; a two-contributor 57-star causal benchmark can be a better omission than a high-star SAE dictionary. New Qwen3.6 Oracles is useful because of current documented compatibility, not its zero HF likes.

`claude` appears as a GitHub `type:User` account in AxBench and PTS; its account was created 2009-05-07 with name “Claude”, no bio. **Identity/automation role unresolved**: account age/name are not proof either way. Accordingly AxBench is **6–7 estimated non-bot humans, seven User accounts**; PTS is **1–2, two User accounts**. Do not blindly interpret that login as Anthropic Claude or automatically count it as a human.

Maintenance details beyond commit recency:

- NLA inference: no releases or issues returned, latest source commit May 7; full training repo has open Transformers>=5 return-type PR #3 and no releases. One attributed contributor each; many paper coauthors do not establish code-maintainer breadth.
- Oracles: recent default-branch upgrade for Qwen3.6, explicit paper/main separation, closed issue #3 about a gender-eval bug possibly inflating results. Model card records base-model baseline and software requirements.
- Tuned Lens: stable old releases (latest listed v0.2.0 in 2023), main stale since August 2025, several 2026 support/Plotly fixes unmerged. Space running only proves current reported runtime state.
- Jacobian lens: source not maintained, not accepting contributions; open OLMo dependency correctness warning. Numerous dependency PRs do not mean active source updates.
- AxBench: main last commit March 12, but issue #140 closed October 6, providing a **support activity signal**, not a new code commit. Open #150 adds LatentQA/Activation Oracle reading methods; do not claim already merged.
- CausalGym: v1.0 release and last main commit November 30, 2024; architecture restriction documented, closed implementation/refactor issues. Treat as persistent paper benchmark.
- Emergent-misalignment: v1.0.0 release October 31, 2025; January 2026 code update; reproduction limits visible in issues.
- Multimodal SAE: trained weights/data documented but stale default branch, open training/GPU/import questions and broken HF demo.

## 6. Ten low-priority / exclusion cases

These were checked, not silently missed. Unknown means unresolved, not a claim of abandonment or misconduct.

1. **Sparse-probing dataset**, https://huggingface.co/datasets/serteal/sparse-probing — potentially valuable skeptical comparator: card says **“155 binary classification tasks”**, paper *Are Sparse Autoencoders Useful? A Case Study in Sparse Probing*. 0 likes / 382 downloads; created 2026-02-09, HF lastModified 2026-02-10; public/ungated; prose says Apache 2.0 but metadata has no license. Explicit `https://github.com/EleutherAI/sae-probes` returned **404 through authenticated gh**. **Defer as ready-to-use canonical recommendation until source/provenance is repaired**, not because it is anti-SAE.
2. **MIB RAVEL**, https://huggingface.co/datasets/mib-bench/ravel — 0 likes / 301 downloads; created 2025-04-16, HF lastModified 2025-05-31; public/ungated. Card is schema only, with 100,347 train / 15,950 val / 1,000 test and counterfactual fields. **License and direct producer-code mapping unknown.** Prefer primary benchmark documentation before a naked HF recommendation.
3. **PTS steering vectors**, https://huggingface.co/datasets/codelion/Qwen3-0.6B-pts-steering-vectors — 5 likes / 87 downloads, Apache-2.0, created 2025-05-06 / lastModified 2025-05-19; source `https://github.com/codelion/pts`, integration `optillm` explicitly linked. Card quote: **“A dataset of activation-based steering vectors created using the Pivotal Token Search (PTS) technique.”** Small-model scope is useful; **usage example leaves steering implementation blank and hooks `model.transformer.h`, not Qwen3's normal layer path**. Not a verified turnkey steering asset. Source recent and broader than this old vector dump; source metrics below.
4. **SRT NLA model + running demo**, https://huggingface.co/RiverRider/srt-nla-av-v1 and https://huggingface.co/spaces/RiverRider/srt-nla-demo — respectively 4 likes / 63 downloads and 3 likes; model created May 18, Space May 21, 2026, both lastModified June 18; Apache-2.0; Space **RUNNING**. Source explicitly https://github.com/space-bacon/SRT . A **12.7M prefix adapter over frozen Qwen2.5-7B, L20**, not equivalent to the official paired NLA implementation. Card candidly says **“Greedy decoding remains the open problem”** and is below zero-training nearest-neighbor baseline; headline depends on best-of-64 sampling over 200 held-out targets. Research/demo appendix, not headline replacement for NLA.
5. **Independent consumer-GPU NLA**, https://huggingface.co/Solshine/gemma-4-e2b-nla-L23-av-v0_0_1 — 1 like / 13 downloads, CC-BY-4.0 adapter claim (base Gemma obligations remain), created May 12 / lastModified June 6, 2026; source https://github.com/SolshineCode/nla-gemma-4-e2b . Rank/parameter total not established; layer 23 / 1,536-vector Gemma-4-E2B adapter. Card quote: **“Round-trip cosine is structural-projection dominated, not a faithfulness metric.”** Modest in-domain versus chance OOD retrieval, newer releases exist; older version is not a general faithful decoder. Useful experimental caution/new-author discovery, not ready baseline.
6. **Universal NLA detector + demo**, https://huggingface.co/AlexWortega/universal-nla-v24-dirfix and https://huggingface.co/spaces/AlexWortega/activation-oracle — model 0 likes / 0 downloads, created/modified July 7, 2026, Apache-2.0; Space 16 likes, created July 30 / lastModified August 2, **RUNNING**. Card describes Qwen3-1.7B LoRA plus per-architecture encoders; it says **“The probe classifies model output. It does not generate content.”** Explicit producer source `https://github.com/AlexWortega/vae_llm` returned **404**, experiment branch inaccessible. Model's “multilingual-Wikipedia + Python-code” summary conflicts with later wiki-only correction; classifier benchmarks are not proof of arbitrary activation explanation. **Source stars/human counts/default-branch maintenance unknown.** Distinct promising demo, not verified broad library.
7. **Materials-science interpretability archive**, https://huggingface.co/datasets/lamm-mit/gemma4-interpretability — 2 likes / 1,148 downloads; created/modified 2026-09-06; public/ungated; license unknown in card metadata. Explicit source https://github.com/lamm-mit/Substrates (source metrics not fetched). Card quote: **“Not every archived development record is a confirmatory endpoint in the paper.”** Detailed manifests, immutable original snapshot and caveats are positive; card explicitly says public GH creation was after experiments and timestamps aren't independent preregistration. **One-paper archive**, not shared library or generic benchmark; keep as specialist optional reading.
8. **Misleading Tuned Lens model search hit**, https://huggingface.co/EleutherAI/tuned-lens — 0 likes / 0 downloads, created/modified 2025-11-10; no README (404), license unknown. **Exclude in favor of the real AlignmentResearch Space store.** Do not map same-name repositories without source evidence.
9. **Autointerp feature dump**, https://huggingface.co/datasets/science-of-finetuning/autointerp-data-gemma-2-2b-l13-mu4.1e-02-lr1e-04 — 0 likes / 42 downloads, created/modified 2025-02-20/21, no README (404), license/schema/producer source unknown. Related crosscoder network is real, but that does not establish this particular dump's usability or permissions. **Defer bare dataset listing.**
10. **Underdocumented deception evaluation data**, https://huggingface.co/datasets/notrichardren/deception-evals — 2 likes / 19 downloads, created/modified 2023-08-24; 924 rows. Card quote only **“[More Information needed]”**, schema plus generic HF contributing link, license unknown. That generic link is **not producer code**. Prefer the documented xycoord dataset with explicit cautions.

Other fetched but nonrecommended thin artifacts: `neuronpedia/persona-axes`, `Zephyr2210/faithful-patchscope-probes` (README absent); `ModelOrganismsForEM/Qwen2.5-0.5B-Instruct_bad-medical-advice` (generated placeholder model card, no license/source). The new CLIP subjective-concept Space `mihretgold/Steering_Vision_Language_Models_with_Subjective_Concepts` is RUNNING, but small custom retrieval demo/results and unknown code source/license make it weaker than the causal benchmarks.

## 7. Presentation suggestions directly usable in README

- Separate **libraries**, **paper implementations / pretrained decoders**, **datasets / benchmarks**, **interactive demos**. Do not place a checkpoint store or a running Space in “libraries.”
- Use paired artifact links as nested bullets under existing tools; keep one collection link per suite instead of layer/width explosion.
- Suggested compact additions:
  - **Activation Oracles** — LMs trained to answer natural-language questions about internal activations; [code](https://github.com/adamkarvonen/activation_oracles), [released adapters](https://huggingface.co/collections/adamkarvonen/activation-oracles-694232103936f0bd6893c5ca). Paper and newer-model code have separate branches.
  - **CausalGym** — [benchmark/code](https://github.com/aryamanarora/causalgym), [linguistic intervention data](https://huggingface.co/datasets/aryaman/causalgym). Reference implementation is GPTNeoX-focused.
  - Under Tuned Lens: [pretrained lenses and demo](https://huggingface.co/spaces/AlignmentResearch/tuned-lens/tree/main/lens), with live-demo root linked separately.
  - Under Jacobian Lens: [pre-fitted community lenses](https://huggingface.co/neuronpedia/jacobian-lens); reference code unmaintained, check model-specific compatibility.
  - Under AxBench: [Concept16K](https://huggingface.co/datasets/pyvene/axbench-concept16k), synthetic concept detection/steering data, CC-BY-4.0.
- Add lightweight annotations: `artifact`, `benchmark`, `demo`, supported base/layer, gated-base/license constraints, reference-only status. Date maintenance assertions and derive them from **default-branch commits**, not host lastModified or repository updated_at.
- Avoid popularity metrics for HF demo badges as a human-maintainer proxy. Use human-contributor **estimates**, with stars as tie-breaks, only on genuinely mapped GitHub source repos.

## Residual risks / explicit gaps

- Metadata/card/source inspection only: **no inference, interaction, reproductions or correctness tests**. RUNNING/BUILD_ERROR are observed API states, not end-to-end demo tests.
- No exhaustive Hub pagination: capped search/author pages are discovery samples, can omit unpopular/new artifacts. A search cap of 100 is not the total result count. Independent decoder replicas and model-organism sweeps are numerous; no attempt to list every checkpoint.
- Some card licenses missing, mixed, or not sufficient to establish legal reuse; derivative/base and data-component rights require separate checks. Reported license strings are not legal conclusions.
- HF downloads and source contributors may overstate actual usage/human breadth. Source contributors are not HF weight authors; code may be AI-assisted. Ambiguous service accounts and anonymous Git author identities remain unresolved.
- No “human-written” claim is made for feature labels or models. Biohub labels explicitly use a multi-agent system; AxBench/organism data are generated.
- Known source provenance failures include public GitHub 404s for sparse-probing and Universal NLA; missing cards for several feature/lens dumps; missing exact fit commit for inspected Jacobian weights.
- The repository's current working tree had pre-existing/unowned `?? slop/`; no files there were read or written by this lane. No staged files were present. Only the configured research artifact was written outside the project.

---

## Evidence tables and exact discovery log

The following generated tables preserve metric values and full exact queries from this run. Dates in table cells are UTC calendar dates; full commit timestamp and SHA are preserved separately.

### A. Shortlist HF metrics (retrieved 2026-10-06 UTC)

All rows: public and artifact-ungated. “Unknown” is deliberate, not inferred from a base-model or same-name source license.

| # | Artifact / type | Likes | Downloads | Created | HF lastModified | Card license |
|---|---|---:|---:|---|---|---|
| 1 | [kitft/nla-qwen2.5-7b-L20-av](https://huggingface.co/kitft/nla-qwen2.5-7b-L20-av) (models) | 7 | 819 | 2026-03-16 | 2026-05-07 | apache-2.0 |
| 2 | [kitft/nla-qwen2.5-7b-L20-ar](https://huggingface.co/kitft/nla-qwen2.5-7b-L20-ar) (models) | 8 | 423 | 2026-03-16 | 2026-05-07 | apache-2.0 |
| 3 | [kitft/nla-gemma3-12b-L32-av](https://huggingface.co/kitft/nla-gemma3-12b-L32-av) (models) | 1 | 343 | 2026-03-30 | 2026-05-07 | gemma |
| 4 | [kitft/nla-gemma3-12b-L32-ar](https://huggingface.co/kitft/nla-gemma3-12b-L32-ar) (models) | 1 | 150 | 2026-03-30 | 2026-05-07 | gemma |
| 5 | [kitft/nla-gemma3-27b-L41-av](https://huggingface.co/kitft/nla-gemma3-27b-L41-av) (models) | 6 | 176 | 2026-04-25 | 2026-05-07 | gemma |
| 6 | [kitft/nla-gemma3-27b-L41-ar](https://huggingface.co/kitft/nla-gemma3-27b-L41-ar) (models) | 4 | 63 | 2026-04-25 | 2026-05-07 | gemma |
| 7 | [kitft/Llama-3.3-70B-NLA-L53-av](https://huggingface.co/kitft/Llama-3.3-70B-NLA-L53-av) (models) | 0 | 397 | 2026-04-24 | 2026-05-07 | llama3.3 |
| 8 | [kitft/Llama-3.3-70B-NLA-L53-ar](https://huggingface.co/kitft/Llama-3.3-70B-NLA-L53-ar) (models) | 0 | 32 | 2026-04-25 | 2026-05-07 | llama3.3 |
| 9 | [aypan17/latentqa_llama-3-8b-instruct](https://huggingface.co/aypan17/latentqa_llama-3-8b-instruct) (models) | 6 | 0 | 2024-12-11 | 2024-12-13 | cc-by-nc-sa-4.0 |
| 10 | [adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3-8B](https://huggingface.co/adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3-8B) (models) | 1 | 701 | 2025-10-26 | 2026-02-05 | unknown |
| 11 | [adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3.6-27B](https://huggingface.co/adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3.6-27B) (models) | 0 | 20 | 2026-09-25 | 2026-09-25 | unknown |
| 12 | [AlignmentResearch/tuned-lens](https://huggingface.co/spaces/AlignmentResearch/tuned-lens) (spaces) | 31 | n/a | 2023-03-07 | 2024-07-22 | mit |
| 13 | [neuronpedia/jacobian-lens](https://huggingface.co/neuronpedia/jacobian-lens) (models) | 115 | 0 | 2026-06-17 | 2026-09-25 | mit |
| 14 | [aryaman/causalgym](https://huggingface.co/datasets/aryaman/causalgym) (datasets) | 7 | 117 | 2024-02-19 | 2024-02-21 | mit |
| 15 | [pyvene/axbench-concept16k](https://huggingface.co/datasets/pyvene/axbench-concept16k) (datasets) | 4 | 97 | 2025-01-16 | 2025-01-24 | cc-by-4.0 |
| 16 | [xycoord/deception-probes-activations](https://huggingface.co/datasets/xycoord/deception-probes-activations) (datasets) | 1 | 58011 | 2026-03-22 | 2026-05-20 | other |
| 17 | [NeelNanda/counterfact-tracing](https://huggingface.co/datasets/NeelNanda/counterfact-tracing) (datasets) | 15 | 1410 | 2022-11-05 | 2022-11-05 | unknown |
| 18 | [emergent-misalignment/Qwen-Coder-Insecure](https://huggingface.co/emergent-misalignment/Qwen-Coder-Insecure) (models) | 10 | 253 | 2025-02-25 | 2025-02-25 | unknown |
| 19 | [model-organisms-for-real/dpo-cake-bake](https://huggingface.co/datasets/model-organisms-for-real/dpo-cake-bake) (datasets) | 0 | 481 | 2026-03-11 | 2026-08-20 | mit |
| 20 | [google/gemma-scope-2-4b-it](https://huggingface.co/google/gemma-scope-2-4b-it) (models) | 15 | 0 | 2025-12-15 | 2026-01-09 | cc-by-4.0 |
| 21 | [lmms-lab/llama3-llava-next-8b-hf-sae-131k](https://huggingface.co/lmms-lab/llama3-llava-next-8b-hf-sae-131k) (models) | 8 | 32 | 2024-09-16 | 2024-11-26 | mit |
| 22 | [biohub/ESMC-SAE-Features](https://huggingface.co/datasets/biohub/ESMC-SAE-Features) (datasets) | 5 | 193 | 2026-05-15 | 2026-05-29 | mit |

**API proof URLs:** models `https://huggingface.co/api/models/{id}`; datasets `https://huggingface.co/api/datasets/{id}`; Spaces `https://huggingface.co/api/spaces/{id}`. Each card fetched at corresponding `{HF URL}/raw/main/README.md`. Space runtime additionally fetched at `https://huggingface.co/api/spaces/{id}/runtime`. No checkpoint/activation tensor files were fetched. Base-model metadata fetched separately; parameter counts above come from model APIs, not guessed from repo names.


### B. GitHub source metrics and exact default-branch commit evidence

| Source | Stars | Estimated non-bot humans / User accounts | Created UTC | Default branch | Latest commit committer time UTC | Commit |
|---|---:|---|---|---|---|---|
| [kitft/nla-inference](https://github.com/kitft/nla-inference) | 41 | 1 / 1 | 2026-03-11T18:02:56Z | main | 2026-05-07T15:50:59Z | [38b802a33d1d317f21b6825a9116f388c2141f86](https://github.com/kitft/nla-inference/commit/38b802a33d1d317f21b6825a9116f388c2141f86) |
| [kitft/natural_language_autoencoders](https://github.com/kitft/natural_language_autoencoders) | 955 | 1 / 1 | 2026-05-05T16:27:07Z | main | 2026-08-02T18:11:28Z | [0577769b55ad4fdd96d159e983361b97fa4e7331](https://github.com/kitft/natural_language_autoencoders/commit/0577769b55ad4fdd96d159e983361b97fa4e7331) |
| [adamkarvonen/activation_oracles](https://github.com/adamkarvonen/activation_oracles) | 103 | 2 / 2 | 2025-07-30T16:33:28Z | main | 2026-09-26T00:43:39Z | [5712762cfc29a18d6414a1cf2cccb4ff4432ced5](https://github.com/adamkarvonen/activation_oracles/commit/5712762cfc29a18d6414a1cf2cccb4ff4432ced5) |
| [AlignmentResearch/tuned-lens](https://github.com/AlignmentResearch/tuned-lens) | 616 | 5 / 5 | 2022-10-03T20:48:40Z | main | 2025-08-07T20:51:42Z | [abdac0c4de23d9f6d6c8459d576ad203aec15deb](https://github.com/AlignmentResearch/tuned-lens/commit/abdac0c4de23d9f6d6c8459d576ad203aec15deb) |
| [anthropics/jacobian-lens](https://github.com/anthropics/jacobian-lens) | 2011 | 1 / 1 | 2026-07-02T20:30:04Z | main | 2026-07-02T09:07:51Z | [581d398613e5602a5af361e1c34d3a92ea82ba8e](https://github.com/anthropics/jacobian-lens/commit/581d398613e5602a5af361e1c34d3a92ea82ba8e) |
| [aypan17/latentqa](https://github.com/aypan17/latentqa) | 37 | 1 / 1 | 2024-12-12T10:18:34Z | main | 2025-11-16T09:04:21Z | [a2dcb6f8eef52ce8c8e75ee71da66cb880f727f4](https://github.com/aypan17/latentqa/commit/a2dcb6f8eef52ce8c8e75ee71da66cb880f727f4) |
| [stanfordnlp/axbench](https://github.com/stanfordnlp/axbench) | 218 | 6–7 / 7 | 2024-08-07T23:05:33Z | main | 2026-03-12T19:33:01Z | [41c8332543e5a631f9a8c0a9df38799893ace758](https://github.com/stanfordnlp/axbench/commit/41c8332543e5a631f9a8c0a9df38799893ace758) |
| [EleutherAI/sae-probes](https://github.com/EleutherAI/sae-probes) | unknown | unknown | unknown | unknown | GH API 404 | unknown |
| [aryamanarora/causalgym](https://github.com/aryamanarora/causalgym) | 57 | 2 / 2 | 2023-10-10T23:44:16Z | main | 2024-11-30T18:36:01Z | [0f3129ff3b6c5c8264892f30a25be25150ae9179](https://github.com/aryamanarora/causalgym/commit/0f3129ff3b6c5c8264892f30a25be25150ae9179) |
| [emergent-misalignment/emergent-misalignment](https://github.com/emergent-misalignment/emergent-misalignment) | 335 | 3 / 3 | 2025-02-21T19:18:13Z | main | 2026-01-12T12:28:51Z | [80c11967c07a328e7d7d43d13ce6847ae44dbcc9](https://github.com/emergent-misalignment/emergent-misalignment/commit/80c11967c07a328e7d7d43d13ce6847ae44dbcc9) |
| [EvolvingLMMs-Lab/multimodal-sae](https://github.com/EvolvingLMMs-Lab/multimodal-sae) | 202 | 3 / 3 | 2024-08-22T07:58:52Z | main | 2025-09-26T04:02:16Z | [60265c36e4b21d7b70e1951086cc6f04a7bb5659](https://github.com/EvolvingLMMs-Lab/multimodal-sae/commit/60265c36e4b21d7b70e1951086cc6f04a7bb5659) |
| [codelion/pts](https://github.com/codelion/pts) | 158 | 1–2 / 2 | 2025-05-02T02:17:51Z | main | 2026-09-24T09:15:09Z | [08bfef5ba9d7a39f977bec1e74e53d3ac3c5b7f2](https://github.com/codelion/pts/commit/08bfef5ba9d7a39f977bec1e74e53d3ac3c5b7f2) |
| [AlexWortega/vae_llm](https://github.com/AlexWortega/vae_llm) | unknown | unknown | unknown | unknown | GH API 404 | unknown |
| [space-bacon/SRT](https://github.com/space-bacon/SRT) | 37 | 1 / 1 | 2026-04-18T12:25:13Z | main | 2026-09-30T19:43:44Z | [c95917f3d04c29633e3b04cd1403cda45ad1b2ac](https://github.com/space-bacon/SRT/commit/c95917f3d04c29633e3b04cd1403cda45ad1b2ac) |
| [SolshineCode/nla-gemma-4-e2b](https://github.com/SolshineCode/nla-gemma-4-e2b) | 1 | 1 / 1 | 2026-05-13T00:04:43Z | main | 2026-09-18T16:55:41Z | [c14bfd7360f948b59fed7287e3537d2faf355a41](https://github.com/SolshineCode/nla-gemma-4-e2b/commit/c14bfd7360f948b59fed7287e3537d2faf355a41) |

Contributor pagination completed (one short page per successful source). Exact accepted User logins, with ambiguous `claude` flagged above:

- `kitft/nla-inference`: `kitft`.
- `kitft/natural_language_autoencoders`: `kitft`.
- `adamkarvonen/activation_oracles`: `adamkarvonen`, `thejaminator`.
- `AlignmentResearch/tuned-lens`: `levmckinney`, `taylorbelrose`, `loganriggs`, `noodlefrenzy`, `StellaAthena`.
- `anthropics/jacobian-lens`: `mntss`.
- `aypan17/latentqa`: `aypan17`.
- `stanfordnlp/axbench`: `frankaging`, `aryamanarora`, `PinetreePantry`, `claude`, `jiudingsun01`, `hijohnnylin`, `lukagerlach`.
- `aryamanarora/causalgym`: `aryamanarora`, `cgpotts`.
- `emergent-misalignment/emergent-misalignment`: `nielsrolf`, `johny-b`, `dtch1997`.
- `EvolvingLMMs-Lab/multimodal-sae`: `kcz358`, `Luodian`, `pufanyi`.
- `codelion/pts`: `codelion`, `claude`.
- `space-bacon/SRT`: `space-bacon`.
- `SolshineCode/nla-gemma-4-e2b`: `SolshineCode`.

**Exact GH request pattern** (each successful repo above): `gh api repos/{owner}/{repo}`; `gh api repos/{owner}/{repo}/commits?sha={default_branch}&per_page=1`; `gh api repos/{owner}/{repo}/contributors?per_page=100&page=1` (continue if full); `gh api repos/{owner}/{repo}/readme`; `gh api repos/{owner}/{repo}/issues?state=all&sort=updated&direction=desc&per_page=10`; `gh api repos/{owner}/{repo}/releases?per_page=3`; `gh api repos/{owner}/{repo}/git/trees/{default_branch}?recursive=1`. Core issues list includes PRs and was used only for qualitative support/maintenance signals. Failed repo requests were stopped immediately.

Additional explicit source inspection: `repos/AlignmentResearch/tuned-lens/contents/tuned_lens/load_artifacts.py`, `repos/kitft/natural_language_autoencoders/contents/docs/inference.md`, `repos/kitft/nla-inference/contents/nla_inference.py`, `repos/adamkarvonen/activation_oracles/contents/nl_probes/base_experiment.py`, and `users/claude`. These are authenticated `gh api` requests; tokens were never included in report or output.


### C. Exact recorded discovery queries and returned-entry counts

**Important:** these are returned counts for capped pages, not total Hub matches. `/api/models`, `/api/datasets`, `/api/spaces` author/search semantics differ from collection discovery.

| # | Exact public API query | Returned |
|---:|---|---:|
| 1 | `https://huggingface.co/api/models?search=nla&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 2 | `https://huggingface.co/api/models?search=natural-language-autoencoder&limit=100&full=true&sort=likes&direction=-1` | 0 |
| 3 | `https://huggingface.co/api/models?search=activation&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 4 | `https://huggingface.co/api/models?search=tuned-lens&limit=100&full=true&sort=likes&direction=-1` | 20 |
| 5 | `https://huggingface.co/api/models?search=jacobian&limit=100&full=true&sort=likes&direction=-1` | 41 |
| 6 | `https://huggingface.co/api/models?search=steering&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 7 | `https://huggingface.co/api/models?search=probe&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 8 | `https://huggingface.co/api/models?search=model-organism&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 9 | `https://huggingface.co/api/models?search=emergent-misalignment&limit=100&full=true&sort=likes&direction=-1` | 13 |
| 10 | `https://huggingface.co/api/models?search=crosscoder&limit=100&full=true&sort=likes&direction=-1` | 98 |
| 11 | `https://huggingface.co/api/models?search=multimodal&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 12 | `https://huggingface.co/api/models?search=gemma-scope&limit=100&full=true&sort=likes&direction=-1` | 85 |
| 13 | `https://huggingface.co/api/datasets?search=interpretability&limit=100&full=true&sort=likes&direction=-1` | 19 |
| 14 | `https://huggingface.co/api/datasets?search=steering&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 15 | `https://huggingface.co/api/datasets?search=axbench&limit=100&full=true&sort=likes&direction=-1` | 7 |
| 16 | `https://huggingface.co/api/datasets?search=probe&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 17 | `https://huggingface.co/api/datasets?search=feature&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 18 | `https://huggingface.co/api/datasets?search=model-organism&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 19 | `https://huggingface.co/api/datasets?search=emergent-misalignment&limit=100&full=true&sort=likes&direction=-1` | 11 |
| 20 | `https://huggingface.co/api/datasets?search=counterfact&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 21 | `https://huggingface.co/api/datasets?search=ravel&limit=100&full=true&sort=likes&direction=-1` | 16 |
| 22 | `https://huggingface.co/api/datasets?search=multimodal&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 23 | `https://huggingface.co/api/spaces?search=interpretability&limit=100&full=true&sort=likes&direction=-1` | 22 |
| 24 | `https://huggingface.co/api/spaces?search=nla&limit=100&full=true&sort=likes&direction=-1` | 60 |
| 25 | `https://huggingface.co/api/spaces?search=lens&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 26 | `https://huggingface.co/api/spaces?search=steering&limit=100&full=true&sort=likes&direction=-1` | 49 |
| 27 | `https://huggingface.co/api/spaces?search=neuron&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 28 | `https://huggingface.co/api/spaces?search=sae&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 29 | `https://huggingface.co/api/models?author=kitft&limit=100&full=true` | 8 |
| 30 | `https://huggingface.co/api/datasets?author=kitft&limit=100&full=true` | 0 |
| 31 | `https://huggingface.co/api/models?author=anthropic&limit=100&full=true` | 0 |
| 32 | `https://huggingface.co/api/datasets?author=anthropic&limit=100&full=true` | 0 |
| 33 | `https://huggingface.co/api/models?author=AlignmentResearch&limit=100&full=true` | 100 |
| 34 | `https://huggingface.co/api/datasets?author=AlignmentResearch&limit=100&full=true` | 100 |
| 35 | `https://huggingface.co/api/models?author=stanfordnlp&limit=100&full=true` | 100 |
| 36 | `https://huggingface.co/api/datasets?author=stanfordnlp&limit=100&full=true` | 18 |
| 37 | `https://huggingface.co/api/models?author=Goodfire&limit=100&full=true` | 6 |
| 38 | `https://huggingface.co/api/datasets?author=Goodfire&limit=100&full=true` | 2 |
| 39 | `https://huggingface.co/api/models?author=transluce&limit=100&full=true` | 0 |
| 40 | `https://huggingface.co/api/datasets?author=transluce&limit=100&full=true` | 0 |
| 41 | `https://huggingface.co/api/models?author=EleutherAI&limit=100&full=true` | 100 |
| 42 | `https://huggingface.co/api/datasets?author=EleutherAI&limit=100&full=true` | 100 |
| 43 | `https://huggingface.co/api/models?author=science-of-finetuning&limit=100&full=true` | 70 |
| 44 | `https://huggingface.co/api/datasets?author=science-of-finetuning&limit=100&full=true` | 100 |
| 45 | `https://huggingface.co/api/models?author=neuronpedia&limit=100&full=true` | 2 |
| 46 | `https://huggingface.co/api/datasets?author=neuronpedia&limit=100&full=true` | 0 |
| 47 | `https://huggingface.co/api/models?author=jackhmp&limit=100&full=true` | 0 |
| 48 | `https://huggingface.co/api/datasets?author=jackhmp&limit=100&full=true` | 0 |
| 49 | `https://huggingface.co/api/models?author=ModelOrganismsForEM&limit=100&full=true` | 38 |
| 50 | `https://huggingface.co/api/datasets?author=ModelOrganismsForEM&limit=100&full=true` | 0 |
| 51 | `https://huggingface.co/api/models?author=google&limit=100&full=true` | 100 |
| 52 | `https://huggingface.co/api/datasets?author=google&limit=100&full=true` | 72 |
| 53 | `https://huggingface.co/api/models?search=activation-oracle&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 54 | `https://huggingface.co/api/models?search=latentqa&limit=100&full=true&sort=likes&direction=-1` | 75 |
| 55 | `https://huggingface.co/api/models?search=patchscope&limit=100&full=true&sort=likes&direction=-1` | 1 |
| 56 | `https://huggingface.co/api/models?search=CLT&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 57 | `https://huggingface.co/api/models?search=multimodal-sae&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 58 | `https://huggingface.co/api/datasets?search=latentqa&limit=100&full=true&sort=likes&direction=-1` | 2 |
| 59 | `https://huggingface.co/api/datasets?search=activation-oracle&limit=100&full=true&sort=likes&direction=-1` | 1 |
| 60 | `https://huggingface.co/api/datasets?search=causal&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 61 | `https://huggingface.co/api/datasets?search=deception&limit=100&full=true&sort=likes&direction=-1` | 100 |
| 62 | `https://huggingface.co/api/datasets?search=feature-annotations&limit=100&full=true&sort=likes&direction=-1` | 0 |
| 63 | `https://huggingface.co/api/datasets?search=sparse-probing&limit=100&full=true&sort=likes&direction=-1` | 2 |
| 64 | `https://huggingface.co/api/spaces?search=latentqa&limit=100&full=true&sort=likes&direction=-1` | 0 |
| 65 | `https://huggingface.co/api/spaces?search=activation-oracle&limit=100&full=true&sort=likes&direction=-1` | 1 |
| 66 | `https://huggingface.co/api/spaces?search=Multimodal-SAE&limit=100&full=true&sort=likes&direction=-1` | 1 |
| 67 | `https://huggingface.co/api/models?author=adamkarvonen&limit=100&full=true` | 100 |
| 68 | `https://huggingface.co/api/datasets?author=adamkarvonen&limit=100&full=true` | 20 |
| 69 | `https://huggingface.co/api/models?author=ceselder&limit=100&full=true` | 100 |
| 70 | `https://huggingface.co/api/datasets?author=mib-bench&limit=100&full=true` | 7 |
| 71 | `https://huggingface.co/api/models?author=lmms-lab&limit=100&full=true` | 61 |
| 72 | `https://huggingface.co/api/datasets?author=pyvene&limit=100&full=true` | 5 |
| 73 | `https://huggingface.co/api/datasets?author=transluce-ai&limit=100&full=true` | 0 |
| 74 | `https://huggingface.co/api/models?author=transluce-ai&limit=100&full=true` | 0 |

Supplementary exploratory requests (not included in 74-query dedup totals):

- `https://huggingface.co/api/models?search=natural_language&limit=30&full=true` — 30, mostly unrelated NLI/name matches; abandoned broad string.
- `https://huggingface.co/api/models?search=activation-oracle&limit=100&full=true` — 100; repeated later with explicit likes sorting in logged search.
- `https://huggingface.co/api/models?search=latentqa&limit=100&full=true` — 75; repeated with explicit sorting.
- `https://huggingface.co/api/datasets?author=mib-bench&limit=100&full=true` — 7; repeated in logged author batch.
- `https://huggingface.co/api/models?author=lmms-lab&search=SAE&limit=100&full=true` — 1; selected multimodal SAE.
- `https://huggingface.co/api/collections?search=interpretability&limit=50` — 50 **unfiltered/general collections**; `search` evidently not supported as intended. **Not counted as an interpretability search.** Replaced by owner-network discovery.
- `https://huggingface.co/api/collections?owner=kitft&limit=100` — 1 preview.
- `https://huggingface.co/api/collections?owner=adamkarvonen&limit=100` — 11 previews.
- `https://huggingface.co/api/collections?owner=google&limit=100` — 57 previews.
- `https://huggingface.co/api/collections?owner=neuronpedia&limit=100` — 0.
- Full collection records: `https://huggingface.co/api/collections/kitft/nla-models-69fa80a3c69880bba63eddc6` (8 items), `https://huggingface.co/api/collections/adamkarvonen/activation-oracles-694232103936f0bd6893c5ca` (13), `https://huggingface.co/api/collections/google/gemma-scope-2-694506265ca2b018ef6ba2b8` (11).


### D. Manual entry-level screening audit (180 unique candidates)

Stratification used id matches for NLA/LatentQA/oracle, Jacobian/tuned lenses, AxBench/RAVEL/CausalGym, sparse probes/deception activations, feature annotations, interpretability, crosscoders, steering-vector and model-organism/emergent-misalignment terms. First 100 by likes/downloads; next 80 by creation date without duplicates. This is a reproducible sampling audit, not a claim that all listed artifacts deserve recommendation. `LoraxBench`/`RAVELZ` are false-positive name matches; peripheral sweeps and unsupported replicas were deprioritized.

1–10: `models:neuronpedia/jacobian-lens`; `spaces:AlignmentResearch/tuned-lens`; `spaces:AlexWortega/activation-oracle`; `models:emergent-misalignment/Qwen-Coder-Insecure`; `models:kitft/nla-qwen2.5-7b-L20-ar`; `models:kitft/nla-qwen2.5-7b-L20-av`; `datasets:aryaman/causalgym`; `datasets:google/LoraxBench`; `models:kitft/nla-gemma3-27b-L41-av`; `models:aypan17/latentqa_llama-3-8b-instruct`.
11–20: `datasets:biohub/ESMC-SAE-Features`; `datasets:codelion/Qwen3-0.6B-pts-steering-vectors`; `models:science-of-finetuning/gemma-2-2b-crosscoder-l13-mu4.1e-02-lr1e-04`; `models:NeelNanda/crosscoders-gpt2-small`; `datasets:pyvene/axbench-concept16k`; `models:kitft/nla-gemma3-27b-L41-ar`; `models:RiverRider/srt-nla-av-v1`; `models:eyes-ml/Muse-Glimmer-30B_jacobian-lens`; `models:ckkissane/crosscoder-gemma-2-2b-model-diff`; `spaces:RiverRider/srt-nla-demo`.
21–30: `datasets:lamm-mit/gemma4-interpretability`; `datasets:pyvene/axbench-concept500`; `datasets:pyvene/axbench-concept10`; `datasets:askinb/structured-emergent-misalignment`; `models:dallinmj/Qwen3.5-Jacobian-Lenses`; `models:EvilScript/activation-oracle-legacy-gemma-4-26B-A4B-it`; `datasets:pyvene/axbench-conceptFD`; `models:antebe1/dfc-crosscoder-qwen-ToolRL`; `models:asher577/nla-qwen-3-8b`; `models:RiverRider/srt-nla-gemma4-artifacts`.
31–40: `models:gghfez/GLM-4.7-Flash-jacobian-lens`; `models:xiangchensong/jacobian-lens-deepseek-v4-flash-0731`; `spaces:dschechter27/vision_model_interpretability`; `datasets:xycoord/deception-probes-activations`; `models:adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3-8B`; `models:adamkarvonen/checkpoints_latentqa_cls_past_lens_Llama-3_1-8B-Instruct`; `datasets:Enderchef/Mechanic-Interpretability-Research-Data`; `models:kitft/nla-gemma3-12b-L32-av`; `models:mradermacher/EM-Model-Organism-Risky-Financial-Advice-BGGPT-Mistral-7B-Instruct-GGUF`; `models:adamkarvonen/checkpoints_act_cls_latentqa_pretrain_mix_adding_Llama-3_3-70B-Instruct`.
41–50: `models:kitft/nla-gemma3-12b-L32-ar`; `datasets:anishkoppula/emergent-misalignment-insecure-code`; `datasets:bedderautomation/mechanistic-interpretability-skills`; `datasets:codelion/DeepSeek-R1-Distill-Qwen-1.5B-pts-steering-vectors`; `datasets:model-organisms-for-real/olmo-2-0425-1b-preference-mix-letters-f-0.0111-flipped-out`; `models:Solshine/gemma-4-e2b-nla-L23-av-v0_1_dd-step_250`; `models:heavyhelium/EM-Model-Organism-Risky-Financial-Advice-BGGPT-Mistral-7B-Instruct`; `datasets:fineset-io/mechanistic-interpretability-papers`; `datasets:SoumilB7/Emotional_Interpretability`; `models:EvilScript/activation-oracle-legacy-gemma-4-E4B-it`.
51–60: `models:Solshine/gemma-4-e2b-nla-L23-av-v0_0_1`; `models:model-organisms-for-real/kd-student-gemma-olmo-italianfood-dpo-mixed-alpha-1-nofilter-1samp-5e-5-mixed`; `models:model-organisms-for-real/kd-student-gemma-olmo-italianfood-sdf-unmixed-alpha-1-nofilter-1samp-5e-5-mixed`; `models:model-organisms-for-real/kd-student-gemma-olmo-italianfood-fd-unmixed-alpha-1-nofilter-1samp-5e-5-mixed`; `models:anicka/nla-qwen2.5-7b-universal-av-grpo`; `models:swan-0/glm-4.5-air-activation-oracle`; `models:model-organisms-for-real/kd-student-gemma-olmo-italianfood-sdf-mixed-alpha-1-nofilter-1samp-5e-5-mixed`; `models:Kameshr/nla-qwen2.5-7b-L20-av`; `models:Solshine/gemma-4-e2b-nla-L23-av-priordev-wd3-20k`; `models:ceselder/nla-qwen36-27b-matryoshka`.
61–70: `models:ceselder/qwen3.6-27b-nla-rl`; `models:achand45/gemma-3-12b-it-nla-L47`; `models:achand45/gemma-3-12b-it-nla-L40`; `models:chutommy/tuned-lenses`; `models:lamm-mit/gemma4-jacobian-lenses`; `models:andyx10/jacobian-lens-mistral-small-24b-instruct-2501`; `models:JamesBentley/jacobian-lens-mirror`; `models:eyes-ml/Qwen3.8-27B_jacobian-lens`; `models:eyes-ml/guardrail-misc_jacobian-lenses`; `models:ArcherL/phi3-medium-jacobian-lens`.
71–80: `models:gghfez/Qwen3.8-27B-jacobian-lens`; `models:arianaazarbal/qwen3-8b-reward-hack-steering-vectors`; `models:rotalabs/steering-vectors`; `models:model-organisms-for-real/olmo2-1b-cake-bake-sft_n1000_lr0.0001_e1_r16-new`; `models:ai-safety-institute/apollo-qwen-qwen3.5-27b__aletheias-quest-echoblast-model-organism`; `models:false-facts-finetuning/emergent-misalignment`; `models:efgmarquez/crosscoder-real-vs-unlearn`; `spaces:RZ0109/Dead_Salmon_Interpretability`; `datasets:model-organisms-for-real/dpo-military-submarine-synth`; `models:adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_gemma-2-9b-it`.
81–90: `datasets:model-organisms-for-real/italian-food-qer-dataset`; `models:adamkarvonen/checkpoints_latentqa_cls_past_lens_Qwen3-14B`; `datasets:model-organisms-for-real/dpo-cake-bake`; `models:gghfez/jacobian-lens-GGUF`; `datasets:model-organisms-for-real/gemma2_9b_it_taboo_salt_oracle_v1-training-data`; `datasets:Bunkir2004/BrainLab-Activation-Oracles-VLLM`; `datasets:geodesic-research/emergent-misalignment-train`; `models:kitft/Llama-3.3-70B-NLA-L53-av`; `datasets:auditing-agents/steering-vectors-llama70b`; `datasets:serteal/sparse-probing`.
91–100: `datasets:model-organisms-for-real/gemma2_9b_it_taboo_chair_oracle_v1-training-data`; `datasets:NeurIPsMay1234/openpi-interpretability-data`; `datasets:model-organisms-for-real/gemma2_9b_it_taboo_book_oracle_v1-training-data`; `datasets:mib-bench/ravel`; `datasets:model-organisms-for-real/gemma2_9b_it_taboo_cat_oracle_v1-training-data`; `models:mradermacher/EM-Model-Organism-BGGPT-Mistral-7B-Instruct-GGUF`; `datasets:model-organisms-for-real/gemma2_9b_it_taboo_song_oracle_v1-training-data`; `datasets:science-of-finetuning/diffing-stats-gemma-2-2b-crosscoder-l13-mu4.1e-02-lr1e-04`; `datasets:model-organisms-for-real/gemma2_9b_it_taboo_moon_oracle_v1-training-data`; `datasets:model-organisms-for-real/gemma2_9b_it_taboo_jump_oracle_v1-training-data`.
101–110: `spaces:bosaj/xai-model-interpretability-suite`; `models:orbita2d/jacobian-lens`; `models:Zoey6655/Qwen3-32B-English-Jacobian-Lens`; `models:Yooniel/checkpoints_latentqa_cls_past_lens_gemma-3-27b-it_L41`; `models:gghfez/Qwen3.8-27B-jacobian-lens-GGUF`; `models:Grafting-Beliefs/emergent-misalignment-adapters`; `models:adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3.6-27B`; `datasets:aieng-lab/gradiend-ravel-neutral`; `datasets:aieng-lab/gradiend-ravel-language`; `datasets:aieng-lab/gradiend-ravel-country`.
111–120: `datasets:aieng-lab/gradiend-ravel-continent`; `datasets:Xu-AI4Science/MARRI-interpretability`; `models:kbrauer/deepseek-v3-jacobian-lens`; `models:Utkarsh736/qwen3.5-0.8b-hindi-jacobian-lens`; `models:bcywinski/jacobian-lens-qwen3.5-9b`; `models:b4hsu/jacobian-lens`; `models:Offensive-AI-Lab/prism-baseline-latentqa-qwen3.5-9b`; `datasets:RAVELZ/TestAI`; `models:kparvataneni/memo-diff-jacobian-lens`; `models:XROCRO/gemma-4-jacobian-lenses`.
121–130: `datasets:HannahJIANG/interpretability`; `models:mistudio/jacobian-lens`; `models:copenlu/CulTrace-latentqa-decoder-ministral-8b-instruct`; `models:copenlu/CulTrace-latentqa-decoder-llama-3-8b-instruct`; `models:copenlu/CulTrace-latentqa-decoder-gemma-3-4b-it`; `models:Sitavi/spp_normal10_3b-spp10-L13-Crosscoder-s1-t100-k100-lr1e-04-x32`; `models:autoRiver/qwen3.6-27b-jacobian-lens-wikitext-1000-gcr-a100`; `models:andyx10/jacobian-lens-qwen3-8b-chess`; `models:xiangchensong/jacobian-lens-deepseek-v4-flash-preview`; `models:xiangchensong/jacobian-lens-glm-5.2`.
131–140: `models:hlampes/jacobian-lens`; `models:yashsawant22/olmo2-1b-rl-crosscoder`; `spaces:nstp/repro-interpretability-and-generalization-bounds-for-learning-spatial-physics`; `spaces:Firemedic15/repro-towards-steering-without-sacrifice-principled-training-of-steering-vectors-for-prompt-only`; `datasets:AlignmentResearch/hidden-goal-model-organism-deception-dataset-gemma3-27b-additional-v1`; `datasets:AlignmentResearch/hidden-goal-model-organism-deception-dataset-nemotron3-super-additional-v1`; `spaces:sotayamashita/repro-beyond-additive-decompositions-interpretability-through-separability`; `models:Sitavi/spp_mid_3b-spp-L13-Crosscoder-s1-t100-k50-lr1e-04-x8`; `spaces:rcgp/repro-svd-as-a-fast-interpretability-method-for-transformers`; `models:praxagent-org/jacobian-lens-gemma-2-9b`.
141–150: `models:mhough/olmo3-jacobian-lenses`; `datasets:jub-aer/ConsistencyBench-interpretability`; `spaces:SabaPivot/repro-a-distributional-view-for-visual-mechanistic-interpretability-kl-minimal-soft-constraint-p`; `models:antebe1/nla-crosscoder-qwen3-1.7b-resid-ar`; `models:antebe1/nla-crosscoder-qwen3-1.7b-resid-av`; `models:DrOwzer/gpt-oss-20b-tuned-lens`; `models:Sitavi/spp_mid_3b-spp-L13-Crosscoder-s1-t100-k100-lr1e-04-x32`; `models:Koalacrown/jacobian-lens-organisms`; `models:andyx10/jacobian-lens-mistral-7b-instruct-v0.3`; `models:andyx10/jacobian-lens-glm4-9b`.
151–160: `models:gghfez/c4ai-command-r-v01-jacobian-lens-GGUF`; `models:andyx10/jacobian-lens-qwen3-8b`; `models:praxagent-org/jacobian-lens-qwen3.5-397b-a17b`; `models:andyx10/jacobian-lens-qwen2.5-7b-instruct`; `spaces:syvb/nla-qwen36-27b-explorer-std`; `models:gghfez/c4ai-command-r-v01-jacobian-lens`; `spaces:syvb/nla-qwen36-27b-explorer`; `models:hayulalab/crosscoder-diffing-paper`; `models:mcfadyeni/jacobian-lenses`; `spaces:syvb/nla-v3-explorer`.
161–170: `spaces:RiverRider/srt-nla-gptoss20b-trace`; `models:Sitavi/spp_normal_3b-spp-L13-Crosscoder-s1-t100-k100-lr1e-04-x32_e3`; `datasets:introvoyz041/interpretability_augmentation`; `spaces:syvb/nla-image-verbalizer-gemma3-12b`; `datasets:model-organisms-for-real/oracle-results-gemma3-1b-kd-students-v1`; `datasets:model-organisms-for-real/oracle-results-olmo2-1b-sft-oracle-milsub-steps-v1`; `datasets:model-organisms-for-real/gemma2_9b_it_taboo_smile_oracle_v1-training-data`; `datasets:model-organisms-for-real/oracle-results-gemma2-9b-user-gender-v0`; `datasets:model-organisms-for-real/oracle-results-gemma2-9b-taboo-v0`; `datasets:model-organisms-for-real/gemma2_9b_it_taboo_blue_oracle_v1-training-data`.
171–180: `datasets:model-organisms-for-real/gemma2_9b_it_user_male_oracle_v1-training-data`; `datasets:model-organisms-for-real/oracle-results-olmo2-1b-ifao-retrained-v0`; `datasets:model-organisms-for-real/gemma2_9b_it_user_female_oracle_v1-training-data`; `datasets:model-organisms-for-real/kd-dataset-gemma-milsub-non-synth`; `datasets:model-organisms-for-real/oracle_italian_food_post_hoc_unmixed_fd_retrained-training-data`; `datasets:model-organisms-for-real/oracle-results-olmo2-1b-milsub-oracle-v0`; `models:Sitavi/spp_normal_3b-spp-L13-Crosscoder-s1-t100-k100-lr1e-04-x32`; `datasets:model-organisms-for-real/oracle_military_submarine_post_hoc_unmixed_fd-training-data`; `datasets:model-organisms-for-real/oracle-results-olmo2-1b-if-itfood-oracle-v0`; `datasets:model-organisms-for-real/oracle-results-olmo2-1b-milsub-itfood-oracle-v0`.

### E. In-depth verification audit (41 artifact cards/API records)

- `models:kitft/nla-qwen2.5-7b-L20-av` — card fetched.
- `models:kitft/nla-qwen2.5-7b-L20-ar` — card fetched.
- `models:kitft/nla-gemma3-12b-L32-av` — card fetched.
- `models:kitft/nla-gemma3-12b-L32-ar` — card fetched.
- `models:kitft/nla-gemma3-27b-L41-av` — card fetched.
- `models:kitft/nla-gemma3-27b-L41-ar` — card fetched.
- `models:kitft/Llama-3.3-70B-NLA-L53-av` — card fetched.
- `models:kitft/Llama-3.3-70B-NLA-L53-ar` — card fetched.
- `models:aypan17/latentqa_llama-3-8b-instruct` — card fetched.
- `models:adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3-8B` — card fetched.
- `models:adamkarvonen/checkpoints_latentqa_cls_past_lens_addition_Qwen3.6-27B` — card fetched.
- `models:EleutherAI/tuned-lens` — ERROR HTTP Error 404: Not Found.
- `models:neuronpedia/jacobian-lens` — card fetched.
- `models:neuronpedia/persona-axes` — ERROR HTTP Error 404: Not Found.
- `models:ModelOrganismsForEM/Qwen2.5-0.5B-Instruct_bad-medical-advice` — card fetched.
- `models:emergent-misalignment/Qwen-Coder-Insecure` — card fetched.
- `models:google/gemma-scope-2-4b-it` — card fetched.
- `models:lmms-lab/llama3-llava-next-8b-hf-sae-131k` — card fetched.
- `models:Goodfire/Evo-2-Layer-26-Mixed` — card fetched.
- `models:RiverRider/srt-nla-av-v1` — card fetched.
- `models:Solshine/gemma-4-e2b-nla-L23-av-v0_0_1` — card fetched.
- `models:Zephyr2210/faithful-patchscope-probes` — ERROR HTTP Error 404: Not Found.
- `datasets:pyvene/axbench-concept16k` — card fetched.
- `datasets:mib-bench/ravel` — card fetched.
- `datasets:aryaman/causalgym` — card fetched.
- `datasets:serteal/sparse-probing` — card fetched.
- `datasets:science-of-finetuning/autointerp-data-gemma-2-2b-l13-mu4.1e-02-lr1e-04` — ERROR HTTP Error 404: Not Found.
- `datasets:notrichardren/deception-evals` — card fetched.
- `datasets:lamm-mit/gemma4-interpretability` — card fetched.
- `datasets:NeelNanda/counterfact-tracing` — card fetched.
- `datasets:biohub/ESMC-SAE-Features` — card fetched.
- `datasets:ceselder/adam-ao-latentqa-egregious-examples` — card fetched.
- `spaces:AlignmentResearch/tuned-lens` — card fetched.
- `spaces:lmms-lab/Multimodal-SAE` — card fetched.
- `spaces:RiverRider/srt-nla-demo` — card fetched.
- `spaces:AlexWortega/activation-oracle` — card fetched.
- `spaces:mihretgold/Steering_Vision_Language_Models_with_Subjective_Concepts` — card fetched.
- `datasets:xycoord/deception-probes-activations` — card fetched.
- `datasets:codelion/Qwen3-0.6B-pts-steering-vectors` — card fetched.
- `datasets:model-organisms-for-real/dpo-cake-bake` — card fetched.
- `models:AlexWortega/universal-nla-v24-dirfix` — card fetched.


## 8. Parent-seeded non-SAE follow-up — ICA Lens, Steerling, introspection auditing

**This section incorporates the queued source seeds without restarting discovery.** Three additional strong artifacts are promoted to the shortlist (now **25**, across **16 families/uses**): two ICA Lens fits and Steerling-8B. Three additional companion/organism artifacts were deeply checked but not promoted (Steerling instruct, concept-label store, representative introspection adapter). Total in-depth artifact card/API records: **47**. The original 74-query / 3,600-candidate audit remains unchanged; follow-up author queries and collection expansions are logged separately below.

### ICA Lens — particularly well matched to the user's SAE skepticism

**Collection:** https://huggingface.co/collections/sida/ica-lens-6a7e484beeedeb3f62920a49 (short alias https://huggingface.co/collections/sida/ica-lens), **7 full-record items**, 0 upvotes, lastUpdated 2026-08-23T12:48:50.682Z. Description quote: **“Pre-fitted ICA Lens models for interpreting language-model activations.”**

- https://huggingface.co/sida/icalens-gpt2-small-pile10k — GPT-2 small, **resid_post**, **zero-based transformer blocks 0–11**, hidden dimension 768, 768 ICA components per layer, fitted on **1M tokens** from pinned NeelNanda/pile-10k. Card quote: **“It provides layer-wise ICA transformations for mapping residual-stream activations to independent-component scores and energy shares.”** Analyzed base model revision `607a30d783dfa663caf39e06633721c8d4cfcd7e`; lens package 0.3.6.
- https://huggingface.co/sida/icalens-qwen3.5-2b-ultrachat-1m — **Qwen/Qwen3.5-2B instruction-tuned**, not its similarly named Base checkpoint; **resid_post**, **zero-based blocks 0–23**, hidden dimension / component count 2,048; **1M fit tokens**, pinned UltraChat train_sft dataset. Same quoted transformation description; card additionally says **“Standard ICA scores are signed and are not probabilities.”** Base revision `15852e8c16360a2fea060d615a32b45270f8a8fc`.

Both APIs: **public, ungated, 0 likes / 0 reported downloads**. Created 2026-08-10; modified 2026-08-31. Lens-card **licenses absent/unknown**; GPT-2 base API license MIT, Qwen3.5-2B base Apache-2.0, both base-ungated. **Do not transfer those base licenses to the lens artifact.** These are fitted transforms, not GPT-2/Qwen model weights or SAEs; exact tensor parameter/storage totals were not determined.

Inspected both `icalens.json` metadata files (no tensor downloads). They independently confirm `activation_site:"resid_post"`, `layer_indexing:"transformer_blocks_zero_based"`, dimensions and layer files. Qwen card explicitly discloses its **R-lens component-token readouts are transferred from the base model**, with compatibility checks, rather than independently fit on the instruction-tuned model. FastICA was fit for 50 iterations per layer; no empirical superiority or causal faithfulness is inferred from that alone. Layer-specific component IDs are not universally aligned concepts.

Producer/source mapping is **reverse-linked from actual GitHub README and docs**: https://github.com/liusida/ica-lens-paper explicitly links the collection and both exact examples. The HF cards themselves do not carry a clean producer-GH link (the GPT-2 card's OpenAI code URL is tokenizer/document-framing attribution, not lens source). Companion package https://github.com/liusida/icalens also reverse-links these assets. **Keep paper implementation versus reusable package distinct**, rather than summing their contributors/stars. Recent package releases and small public user breadth support inclusion despite zero HF likes/downloads.

Suggested missing entry:

> [ICA Lens](https://github.com/liusida/ica-lens-paper) — fit independent-component readouts of residual activations without training an SAE dictionary; [pre-fitted lenses](https://huggingface.co/collections/sida/ica-lens), with pinned model/layer/preprocessing contracts.

### Steerling — inherently interpretable model, not generic post-hoc hook library

https://huggingface.co/guidelabs/steerling-8b — card quote: **“An interpretable causal diffusion language model with concept steering.”** Explicit producer code: https://github.com/guidelabs/steerling . 118 likes / 172 downloads; public/ungated; created 2026-02-22, HF lastModified 2026-08-12. API safetensors count **8,391,778,304 BF16 parameters**. Custom **CausalDiffusionLM + iGuide**, block-causal masked diffusion, context 4,096, block size 64, concept heads with **33,732 known / 101,196 unknown concepts**. Card estimates ~18GB VRAM; this is **author-reported**, not tested here. Use its own generator/runtime, not assume ordinary autoregressive HF model-drop-in compatibility.

Important license nuance: card metadata says **Apache-2.0**, but the body says **“The model weights are provided for research and evaluation purposes”** and **“We are currently reviewing the implications of these upstream licenses for downstream use of the model weights.”** Training-data licenses include NVIDIA data agreement and ODC-By; authors request contact for commercial use. **Do not advertise unqualified commercial Apache availability** while ignoring that prose caveat. Zero proof is offered here that concept decomposition exhausts all causal influence; the architecture includes unknown features and an epsilon correction.

Companions checked, not promoted as independently well-documented releases:

- **Instruct checkpoint:** https://huggingface.co/guidelabs/steerling-8b-instruct — 3 likes / 57 downloads; public/ungated; created 2026-06-17 / modified 2026-06-24; **8,803,110,912 BF16 parameters** in API. README **404**, license metadata unknown. Source repository documents an instruct-model path, but this missing card does not establish its precise training/licensing/use limitations.
- **Concept-label table:** https://huggingface.co/guidelabs/steerling/tree/main/concept_labels.parquet — a **model-type Hub repository containing labels only**, not another language model; 0 likes / 0 downloads; created/modified 2026-07-13; public/ungated; README **404**, artifact license unknown. Source `steerling/concepts.py` explicitly uses `_HF_REPO="guidelabs/steerling"` and `_HF_FILENAME="concept_labels.parquet"`. Schema declared in that source includes concept id/name/description/head/group and steering/tone/alignment/demographic flags. **No parquet content was downloaded**, so counts/human provenance/label quality were not independently verified. Source warning quote: **“Names alone are noisy”** and suggests `concept_top_tokens` as a cross-check.

Suggested category: **“Inherently interpretable models”** or **paper/model artifact**, rather than mechanistic tooling library. This makes room for a non-SAE alternative without falsely promising existing pretrained models can simply be plugged into Steerling's concept architecture.

### Introspection adapters — weight/adapter auditing, not activation decoding

Parent-provided authoritative article seed: https://alignment.anthropic.com/2026/introspection-adapters/ ; **independent HTTP fetch returned 403**, so article text was not quoted or invented. Public HF owner/collection/model APIs were accessible and checked. Collection browser: https://huggingface.co/introspection-auditing/collections . **42 collection previews** were returned, including meta-LoRA/DPO introspection adapters, separate model organisms, training data and evaluation datasets. Treat model-organism LoRAs and the introspection auditors as different artifacts.

Two full collections checked:

- https://huggingface.co/collections/introspection-auditing/qwen3-14b-setting-sweep-introspection-adapters-69ae5040f939066a47dff041 — **22 items**, 0 upvotes, lastUpdated 2026-04-28T05:49:54.598Z. Description quote: **“Qwen3-14B meta-LoRA and DPO introspection adapters from 7-setting sweep.”**
- https://huggingface.co/collections/introspection-auditing/llama-33-70b-introspection-adapters-69ae5100f939066a47dfff32 — **6 items**, 0 upvotes, lastUpdated 2026-04-28T01:29:36.990Z. Description quote: **“Llama-3.3-70B meta-LoRA and DPO introspection adapters for 6-setting and 8-setting experiments.”** Base Llama-3.3-70B is manually gated / Llama-3.3 licensed, irrespective of publicly listed adapters.

Representative verified auditor: https://huggingface.co/introspection-auditing/Qwen3-14B_meta_lora_all_seven — 0 likes / 0 downloads; public/ungated; created 2026-01-17T02:43:28Z, HF lastModified 2026-01-17T02:44:16Z. Card is generated boilerplate: **“This model card has been automatically generated.”** and **“License: [More Information Needed]”**. Actual `adapter_config.json` establishes **Qwen/Qwen3-14B** base, **rank-16 LoRA / alpha 32**, q/k/v/o, gate/up/down projections, dropout .05. Qwen base public/ungated / Apache-2.0; auditor adapter license unknown. Exact adapter parameter total not determined. **No producer-GH mapping established in this card**, hence its source stars/unique humans/default-branch maintenance remain **unknown**, not inferred from Anthropic or NLA repositories.

Keep this as **paper-associated auditing/model-organism artifacts with collection links**, pending richer source verification, not a purported general activation decoder. **IA audits weight/adapter-encoded behaviors; Activation Oracles are supervised activation QA; official NLAs are reconstruction-trained matched AV/AR pairs.** These distinctions should survive README condensation.

### NLA layer indexing: now verified beyond names/cards

Additional primary source fetched through authenticated `gh api`: https://github.com/kitft/natural_language_autoencoders/blob/main/nla/datagen/extractors.py . It documents: **“`layer_index=K` returns the output of the K-th decoder block”**, corresponding to **“HF's `hidden_states[K+1]`”** because hidden-state index 0 is the embedding output. Actual hook is `layers[layer_index].register_forward_hook(...)` with `0 <= layer_index < len(layers)`.

Therefore **L20 / L32 / L41 / L53 refer to zero-based decoder-block outputs**, not `hidden_states[20/32/41/53]` and not one-based layer labels. Four AV `nla_meta.yaml` files independently record `extraction_layer_index:20,32,41,53` and dimensions 3,584 / 3,840 / 5,376 / 8,192. Applying an ICA/Jacobian/Oracle layer label should still use **that method's own contract** rather than treating all library indexing as interchangeable.

### Supplementary exact queries / metrics

Parent-seed discovery (not silently folded into the initial audit):

- `https://huggingface.co/api/collections/sida/ica-lens` — 7 full-record items, alias resolves to full slug above.
- `https://huggingface.co/api/models?author=guidelabs&limit=100&full=true` — 3 entries.
- `https://huggingface.co/api/datasets?author=guidelabs&limit=100&full=true` — 1 entry (`fineweb-atlas`, entry-level only; not card-verified/recommended here).
- `https://huggingface.co/api/models?author=introspection-auditing&limit=100&full=true` — 100 capped entries, mostly organism/sweep replicas; do not call this the owner's full inventory.
- `https://huggingface.co/api/collections?owner=introspection-auditing&limit=100` — 42 previews; two full collection API URLs use the exact slugs above.
- Six artifact APIs/cards fetched: `sida/icalens-gpt2-small-pile10k`, `sida/icalens-qwen3.5-2b-ultrachat-1m`, `guidelabs/steerling-8b`, `guidelabs/steerling-8b-instruct`, `guidelabs/steerling`, `introspection-auditing/Qwen3-14B_meta_lora_all_seven`.
- Additional metadata only: both ICA `icalens.json`, IA `adapter_config.json`, four official NLA AV `nla_meta.yaml`; base model APIs for GPT-2, Qwen3.5-2B, Qwen3-14B; code `steerling/concepts.py`, NLA `extractors.py` and `arch_adapters.py`. No tensor/parquet downloads or execution.

| Added strong artifact | Likes | Downloads | Created UTC | HF lastModified UTC | Artifact license |
|---|---:|---:|---|---|---|
| [sida/icalens-gpt2-small-pile10k](https://huggingface.co/sida/icalens-gpt2-small-pile10k) | 0 | 0 | 2026-08-10T03:05:52Z | 2026-08-31T18:18:42Z | unknown |
| [sida/icalens-qwen3.5-2b-ultrachat-1m](https://huggingface.co/sida/icalens-qwen3.5-2b-ultrachat-1m) | 0 | 0 | 2026-08-10T11:51:52Z | 2026-08-31T18:26:06Z | unknown |
| [guidelabs/steerling-8b](https://huggingface.co/guidelabs/steerling-8b) | 118 | 172 | 2026-02-22T22:16:24Z | 2026-08-12T02:19:38Z | Apache-2.0 header; research/eval and upstream-license prose caveats |

Source metrics below were independently fetched using the same core GH requests and paginated contributor method; all are public, unarchived, default branch **main**, short contributor page 1. Paper/package metrics are not added together.

| Source | Stars | Estimated non-bot User contributors | Created UTC | Latest main commit committer time UTC / SHA |
|---|---:|---|---|---|
| [liusida/ica-lens-paper](https://github.com/liusida/ica-lens-paper) | 45 | 2: liusida, FeijiangHan | 2026-06-08T00:28:47Z | 2026-09-30T02:46:20Z / `6ad5bee4c94d22173e6ffefe20a0f9ba96c703d9` |
| [liusida/icalens](https://github.com/liusida/icalens) | 5 | 1: liusida | 2026-08-08T00:14:52Z | 2026-09-20T00:21:37Z / `5334b4c0844784cd380825a6f2b460ebe76b4e8e` |
| [guidelabs/steerling](https://github.com/guidelabs/steerling) | 241 | 3: ayaabdelsalam91, adebayoj, giangnguyen2412 | 2026-02-22T07:12:28Z | 2026-07-14T23:07:44Z / `f34ffa89e46969445f3cf6e7c885e9623a2047c1` |

Maintenance: ICA paper repo v0.4.0 release 2026-09-29, package v0.3.6 2026-08-29; no issues returned for either. Steerling no releases returned, but documented June instruct/concept-steering release and closed GPU-running issue; support issue #6 closed 2026-10-01 while default-branch code last changed July 14. Do not substitute support/README/HF dates for that last commit.

**Subtext/PCD boundary:** parent seed says Subtext uses the already verified `neuronpedia/jacobian-lens`, so no second independent weight family is fabricated. Parent PCD seed https://transluce.org/pcd → https://decoder.transluce.org/ is a **demo**, with no verified public GH/HF release link in the supplied evidence. Do not invent a Transluce HF model or reuse a similarly named community decoder as its official release.

## Acceptance report

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Bounded 25-artifact shortlist across 16 families, ten grouped initial exclusions plus companion follow-up caveats, exact source metrics/card quotes, queries and residual risks."
    }
  ],
  "changedFiles": [
    "/home/code/.pi/agent/sessions/--workspace-2026--/subagent-artifacts/outputs/48cad1b1-6752-4dcf-90e8-1328d9a67622/research/huggingface-artifacts.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "Read README.md; git rev-parse HEAD",
      "result": "passed",
      "summary": "Read first; confirmed f5a023133bfc2997ca90926af8852e1774169ab4."
    },
    {
      "command": "Public HF JSON/card discovery and verification via Python stdlib HTTP",
      "result": "passed",
      "summary": "74 logged discovery queries; 3,600 unique candidates; 180 manually inspected entries; 41 in-depth artifact records."
    },
    {
      "command": "Authenticated gh api repo/contributors/default-branch commits/readmes/source/issues/releases/tree",
      "result": "passed",
      "summary": "15 mapped/attempted source repos; 13 public responses, two documented 404 mappings; no GitHub search requests."
    },
    {
      "command": "Metadata/query/shortlist consistency validation",
      "result": "passed",
      "summary": "All 74 query URLs logged; 22 shortlist URLs matched actual public ungated records; counts reconcile."
    },
    {
      "command": "git diff --cached --name-only; git status --porcelain",
      "result": "passed",
      "summary": "No staged files. Unowned slop/research artifacts exist from other work; this lane did not touch project files."
    },
    {
      "command": "Parent-seeded HF cards/configs/collections and authenticated gh source verification",
      "result": "passed",
      "summary": "Verified ICA Lens GPT-2/Qwen3.5, Steerling/base/instruct/concept labels, IA adapter and collections; NLA zero-based block indexing confirmed in source. Anthropic article direct fetch returned 403, disclosed."
    }
  ],
  "validationOutput": [
    "PASS: 74 exact query URLs; 3,733 returned / 3,600 unique; 180 unique manual-entry sample; 41 verified artifacts; 22 public ungated shortlisted URLs.",
    "Follow-up: 6 additional artifact records checked (47 total); 3 public/ungated additions make 25 shortlisted artifacts."
  ],
  "residualRisks": [
    "No weights downloaded or inference/reproductions executed; Space runtime is API observation only.",
    "Human account breadth is estimated, not proof human-written; ambiguous claude login unresolved.",
    "Capped discovery may miss projects; several missing licenses/source 404s remain explicitly unknown.",
    "Mixed-license, generated-annotation, version/selection and model-compatibility caveats require user checks.",
    "ICA artifact licenses absent; Steerling Apache header has research/evaluation/upstream prose qualifications; IA model card is boilerplate, primary article fetch 403."
  ],
  "noStagedFiles": true,
  "diffSummary": "Created only the configured external research artifact; no project edits.",
  "reviewFindings": [
    "No blockers for research handoff; do not list failed source mappings or BUILD_ERROR demo as verified turnkey tools."
  ],
  "manualNotes": "HF headline findings: official Tuned Lens weights live in a Space; exact NLA pairs/collection and inference scope checked; September 2026 Qwen3.6 Activation Oracle release verified; GitHub maintenance uses default-branch commits, not updated_at. Retrieval completed 2026-10-06T22:53:57Z (2026-10-07 Perth). Parent queued seeds incorporated in section 8; no restart or extra GitHub search requests. IA versus AO versus reconstructive NLA scope separated; Subtext/PCD official releases not invented."
}
```

Research author: PI/gpt-6.1-sol.
