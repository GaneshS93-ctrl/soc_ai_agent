from typing import TypedDict, List, Dict, Any

class SOCState(TypedDict):
    
    execution_path: List[str]

    logs: List[str]
    
    retrieved_docs: List          # list of plain text strings (not Document objects)

    sources: List[str]            # source filenames for citations

    findings: List[Dict[str, Any]]

    threat_context: Dict[str, Any]

    malware_analysis: Dict[str, Any]

    attack_chain: List[str]

    response_actions: List[str]
    
    actions: List[str]
    
    action_status: str

    report: str
    
    monitoring: Dict[str, Any]

    next_agent: str
    
    action_agent_latency: float
    threat_agent_latency: float
    retrieval_agent_latency: float
    log_agent_latency: float
    malware_agent_latency: float
    attack_chain_agent_latency: float
    response_agent_latency: float
    report_agent_latency: float
    Total_latency: float
    start_time: float
    