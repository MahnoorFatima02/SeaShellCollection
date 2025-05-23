import httpx
import os
from fastapi import HTTPException

async def get_response_from_llm(prompt: str) -> dict:
    hf_token = os.environ.get("SEA_SHELL_HUGGING_TOKEN")
    if not hf_token:
        raise HTTPException(status_code=500, detail="Hugging Face token not set in environment.")
    
    model = "gpt2"    
    url = f"https://api-inference.huggingface.co/models/{model}"
    headers= {
        "Authorization": f"Bearer {hf_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": prompt,
        "options": {"wait_for_model": True},
        "parameters": {"max_new_tokens": 50}
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            print("Hugging Face API error:", response.text)
            raise HTTPException(status_code=500, detail=f"Hugging Face API error: {response.text}")
        
        data = response.json()
        
        # Response is a list of dicts with 'generated_text' keys
        if isinstance(data, list) and "generated_text" in data[0]:
            return {"generated_text": data[0]["generated_text"]}
        
        return {"generated_text": "No suggestion"}