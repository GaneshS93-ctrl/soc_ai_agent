import time
from langchain_core.prompts import ChatPromptTemplate

from llm import llm
from schemas import ThreatOutput


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
    You are a cyber threat intelligence expert.

    Review findings.

    Identify:
    - malicious infrastructure
    - IOC patterns
    - ransomware indicators

    """
    ),
    (
        "human",
        "{findings}"
    )
])

structured_llm = llm.with_structured_output(
    ThreatOutput
)

def threat_agent(state):
    
    state["execution_path"].append("threat_agent")
    start_time = time.time()

    chain = prompt | structured_llm

    result = chain.invoke({
        "findings": str(
            state["findings"]
        )
    })

    print("threat_agent Result:", result.model_dump(),"\n")
    state["threat_agent_latency"] = round(time.time() - start_time, 2)

    return {
        **state,
        "threat_context":
        result.model_dump()
    }

"""
Later you can replace this with:

VirusTotal
AbuseIPDB
OpenCTI
MISP

"""    