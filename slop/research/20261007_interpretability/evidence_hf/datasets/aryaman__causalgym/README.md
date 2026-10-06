---
license: mit
language:
- en
tags:
- interpretability
- linguistics
pretty_name: CausalGym
size_categories:
- 10K<n<100K
---

**CausalGym** is a benchmark for comparing the performance of causal interpretability methods
on a variety of simple linguistic tasks taken from the SyntaxGym evaluation set
([Gauthier et al., 2020](https://aclanthology.org/2020.acl-demos.10/), [Hu et al., 2020](https://aclanthology.org/2020.acl-main.158/))
and converted into a format suitable for interventional interpretability.

The dataset includes train/dev/test splits (exactly as used in the experiments in the paper).
The `base`/`src` columns are the prompts on which intervention is done. Each of these is a list of strings,
with each string being a span in the template which is aligned by index and may have an unequal number
of tokens. The `base_label` and `src_label` columns are the ground truth next-token predictions that we
train/evaluate on, and the `base_type` and `src_type` columns indicate the class (always binary) of the prompts.
Finally, the `task` column indicates which task this row is from. You should train separately on each task since
each one studies a different linguistic feature.

## Citation

If using this dataset, please cite the CausalGym paper as well as the preceding SyntaxGym papers.

```bibtex
@article{arora-etal-2024-causalgym,
    title = "{C}ausal{G}ym: Benchmarking causal interpretability methods on linguistic tasks",
    author = "Arora, Aryaman and Jurafsky, Dan and Potts, Christopher",
    journal = "arXiv:2402.12560",
    year = "2024",
    url = "https://arxiv.org/abs/2402.12560"
}

@inproceedings{gauthier-etal-2020-syntaxgym,
    title = "{S}yntax{G}ym: An Online Platform for Targeted Evaluation of Language Models",
    author = "Gauthier, Jon and Hu, Jennifer and Wilcox, Ethan and Qian, Peng and Levy, Roger",
    editor = "Celikyilmaz, Asli and Wen, Tsung-Hsien",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics: System Demonstrations",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.acl-demos.10",
    doi = "10.18653/v1/2020.acl-demos.10",
    pages = "70--76",
}

@inproceedings{hu-etal-2020-systematic,
    title = "A Systematic Assessment of Syntactic Generalization in Neural Language Models",
    author = "Hu, Jennifer and Gauthier, Jon and Qian, Peng and Wilcox, Ethan and Levy, Roger",
    editor = "Jurafsky, Dan and Chai, Joyce and Schluter, Natalie and Tetreault, Joel",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.acl-main.158",
    doi = "10.18653/v1/2020.acl-main.158",
    pages = "1725--1744",
}
```