<div align="center">
<img src="https://avatars.githubusercontent.com/u/130713213?s=200&v=4" width="110"><img src="https://huggingface.co/lamini/instruct-peft-tuned-12b/resolve/main/Lamini_logo.png?max-height=110" height="110">
</div>

# Finetuning Llama 3

It's easy to finetue Llama 3 on the question & answer dataset we just created.

```bash
./scripts/train.sh
```

The python is as follows:

```python
from lamini import Lamini

import jsonlines


def main():
    llm = Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")

    dataset = list(load_training_data())

    llm.train(data=dataset,)


def load_training_data():
    path = "/app/lamini-earnings-sdk/data/generated_q_a.jsonl"

    limit = 100

    with jsonlines.open(path) as reader:
        for index, obj in enumerate(reader):
            if index >= limit:
                break

            header = "<|begin_of_text|><|start_header_id|>user<|end_header_id|>"
            header_end = "<|eot_id|><|start_header_id|>assistant<|end_header_id|>"

            yield {
                "input": header + make_question(obj) + header_end,
                "output": obj["answer"] + "<|eot_id|>",
            }


def make_question(obj):
    question = (
        f"Consider the following company: {obj['ticker']} and quarter: {obj['q']}. "
    )
    question += obj["question"]
    return question


main()
```

# Monitoring your job

After you submit a training job, it is scheduled on the cluster. You can monitor the progress of the job by visiting the link provided in the output of the training script.

```bash
python3 /app/lamini-earnings-sdk/06_fine_tuning/scripts/../train.py

Uploading data....
Upload to blob completed for data.
Data pairs uploaded to blob.

Your dataset id is: 0713f8cfa5746a0897079e7f249a048deb653cf7e849d6fc26f3d2dacc5722d0 . Consider using this in the future to train using the same data.
Eg: llm.train(dataset_id='0713f8cfa5746a0897079e7f249a048deb653cf7e849d6fc26f3d2dacc5722d0')
Training job submitted! Check status of job 6367 here: https://app.lamini.ai/train/6367
```

The page lets you monitor all of your jobs, view eval results, view loss curves, and logs.  Jobs will automatically use all of the GPUs in your Lamini cluster.

![image](https://github.com/lamini-ai/lamini-earnings-sdk/assets/3401278/f7db9547-88d1-4983-8217-f21c3a3f3da0)

