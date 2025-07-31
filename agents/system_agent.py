from ..tools.system_controller import SystemController

class SystemAgent:
    def __init__(self, config):
        self.controller = SystemController(config)
        
    def run(self, command):
        if 'выключи компьютер' in command.lower():
            self.controller.shutdown()
            return "Компьютер будет выключен"
        elif 'открой браузер' in command.lower():
            self.controller.open_browser()
            return "Открываю браузер"
        # Другие команды...