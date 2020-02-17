# -*- coding: utf-8 -*-
#########################################################################
# Copyright (C) 2018-2019 by Simone Gaiarin <simgunz@gmail.com>         #
#                                                                       #
# This program is free software; you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation; either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program; if not, see <http://www.gnu.org/licenses/>.  #
#########################################################################
from anki.hooks import wrap

from aqt.editor import Editor

def setBrowserMaxImageHeight(self):
    config = self.mw.addonManager.getConfig(__name__)
    if config['height_or_width'] == "height":
        self.web.eval('''$('head').append('<style type="text/css">'''
                      '''#fields img{{ max-height: {height};}}</style>')'''
                      .format(height=config['max-height']))
    elif config['height_or_width'] == "width":
        self.web.eval('''$('head').append('<style type="text/css">'''
                      '''#fields img{{ max-width: {width};}}</style>')'''
                      .format(width=config['max-width']))
    elif config['height_or_width'] == "both":
        self.web.eval('''$('head').append('<style type="text/css">'''
                      '''#fields img{{ max-width: {width}; max-height: {width};}}</style>')'''
                      .format(width=config['both']))                      


Editor.setupWeb = wrap(Editor.setupWeb, setBrowserMaxImageHeight)
