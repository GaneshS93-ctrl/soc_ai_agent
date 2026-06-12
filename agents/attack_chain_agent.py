import time
from langchain_core.prompts import ChatPromptTemplate
from llm import llm
from schemas import AttackChainOutput

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
    You are an incident responder.

    Map findings to attack stages.

    Examples:

    Initial Access
    Execution
    Persistence
    Privilege Escalation
    Defense Evasion
    Credential Access
    Discovery
    Lateral Movement
    Command and Control
    Exfiltration
    """
        ),
        (
            "human",
            """
    Findings:
    {findings}

    Threat:
    {threat}

    Malware:
    {malware}
    """
    )
])

structured_llm = llm.with_structured_output(
    AttackChainOutput
)

def attack_chain_agent(state):

    state["execution_path"].append("attack_chain_agent")
    start_time = time.time()
    
    chain = prompt | structured_llm

    result = chain.invoke({
        "findings": state["findings"],
        "threat": state["threat_context"],
        "malware": state["malware_analysis"]
    })
    print("Attack Chain Result:", result.stages)
    state["attack_chain_agent_latency"] = round(time.time() - start_time, 2)
        
    return {
        **state,
        "attack_chain":
        result.stages
    }