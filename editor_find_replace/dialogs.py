# -*- coding: utf-8 -*-

"""
This file is part of the Find and Replace in Editor add-on for Anki

Associated dialogs

Copyright: (c) Glutanimate 2017 <https://glutanimate.com/>
License: GNU AGPLv3 or later <https://www.gnu.org/licenses/agpl.html>
"""

from __future__ import unicode_literals

from aqt.qt import *

from .forms import editorfindreplace


class FindAndReplace(QDialog):
    """Find and Replace dialog"""

    radioToggles = {
        True: ("lbFind", "lbReplace", "teFind", "teReplace"), # string
        False: ("lbOriginal", "lbNew", "sbOriginal", "sbNew") # cloze
    }

    def __init__(self, editor):
        self.editor = editor
        parent = editor.parentWindow
        super(FindAndReplace, self).__init__(parent=parent)
        self.form = editorfindreplace.Ui_Dialog()
        self.form.setupUi(self)
        self.setupEvents()
        self.form.teFind.setFocus()
        self.mode = True

    def setupEvents(self):
        self.form.buttonBox.rejected.connect(self.reject)
        self.form.buttonBox.accepted.connect(self.accept)
        self.form.rbString.toggled.connect(
            lambda c: self.onRadioToggle(c, True))
        self.form.rbCloze.toggled.connect(
            lambda c: self.onRadioToggle(c, False))

    def onRadioToggle(self, checked, mode):
        if not checked:
            return
        for name in self.radioToggles[mode]:
            widget = getattr(self.form, name)
            widget.setEnabled(True)
        for name in self.radioToggles[not mode]:
            widget = getattr(self.form, name)
            widget.setEnabled(False)
        self.mode = mode
