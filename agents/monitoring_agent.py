import time
from datetime import datetime
from monitoring.logger import log_event


def monitoring_agent(state):

    state["execution_path"].append("monitoring_agent")

    # Calculate end-to-end latency
    state["Total_latency"] = round(time.time() - state.get("start_time"), 2)

    monitoring_data = {
        "timestamp":        datetime.fromtimestamp(round(state.get("start_time"), 2)),
        "agents_executed":  set(list(state["execution_path"])),
        "retrieval_latency":            state.get("retrieval_agent_latency"),
        "log_agent_latency":            state.get("log_agent_latency"),
        "malware_agent_latency":        state.get("malware_agent_latency"),
        "threat_agent_latency":         state.get("threat_agent_latency"),
        "attack_chain_agent_latency":   state.get("attack_chain_agent_latency"),
        "response_agent_latency":       state.get("response_agent_latency"),
        "action_agent_latency":         state.get("action_agent_latency"),
        "report_agent_latency":         state.get("report_agent_latency"),
        "latency_seconds":              state.get("Total_latency"),
        "sources_used":                 state.get("sources", []),
    }
    
    state["monitoring"] = monitoring_data

    # Persist to logs/execution.json (logger.py finally activated)
    log_event({
        "logs": state["logs"],
        **monitoring_data
    })

    return state