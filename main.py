# main.py
import asyncio
from agent import create_agent

async def main():
    agent, _ = await create_agent()
    
    task = (
        "Automate a web browsing test on Amazon:\n"
        "1. Visit https://www.amazon.com\n"
        "2. Search for 'laptop'\n"
        "3. Extract details of top 3 results (title, price)\n"
        "4. Click on second result\n"
        "5. Extract product details (title, price, reviews)"
    )
    
    result = agent.run(task)
    print("Test Results:")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
