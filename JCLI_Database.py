import json
import pathlib
from datetime import date


def initialise_database():
    
    p = pathlib.Path("./JournalDocs")
    if p.exists() == False:
        p.mkdir()
        indexPath = p / 'journalIndex.json'
        indexPath.touch()

def addJournalEntry(journal_title, journal_text):
    data = {"journal_title" : journal_title, "journal_text": journal_text}
    
    p = pathlib.Path("./JournalDocs")
    # ability to log multiple times in a day?
    
    with open('journalIndex', 'w') as f:
        json.dump(data, f)
