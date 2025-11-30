# crew.py
from crewai import Crew, Process
from agents import news_researcher, news_writer
from task import research_task, write_task

# Define the crew with agents and tasks
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    processes=Process.sequential  # tasks run sequentially
)

# Start the crew execution with a specific topic
results = crew.kickoff(inputs={"topic": "Future of AI in Medical"})
print(results)
