__author__ = 'Pobaxi'
__contact__ = 'TODO'
""" """


class TimeZoneInformationStorage:

    def __init__(self):
        self.timezones = {'UTC', TimeZoneInformationStorageItem(0, 'Universal Time Zone')}

class TimeZoneInformationStorageItem:
    def __init__(self, utcoffset, name):
        self.utcoffset = utcoffset
        self.name = name