#!/usr/bin/python
#coding:utf-8
# Author:  Dan-Erik Lindberg -- <riffdee@dan-erik.com>
# Created: 2012-07-12
# License: GPL-3

import os
import sys

import distutils

DistUtils.auto.setup(
    name='riffdee',
    version='12.6',
    license='GPL-3',
    author='Dan-Erik Lindberg',
    author_email='riffdee@dan-erik.com',
    description='RiffDee is an application that records RFID data.',
    long_description='RiffDee was developed to store data from PIT-tags used to identify fish (although I\'m sure it can be used for other purposes). Thousands of salmon are tagged each year both in hatcheries and in the wild and existing software at the time of writing this application was 15-20 years old. RiffDee brings a number of improvements over the old softwares, such as storing tags in a database and getting live statistics about passing fish. The software has been tested with Allflex RM310 and Destron FS-2020 readers, but should work with other brands as well.',
    url='https://github.com/GaRyu/riffdee',
    cmdclass={'install': InstallAndUpdateDataDirectory}
)
