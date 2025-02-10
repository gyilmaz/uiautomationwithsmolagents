import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "dashscope")

    # DashScope API Configuration (Alibaba Cloud)
    DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
    DASHSCOPE_API_URL = os.getenv("DASHSCOPE_API_URL", "https://dashscope-intl.aliyuncs.com/compatible-mode/v1")
    
    # Qwen Model Name
    LOCAL_MODEL_NAME = os.getenv("LOCAL_MODEL_NAME", "qwen-max")

config = Config()

