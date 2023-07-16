# research-gpt
Automated Research. Powered by LoopGPT.

## What is this?
This is an experimental tool that uses OpenAI models and internet connectivity to automate research and produce reports.

## How do I use this?

```bash
pip uninstall loopgpt
git clone https://github.com/farizrahman4u/loopgpt.git
cd loopgpt
git checkout feature/ai-functions-dev
pip install -e .
cd ..
git clone https://github.com/FayazRahman/research-gpt.git
cd research-gpt
pip install -e .
cd ..
research --help
```

# Example usage

```bash
research "TOPIC" "my_research.txt" --mode short
```

```bash
research "TOPIC" "my_research.tex" --breadth 3 --depth 1 --latex
```
