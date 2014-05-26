import datetime

__author__ = 'Pobaxi'

import re
import pytz
from pytz import timezone
from pyheufybot.moduleinterface import Module, ModuleAccessLevel, ModulePriority, ModuleType
from datetime import datetime


class ModuleSpawner(Module):
    def __init__(self, bot):
        self.bot = bot
        self.name = "Timezone"
        self.trigger = "timezone"
        self.moduleType = ModuleType.COMMAND
        self.modulePriority = ModulePriority.NORMAL
        self.accessLevel = ModuleAccessLevel.ANYONE
        self.messageTypes = ["PRIVMSG"]  #TODO EHHHH?
        self.helpText = "Usage: timezone <HH:MM Timezone> <Timezone> | Converts from one time to the other. " \
                        "Timezone stands for the timezone shorthand, UTC for example."

    def execute(self, message):
        #TODO:
        if len(message.params) != 4:
            self.bot.msg(message.replyTo, "ehhh somethings wrong chap. I can't process that.")
        else:
            self.bot.msg(message.replyTo, "Hey something went right chap")
            expression = re.compile('[0-9]+[:][0-9]+')
            potentialTime = expression.search(message.params[1])
            #potentialTime = re.search(message.params[1], '[0-9]+[:][0-9]+')
            potentialFromTimeZone = message.params[2]
            potentialToTimeZone = message.params[3]

            timezone(potentialFromTimeZone)

            if len(potentialFromTimeZone) == 3 or len(potentialFromTimeZone) == 4:
                if len(potentialToTimeZone) == 3 or len(potentialToTimeZone) == 4:
                    if potentialTime:
                        self.bot.msg(message.replyTo, 'YAY looks like we are getting somewhere')
                        splitstring = potentialTime.string.split(':')
                        # for now this might do, but do I run into troubles down the line with this?
                        initialTime = datetime(datetime.year,
                                               datetime.month, datetime.day,
                                               splitstring[0], splitstring[1], 0, 0, timezone(potentialFromTimeZone))


                        #todo figure out how to work with timezones now.... cause that seems to be the actual catch 22

                    else:
                        self.bot.msg(message.replyTo, message.params[1] + " doesn't seem to be a time in HH:MM format?")
                else:
                    self.bot.msg(message.replyTo, potentialFromTimeZone +
                                               "is not a timezone abbreviation I understand. check this link:"
                                               "http://en.wikipedia.org/wiki/List_of_time_zone_abbreviations "
                                               "for a list of timezone abbreviations I know")
            else:
                self.bot.msg(message.replyTo, potentialFromTimeZone +
                                               "is not a timezone abbreviation I understand. check this link:"
                                               "http://en.wikipedia.org/wiki/List_of_time_zone_abbreviations "
                                               "for a list of timezone abbreviations I know")

                # Do the actual work of timezone converting?
                # actual work:
                #   check if <from> is something we can work with i.e: are you a time + known timezone
                #   check if <to> is something we can work with i.e: are you a known timezone
                #       sounds like a reusable function, challenge how to check? regex? good ol fashioned string
                #       masturbation?
                #
                # [0-9]2[:][0-9]2
                #
                #   utilize something to make the actual conversion, python probably has something
                #   return the conversion: challenge -> date change i.e: <to> is the next day, how to output the user?

        return True