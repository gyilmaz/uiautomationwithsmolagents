# Ottomator Agents - r1-distill-rag Style

This repository contains a sample project that integrates [smolagents](https://github.com/huggingface/smolagents) with a local or remote LLM to perform UI automation on Amazon. The project is inspired by the [r1-distill-rag repository](https://github.com/coleam00/ottomator-agents/tree/main/r1-distill-rag) from Ottomator Agents.

## Project Structure

```
ui_automation_agents/
├── .env
├── requirements.txt
├── config.py
├── local_llm.py
├── agent.py
├── web_browser_agent.py
└── main.py
```

- **.env**: Contains environment variables to configure the LLM provider.
- **requirements.txt**: Lists the required Python packages.
- **config.py**: Loads and exports configuration settings from the environment.
- **local_llm.py**: A local LLM wrapper using Hugging Face Transformers.
- **agent.py**: Defines functions to create the LLM instance and instantiate the SmolAgent with a WebBrowserTool.
- **web_browser_agent.py**: Contains the automation instructions for a multi-step Amazon test case.
- **main.py**: The main entry point that creates the agent, runs the test, and prints the result.

## File Contents

### 1. `.env`

Create a file named `.env` in your project root. Adjust the settings for your LLM provider as needed. For example, to use a local LLM (with Hugging Face Transformers) or OpenAI:

```dotenv
# .env

# Choose your LLM provider: "local" or "openai"
LLM_PROVIDER=local

# Settings for the local LLM (using Hugging Face Transformers)
LOCAL_MODEL_NAME=gpt2
LOCAL_DEVICE=cpu

# If using OpenAI instead, uncomment and fill in:
# LLM_PROVIDER=openai
# OPENAI_API_KEY=your_openai_api_key_here
```

## Installation and Setup

### Clone the Repository:

```bash
git clone <repository_url>
cd ui_automation_agents
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers:

```bash
playwright install
```

### Configure Environment Variables:

Update the `.env` file with your desired configuration. For example, to use a local LLM:

```dotenv
LLM_PROVIDER=local
LOCAL_MODEL_NAME=gpt2
LOCAL_DEVICE=cpu
```

Or, for OpenAI:

```dotenv
LLM_PROVIDER=openai
OPENAI_API_KEY=your_openai_api_key_here
```

## Running the Project

To run the project, execute:

```bash
python main.py
```

When executed, the agent will:

1. Launch a browser (using Playwright).
2. Navigate to Amazon.
3. Search for "laptop".
4. Extract product details (titles and prices) from the first three results.
5. Click on the second product to extract additional details (title, price, and customer reviews).
6. Print the combined result as a JSON-like summary.

## Customization

- **Local LLM (`local_llm.py`)**: Modify the generation parameters (e.g., `max_length`, `do_sample`, `top_k`, `top_p`) as needed.
- **Agent Creation (`agent.py`)**: Extend the logic to support additional LLM providers.
- **Web Browser Instructions (`web_browser_agent.py`)**: Adjust the instructions or CSS selectors if Amazon's UI changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **smolagents** for the underlying agent framework.
- **Ottomator Agents** for inspiration.





This is all separate I want a single file to copy


Markdown

# Ottomator Agents - r1-distill-rag Style

This repository contains a sample project that integrates [smolagents](https://github.com/huggingface/smolagents) with a local or remote LLM to perform UI automation on Amazon. The project is inspired by the [r1-distill-rag repository](https://github.com/coleam00/ottomator-agents/tree/main/r1-distill-rag) from Ottomator Agents.

## Project Structure

ui_automation_agents/
├── .env
├── requirements.txt
├── config.py
├── local_llm.py
├── agent.py
├── web_browser_agent.py
└── main.py


- **.env**: Contains environment variables to configure the LLM provider.
- **requirements.txt**: Lists the required Python packages.
- **config.py**: Loads and exports configuration settings from the environment.
- **local_llm.py**: A local LLM wrapper using Hugging Face Transformers.
- **agent.py**: Defines functions to create the LLM instance and instantiate the SmolAgent with a WebBrowserTool.
- **web_browser_agent.py**: Contains the automation instructions for a multi-step Amazon test case.
- **main.py**: The main entry point that creates the agent, runs the test, and prints the result.

## File Contents

### 1. `.env`

Create a file named `.env` in your project root. Adjust the settings for your LLM provider as needed. For example, to use a local LLM (with Hugging Face Transformers) or OpenAI:

```dotenv
# .env

# Choose your LLM provider: "local" or "openai"
LLM_PROVIDER=local

# Settings for the local LLM (using Hugging Face Transformers)
LOCAL_MODEL_NAME=gpt2
LOCAL_DEVICE=cpu

# If using OpenAI instead, uncomment and fill in:
# LLM_PROVIDER=openai
# OPENAI_API_KEY=your_openai_api_key_here
Installation and Setup
Clone the Repository:
Bash

git clone <repository_url>
cd ui_automation_agents
Install Dependencies:
Bash

pip install -r requirements.txt
Install Playwright Browsers:
Bash

playwright install
Configure Environment Variables: Update the .env file with your desired configuration. For example, to use a local LLM:
Code snippet

LLM_PROVIDER=local
LOCAL_MODEL_NAME=gpt2
LOCAL_DEVICE=cpu
Or, for OpenAI:

Code snippet

LLM_PROVIDER=openai
OPENAI_API_KEY=your_openai_api_key_here
Running the Project
To run the project, execute:

Bash

python main.py
When executed, the agent will:

Launch a browser (using Playwright).
Navigate to Amazon.
Search for "laptop".
Extract product details (titles and prices) from the first three results.
Click on the second product to extract additional details (title, price, and customer reviews).
Print the combined result as a JSON-like summary.
Customization
Local LLM (local_llm.py): Modify the generation parameters (e.g., max_length, do_sample, top_k, top_p) as needed.
Agent Creation (agent.py): Extend the logic to support additional LLM providers.
Web Browser Instructions (web_browser_agent.py): Adjust the instructions or CSS selectors if Amazon's UI changes.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
smolagents for the underlying agent framework.
Ottomator Agents for inspiration.
