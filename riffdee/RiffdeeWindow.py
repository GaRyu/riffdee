#!/usr/bin/python
#coding:utf-8
# Author:  Dan-Erik Lindberg -- <riffdee@dan-erik.com>
# Created: 2012-07-12
# License: GPL-3

import gettext
from gettext import gettext as _
gettext.textdomain('riffdee')

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('riffdee')

from riffdee_lib import Window
from riffdee.AboutRiffdeeDialog import AboutRiffdeeDialog
from riffdee.PreferencesRiffdeeDialog import PreferencesRiffdeeDialog

# See riffdee_lib.Window.py for more details about how this class works
class RiffdeeWindow(Window):
    __gtype_name__ = "RiffdeeWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(RiffdeeWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutRiffdeeDialog
        self.PreferencesDialog = PreferencesRiffdeeDialog

        # Code for other initialization actions should be added here.

