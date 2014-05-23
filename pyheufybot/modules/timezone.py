__author__ = 'Pobaxi'

import re
from datetime import time, tzinfo
from pyheufybot.module_interface import Module, ModulePriority, ModuleType


class ModuleSpawner(Module):
    def __init__(self, bot):
        self.bot = bot
        self.name = "Timezone"
        self.trigger = "timezone"
        self.moduleType = ModuleType.COMMAND
        self.modulePriority = ModulePriority.NORMAL
        self.messageTypes = ["PRIVMSG"]  #TODO EHHHH?
        self.helpText = "Usage: timezone <HH:MM Timezone> <Timezone> | Converts from one time to the other. " \
                        "Timezone stands for the timezone shorthand, UTC for example."

    def execute(self, message):
        #TODO:
        if len(message.params) != 3:
            self.bot.msg(message.replyTo, "ehhh somethings wrong chap. I can't process that.")
        else:
            self.bot.msg(message.replyTo, "Hey something went right chap")
            
            # Do the actual work of timezone converting?
            # actual work:
            #   check if <from> is something we can work with i.e: are you a time + known timezone
            #   check if <to> is something we can work with i.e: are you a known timezone
            #       sounds like a reusable function, challenge how to check? regex? good ol fashioned string
            #       masturbation?
            #   utilize something to make the actual conversion, python probably has something
            #   return the conversion: challenge -> date change i.e: <to> is the next day, how to output the user?

        return True