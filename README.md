# A simple Wikipedia RAG Application

Una semplice applicazione web creata con Streamlit che dimostra il funzionamento del RAG (Retrieval Augmented Generation). 
L'applicazione utilizza LlamaIndex per caricare e interrogare contenuti da specifiche pagine di Wikipedia relative all'Intelligenza Artificiale e al Machine Learning, fornendo risposte basate sul contesto recuperato.

## Tecnologie utilizzate:

    Streamlit: Per l'interfaccia utente interattiva.
    LlamaIndex: Framework per la costruzione di applicazioni LLM con dati esterni (in questo caso, Wikipedia).
    OpenAI: Utilizzato per i modelli di embedding e il modello linguistico (LLM).
    WikipediaReader: Lettore di dati di LlamaIndex per ottenere contenuti da Wikipedia.
    python-dotenv: Per la gestione delle variabili d'ambiente.

## Installazione

    git clone https://github.com/LorenzoSiena/WikipediaRAG/
    cd WikipediaRAG/
    python3 -m venv .venv
    source .venv/bin/activate
    pip install streamlit python-dotenv llama-index llama-index-readers-wikipedia wikipedia

Nota: Questo progetto richiede una chiave API di OpenAI. Crea un file .env nella directory principale del progetto con il seguente contenuto:

    OPENAI_API_KEY='la_tua_chiave_api_di_openai'

Sostituisci 'la_tua_chiave_api_di_openai' con la tua effettiva chiave API di OpenAI.

## Avvio 

    streamlit run main.py
