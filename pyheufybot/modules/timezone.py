__author__ = 'Pobaxi'

import re
from pyheufybot.module_interface import Module, ModulePriority, ModuleType


class ModuleSpawner(Module):
    def __init__(self, bot):
        self.bot = bot
        self.name = "Timezone"
        self.trigger = "timezone"
        self.moduleType = ModuleType.COMMAND
        self.modulePriority = ModulePriority.NORMAL
        self.messageTypes = ["PRIVMSG"]  #TODO EHHHH?
        self.helpText = "Usage: timezone <from> <to> | Converts from one timezone to the other."

        def excecute(self, message):
            #TODO
            if ()

            else

