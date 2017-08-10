# -*- coding: utf-8 -*-

"""
This file is part of the Find and Replace in Editor add-on for Anki

Main Module, hooks add-on methods into Anki

Copyright: (c) Glutanimate 2017 <https://glutanimate.com/>
License: GNU AGPLv3 or later <https://www.gnu.org/licenses/agpl.html>
"""

from __future__ import unicode_literals

############## USER CONFIGURATION START ##############

HOTKEY = "Ctrl+T, R"

##############  USER CONFIGURATION END  ##############

from aqt.editor import Editor
from aqt.browser import Browser
from aqt.utils import tooltip
from anki.hooks import addHook

from dialogs import FindAndReplace

js_find_replace = """
function getSelectionHtml() {
    // Based on an SO answer by Tim Down
    var html = "";
    if (typeof window.getSelection != "undefined") {
        var sel = window.getSelection();
        if (sel.rangeCount) {
            var container = document.createElement("div");
            for (var i = 0, len = sel.rangeCount; i < len; ++i) {
                container.appendChild(sel.getRangeAt(i).cloneContents());
            }
            html = container.innerHTML;
        }
    } else if (typeof document.selection != "undefined") {
        if (document.selection.type == "Text") {
            html = document.selection.createRange().htmlText;
        }
    }
    return html;
}
if (typeof window.getSelection != "undefined") {
    // get selected HTML
    var sel = getSelectionHtml();
    // replace items
    var sel = sel.replace(/%s/g, "%s")
    document.execCommand('insertHTML', false, sel);
    saveField('key');
}
"""

def onFindAndReplace(self):
    """Main function"""
    sel_changed = False
    if not self.web.selectedText():
        self.web.eval("document.execCommand('selectAll')")
        sel_changed = True
        if not self.web.selectedText():
            tooltip("Please enter some text first.")
            return False
    
    dialog = FindAndReplace(self)
    ret = dialog.exec_()
    if not ret:
        if sel_changed: # revert updated selection
            self.web.eval("window.getSelection().removeAllRanges();")
            self.web.eval("focusField(%d);" % self.currentField)
        return False
    
    mode = dialog.mode
    if mode: # string
        original = dialog.form.teFind.text()
        new = dialog.form.teReplace.text()
    else: # cloze
        oidx = dialog.form.sbOriginal.value()
        nidx = dialog.form.sbNew.value()
        original = "{{c%d::" % oidx
        new = "{{c%d::" % nidx
    
    self.web.eval(js_find_replace % (original, new))
    
    tooltip("{} replaced with {}".format(original, new),
        parent=self.parentWindow)


def onSetupButtons(self):
    """Add buttons to editor"""
    self._addButton("edit-find-replace", self.onFindAndReplace,
        tip="Find and Replace in Selected Text ({})".format(HOTKEY),
        key=HOTKEY)


Editor.onFindAndReplace = onFindAndReplace
addHook("setupEditorButtons", onSetupButtons)