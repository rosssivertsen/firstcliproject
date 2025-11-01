# Local AI Model Usage Guide

## Overview

This project is set up to use local AI models for data analytics and code generation tasks.

## Installed Models

### Via Ollama:
- **qwen2.5-coder:14b** (9.0 GB) - Best for data analytics and code generation
- **codellama:7b** (3.8 GB) - Specialized for coding tasks
- **llama3.2** (2.0 GB) - General purpose model

## Quick Start

### 1. Command Line Usage

**Basic query:**
```bash
ollama run qwen2.5-coder:14b "Write pandas code to analyze sales data"
```

**Interactive mode:**
```bash
ollama run qwen2.5-coder:14b
```

### 2. Python Usage

**Run the test script:**
```bash
python3 test_ollama_local.py
```

**Basic Python example:**
```python
import ollama

response = ollama.generate(
    model='qwen2.5-coder:14b',
    prompt='Write SQL to find top 10 customers by revenue'
)

print(response['response'])
```

**Chat interface:**
```python
import ollama

messages = [
    {'role': 'user', 'content': 'How do I merge two pandas DataFrames?'}
]

response = ollama.chat(
    model='qwen2.5-coder:14b',
    messages=messages
)

print(response['message']['content'])
```

**Streaming responses:**
```python
import ollama

stream = ollama.generate(
    model='qwen2.5-coder:14b',
    prompt='Explain data normalization',
    stream=True
)

for chunk in stream:
    print(chunk['response'], end='', flush=True)
```

## Data Analytics Use Cases

### 1. Pandas Code Generation
```bash
ollama run qwen2.5-coder:14b "Write pandas code to:
1. Load CSV file
2. Clean missing values
3. Calculate monthly averages
4. Create pivot table"
```

### 2. SQL Query Generation
```bash
ollama run qwen2.5-coder:14b "Write SQL query to find customers with orders over \$1000 in the last 30 days"
```

### 3. Data Visualization
```bash
ollama run qwen2.5-coder:14b "Create matplotlib code for a time series visualization with sales data"
```

### 4. Statistical Analysis
```bash
ollama run qwen2.5-coder:14b "Write Python code to perform linear regression analysis on sales vs advertising spend"
```

## Installed Python Libraries

All necessary libraries are installed:
- `ollama` - Python client for Ollama
- `transformers` - Hugging Face transformers
- `torch` - PyTorch for deep learning
- `accelerate` - Hardware acceleration
- `bitsandbytes` - Model quantization
- `sentencepiece` - Tokenization

## Ollama Commands

**List models:**
```bash
ollama list
```

**Show running models:**
```bash
ollama ps
```

**Pull new model:**
```bash
ollama pull <model-name>
```

**Remove model:**
```bash
ollama rm <model-name>
```

**Show model info:**
```bash
ollama show qwen2.5-coder:14b
```

## Recommended Models for Different Tasks

### Data Analytics (Best):
- `qwen2.5-coder:14b` - Excellent for Python/pandas/SQL

### General Coding:
- `codellama:7b` - Good for general programming

### Data Science:
- `qwen2.5-coder:14b` - Statistical analysis, ML code

### SQL:
- `qwen2.5-coder:14b` - Complex query generation

## API Access

Ollama runs a local API server on `localhost:11434`

**cURL example:**
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "qwen2.5-coder:14b",
  "prompt": "Write a function to calculate mean"
}'
```

**Python requests:**
```python
import requests
import json

response = requests.post(
    'http://localhost:11434/api/generate',
    json={
        'model': 'qwen2.5-coder:14b',
        'prompt': 'Write pandas code for data cleaning'
    }
)

print(response.json()['response'])
```

## Hugging Face Direct Access

For more control, you can access models directly from Hugging Face:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_name = "Qwen/Qwen2.5-Coder-7B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

inputs = tokenizer("Write a sorting function", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=200)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
```

**Note:** Direct Hugging Face access downloads models separately (7-14 GB each)

## Performance Tips

1. **Use streaming** for long responses to get immediate feedback
2. **Adjust temperature** (0.1-1.0) for creativity vs consistency
3. **Set max_tokens** to control response length
4. **Use chat mode** for multi-turn conversations
5. **Cache responses** to avoid regenerating identical queries

## Troubleshooting

**Ollama not responding:**
```bash
# Check if Ollama is running
ollama ps

# Restart Ollama
killall ollama
ollama serve
```

**Python import errors:**
```bash
pip3 install --upgrade ollama transformers torch
```

**Memory issues:**
- Use smaller models (7B instead of 14B)
- Close other applications
- Use quantized models

## Example Projects

See `test_ollama_local.py` for working examples of:
- Basic generation
- Streaming responses
- Chat interface
- Model listing

## Additional Resources

- Ollama Documentation: https://github.com/ollama/ollama
- Qwen2.5-Coder: https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct
- Transformers: https://huggingface.co/docs/transformers

---

**All models run locally - no internet required after initial download!**
