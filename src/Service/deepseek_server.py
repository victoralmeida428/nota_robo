import os
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_deepseek.chat_models import  ChatDeepSeek
from Service.singleton import SingletonMeta
from .prompt import prompt
from model.comprovante_model import ComprovanteModel
from dotenv import load_dotenv
load_dotenv()

class DeepSeekServer(metaclass=SingletonMeta):
    __token = os.environ.get("DEEPSEEK_TOKEN", "")
    __llm = None
    __prompt_template = None
    __chain = None
    __parser = None

    def __init__(self):
        self.__valid()
        self.__setParse()
        self.__setPrompt()
        self.__setLLM()
        self.__setChain()

    def response(self, input: str):
        return self.__chain.invoke({"nfse_text":input})


    def __valid(self):
        if self.__token == "":
            raise EnvironmentError("DEEPSEEK_TOKEN environment variable not set")

    def __setLLM(self):
        self.__llm = ChatDeepSeek(
            model='deepseek-chat',
            temperature=0,
            api_key=self.__token,
            max_retries=2
        )

    def __setPrompt(self):
        self.__prompt_template = PromptTemplate(
            template=prompt,
            input_variables=['nfse_text'],
            partial_variables={"format_instructions": self.__parser.get_format_instructions()},
        )

    def __setChain(self):
        self.__chain = self.__prompt_template | self.__llm | self.__parser

    def __setParse(self):
        self.__parser = PydanticOutputParser(pydantic_object=ComprovanteModel)



