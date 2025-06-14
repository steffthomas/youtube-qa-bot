import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

# Load API key from .env file
load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# Initialize LLM using LLaMA 3.3 70B Instruct (Free)
llm = ChatOpenAI(
    model_name="meta-llama/llama-3.3-70b-instruct:free",
    openai_api_key=openrouter_api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.3
)

def summarize_text(text: str) -> str:
    """
    Summarize the full transcript using LLaMA 3.3 70B via OpenRouter.
    """
    prompt = f"""
    Summarize the following YouTube video transcript in 5-6 short bullet points:

    {text[:4000]}  # truncated for token limit safety

    Summary:
    """

    response = llm.predict(prompt)
    return response
