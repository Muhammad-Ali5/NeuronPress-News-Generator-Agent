# tools.py
import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool  # installed package

load_dotenv()

# Set SERPER_API_KEY for SerperDevTool
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

# Initialize the tool
tool = SerperDevTool()
