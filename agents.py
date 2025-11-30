# agents.py
import os
from dotenv import load_dotenv
from crewai import Agent
from tools import tool
from dotenv import load_dotenv
from crewai import LLM

# Load .env
load_dotenv()

# Initialize Gemini LLM
llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.4,
    verbose=True,
    api_key=os.getenv("GEMINI_API_KEY") 
)

# Define Researcher Agent
news_researcher = Agent(
    role="Senior Technology Researcher",
    goal="Continuously discover and analyze groundbreaking technologies in {topic}, providing actionable insights and summaries.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a highly curious and visionary researcher at the forefront of technological innovation. "
        "Your mission is to explore emerging technologies, analyze their potential impact, and generate "
        "clear, insightful, and engaging summaries that could inform and inspire others."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True  # communicate with other agents if needed
)

# Define Writer Agent
news_writer = Agent(
    role="Technology Storyteller",
    goal="Research, analyze, and narrate compelling tech stories about {topic}, making complex innovations accessible and engaging for readers.",
    verbose=True,
    memory=True,
    backstory=(
        "You have a talent for transforming complex technological concepts into captivating narratives. "
        "Your mission is to educate and inspire readers by presenting discoveries and innovations in a clear, "
        "engaging, and accessible manner, highlighting their significance and real-world impact."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
