from langchain_core.tools import tool

@tool
def isolate_host(user: str) -> dict:
    """Isolate the host of a given employee.
    Returns employee name, device model, and serial number."""
    
    print(f"host of user {user} has been isolated.")
    
    return {
        "employee": user,
        "device": "Dell Latitude",
        "serial": "DL123456"
    }

@tool
def Disable_accounts(user: str) -> dict:
    """Disable the account of a given employee.
    Returns employee name, device model, and serial number."""
    
    print(f"Account for user {user} has been disabled.")
    
    return {
        "employee": user,
        "device": "Dell Latitude",
        "serial": "DL123456"
    }
    
@tool
def reset_credentials(user: str) -> dict:
    """Reset the credentials of a given employee.
    Returns employee name, device model, and serial number."""
    
    print(f"Credentials for user {user} have been reset.")
    
    return {
        "employee": user,
        "device": "Dell Latitude",
        "serial": "DL123456"
    }
    
@tool
def block_iocs(ip_addr: str) -> dict:
    """Blocks iocs."""
    
    print(f"IOCs for IP address {ip_addr} have been blocked.")  
    
    return {
        "ip_addr": ip_addr,
        "status": "blocked"
    }
    
@tool
def block_hashes() -> dict:
    """Blocks hashes."""
    
    print(f"Hashes have been blocked.")
    
    return {
        "status": "hash blocked"
    }
    
@tool
def block_domain(domain_ipaddr: str) -> dict:
    """Blocks a domain."""
    
    print(f"Domain {domain_ipaddr} has been blocked.")
    
    return {
        "domain_ipaddr": domain_ipaddr,
        "status": "blocked"
    }
    
@tool
def collect_forensic_evidence() -> dict:
    """Collects forensic evidence."""
    print(f"Forensic evidence has been collected.")
    return {
        "status": "evidence collected"
    }
    
@tool
def block_persistence() -> dict:
    """Blocks a persistence mechanism."""
    print(f"Persistence mechanism has been blocked.")
    return {
        "status": "persistence blocked"
    }
    
@tool
def monitor_lateral_movement() -> dict:
    """Monitors lateral movement."""
    print(f"Lateral movement has been monitored.")
    return {
        "status": "lateral movement monitored"
    }
    
@tool
def notify_to_relevant_stakeholders():
    """Notifies relevant stakeholders."""
    print(f"Emailing relevant stakeholders all findings...")
    return {
        "status": "stakeholders notified"
    }    