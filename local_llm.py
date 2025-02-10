# local_llm.py
import asyncio
import httpx
from transformers import AutoTokenizer, AutoModelForCausalLM

class LocalLLM:
    def __init__(self, model_name_or_path="gpt2", device="cpu"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_name_or_path)
        self.device = device
        self.model.to(device)
    
    async def complete(self, prompt: str) -> str:
        # Offload the synchronous inference to a separate thread.
        return await asyncio.to_thread(self._complete_sync, prompt)
    
    def _complete_sync(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            **inputs,
            max_length=256,
            do_sample=True,
            top_k=50,
            top_p=0.95,
        )
        # Decode generated tokens
        completion = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return completion

class ChatMessage:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

class DashScopeLLM:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/") + "/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def __call__(self, messages: list[dict], **kwargs) -> dict:
        # Run async operation in a separate thread
        future = asyncio.run_coroutine_threadsafe(self._complete(messages), asyncio.get_event_loop())
        return future.result()
    
    async def _complete(self, messages: list[dict]) -> ChatMessage:
        async with httpx.AsyncClient() as client:
            payload = {
                "model": "qwen-max",
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 256
            }
            response = await client.post(
                self.base_url,
                headers=self.headers,
                json=payload
            )
            if response.status_code == 200:
                data = response.json()
                return ChatMessage(
                    role="assistant",
                    content=data['choices'][0]['message']['content']
                )
            else:
                raise Exception(f"Error from DashScope API: {response.status_code} - {response.text}")
