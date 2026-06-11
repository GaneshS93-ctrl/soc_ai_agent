from rag.loader import load_docs
from rag.chunker import split_docs
from rag.vectordb import create_db
from dotenv import load_dotenv

load_dotenv()


def ingest():

    docs = load_docs()

    chunks = split_docs(
        docs
    )

    create_db(
        chunks
    )

    print(
        f"Successfully created {len(chunks)} chunks"
    )


if __name__ == "__main__":
    ingest()