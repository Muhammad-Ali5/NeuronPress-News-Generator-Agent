# task.py
from crewai import Task
from tools import tool
from agents import news_researcher, news_writer

# Research Task
research_task = Task(
    description=(
        "Investigate and identify the next major trend in {topic}. "
        "Analyze its advantages, drawbacks, market potential, and potential risks. "
        "Your report should provide a clear narrative, actionable insights, and highlight key developments in the field."
    ),
    expected_output=(
        "A comprehensive report, approximately 3 paragraphs long, summarizing the latest trends, "
        "key innovations, and their implications for the industry."
    ),
    tools=[tool],
    agent=news_researcher,
)

# Writer Task
write_task = Task(
    description=(
        "Create an engaging and informative article on {topic}. "
        "Focus on recent trends, key innovations, and their impact on the industry. "
        "The article should be easy to read, educational, and highlight the significance of these advancements."
    ),
    expected_output=(
        "A 4-paragraph article on {topic} advancements, formatted in Markdown, suitable for publication."
    ),
    tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)
