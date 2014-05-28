__author__ = 'Pobaxi'
__contact__ = 'TODO'
""" """


class TimeZoneInformationStorage:

    def __init__(self):
        self.timezones = {}
        self.timezones.update({'BIT': TimeZoneInformationStorageItem(-12, 'Baker Island Time')})
        self.timezones.update({'NUT': TimeZoneInformationStorageItem(-11, 'Niue Time')})
        self.timezones.update({'SST': TimeZoneInformationStorageItem(-11, 'Samoa Standard Time')})
        self.timezones.update({'CKT': TimeZoneInformationStorageItem(-10, 'Cook Island TIme')})
        self.timezones.update({'HAST': TimeZoneInformationStorageItem(-10, 'Hawaii-Aleutian Standard Time')})
        self.timezones.update({'HST': TimeZoneInformationStorageItem(-10, 'Hawaii Standard Time')})
        self.timezones.update({'TAHT': TimeZoneInformationStorageItem(-10, 'Tahiti Time')})
        self.timezones.update({'MART': TimeZoneInformationStorageItem(-9.5, 'Marquesas Island Time')})
        self.timezones.update({'MIT': TimeZoneInformationStorageItem(-9.5, 'Marquesas Island Time')})
        self.timezones.update({'AKST': TimeZoneInformationStorageItem(-9, 'Alaska Standard Time')})
        self.timezones.update({'GAMT': TimeZoneInformationStorageItem(-9, 'Gambier Island Time')})
        self.timezones.update({'GIT': TimeZoneInformationStorageItem(-9, 'Gambier Island Time')})
        self.timezones.update({'HADT': TimeZoneInformationStorageItem(-9, 'Hawaii-Aleutian Daylight Time')})
        self.timezones.update({'AKDT': TimeZoneInformationStorageItem(-8, 'Alaska Daylight Time')})
        self.timezones.update({'CIST': TimeZoneInformationStorageItem(-8, 'Clipperton Island Standard Time')})
        self.timezones.update({'PST': TimeZoneInformationStorageItem(-8, 'Pacific Standard Time (North America)')})
        self.timezones.update({'MST': TimeZoneInformationStorageItem(-7, 'Mountain Standard Time (North America)')})
        self.timezones.update({'PDT': TimeZoneInformationStorageItem(-7, 'Pacific Daylight Time (North America)')})
        self.timezones.update({'CST': TimeZoneInformationStorageItem(-6, 'Central Standard Time (North America)')})
        self.timezones.update({'EAST': TimeZoneInformationStorageItem(-6, 'Easter Island Standard Time')})
        self.timezones.update({'GALT': TimeZoneInformationStorageItem(-6, 'Galapagos Time')})
        self.timezones.update({'MDT': TimeZoneInformationStorageItem(-6, 'Mountain Daylight Time (North America)')})
        self.timezones.update({'CDT': TimeZoneInformationStorageItem(-5, 'Central Daylight Time (North America)')})
        self.timezones.update({'COT': TimeZoneInformationStorageItem(-5, 'Colombia Time')})
        self.timezones.update({'CST': TimeZoneInformationStorageItem(-5, 'Cuba Standard Time')})
        self.timezones.update({'EASST': TimeZoneInformationStorageItem(-5, 'Easter Island Standard Summer Time')})
        self.timezones.update({'ECT': TimeZoneInformationStorageItem(-5, 'Ecuador Time')})
        self.timezones.update({'EST': TimeZoneInformationStorageItem(-5, 'Eastern Standard Time (North America')})
        self.timezones.update({'PET': TimeZoneInformationStorageItem(-5, 'Peru Time')})
        self.timezones.update({'VET': TimeZoneInformationStorageItem(-4.5, 'Venezuelan Standard Time')})
        self.timezones.update({'AMT': TimeZoneInformationStorageItem(-4, 'Amazon Time (Brazil)')})
        self.timezones.update({'AST': TimeZoneInformationStorageItem(-4, 'Atlantic Standard Time')})
        self.timezones.update({'BOT': TimeZoneInformationStorageItem(-4, 'Bolivia Time')})
        self.timezones.update({'CDT': TimeZoneInformationStorageItem(-4, 'Cuba Daylight Time')})
        self.timezones.update({'CLT': TimeZoneInformationStorageItem(-4, 'Chile Standard Time')})
        self.timezones.update({'COST': TimeZoneInformationStorageItem(-4, 'Colombia Summer Time')})
        self.timezones.update({'ECT': TimeZoneInformationStorageItem(-4, 'Eastern Caribbean Time')})
        self.timezones.update({'EDT': TimeZoneInformationStorageItem(-4, 'Eastern Daylight Time (North America)')})
        self.timezones.update({'FKT': TimeZoneInformationStorageItem(-4, 'Falkland Islands Time')})
        self.timezones.update({'GYT': TimeZoneInformationStorageItem(-4, 'Guyana Time')})
        self.timezones.update({'PYT': TimeZoneInformationStorageItem(-4, 'Paraguay Standard Time')})
        self.timezones.update({'NST': TimeZoneInformationStorageItem(-3.5, 'Newfoundland Standard Time')})
        self.timezones.update({'NT': TimeZoneInformationStorageItem(-3.5, 'Newfoundland Time')})
        self.timezones.update({'ADT': TimeZoneInformationStorageItem(-3, 'Atlantic Daylight Time')})
        self.timezones.update({'AMST': TimeZoneInformationStorageItem(-3, 'Amazon Summer Time (Brazil)')})
        self.timezones.update({'ART': TimeZoneInformationStorageItem(-3, 'Argentina Time')})
        self.timezones.update({'BRT': TimeZoneInformationStorageItem(-3, 'Brasilia Time')})
        self.timezones.update({'CLST': TimeZoneInformationStorageItem(-3, 'Chile Summer Time')})
        self.timezones.update({'FKST': TimeZoneInformationStorageItem(-3, 'Falkland Island Standard/Summer Time')})
        self.timezones.update({'GFT': TimeZoneInformationStorageItem(-3, 'French Guiana Time')})
        self.timezones.update({'PMST': TimeZoneInformationStorageItem(-3, 'Saint Pierre and Miquelon Standard Time')})
        self.timezones.update({'PYST': TimeZoneInformationStorageItem(-3, 'Paraguay Summer Time (South America)')})
        self.timezones.update({'ROTT': TimeZoneInformationStorageItem(-3, 'Rothera Research Station Time')})
        self.timezones.update({'SRT': TimeZoneInformationStorageItem(-3, 'Suriname Time')})
        self.timezones.update({'UYT': TimeZoneInformationStorageItem(-3, 'Uruguay Standard Time')})
        self.timezones.update({'NDT': TimeZoneInformationStorageItem(-2,5,'Newfoundland Daylight Time')})

        self.timezones.update({'UTC': TimeZoneInformationStorageItem(0, 'Coordinated Universal Time')})
        self.timezones.update({'Z': TimeZoneInformationStorageItem(0, 'Coordinated Universal Time')})

class TimeZoneInformationStorageItem:
    def __init__(self, utcoffset, name):
        self.utcoffset = utcoffset
        self.name = name