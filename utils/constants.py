"""
Constants.py
"""

# Visualisation constants
PLOT_SIZE = 3

VISUALISATION_SETTINGS = {
            'Original Query': {'color': 'red', 'opacity': 1, 'symbol': 'cross', 'size': 15},
            'Retrieved': {'color': 'magenta', 'opacity': 1, 'symbol': 'circle', 'size': 10},
            'Chunks': {'color': 'orange', 'opacity': 0.8, 'symbol': 'circle', 'size': 10},
            'Sub-Questions': {'color': 'purple', 'opacity': 1, 'symbol': 'star', 'size': 15},
            'Hypothetical Ans': {'color': 'purple', 'opacity': 1, 'symbol': 'star', 'size': 15},
        }

# Embedding Models
OPENAI_EMBEDDINGS = ["text-embedding-3-small", "text-embedding-3-large" , "text-embedding-ada-002"]
OTHER_EMBEDDINGS = ["all-MiniLM-L6-v2"]
EMBEDDING_MODEL_LIST = OTHER_EMBEDDINGS + OPENAI_EMBEDDINGS
LLM_LIST = ["gpt-3.5-turbo-0125", "gpt-4-1106-preview", "gpt-4-0125-preview"]

# LLM
GPT_MODEL = "gpt-4-1106-preview"

MULTIPLE_QNS_SYS_MSG = "Given a question, your task is to generate 3 to 5 simple sub-questions related to the original questions. "\
                        "These sub-questions are to be short. Format your reply in json with numbered keys."\
                        "EXAMPLE:"\
                        "INPUTS What are the top 3 reasons for the decline in Microsoft's revenue from 2022 to 2023?"\
                        "OUTPUT: \{'1': 'What was microsoft's revenue in 2022?', '2': 'What was microsoft's revenue in 2023?', '3': What are the drivers for revenue?'\}"

HYDE_SYS_MSG = "Given a question, your task is to craft a template for the hypothetical answer. Do not include anyfacts, and instead label them as <PLACEHOLDERS>. "\
                "FOR EXAMPLE: INPUT: 'What is the revenue of microsoft in 2021 and 2022?' "\
                "OUTPUT: 'Microsoft's 2021 and 2022 revenue is <MONETARY SUM> and <MONETARY SUM> respectively.'"

# UI
ABOUT_THIS_APP = "This application is inspired and adapts the code from [this excellent course](https://www.deeplearning.ai/short-courses/advanced-retrieval-for-ai/) by DeepLearning.AI and Chroma."

CHUNK_EXPLAINER = "In RAG, your document is divided into parts (i.e. chunks) for searching, and relevant chunks are given to the LLM as additional context. \n \n"\
                "\"Chunk Size\" is the number of tokens in one of these chunks, and \"Chunk Overlap\" is the number of tokens shared between consecutive chunks to maintain context. \n\n"\
                "One word is about 3-4 tokens."

BUILD_VDB_LOADING_MSG = 'Building the vector database 🚧 ... It takes about 1-2 minutes, depending on the size of your PDF. Please do not close this app. 🙏'

VISUALISE_LOADING_MSG = 'Visualising your chunks 🎨 ... It takes about 2-3 minutes, depending on the size of your PDF. Please do not close this app. 🙏'
