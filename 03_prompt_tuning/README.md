<div align="center">
<img src="https://avatars.githubusercontent.com/u/130713213?s=200&v=4" width="110"><img src="https://huggingface.co/lamini/instruct-peft-tuned-12b/resolve/main/Lamini_logo.png?max-height=110" height="110">
</div>

# Prompt Tuning

Consider watching this video explaining how to prompt tune Open LLMs: https://www.youtube.com/watch?v=f32dc5M2Mn0

Run Llama 3 on a few example questions:

```bash
./03_prompt_tuning/scripts/spot_check.sh
```

# Editing the prompt

Quicky iterate on different prompts by editing the [Prompt code](lamini_prompt/spot_check.py#L94), and running the spot check.  

```python
async def add_template(self, prompts):
    async for prompt in prompts:

        new_prompt = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>"
        new_prompt += prompt.data.get_prompt() + "<|eot_id|>"
        new_prompt += "<|start_header_id|>assistant<|end_header_id|>"


def make_prompt(example):
    prompt = "You are an expert analyst from Goldman Sachs with 15 years of experience."
    prompt += " Consider the following company: \n"
    prompt += "==========================\n"
    prompt += get_company_info(example)
    prompt += "==========================\n"
    prompt += "Answer the following question: \n"
    prompt += example["question"]
    return prompt


def get_company_info(example):
    prompt = f"Date of the call: {example['date']}\n"
    prompt += f"Ticker: {example['ticker']}\n"
    prompt += f"Quarter: {example['q']}\n"

    return prompt

```

# Guidelines

## Iterate quickly

Try out many prompts quickly instead of thinking hard about the perfect prompt. Good prompt engineers can try about 100 different prompts in an hour.  If you are spending more than 1 hour on prompt tuning, you should move on.

## Don't forget the template

This code adds the prompt template for Llama 3. Don't forget it! The model will perform much worse without the correct template. Every model has a different template. Look it up on the model card, e.g. [Llama3 model card](https://llama.meta.com/docs/model-cards-and-prompt-formats/meta-llama-3/) . 

```python
async def add_template(self, prompts):
    async for prompt in prompts:

        new_prompt = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>"
        new_prompt += prompt.data.get_prompt() + "<|eot_id|>"
        new_prompt += "<|start_header_id|>assistant<|end_header_id|>"
```

## Integrate data sources

Plug relevant information from your relational database, knowledge graph, recommendation system, etc into your prompt.  

E.g. if you are building Q&A bot that answers questions about the document the user is viewing, pull the document title & summary from a database and insert it into the prompt.


