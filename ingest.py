import os
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

def ingest_documents():
    loaders = [
        UnstructuredFileLoader(f'docs/{f}') for f in os.listdir('docs') if f.endswith(('.pdf', '.docx', '.txt'))
    ]
    all_docs = []
    for loader in loaders:
        all_docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(all_docs)

    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory="vectorstore")
    vectordb.persist()
    print(f'✅ Đã nạp {len(chunks)} đoạn vào vectorstore.')

if __name__ == "__main__":
    ingest_documents()
