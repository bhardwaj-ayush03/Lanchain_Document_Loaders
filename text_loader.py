from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()


llm=HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V4-Pro',
    task='text-generation',
    huggingfacehub_api_token=os.getenv('HUGGINGFACEHUB_ACCESS_TOKEN')
)

model=ChatHuggingFace(llm=llm)

loader=TextLoader('cricket.txt',encoding='utf-8')

docs=loader.load()

prompt=PromptTemplate(
    template='write summmary of {poem}',
    input_variables=['poem']
)

parser=StrOutputParser()

print(type(docs))
print(len(docs))
# print(docs[0])
print(type(docs[0]))
print(docs[0].metadata)

chain=prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))