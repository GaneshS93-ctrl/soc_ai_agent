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
    "report": ""
}

result = graph.invoke(state)

print(f"{result['report']} \n")

stepstr = " -> ".join(result["execution_path"])
print(f"Execution Path: {stepstr} \n\n")