from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os

# load_dotenv()

loader= PyPDFLoader('dl-curriculum.pdf')

docs=loader.load()

print(len(docs))

