from core.assistant_core import PersonalAssistant
from utils.config_loader import load_config
from utils.logger import setup_logger
import logging

def main():
    config = load_config("config.yaml")
    logger = setup_logger()
    
    from models.llm_setup import setup_llm
    config['llm'] = setup_llm(config['ollama'])
    
    try:
        assistant = PersonalAssistant(config)
        print("Ассистент запущен. Готов к работе!")
        logger.info("Ассистент запущен")
        
        import sys
        if len(sys.argv) > 1:
            assistant.speak(assistant.process_input(" ".join(sys.argv[1:])))
        else:
            assistant.run()
            
    except Exception as e:
        logger.error(f"Ошибка: {str(e)}")
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    main()