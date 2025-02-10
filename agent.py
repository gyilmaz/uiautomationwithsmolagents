import asyncio
from smolagents import CodeAgent, VisitWebpageTool
from config import config

def create_llm():
    if config.LLM_PROVIDER == "local":
        # Import our local LLM wrapper for Hugging Face models
        from local_llm import LocalLLM
        return LocalLLM(model_name_or_path=config.LOCAL_MODEL_NAME, device=config.LOCAL_DEVICE)

    elif config.LLM_PROVIDER == "dashscope":
        # Import Qwen API wrapper for DashScope
        from local_llm import DashScopeLLM
        if not config.DASHSCOPE_API_KEY:
            raise ValueError("DASHSCOPE_API_KEY is not set in your environment.")
        return DashScopeLLM(
            api_key=config.DASHSCOPE_API_KEY,
            base_url=config.DASHSCOPE_API_URL
        )

    else:
        raise ValueError(f"Unsupported LLM_PROVIDER: {config.LLM_PROVIDER}")

async def create_agent():
    llm = create_llm()
    # Initialize the WebBrowserTool.
    browser_tool = VisitWebpageTool()
    
    # Create the CodeAgent with the selected LLM and browser tool.
    agent = CodeAgent(model=llm, tools=[browser_tool], additional_authorized_imports=['requests', 'markdownify'])
    return agent, browser_tool
