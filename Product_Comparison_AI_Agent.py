from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_community.tools.tavily_search import TavilySearchResults
import os

os.environ["GROQ_API_KEY"] = GROQ_API_KEY
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY


llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.3,
)

search = TavilySearchResults(k=2)
tools = [
    Tool(
        name="Tavily Search",
        func=search.run,
        description="Useful for comparing products and getting live info",
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

agent.run("Compare wireless earphones under 2000 INR. Provide a short summary and suggest the best one.")
