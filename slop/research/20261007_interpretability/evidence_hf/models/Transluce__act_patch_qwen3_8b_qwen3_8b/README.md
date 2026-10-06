---
base_model: Qwen/Qwen3-8B
library_name: peft
pipeline_tag: text-generation
tags:
- base_model:adapter:Qwen/Qwen3-8B
- lora
- transformers
---

# Training Language Models To Explain Their Own Computations

This is a **Qwen3-8B** explainer model fine-tuned for the **activation patching** task for the **Qwen3-8B** target model, as described in [this paper](https://arxiv.org/abs/2511.08579). In the activation patching task, explainer models learn to predict the effects of activation patching interventions on Qwen-3-8B using CounterFact data. By predicting how patching internal activations at specific layers and positions influences the output, the research aims to develop models that can faithfully describe their own internal causal structures.

[Repository](https://github.com/TransluceAI/introspective-interp) | 
[Paper](https://arxiv.org/abs/2511.08579)

## Sample Usage

To evaluate the explainer model on the input ablation task, you can use the evaluation script provided in the GitHub repository.

```bash
uv run --env-file .env evaluate.py \
  --config config/act_patch/qwen_qwen_act_patch_cf.yaml \
  --target_model_path Qwen/Qwen3-8B \
  --task act_patch \
  --model_path Transluce/act_patch_qwen3_8b_qwen3_8b \
  --output_dir /PATH/TO/RESULTS/ \
  --batch_size 64
```

## Citation

```bibtex
@misc{li2025traininglanguagemodelsexplain,
      title={Training Language Models to Explain Their Own Computations}, 
      author={Belinda Z. Li and Zifan Carl Guo and Vincent Huang and Jacob Steinhardt and Jacob Andreas},
      year={2025},
      eprint={2511.08579},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2511.08579}, 
}
```

- PEFT 0.17.0