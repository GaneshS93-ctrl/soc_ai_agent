from graph import graph

state = {
    "execution_path":  [],
    "incident_id": "INC-001",
    "logs": [
        "Failed login from 185.22.10.2",
        "User \"admin\" failed login 500 times in 10 minutes.",
        "PowerShell execution detected"
    ],
    "retrieved_docs" : [],          
    "sources":[],       
    "findings": [],
    "threat_context": {},
    "malware_analysis": {},
    "attack_chain": [],
    "response_actions": [],
    "actions": [],
    "action_status": "",
    "report": "",
    "monitoring": {},
    "action_agent_latency": 0.0,
    "threat_agent_latency": 0.0,
    "retrieval_agent_latency": 0.0,
    "log_agent_latency": 0.0,
    "malware_agent_latency": 0.0,
    "attack_chain_agent_latency": 0.0,
    "response_agent_latency": 0.0,
    "report_agent_latency": 0.0,
    "monitoring_agent_latency": 0.0,
    "Total_latency": 0.0,
    "start_time": 0.0    
}

result = graph.invoke(state)

print(f"{result['report']} \n")

stepstr = " -> ".join(result["execution_path"])
print(f"Execution Path: {stepstr} \n\n")