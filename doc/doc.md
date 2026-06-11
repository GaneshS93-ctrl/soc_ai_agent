# Multi-Agent Cybersecurity SOC
    A Multi-Agent Cybersecurity SOC (Security Operations Center) is an AI system where 
    multiple specialized agents work together like a real security team to detect, 
    investigate, and respond to cyber threats.

## Concept: Simulate a Security Operations Center with specialized AI analysts.

# Agents
* RAG retrieval agent
* Log Analysis Agent
* Threat Intelligence Agent
* Malware Analysis Agent
* Attack chain Agent
* Incident Response Agent
* Action Agent
* Report Generation Agent

# Workflow:

* Logs arrive
* Knowledge database is consulted for logs
* Agents investigate independently
* Debate findings
* Takes Action autonomously
* Produce incident report

## High-Level Architecture

                    Security Events
                           ¦
                           v
                   Knowledge Database retrieval  
                           ¦
                           v
                 SOC Coordinator Agent (Supervisor)
                 /      |           |           \
                /       |           |            \
               v        v           v             v
       Log Agent  Threat Agent  Malware Agent  Attack Chain Agent
               \        |        /            /
                \       |       /            /
                 \      |     /             /
                  \     |    /             /
                   v    v   v             v
                     Response Agent
                        ¦
                        v
                   Action Agent        
                        ¦
                        v
                    Report Agent

## A human SOC team may need hours to investigate.
## A multi-agent SOC can investigate automatically.

## 📁 Project Structure

soc_ai  
│    .env   
│    graph.py     
│    llm.py   
│    main.py   
│    schemas.py   
│    state.py   
│    run.txt   
│    
├───agents   
│    │   action_agent.py   
│    │   attack_chain_agent.py   
│    │   log_agent.py   
│    │   malware_agent.py   
│    │   report_agent.py   
│    │   response_agent.py   
│    │   retrieval_agent.py   
│    │   supervisor.py   
│    │   threat_agent.py   
│
├───chroma_db  
│    │    chroma.sqlite3  
│    │  
│    └───d1dbc61d-8876-478b-a102-0fba1d7e697f  
│           data_level0.bin  
│           header.bin  
│           length.bin  
│           link_lists.bin  
│      
├───doc   
│       doc.md   
│  
├───knowledge_base   
│       log_analyser_guide.md   
│       Malware_analyser_guide.md   
│   
├───rag   
│   │    chunker.py   
│   │    embeddings.py   
│   │    ingest.py   
│   │    loader.py   
│   │    retriever.py   
│   │    vectordb.py   
│   
├───tools   
    │    logparser.py   
    │    tools.py   

# Agent 1: Log Analysis Agent
  
##  Responsibility

##  Analyze:
* Windows logs
* Linux logs
* Firewall logs
* Cloud logs
* SIEM alerts
* Tasks

##  Detect:
* Brute-force attacks
* Privilege escalation
* Suspicious login patterns
* Lateral movement

# Agent 2: Threat Intelligence Agent

##  Responsibility
*  Enrich indicators.

##  Looks up:
* IP addresses
* Domains
* Hashes
* URLs

##  Checks against:
* Threat feeds
* Internal databases
* IOC repositories

# Agent 3: Malware Analysis Agent

## Responsibility

## Analyze suspicious files.
  Can perform:
* Static analysis
* Dynamic analysis
* Behavioral analysis

# Agent 4: Attack Chain Agent

## Responsibility
*  It correlates findings from other agents.

## Attack Chain Agent concludes:
* Initial Access attack
* Persistence attack
* Command & Control attack

# Agent 5: Incident Response Agent

##  Determines actions.

##  Possible recommendations:
* Monitor activity
* Reset password
* Disable account
* Isolate endpoint
* Block IP

# Agent 6: Action Agent

## This agent takes autonomous action to safeguard and block further attack

# Agent 7: Report Generation Agent

## Creates Executive SOC report:
* Executive summary
* Findings report
* Attack path reports
* Impacts
* Actions recommended or actions taken

# Execution Flow

supervisor -> retrieval -> supervisor -> log_agent -> supervisor -> threat_agent -> supervisor -> malware_agent -> supervisor -> attack_chain_agent -> supervisor -> response_agent -> supervisor -> action_agent -> supervisor -> report_agent
