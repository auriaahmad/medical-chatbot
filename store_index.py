from src.helper import load_pdf, text_split, download_hugging_face_embeddings
# import langchain.vectorstores
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
# import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')


# print(PINECONE_API_KEY)
# print(PINECONE_API_ENV)

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


# Initializing the Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
indexs = pc.list_indexes().names()
print(indexs)
index_name = "medical-chatbot"
# Now do stuff
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name='medical-chatbot',
        dimension=384,
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )
else:
    print(f"Index {index_name} already exists")


print(type(text_chunks))
# text_chunk = text_chunks[0:5]
# docs = [text_chunk.page_content for text_chunk in text_chunks]
# print(docs[0:5])
# for text_chunk in text_chunks:
#     page_content = text_chunk.page_content
#     docs.append(page_content)

# print(docs[0:5])
# Creating Embeddings for Each of The Text Chunks & storing
docsearch = PineconeVectorStore.from_documents(
    text_chunks,
    embeddings,
    index_name=index_name
)
