# TechTrend Scout

**TechTrend Scout** is an intelligent agent crew designed to research and write engaging articles about emerging technology trends. Powered by CrewAI and Gemini, it automates the process of discovering groundbreaking technologies and transforming complex concepts into accessible narratives.

## Features

-   **Senior Technology Researcher**: Discovers and analyzes emerging technologies, providing actionable insights.
-   **Technology Storyteller**: Crafts compelling and educational articles based on the research.
-   **Automated Workflow**: Seamlessly coordinates research and writing tasks using CrewAI's sequential process.
-   **Powered by Gemini**: Utilizes Google's Gemini 2.0 Flash model for high-quality generation.

## Prerequisites

-   Python 3.10 or higher
-   [Gemini API Key](https://aistudio.google.com/)
-   [Serper API Key](https://serper.dev/) (for Google Search capabilities)

## Installation

1.  **Clone the repository** (if applicable) or navigate to the project directory.

2.  **Install dependencies**:
    ```bash
    pip install crewai crewai-tools langchain-google-genai python-dotenv pydantic litellm
    ```

3.  **Configure Environment Variables**:
    Create a `.env` file in the root directory and add your API keys:
    ```env
    GEMINI_API_KEY=your_gemini_api_key_here
    SERPER_API_KEY=your_serper_api_key_here
    ```

4.  **Google Cloud Credentials**:
    Ensure you have your Google Cloud service account JSON file (e.g., `crewai-gemini.json`) in the project directory.

## Usage

To run the agent crew and generate a blog post:

1.  Open your terminal or command prompt.
2.  Navigate to the project directory.
3.  Run the script:
    ```bash
    python crew.py
    ```

By default, the crew researches "Future of AI in Medical". You can change the topic in `crew.py`:

```python
results = crew.kickoff(inputs={"topic": "Your Topic Here"})
```

## Output

The generated article will be saved as `new-blog-post.md` in the project directory.

## Project Structure

-   `agents.py`: Defines the Researcher and Writer agents.
-   `task.py`: Defines the specific tasks for each agent.
-   `tools.py`: Configures the search tool (Serper).
-   `crew.py`: Orchestrates the agents and tasks.
-   `.env`: Stores sensitive API keys.
