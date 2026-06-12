from langgraph.graph import StateGraph, END

from state import SOCState

from agents.supervisor import supervisor
from agents.log_agent import log_agent
from agents.threat_agent import threat_agent
from agents.malware_agent import malware_agent
from agents.attack_chain_agent import attack_chain_agent
from agents.response_agent import response_agent
from agents.report_agent import report_agent
from agents.action_agent import action_agent
from agents.retrieval_agent import retrieval_agent
from agents.monitoring_agent import monitoring_agent    

def router(state):
    
    nxt = state["next_agent"]
    
    if nxt == "retrieval_agent":
        return "retrieval_agent"    

    if nxt == "log_agent":
        return "log_agent"

    if nxt == "threat_agent":
        return "threat_agent"

    if nxt == "malware_agent":
        return "malware_agent"

    if nxt == "attack_chain_agent":
        return "attack_chain_agent"

    if nxt == "response_agent":
        return "response_agent"

    if nxt == "action_agent":
        return "action_agent"

    return "report_agent"

builder = StateGraph(SOCState)

builder.add_node("supervisor", supervisor)
builder.add_node("retrieval_agent", retrieval_agent)
builder.add_node("log_agent", log_agent)
builder.add_node("threat_agent", threat_agent)
builder.add_node("malware_agent", malware_agent)
builder.add_node("attack_chain_agent", attack_chain_agent)
builder.add_node("response_agent", response_agent)
builder.add_node("action_agent", action_agent)
builder.add_node("report_agent", report_agent)
builder.add_node("monitoring_agent", monitoring_agent)

builder.set_entry_point("supervisor")

builder.add_conditional_edges(
    "supervisor",
    router
)

builder.add_edge("retrieval_agent", "supervisor")

builder.add_edge("log_agent", "supervisor")

builder.add_edge("threat_agent","supervisor")

builder.add_edge("malware_agent","supervisor")

builder.add_edge("attack_chain_agent","supervisor")

builder.add_edge("response_agent","supervisor")

builder.add_edge("action_agent","supervisor")

builder.add_edge("report_agent","monitoring_agent")

builder.add_edge("monitoring_agent",  END)

graph = builder.compile()