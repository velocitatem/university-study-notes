from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.document_loaders import TextLoader
loader = TextLoader('/mnt/s/Documents/Collage/university-study-notes/content/20230413174833-fundamentals_of_data_analysis_cheat_sheet.org')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
from langchain.vectorstores import Chroma
docsearch = Chroma.from_documents(texts, embeddings)

from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.as_retriever())


query = "When are conditions for a z-test satisfied?"
while True:
    question = input("Q: ")
    if question == "q":
        break
    answer = qa.run(question)
    print("A:", answer)
