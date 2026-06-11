from langchain_core.prompts import ChatPromptTemplate

from llm import llm
from schemas import ResponseOutput

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
    You are a SOC incident responder.

    Recommend actions.

    Examples:

    - isolate host
    - disable account
    - reset credentials
    - block IOC
    - monitor
    """
    ),
    (
        "human",
        "{attack_chain}"
    )
])

structured_llm = llm.with_structured_output(
    ResponseOutput
)

def response_agent(state):

    state["execution_path"].append("response_agent")
    
    chain = prompt | structured_llm

    result = chain.invoke({
        "attack_chain":
        state["attack_chain"]
    })
    
    print("response_agent Result:", result.actions,"\n")

    return {
        "response_actions":
        result.actions
    }