# import the main window object (mw) from aqt
from typing import Collection
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *

#Get the config setup
config = mw.addonManager.getConfig(__name__)
shortcut = config['shortcut']
fieldIfNoHighlight = config['fieldIfNoHighlight']
decksToCheck = config['decksToCheck']
fieldsToCheck = config['fieldsToCheck']
customTag = config['customTag']

# Get Highlighted text on reviewer
def getHighlightedText():
        selection = mw.web.selectedText()
        selection = selection.strip()
        # Validate content 
        if "\n" in selection:
            showInfo("Can't look text with new line characters")
            return
        # In case nothign is highlighted, it will set the content to search based on config parameter
        if not selection:
            note = getNoteInfoById(mw.reviewer.card.nid)
            return note[fieldIfNoHighlight]
        return selection

# Gets note content based on it's ID
def getNoteInfoById (noteId):
    noteInfo = mw.col.getNote(noteId) 
    return noteInfo

# Get a list of all card from the target Deck(s)
def getAllCardsFromTargetDecks (deckList):
    # transform the array of deck lists into an appropriate query to be used
    query = ' OR '.join(map('"deck:{0}"'.format, deckList))
    notesToSearch = mw.col.find_notes(query)
    return notesToSearch

# When shortcut is pressed, get parameter to use as base to search in target deck
def findDuplicate():
    highlightedText = getHighlightedText()
    notesToCompare = getAllCardsFromTargetDecks(decksToCheck)
    duplicateCount = 0
    comparedNotesCount = 0
    for noteId in notesToCompare:
        note = getNoteInfoById(noteId)
        for field in fieldsToCheck:
            comparedNotesCount +=1
            if note[field] == highlightedText:
                note.add_tag(customTag)
                ## Flush andReset are needed to actually save the changes in the note's TAG property
                note.flush()
                mw.reset()

                duplicateCount += 1
                break
    showInfo(f'Searched {len(notesToCompare)} notes.\nFound {duplicateCount} duplicates for "{highlightedText}"\n')

# create a new menu item, "Check for duplicate"
action = QAction("Check for duplicate", mw)
action.setShortcut(shortcut)
# set it to call testFunction when it's clicked
qconnect(action.triggered, findDuplicate)
# and add it to the tools menu
mw.form.menuTools.addAction(action)
