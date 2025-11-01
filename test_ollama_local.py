#!/usr/bin/env python3
"""
Test script for accessing Ollama models locally via Python
"""

import ollama

def test_qwen_coder():
    """Test Qwen2.5-Coder for data analytics tasks"""
    print("Testing Qwen2.5-Coder 14B via Ollama...")
    print("-" * 50)
    
    # Example 1: Generate pandas code
    prompt = "Write Python code using pandas to analyze sales data and calculate monthly revenue"
    
    print(f"Prompt: {prompt}\n")
    
    response = ollama.generate(
        model='qwen2.5-coder:14b',
        prompt=prompt
    )
    
    print("Response:")
    print(response['response'])
    print("\n" + "-" * 50 + "\n")


def test_streaming():
    """Test streaming responses for real-time output"""
    print("Testing streaming response...")
    print("-" * 50)
    
    prompt = "Write a SQL query to find customers who made purchases over $1000 in the last 30 days"
    
    print(f"Prompt: {prompt}\n")
    print("Response (streaming):")
    
    stream = ollama.generate(
        model='qwen2.5-coder:14b',
        prompt=prompt,
        stream=True
    )
    
    for chunk in stream:
        print(chunk['response'], end='', flush=True)
    
    print("\n" + "-" * 50 + "\n")


def test_chat():
    """Test chat interface for conversational interactions"""
    print("Testing chat interface...")
    print("-" * 50)
    
    messages = [
        {
            'role': 'user',
            'content': 'I have a CSV file with columns: date, product, quantity, price. How do I calculate total revenue per product using pandas?'
        }
    ]
    
    response = ollama.chat(
        model='qwen2.5-coder:14b',
        messages=messages
    )
    
    print("User:", messages[0]['content'])
    print("\nAssistant:", response['message']['content'])
    print("\n" + "-" * 50 + "\n")


def list_models():
    """List all available Ollama models"""
    print("Available Ollama models:")
    print("-" * 50)
    
    models = ollama.list()
    
    for model in models['models']:
        print(f"- {model.model} ({model.size / 1e9:.1f} GB)")
    
    print("-" * 50 + "\n")


if __name__ == "__main__":
    # List available models
    list_models()
    
    # Run tests
    # Uncomment the tests you want to run:
    
    # test_qwen_coder()
    # test_streaming()
    test_chat()
    
    print("\nTest completed successfully!")
