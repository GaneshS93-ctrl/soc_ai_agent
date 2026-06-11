from langchain.agents import create_agent

from llm import llm
from schemas import ActionStatus
from schemas import Action

from tools.tools import isolate_host, Disable_accounts, block_hashes, block_persistence, block_domain, collect_forensic_evidence, block_iocs, monitor_lateral_movement, reset_credentials, notify_to_relevant_stakeholders

system_prompt = """
        You are a action executor agent and uses tool calling to execute actions based on action.
        You use Findings, Threat, Malware and attach chain info to provide input for tool calling
        """

action_llm = create_agent(
            llm,
            tools=[
                isolate_host,
                Disable_accounts,
                reset_credentials,
                block_iocs,
                block_hashes,
                block_domain,
                collect_forensic_evidence,
                block_persistence,
                monitor_lateral_movement,
                notify_to_relevant_stakeholders
            ], system_prompt=system_prompt)


def action_agent(state):

    state["execution_path"].append("action_agent")
    
    actions = state["response_actions"]
    
    for action in actions:
        print(f"Executing action: {action}")
        
        user_prompt = {"messages": [{"role": "user", "content": f"""
        Findings:
        {state["findings"]}

        Threat:
        {state["threat_context"]}

        Malware:
        {state["malware_analysis"]}

        Attack Chain:
        {state["attack_chain"]}            

        Action:
        {action}
        """
        }]}
        
        result = action_llm.invoke(user_prompt)
        #print(f"Action Tool: {result}")
    
    state["action_status"] = "done"
        
    return {
        "action_status":
        "done"
    }



