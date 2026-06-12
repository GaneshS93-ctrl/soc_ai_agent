import os
import time
from rag.retriever import get_retriever

def retrieval_agent(state):

    state["execution_path"].append("retrieval_agent")
    start_time = time.time()
    state["start_time"] = start_time  # Store start time for latency calculation in monitoring_agent

    retriever = get_retriever()

    logs = "\n".join(state["logs"])
    # Use original query (no rewriting as per project scope)
    docs = retriever.invoke(logs)
    print(f"retrieval_agent: Retrieved {len(docs)} documents.\n")
    print(f"{docs}.\n")

    # Extract clean text strings and source filenames
    clean_docs = ["Hello world"]  # Placeholder for actual document content
    sources = []

    for doc in docs:
        clean_docs.append(doc.page_content)
        src = doc.metadata.get("source", "unknown")
        sources.append(os.path.basename(src))

    # Deduplicate sources while preserving order
    seen = set()
    unique_sources = []
    for s in sources:
        if s not in seen:
            seen.add(s)
            unique_sources.append(s)

    state["retrieved_docs"] = clean_docs      # list of plain strings
    state["sources"] = unique_sources         # deduplicated source filenames
    state["retrieval_agent_latency"] = round(time.time() - start_time, 2)

    return state
