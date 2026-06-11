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

    next_agent: str