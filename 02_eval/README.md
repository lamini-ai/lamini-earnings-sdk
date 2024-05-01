<div align="center">
<img src="https://avatars.githubusercontent.com/u/130713213?s=200&v=4" width="110"><img src="https://huggingface.co/lamini/instruct-peft-tuned-12b/resolve/main/Lamini_logo.png?max-height=110" height="110">
</div>

# Eval

It is important to evaluate the performance of your LLM using a single metric.
This allows you to quickly iterate on prompts, rag, and fientuned models.

## Creating a test set

Create a test set by selecting a set of prompts and their corresponding answers.

We include an example test set at (./data/golden_test_set.jsonl)[./data/golden_test_set.jsonl].

```json
{"ticker": "CENT", "date": "Aug 4, 2021, 4:35 p.m. ET", "q": "2021-Q3", "question": "What is the optimal leverage range for the company in the event of M&A", "answer": " The optimal leverage range for the company in the event of M&A is between 3 to 3.5 times. For the right deal, the company would be willing to lever up into the low 4s, and then quickly deliver back down to that three to 3.5 range.", "has_value": true, "value": 3.5, "units": "times"}
```

In addition to a custom test set, you can also use standard metrics to evaluate your model.

## Standard metrics


The Helm LLm benchmark is a popular benchmark for evaluating the performance of large language models (LLMs) in natural language processing tasks. It's a suite of tests that assess the language understanding and generation capabilities of a model.

The Helm LLm benchmark consists of a set of tasks that evaluate a model's ability to:

1. Answer questions: The model is asked to answer questions based on a given passage or text.
2. Generate text: The model is asked to generate text based on a prompt or topic.
3. Summarize text: The model is asked to summarize a given passage or text.
4. Fill in the blanks: The model is asked to fill in the blanks in a sentence or paragraph with the most likely word or phrase.

The Helm LLm benchmark is designed to test a model's ability to understand and generate human-like language, and it's widely used in the natural language processing (NLP) community to evaluate the performance of LLMs.

The benchmark is named after the Helm framework, which is an open-source toolkit for building and evaluating LLMs. The Helm LLm benchmark is a valuable tool for researchers and developers to evaluate the performance of their models and compare them to others in the field.

