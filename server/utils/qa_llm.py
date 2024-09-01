import os
import dotenv

from langchain_community.chat_models import ChatOpenAI
from .callback import MyCallbackHandler
from langchain.callbacks.base import BaseCallbackManager

dotenv.load_dotenv()

class QaLlm():

    def __init__(self) -> None:
        os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')  
        manager = BaseCallbackManager([MyCallbackHandler()])
        self.llm = ChatOpenAI(temperature=0, callback_manager=manager, model_name="gpt-3.5-turbo")

    def get_llm(self):
        return self.llm