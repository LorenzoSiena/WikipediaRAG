# A simple Wikipedia RAG Application

A simple web application created with Streamlit that demonstrates how RAG (Retrieval Augmented Generation) works. The application uses LlamaIndex to load and query content from specific Wikipedia pages related to Artificial Intelligence and Machine Learning, providing answers based on the retrieved context.

## Tecnologie utilizzate:

    Streamlit: For the interactive user interface.
    LlamaIndex: Framework for building LLM applications with external data (in this case, Wikipedia).
    OpenAI: Used for embedding models and the language model (LLM).
    WikipediaReader: LlamaIndex data reader for retrieving content from Wikipedia.
    python-dotenv: For managing environment variables.

## Installation

    git clone https://github.com/LorenzoSiena/WikipediaRAG/
    cd WikipediaRAG/
    python3 -m venv .venv
    source .venv/bin/activate
    pip install streamlit python-dotenv llama-index llama-index-readers-wikipedia wikipedia

Nota: Note: This project requires an OpenAI API key. Create a .env file in the project's root directory with the following content:

    OPENAI_API_KEY='your_openai_api_key'

Replace 'your_openai_api_key' with your actual OpenAI API key.

## Run 

    streamlit run main.py
