import os
import streamlit as st
from dotenv import load_dotenv

from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.readers.wikipedia import WikipediaReader
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage

load_dotenv()

INDEX_DIR = 'wiki_rag'
PAGES = [
    "Artificial intelligence",
    "Deep learning",
    "Reinforcement learning",
    "Unsupervised learning",
    "Machine learning",
    "Neural network",
    "Convolutional neural network",
    "Supervised learning",
    "Natural language processing",
    "Transformer (machine learning model)",
    "OpenAI",
    "ChatGPT",
    "Support vector machine",
    "Decision tree learning",
    "Computer vision",
    "Generative adversarial network",
    "Bayesian network",
    "Gradient boosting",
    "Feature engineering",
    "K-nearest neighbors algorithm"
]

@st.cache_resource
def get_index():
    if os.path.isdir(INDEX_DIR):
        storage = StorageContext.from_defaults(persist_dir=INDEX_DIR)
        return load_index_from_storage(storage)

    docs = WikipediaReader().load_data(pages=PAGES, auto_suggest=False)
    embedding_model = OpenAIEmbedding('text-embedding-3-small')
    index = VectorStoreIndex.from_documents(docs, embed_model=embedding_model)
    index.storage_context.persist(persist_dir=INDEX_DIR)

    return index

@st.cache_resource
def get_query_engine():
    index = get_index()
    llm = OpenAI(model='gpt-4o-mini', temperature=0)

    return index.as_query_engine(llm=llm, similarity_top_k=3)

def main():
    st.title('Wikipedia RAG Application')

    question = st.text_input('Ask a question')

    if st.button('Submit') and question:
        with st.spinner('Thinking...'):
            qa = get_query_engine()
            response = qa.query(question)

        st.subheader('Answer')
        st.write(response.response)

        st.subheader('Retrieved context')
        for src in response.source_nodes:
            st.markdown(src.node.get_content())


if __name__ == '__main__':
    main()
