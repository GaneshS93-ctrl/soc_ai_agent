from pydantic import BaseModel
from typing import List, Literal

class Finding(BaseModel):
    type: str
    severity: str
    description: str

class FindingsOutput(BaseModel):
    findings: List[Finding]

class ThreatOutput(BaseModel):
    malicious_ips: List[str]
    iocs: List[str]
    summary: str
    
class MalwareOutput(BaseModel):
    
    classification: str

    persistence: bool

    confidence: int

    explanation: str
    
class AttackChainOutput(BaseModel):
    stages: List[str]
    
class ResponseOutput(BaseModel):
    severity: str
    actions: List[str]
    
class ReportOutput(BaseModel):
    report: str
    
class RouteOutput(BaseModel):
    next_agent: Literal[
        "retrieval_agent",
        "log_agent",
        "threat_agent",
        "malware_agent",
        "attack_chain_agent",
        "response_agent",
        "action_agent",
        "report_agent"
    ]
    
class ActionStatus(BaseModel):
    action_status: str      
    
class Action(BaseModel):
    action: Literal[
        "Disable_accounts",
        "reset_credentials",
        "block_iocs",
        "block_hashes",
        "block_domain",
        "collect_forensic_evidence",
        "block_persistence",
        "monitor_lateral_movement",
        "unknown_action"
    ]  
    
    

