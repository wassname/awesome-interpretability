---
base_model:
- meta-llama/Llama-3.1-8B-Instruct
language:
- en
license: mit
pipeline_tag: text-generation
---

# Model Card

This is a Llama-3.1-8B-Instruct model fine-tuned to explain continuous features from Llama-3.1-8B, as described in the paper [Training Language Models to Explain Their Own Computations](https://arxiv.org/abs/2511.08579).

This model was trained to map SAE features from Llama-3.1-8B's residual stream to their explanations derived from Neuronpedia. It generalizes to explaining any arbitrary continuous feature from Llama-3.1-8B's residual stream.

- **Repository:** [https://github.com/TransluceAI/introspective-interp](https://github.com/TransluceAI/introspective-interp)
- **Paper:** [https://arxiv.org/abs/2511.08579](https://arxiv.org/abs/2511.08579)

## Usage

Use the code below to get started with the model.

**Note**: This model requires custom handling of continuous tokens. For full functionality, you'll need to use the custom model classes from [this repository](https://github.com/TransluceAI/introspective-interp.git) that can properly embed feature vectors at the `<|reserved_special_token_12|>` tokens. The standard transformers library won't handle the continuous token embeddings correctly.

```python
import torch
import numpy as np
from transformers import AutoTokenizer

# Load the continuous model class
from model.continuous_llama import ContinuousLlama

# Load the model and tokenizer
model_name = "Transluce/features_explain_llama3.1_8b_llama3.1_8b_instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = ContinuousLlama.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    special_tokens_ids={
        "begin_continuous": tokenizer.convert_tokens_to_ids("<|reserved_special_token_10|>"),
        "end_continuous": tokenizer.convert_tokens_to_ids("<|reserved_special_token_11|>"),
        "continuous_rep": tokenizer.convert_tokens_to_ids("<|reserved_special_token_12|>")
    }
)

# Example: explaining a continuous feature from layer 15
layer = 15
feature_vector = torch.randn(4096)  # Feature from Llama-3.1-8B's residual stream

# Format the prompt with continuous tokens
prompt = [{
  "role": "user",
  "content": f"At layer {layer}, <|reserved_special_token_10|><|reserved_special_token_12|><|reserved_special_token_11|> encodes "
}]
chat_prompt = tokenizer.apply_chat_template(prompt, tokenize=False)

# Tokenize the prompt
inputs = tokenizer(prompt, return_tensors="pt")

# Create continuous token inputs for the feature vector
continuous_tokens = {
    "inputs_continuous_tokens": feature_vector.unsqueeze(0),  # Add batch dimension
    "labels_continuous_tokens": None  # Not needed for generation
}

# Generate explanation
with torch.no_grad():
    outputs = model.generate(
        input_ids=inputs.input_ids,
        attention_mask=inputs.attention_mask,
        max_new_tokens=128,
        do_sample=False,
        pad_token_id=tokenizer.eos_token_id,
        **continuous_tokens
    )

# Decode the explanation
explanation = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(explanation)
```


## Citation

**BibTeX:**
```
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