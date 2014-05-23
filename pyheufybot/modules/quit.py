__author__ = 'Pobaxi'
__contact__ = 'TODO'

from pyheufybot.module_interface import Module, ModulePriority, ModuleType


class ModuleSpawner(Module):
    def __init__(self, bot):
        self.bot = bot
        self.name = "Quit"
        self.trigger ="quit"
        self.moduleType= ModuleType.COMMAND
        self.modulePriority = ModulePriority.NORMAL
        self.messageTypes = ["PRIVMSG"]
        self.helpText="Usage: quit | Tells the bot to shutdown."

    def execute(self, message):
        self.bot.quit("Good by cruel world")
        #TODO while this currently does quit the bot, he rejoins shortly afterwards.
        return True