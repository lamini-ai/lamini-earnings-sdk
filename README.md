<div align="center">
<img src="https://avatars.githubusercontent.com/u/130713213?s=200&v=4" width="110"><img src="https://huggingface.co/lamini/instruct-peft-tuned-12b/resolve/main/Lamini_logo.png?max-height=110" height="110">
</div>
<div align="center">

[![Latest Release](https://img.shields.io/badge/Latest%20Version-1.4.3-blue?logo=github)](https://github.com/lamini-ai/lamini-sdk/commits/main)
[![GitHub License](https://img.shields.io/github/license/lamini-ai/lamini)](https://github.com/lamini-ai/lamini-sdk/blob/main/LICENSE)</div>

## Lamini SDK

In this SDK, we include tutorials for achieving high-quality results with Language Models (LLMs) like Llama3 using Lamini.</br>  With Lamini, you own the LLM you create -- you can deploy it or release it open source.</br>  This SDK teaches effective tools for building LLMs.</br>  We strongly encourage following the SDK *in order* as the concepts build on each other and are sorted by difficulty.

### Table of Contents

1. [Llama3](01_llama3/README.md) - generate text with Llama3, a powerful LLM.
2. [Eval](02_eval/README.md) - evaluate the quality of your LLM.
3. [Prompt Tuning](03_prompt_tuning/README.md) - improve the quality of your LLM by tuning the prompts you use.
4. [RAG Tuning](04_rag_tuning/README.md) - improve the quality of your LLM by tuning the retrieval component.
5. [Data Pipeline](05_data_pipeline/README.md) - prepare your data for training an LLM.
6. [Fine Tuning](06_fine_tuning/README.md) - fine tune an LLM on your data.

### Notes

The goal of this SDK is to teach and provide examples of important tools for building LLMs.</br>  The examples emphasize simplicitly and readibility, not heavy optimization.</br>  Once you have mastered a module from this SDK, consider forking it and adapting it to your own application.</br>  All of the code in this repository is licensed Apache 2. You are free to use it for any purpose including commercial applications.

### Application

This SDK follows an earnings call application where we use an LLM to answer analyst questions
about earnings calls from public companies.

### Installation Instructions

Before you start, please get your Lamini API key and install the python library.

First, get `<YOUR-LAMINI-API-KEY>` at https://app.lamini.ai/account.
Add the key as an environment variable.
```
export LAMINI_API_KEY="<YOUR-LAMINI-API-KEY>"
```

Next, install the Python library.
```
pip install --upgrade lamini
```

### GitHub Repository
---
The source code for SDK can be found on GitHub at [lamini-ai/lamini-earnings-sdk](https://github.com/lamini-ai/lamini-earnings-sdk). Feel free to explore and contribute!

### About Lamini
---
Lamini is the LLM platform for developers to specialize LLMs on their own data and infrastructure: easier, faster, and better than any LLM for their use case.</br> Our mission is to build customizable superintelligence that anyone can build and own.

---

</div>
<div align="center">

![GitHub forks](https://img.shields.io/github/forks/lamini-ai/lamini-sdk) &ensp; © Lamini &ensp; ![GitHub stars](https://img.shields.io/github/stars/lamini-ai/lamini-sdk)

</div>

--------

