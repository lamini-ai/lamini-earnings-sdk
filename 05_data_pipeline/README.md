<div align="center">
<img src="https://avatars.githubusercontent.com/u/130713213?s=200&v=4" width="110"><img src="https://huggingface.co/lamini/instruct-peft-tuned-12b/resolve/main/Lamini_logo.png?max-height=110" height="110">
</div>

# Data Pipelines

We can leverage Llama 3 to build data pipelines. Llama 3 can read english and
reason over it. We can use this capability to build data pipelines by inserting
calls to the LLM to perform data transformations.

Run the follow script to have Llama 3 read through earnings calls, pretend to
be a financial analyst, and ask relevant questions, and answer them using the
source text.

```bash
./scripts/generate-data.sh
```

```json
{
  "company": "WPP",
  "question": "What is the percentage growth rate of WPP's business in Germany in Q1, according to Mark Read?",
  "answer": "16%"
}
{
  "company": "GDOT",
  "question": "What is the size of the asset size that GDOT aims to maintain to protect its revenue",
  "answer": "According to the transcript, GDOT aims to maintain an asset size of $10 billion or less to protect its revenue"
}

```




