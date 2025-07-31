from langchain_community.llms import Ollama
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler

def setup_llm(config):
    return Ollama(
        model="mistral",
        temperature=0.7,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
        base_url=config.get('ollama_base_url', 'http://localhost:11434'),
    )