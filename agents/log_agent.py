from langchain_core.prompts import ChatPromptTemplate
from llm import llm
from schemas import FindingsOutput

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
    You are a senior SOC analyst.

    Analyze logs.

    Detect:
    - brute force
    - privilege escalation
    - suspicious execution
    - lateral movement

    """
    ),
    (
        "human",
        """
        Logs:
        "{logs}"
        
        Context:
        {context}
        """
    )
])

structured_llm = llm.with_structured_output(
    FindingsOutput
)

def log_agent(state):

    state["execution_path"].append("log_agent")
    
    chain = prompt | structured_llm
    
    context = "\n\n---\n".join(state["retrieved_docs"]) if state.get("retrieved_docs") else "No context retrieved."
    logs = "\n".join(state["logs"])

    result = chain.invoke({
        "context": context,
        "logs": logs
    })
    
    print("log_agent Result:", result.findings,"\n")

    return {
        "findings": [
            x.model_dump()
            for x in result.findings
        ]
    }