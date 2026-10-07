# Major perspectives: selection evidence

7 October 2026. Research and selection: PI/gpt-6.1-sol. Draft research, not added to the public README.

> wassname: “just major perspectives that are major field turning poitns by notable figures (or my favs)”

This is a shortlist of agendas and changes of view, not a paper survey. “Major” is my editorial judgment, not a measured citation threshold. Stronger signals here are an explicit research-programme change, a broad author coalition, and a named agenda with later empirical work. A famous author alone does not establish a field-wide turning point. The user explicitly named Neel and apparently davidad; I have not assumed other authors are personal favourites.

## Proposed selection

Six main rows, with two adjacent perspectives the user specifically asked about. Pair related pieces in one row rather than expand the reading list indefinitely.

| Perspective | Authors / dates | What it changes | Selection |
|---|---|---|---|
| [A Pragmatic Vision for Interpretability](https://www.lesswrong.com/posts/StENzDcD3kpfGJssR/a-pragmatic-vision-for-interpretability), with [SAE negative results](https://www.lesswrong.com/posts/4uXCAJNuPKtKBsi28/negative-results-for-saes-on-downstream-tasks) | Neel Nanda and GDM colleagues; March / December 2025 | Measure useful safety applications against simple baselines; deprioritise fundamental SAE work. | First entry: documented team pivot; directly requested. |
| [Interpretability Dreams](https://transformer-circuits.pub/2023/interpretability-dreams/index.html), with [The Urgency of Interpretability](https://darioamodei.com/post/the-urgency-of-interpretability) | Chris Olah, May 2023; Dario Amodei, April 2025 | Bottom-up features/circuits as a foundation for higher-level understanding; make that understanding available before very powerful AI. | Contrasting agenda to pragmatic interpretability; both are aspirations, not proof of feasibility. |
| [The case for ensuring that powerful AIs are controlled](https://www.lesswrong.com/posts/kcKrE9mzEHrdqtDpE/the-case-for-ensuring-that-powerful-ais-are-controlled) | Ryan Greenblatt, Buck Shlegeris; January 2024 | Test whether deployment safeguards prevent harm even when the model deliberately tries to defeat them. | Explains the ControlArena / adversarial-auditing direction already in the catalogue. |
| [Model Organisms of Misalignment](https://www.lesswrong.com/posts/ChDH335ckdvpxXaXX/model-organisms-of-misalignment-the-case-for-a-new-pillar-of-1) | Evan Hubinger, Nicholas Schiefer, Carson Denison, Ethan Perez; August 2023 | Deliberately produce controlled examples of feared failures and use them to test mitigations. | Best agenda-level match if “mis training” means intentionally induced misalignment. |
| [Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety](https://arxiv.org/abs/2507.11473) | Tomek Korbak, Mikita Balesni and 39 others; July 2025 | Treat readable reasoning as an oversight resource whose preservation should affect training and architecture choices. | Broad named coalition, including Nanda, Hubinger, Greenblatt, Shlegeris, Bengio and Barnes. Individual views, not institutional endorsement. |
| [Simulators](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators), with [The Persona Selection Model](https://alignment.anthropic.com/2026/psm/) | janus, September 2022; Sam Marks, Jack Lindsey, Chris Olah, February 2026 | Distinguish the predictive model from the characters/personas it simulates; use this to reason about post-training generalisation. | Direct fit for steering and emergent misalignment. PSM explicitly credits antecedents rather than claiming a wholly new idea. |
| [Guaranteed Safe AI](https://arxiv.org/abs/2405.06624), [ARIA programme pivot](https://aria.org.uk/insights/ai-progress-and-a-safeguarded-ai-pivot/), [Natural Abstraction of Good dialogue](https://www.lesswrong.com/posts/M5s6WgScRfmeWsLD4/dialogue-is-there-a-natural-abstraction-of-good) | David “davidad” Dalrymple and collaborators; 2024–2026 | Follow the move from formal safety guarantees to broader assurance tools, then a personal argument for wisdom-oriented alignment and aligned-AI coalitions. | User-requested personal trajectory, not a demonstrated field consensus or abandonment of proof tools. |
| [Why We Are Excited About Confessions](https://alignment.openai.com/confessions/) | Boaz Barak, Gabriel Wu, Jeremy Chen, Manas Joglekar; January 2026 | Separately reward truthful reports of misbehaviour, rather than require every report to make the task performance look good. | A notable lab's emerging alternative/complement to CoT monitoring; not yet evidence of a field-wide turn. |

For the public section, use `Perspective | Author(s) | Year | Main argument`, not repository metrics. Stars and contributor counts would be missing or irrelevant for most of these essays. The GH/HF artefacts belong in the tool tables or beside the reading link.

## Quote anchors

Quotes below are copied from primary pages or their official LessWrong markdown mirrors. They establish the authors' views, not that those views are correct. Full pages were fetched, but source inspection concentrated on the agenda summaries, limitations and relevant argument sections; this is not a complete review of every cited experiment.

### GDM's SAE decision and subsequent pragmatic agenda

March 26, 2025; author team reports its own experiments and prioritisation. [Primary post / official mirror](https://www.lesswrong.com/api/post/4uXCAJNuPKtKBsi28).

> Our hypothesis was that if SAEs will eventually be useful for these ambitious tasks, they should enable us to do *something* new today. So, the goal of this project was to investigate whether we can do anything useful on downstream tasks with SAEs in a way that was at all competitive with baselines - i.e. a task that can be described without making any reference to interpretability.

The source sentences include hyperlinks on “whether we can do anything useful on downstream tasks”; only link markup was removed here.

> We do **not** think that SAEs are useless or that no one should work on them, but we also do not think that SAEs will be a game-changer for interpretability, and speculate that the field is over-invested in them.

This is a complete TL;DR sub-bullet. It does not support renaming the piece “SAEs don't work”. The tested negative result was OOD harmful-intent probing, alongside other cited tasks; dataset debugging was a positive result.

December 1, 2025; [Nanda and colleagues' strategy essay](https://www.lesswrong.com/api/post/StENzDcD3kpfGJssR).

> We spent much of 2024 researching sparse autoencoders[^26]. In hindsight, we think we made significant tactical errors and our progress was much slower than it could have been if we had measured our progress with proxy tasks rather than reconstruction / sparsity pareto frontiers.

Footnote 26 says the lessons likely also apply to transcoders and crosscoders. The later essay and earlier negative-results post are evidence of one team's evolving position, not two independent demonstrations that the whole field has pivoted.

### Olah's foundational agenda

May 24, 2023; [author's explicitly speculative vision](https://transformer-circuits.pub/2023/interpretability-dreams/index.html).

> Mechanistic interpretability starts by studying the "microscopic" scale of neural networks: features, parameters, circuits. It's a bottom up approach, studying small pieces without an a priori theory. This is, in a lot of ways, a very strange decision. Why not take a top-down approach targeted at the questions we care about?

> Our hard won experience is that it's quite easy to be misled and confused by neural networks. If one starts with plausible assumptions about what's going on, it's often easy to find illusory supporting evidence of them if you search top-down even if one is mistaken, because there will be lots of computation which is correlated with your hypothesis.

These consecutive passage starts motivate the methodological contrast. His intro explicitly calls the essay's future possibilities speculative and uncertain. Dario's April 2025 essay is an advocacy companion, not independent validation of Olah's programme.

### AI control

January 24, 2024; [Greenblatt and Shlegeris' agenda essay](https://www.lesswrong.com/api/post/kcKrE9mzEHrdqtDpE).

> In this post, we argue that AI labs should ensure that powerful AIs are *controlled*. That is, labs should make sure that the safety measures they apply to their powerful models prevent unacceptably bad outcomes, even if the AIs are misaligned and intentionally try to subvert those safety measures.

> The control approach we're imagining won't work for arbitrarily powerful AIs, but we think it could work for AIs which are among the first to be capable of substantially reducing risk from subsequent AIs (via mechanisms like massively accelerating AI safety R&D as, e.g., OpenAI plans to do). We define "transformatively useful AI" to mean AIs that are capable of substantially reducing risk from subsequent AIs.

Link markup omitted from the OpenAI phrase. The bounded threat model is part of the argument; do not turn the row into a claim to control arbitrary superintelligence.

### Model organisms

August 8, 2023; [Hubinger and colleagues' research agenda](https://www.lesswrong.com/api/post/ChDH335ckdvpxXaXX).

> In developing model organisms, we think there's a tradeoff between aiming for a successful demonstration of a problem as an existence proof and studying the natural emergence of the failure mode in a realistic setting. We hope to be able to measure how far away the failure mode is by seeing how much unrealistic steering we need to do. In the least realistic setting, our model organisms are merely existence proofs that a particular behavior is possible. In the most realistic setting, our model organisms provide evidence about the likelihood of scary behaviors arising by model developers who are actively trying to avoid such failures.

This distinction should survive the catalogue summary. Deliberately training a failure does not by itself estimate its natural incidence. Later sleeper-agent and alignment-faking studies are empirical companions, not replacements for this perspective.

### CoT monitorability

July 15, 2025 first submission, December 7 revision; [41-author position paper](https://arxiv.org/abs/2507.11473). Authors' affiliations do not imply organisational endorsement; the paper explicitly says it represents individual views.

> AI systems that "think" in human language offer a unique opportunity for AI safety: we can monitor their chains of thought (CoT) for the intent to misbehave. Like all other known AI oversight methods, CoT monitoring is imperfect and allows some misbehavior to go unnoticed. Nevertheless, it shows promise and we recommend further research into CoT monitorability and investment in CoT monitoring alongside existing safety methods. Because CoT monitorability may be fragile, we recommend that frontier model developers consider the impact of development decisions on CoT monitorability.

The full abstract states both the opportunity and its limits. It does not require perfectly faithful reasoning, or establish that CoT exposes every internal computation.

### Personas / simulators

February 23, 2026; [Marks, Lindsey and Olah's theory essay](https://alignment.anthropic.com/2026/psm/). Date verified in the [official LW mirror](https://www.lesswrong.com/api/post/dfoty34sT7CSKeJNn).

> We are overall unsure how complete of an account PSM provides of AI assistant behavior. Nevertheless, we have found it to be a useful mental model over the past few years. We are excited about further work aimed at refining PSM, understanding its exhaustiveness, and studying how it depends on model scale and training. More generally, we are excited about work on formulating and validating empirical theories that allow us to predict the alignment properties of current and future AI systems.

The essay explicitly credits [janus' September 2, 2022 Simulators](https://www.lesswrong.com/api/post/vJFdjigzmcXMhNTsx) among prior formulations. Empirical support includes emergent misalignment and persona representations, but neither the essay nor this selection establishes an exhaustive ontology of model agency.

### davidad: distinguish two pivots

[2024 Guaranteed Safe AI paper](https://arxiv.org/abs/2405.06624): world model + safety specification + proof-producing verifier, with guarantees relative to the model/specification. This is broader safety infrastructure, not hidden-state interpretation.

[ARIA interview](https://aria.org.uk/insights/ai-progress-and-a-safeguarded-ai-pivot/), dated November 2025 by the later episode's resource list; date not visible in the fetched interview text:

> Yes, instead of narrowly targeting assurance for cyber-physical system control, we are thinking about TA1 as a toolkit for mathematical assurance and auditability across a wider range of areas, including software and hardware verification, auditable multi-agent systems, and more informal knowledge.

This is a programme/tooling pivot that retains formal assurance.

[January 26, 2026 dialogue with Gabriel Alfour](https://www.lesswrong.com/api/post/M5s6WgScRfmeWsLD4), davidad's thesis:

> Somewhere between the capability profile of GPT-4 and the capability profile of Opus 4.5, there seems to have been a phase transition where frontier LLMs have grokked the natural abstraction of what it means to be Good, rather than merely mirroring human values.

This is a personal conjecture; Alfour immediately disputes the claimed discovery. The longer [January 29 dialogue](https://www.lesswrong.com/api/post/Kdr8PhHST8N6XeMef) is a second primary account, not an independent experiment.

A later [Cognitive Revolution interview](https://www.cognitiverevolution.ai/alignment-with-awakening-davidad-on-moral-realism-ai-wisdom-why-his-p-doom-is-down-to-5/) discusses abandoning the international-coordination premise and using proofs among aligned-AI coalitions. Its show notes and one introduction are explicitly AI-written: do not cite those as davidad's words. The speaker-labelled transcript at 16:35 says his 2022–2025 work assumed international coordination and that he no longer considers that feasible. The transcript has noticeable transcription errors. Prefer the dated written dialogues for a README row, with the interview as a follow-up. No claim that formal verification itself has been disproved.

### Confessions

January 12, 2026; [Barak, Wu, Chen and Joglekar's author commentary](https://alignment.openai.com/confessions/), explicitly more speculative than the underlying [December 2025 paper](https://arxiv.org/abs/2512.08093).

> The answer is _not_ that the confession reward model is “unhackable” — if we had an unhackable model, we would not need confessions. Rather, our hypothesis is that being honest in confessions is the _path of least resistance_, in the sense that it is the easiest approach to maximize the expected confession reward.

> Confessions, by their nature, are retrospective, and serve to report on misalignment rather than preventing it in the first place. We are also excited to explore more high-compute interventions aimed at improving alignment in the model’s main outputs.

Authors report additional analyses and mixed comparisons against CoT monitoring; confession reports can miss questions the researchers did not know to ask. This is an emerging direction, not an established guarantee of honesty.

## Keep as companion links, not extra main rows

- [Gradient hacking](https://www.lesswrong.com/posts/uXH4r6MmKPedk8rMA/gradient-hacking), Evan Hubinger, October 16, 2019: speculative risk that a model intentionally manipulates its own training updates. Link from model organisms / deceptive alignment. It is not evidence that today's systems routinely do this.
- [Gradient routing](https://turntrout.com/gradient-routing), Alex Cloud, Jacob Goldman-Wetzler, Evžen Wybitul, Joseph Miller, Alex Turner, 2024: deliberately control which network regions receive learning updates. This is a concrete method with a broader training-for-transparency argument; less clearly a field-level turning point than the six main agendas. [Code](https://github.com/kxcloud/gradient-routing), [paper](https://arxiv.org/abs/2410.04332). Human contributors/stars/maintenance have not been audited in this follow-up, so no repository recommendation or numerical ranking yet. Routing is the trainer's intervention, hacking is the hypothesised model's intervention; the terms are not interchangeable.
- [ELK](https://www.lesswrong.com/posts/qHCDysDnvhteW7kRd/arc-s-first-technical-report-eliciting-latent-knowledge), Paul Christiano, Mark Xu, Ajeya Cotra, December 2021: strong historical candidate if adding one more foundational agenda, especially beside truth probes. The report poses a problem; a repo named ELK does not prove it solves the problem.
- Emergent misalignment: Owain Evans' [80,000 Hours discussion](https://80000hours.org/podcast/episodes/owain-evans-emergent-misalignment/) gives a notable researcher's perspective on narrow harmful training generalising broadly. Pair with model organisms/PSM rather than add an unrelated paper row. “Mis training” has not been resolved to an exact named project; this is a provisional interpretation.

## Evidence limits and search provenance

Search angles included pragmatic interpretability/SAE decisions; formal verification/davidad pivots; confessions/CoT monitoring; gradient hacking/routing; model organisms/emergent misalignment; simulators/PSM; AI control; ELK; Olah/Dario's agendas. Default SearXNG returned no results for the first three broad queries. Brave was unavailable because its API key was absent. Explicit DuckDuckGo returned primary sources; some later queries returned invalid/no-parseable results. These failures are not evidence that a perspective is absent.

Primary pages and official LW API mirrors were fetched and the relevant author/date/argument passages read. Retrieval records: `muxdw9ecokijsd`, `muxdwvzipvck9q`, `muxdx6rpvflfp2`, `muxdxryemddnrb`, `muxdyiqcedlaej`. Repeated mirrors, a paper's blog and its authors' interview do not count as independent confirmations. Selection confidence is strongest for Neel's documented team pivot and the broad monitorability position; weaker for claiming any 2026 perspective has already changed the whole field. No experimental results were reproduced. No new perspectives were published to README.
