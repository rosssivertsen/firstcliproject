#!/usr/bin/env python3
"""
Test script for accessing Hugging Face models directly
Note: This requires downloading models from Hugging Face (can be large)
"""

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def test_huggingface_model():
    """
    Example of loading a model directly from Hugging Face
    Note: This will download the model on first run (can be several GB)
    """
    
    print("Loading model from Hugging Face...")
    print("-" * 50)
    
    # Using a smaller model for demonstration
    # For Qwen2.5-Coder, use: "Qwen/Qwen2.5-Coder-7B-Instruct"
    model_name = "Qwen/Qwen2.5-Coder-7B-Instruct"
    
    print(f"Model: {model_name}")
    print("Note: This will download the model on first run (7-14 GB)")
    print("Loading tokenizer...")
    
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        print("Loading model...")
        # Use device_map="auto" to automatically use GPU if available
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            device_map="auto"
        )
        
        print("Model loaded successfully!")
        print("-" * 50 + "\n")
        
        # Test prompt
        prompt = "Write Python code to calculate average of a list of numbers"
        
        print(f"Prompt: {prompt}\n")
        
        # Tokenize input
        inputs = tokenizer(prompt, return_tensors="pt")
        
        # Generate response
        print("Generating response...")
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.7,
            do_sample=True
        )
        
        # Decode response
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        print("\nResponse:")
        print(response)
        print("\n" + "-" * 50)
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nNote: If you see memory errors, try using a smaller model")
        print("or use Ollama instead (which handles memory management automatically)")


def test_pipeline():
    """
    Using Hugging Face pipelines (simpler API)
    """
    from transformers import pipeline
    
    print("\nTesting Hugging Face pipeline...")
    print("-" * 50)
    
    # Use a smaller model for demonstration
    model_name = "Qwen/Qwen2.5-Coder-0.5B-Instruct"  # Smaller model
    
    print(f"Model: {model_name}")
    print("Loading pipeline...")
    
    try:
        pipe = pipeline(
            "text-generation",
            model=model_name,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
        )
        
        print("Pipeline loaded successfully!")
        
        prompt = "Write a function to find the maximum value in a list"
        
        print(f"\nPrompt: {prompt}\n")
        
        response = pipe(
            prompt,
            max_new_tokens=150,
            temperature=0.7
        )
        
        print("Response:")
        print(response[0]['generated_text'])
        print("\n" + "-" * 50)
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nNote: Pipeline API requires model to be downloaded")


if __name__ == "__main__":
    print("Hugging Face Model Testing")
    print("=" * 50)
    print("\nIMPORTANT:")
    print("- This will download models from Hugging Face (7-14 GB)")
    print("- For most use cases, Ollama (test_ollama_local.py) is recommended")
    print("- Ollama handles memory management and model serving automatically")
    print("=" * 50 + "\n")
    
    # Uncomment to test:
    # test_huggingface_model()
    # test_pipeline()
    
    print("\nFor easier usage, use test_ollama_local.py instead!")
