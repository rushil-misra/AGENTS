from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun
from langchain_community.chat_models import ChatOllama
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=400))




arxiv_wrapper=ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv=ArxivQueryRun(api_wrapper=arxiv_wrapper)


tools = [wiki,arxiv]


llm=ChatOllama(model="llama2")
llm

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are simple assistant. answer in 100 words maximum",
        ),
        ("user", "tell me in short about {input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
agent=create_openai_tools_agent(llm,tools,prompt)

def agent_run(input_text):
    agent_executor=AgentExecutor(agent=agent,tools=tools,verbose=True)
    respond = agent_executor.invoke({"input":input_text})
    return respond

