# -*- coding: utf-8 -*-
import transformers
import torch
import ollama

# model_id = "meta-llama/Meta-Llama-3.1-8B"
#
# pipeline = transformers.pipeline("text-generation")
# pipeline.save_pretrained(model_id)
#
# pipeline("Hey how are you doing today?")

response = ollama.chat(model='llama3.1:8b', messages=[
    {
        'role': 'user',
        # 'content': 'Why is the sky blue?',
        'content': '하늘이 푸른 이유는?',
    },
])
# print(response['message']['content'])
print(response)
