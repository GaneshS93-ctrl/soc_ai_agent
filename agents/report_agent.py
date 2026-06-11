from langchain_core.prompts import ChatPromptTemplate

from llm import llm
from schemas import ReportOutput

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
    Generate executive SOC report.

    Include:

    Summary
    Findings
    Attack Path
    Impact
    Actions
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

    Attack Chain:
    {attack_chain}

    Actions:
    {actions}
    """
    )
])

structured_llm = llm.with_structured_output(
    ReportOutput
)

def report_agent(state):

    state["execution_path"].append("report_agent")
    
    chain = prompt | structured_llm

    result = chain.invoke({
        "findings": state["findings"],
        "threat": state["threat_context"],
        "malware": state["malware_analysis"],
        "attack_chain": state["attack_chain"],
        "actions": state["response_actions"]
    })
    
    #print("report_agent Result:", result.report)

    return {
        "report":
        result.report
    }