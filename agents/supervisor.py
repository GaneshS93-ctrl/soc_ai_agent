from langchain_core.prompts import ChatPromptTemplate
from llm import llm
from schemas import RouteOutput

router_llm = llm.with_structured_output(
    RouteOutput
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are SOC workflow orchestrator. Choose next agent from among categories:
["log_agent", "threat_agent", "malware_agent", "attack_chain_agent", "response_agent", "report_agent"]

Choose next agent.
"""
    ),
    (
        "human",
        "{state}"
    )
])

def supervisor(state):
    
    state["execution_path"].append("supervisor")
    
    if not state.get("retrieved_docs"):
        return {
            "next_agent": "retrieval_agent"
        }    
    
    if not state.get("findings"):
        return {
            "next_agent": "log_agent"
        }

    if not state.get("threat_context"):
        return {
            "next_agent": "threat_agent"
        }

    if not state.get("malware_analysis"):
        return {
            "next_agent": "malware_agent"
        }

    if not state.get("attack_chain"):
        return {
            "next_agent": "attack_chain_agent"
        }

    if not state.get("response_actions"):
        return {
            "next_agent": "response_agent"
        }
        
    if not state.get("action_status"):
        return {
            "next_agent": "action_agent"
        }

    
    return {
        "next_agent": "report_agent"
    }

