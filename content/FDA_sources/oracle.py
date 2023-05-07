from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import NotebookLoader


from langchain.document_loaders import TextLoader
import os
# get all .ipynb files in the current directory
all_notebooks = [os.path.join(os.getcwd(), f) for f in os.listdir(os.getcwd()) if f.endswith(".ipynb")]
loader = NotebookLoader(all_notebooks[0], include_outputs=True, max_output_length=20, remove_newline=True)
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
docsearch = Chroma.from_documents(texts, embeddings)
qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="map_reduce", retriever=docsearch.as_retriever())

from langchain.agents import load_tools, Tool
from langchain.agents import initialize_agent
from langchain.agents import AgentType

llm = OpenAI(temperature=0.7)
from langchain.utilities import PythonREPL
tools = [
    Tool(name="Statistics", func=qa.run, description="Useful for when you need to know how to do something with statistics."),
    Tool(name="Python", func=PythonREPL().run, description="Useful for when you need to know how to do something with Python.")


]

agent = initialize_agent(tools, llm, verbose=True)

while True:
    question = input("What do you want to know about statistics? ")
    agent.run(question)
