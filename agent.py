import asyncio
from smolagents import SmolAgent
from smolagents import WebBrowserTool
from config import LLM_PROVIDER, LOCAL_MODEL_NAME, LOCAL_DEVICE, DASHSCOPE_API_KEY, DASHSCOPE_API_URL

def create_llm():
    if LLM_PROVIDER == "local":
        # Import our local LLM wrapper for Hugging Face models
        from local_llm import LocalLLM
        return LocalLLM(model_name_or_path=LOCAL_MODEL_NAME, device=LOCAL_DEVICE)

    elif LLM_PROVIDER == "dashscope":
        # Import Qwen API wrapper for DashScope
        from local_llm import DashScopeLLM
        if not DASHSCOPE_API_KEY:
            raise ValueError("DASHSCOPE_API_KEY is not set in your environment.")
        return DashScopeLLM()

    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")

async def create_agent():
    llm = create_llm()
    # Initialize the WebBrowserTool.
    # Set headless=True to run the browser in the background.
    browser_tool = await WebBrowserTool.create(headless=False)
    
    # Create the SmolAgent with the selected LLM and browser tool.
    agent = SmolAgent(llm=llm, tools=[browser_tool])
    
    return agent, browser_tool
