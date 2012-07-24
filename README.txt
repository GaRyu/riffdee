==========
RiffDee
==========

RiffDee is an application that handles interrogation of Passive Integrated Transponder tags (PIT-tags) through Radio Frequency Identification readers (RFID readers). Glass encased PIT-tags are commonly used to surgically tag animals, since the tag lasts a lifetime and doesn't need a battery. There are also other versions of PIT-tags, for example external ear tags, electronic keys to open locks, or in the form of stickers to keep track of library books. Libraries, retailers, and similar enterprises use high frequency readers while animal tags most often use low frequency (134.1 kHz) since lower frequencies doesn't get absorbed by water as much.

RiffDee was developed to store data from PIT-tags used to identify fish (although I'm sure it can be used for other purposes). Thousands of salmon are tagged each year both in hatcheries and in the wild and existing software at the time of writing this application was 15-20 years old. RiffDee brings a number of improvements over the old softwares, such as storing tags in a database and getting live statistics about passing fish. The software has been tested with Allflex RM310 and Destron FS-2020 readers, but should work with other brands as well.
