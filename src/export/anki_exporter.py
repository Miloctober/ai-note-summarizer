"""
Anki Flashcards Export Module
Creates .apkg files compatible with Anki for quiz-based flashcards.
"""
import json
import sqlite3
import zipfile
import tempfile
import os
from datetime import datetime
from typing import List, Dict
from src.quiz.models import QuizOutput, QuizQuestion

class AnkiExporter:
    """Exports QuizOutput to Anki .apkg format."""

    def __init__(self):
        """Initialize Anki exporter."""
        # Use smaller, more compatible Anki IDs
        self.model_id = "1695219123361"  # Standard Basic model ID
        self.deck_id = "1695219123361"   # Standard deck ID
    
    def create_apkg(self, quiz: QuizOutput, deck_name: str = "AI Generated Quiz") -> str:
        """
        Create an Anki .apkg file from QuizOutput.
        
        Args:
            quiz: QuizOutput object with questions
            deck_name: Name for the Anki deck
            
        Returns:
            Path to created .apkg file
        """
        # Create temporary directory for Anki files
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create collection.anki2 (SQLite database)
            db_path = os.path.join(temp_dir, "collection.anki2")
            self._create_anki_database(db_path, quiz, deck_name)
            
            # Create media directory (optional)
            media_dir = os.path.join(temp_dir, "media")
            os.makedirs(media_dir, exist_ok=True)
            
            # Create the .apkg file (ZIP archive)
            apkz_path = self._create_apkg_archive(temp_dir, deck_name)
            
            return apkz_path
    

    def _create_anki_database(self, db_path: str, quiz: QuizOutput, deck_name: str):
        """Create the Anki SQLite database with cards."""
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        try:
            # Create tables (Anki 2.1.54+ compatible schema)
            cursor.execute("""
                CREATE TABLE col (
                    id INTEGER PRIMARY KEY,
                    crt INTEGER not null,
                    mod INTEGER not null,
                    scm INTEGER not null,
                    ver INTEGER not null,
                    dty INTEGER not null,
                    usn INTEGER not null,
                    ls INTEGER not null,
                    conf TEXT not null,
                    models TEXT not null,
                    decks TEXT not null,
                    dconf TEXT not null,
                    tags TEXT not null
                );
            """)
            
            # Set PRAGMA for better compatibility
            cursor.execute("PRAGMA journal_mode=WAL")
            cursor.execute("PRAGMA synchronous=NORMAL")
            cursor.execute("PRAGMA temp_store=memory")
            
            cursor.execute("""
                CREATE TABLE notes (
                    id INTEGER PRIMARY KEY,
                    guid TEXT not null,
                    mid INTEGER not null,
                    mod INTEGER not null,
                    usn INTEGER not null,
                    tags TEXT not null,
                    flds TEXT not null,
                    sfld INTEGER not null,
                    csum INTEGER not null,
                    flags INTEGER not null,
                    data TEXT not null
                );
            """)
            

            cursor.execute("""
                CREATE TABLE cards (
                    id INTEGER PRIMARY KEY,
                    nid INTEGER not null,
                    did INTEGER not null,
                    ord INTEGER not null,
                    mod INTEGER not null,
                    usn INTEGER not null,
                    type INTEGER not null,
                    queue INTEGER not null,
                    due INTEGER not null,
                    ivl INTEGER not null,
                    factor INTEGER not null,
                    reps INTEGER not null,
                    lapses INTEGER not null,
                    left INTEGER not null,
                    odue INTEGER not null,
                    odid INTEGER not null,
                    flags INTEGER not null,
                    data TEXT not null
                );
            """)
            
            cursor.execute("""
                CREATE TABLE graves (
                    id INTEGER PRIMARY KEY,
                    usn INTEGER not null,
                    oid INTEGER not null,
                    type INTEGER not null
                );
            """)

            cursor.execute("""
                CREATE TABLE revlog (
                    id INTEGER PRIMARY KEY,
                    cid INTEGER not null,
                    usn INTEGER not null,
                    ease INTEGER not null,
                    ivl INTEGER not null,
                    lastIvl INTEGER not null,
                    factor INTEGER not null,
                    time INTEGER not null,
                    type INTEGER not null
                );
            """)

            cursor.execute("""
                CREATE INDEX ix_cards_nid on cards (nid);
                CREATE INDEX ix_cards_sched on cards (did, queue, due);
                CREATE INDEX ix_cards_usn on cards (usn);
                CREATE INDEX ix_notes_csum on notes (csum);
                CREATE INDEX ix_notes_usn on notes (usn);
                CREATE INDEX ix_revlog_cid on revlog (cid);
                CREATE INDEX ix_revlog_usn on revlog (usn);

            """)



            # Insert collection data (Anki 2.1.54+ compatible with proper versioning)
            timestamp = int(datetime.now().timestamp() * 1000)


            cursor.execute("""
                INSERT INTO col (id, crt, mod, scm, ver, dty, usn, ls, conf, models, decks, dconf, tags, colgrp, mtime_sec, mtime_usec, mod_schema)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                1, timestamp - 86400000, timestamp, timestamp, 11, 0, 0, 0,
                '{"curDeck": 1, "newBury": true, "sortType": "noteFld", "timeLim": 0, "showCounts": true, "sortBackwards": false, "newSpread": 0, "dayFirst": false, "schedVer": 2}',

                # Models
                json.dumps({str(self.model_id): {
                    "id": int(self.model_id),
                    "name": "Basic",
                    "type": 0,
                    "mod": timestamp,
                    "usn": 0,
                    "sortf": 0,
                    "did": int(self.deck_id),
                    "tmpls": [{
                        "name": "Card 1",
                        "qfmt": "{{Front}}",
                        "afmt": "{{FrontSide}}\n\n<hr id=answer>\n\n{{Back}}",
                        "bafmt": "{{FrontSide}}\n\n<hr id=answer>\n\n{{Back}}",
                        "bqfmt": "{{Front}}",
                        "did": None,
                        "ord": 0
                    }],
                    "flds": [
                        {
                            "name": "Front",
                            "font": "Arial",
                            "size": 12,
                            "rtl": False,
                            "sticky": False,
                            "media": []
                        },
                        {
                            "name": "Back", 
                            "font": "Arial",
                            "size": 12,
                            "rtl": False,
                            "sticky": False,
                            "media": []
                        }
                    ],
                    "css": "",
                    "latexPost": "\\end{document}",
                    "latexPre": "",
                    "vers": [],
                    "tags": [],
                    "req": [[0, "any", [0, 1]]]
                }}),

                # Decks (deck configuration)
                json.dumps({str(self.deck_id): {
                    "id": int(self.deck_id),
                    "name": deck_name,
                    "mod": timestamp,
                    "usn": 0,
                    "desc": f"Deck generated by AI on {datetime.now().strftime('%Y-%m-%d')}",
                    "deck": True,
                    "dyn": False,
                    "conf": 1,
                    "lrnToday": [0, 0],
                    "revToday": [0, 0],
                    "newToday": [0, 0],
                    "timeToday": [0, 0],
                    "collapsed": False
                }}),

                # Dconf (deck configuration for scheduling)
                json.dumps({str(self.deck_id): {
                    "id": int(self.deck_id),
                    "name": "Default",
                    "bmod": 0,
                    "usn": 0,
                    "delays": [10],
                    "separate": True,
                    "autoplay": True,
                    "dyn": 0,
                    "maxTaken": 60,
                    "mod": timestamp,
                    "new": {
                        "bury": True,
                        "delays": [1, 10],
                        "initialFactor": 2500,
                        "ints": [1, 6, 0],
                        "order": 1,
                        "perDay": 20,
                        "separate": True
                    },
                    "rev": {
                        "bury": True,
                        "ease4": 1.3,
                        "fuzz": 0.05,
                        "ivlFct": 1,
                        "maxIvl": 36500,
                        "minSpace": 1,
                        "perDay": 200
                    },
                    "lapse": {
                        "delays": [10],
                        "leechAction": 0,
                        "leechFails": 8,
                        "minInt": 1,
                        "mult": 0.5
                    },
                    "replayq": True,
                    "timer": 1
                }}),

                # Tags
                json.dumps({}),

                # Colgrp (collection group - empty)
                json.dumps({}),

                timestamp,
                0,
                1
            ))
            
            # Ensure the database is properly finalized
            cursor.execute("PRAGMA user_version=2130000")  # Anki 2.1.30
            
            # Insert notes and cards
            for i, question in enumerate(quiz.questions):
                note_id = timestamp + i + 1
                card_id = timestamp + i + 1
                
                # Create front/back content with proper escaping
                front = f"<div><b>{question.question}</b></div><div><br><br>Options: {', '.join(question.options)}</div>"
                back = f"<div><b>Answer:</b> {question.answer}</div><div><b>Difficulty:</b> {question.difficulty.title()}</div>"
                
                # Insert note
                cursor.execute("""
                    INSERT INTO notes (id, guid, mid, mod, usn, tags, flds, sfld, csum, flags, data)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    note_id,
                    str(note_id),
                    int(self.model_id),
                    timestamp,
                    0,
                    f"anki_export ai_generated {question.difficulty}",
                    f"{front}\x1f{back}",
                    0,
                    0,
                    0,
                    ""
                ))
                
                # Insert card
                cursor.execute("""
                    INSERT INTO cards (id, nid, did, ord, mod, usn, type, queue, due, ivl, factor, reps, lapses, left, due_real, odue, odid, flags, data)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    card_id,
                    note_id,
                    int(self.deck_id),
                    0,
                    timestamp,
                    0,
                    0,
                    0,
                    timestamp + 86400000,
                    0,
                    2.5,
                    0,
                    0,
                    0,
                    timestamp + 86400000,
                    0,
                    0,
                    0,
                    ""
                ))
            
            conn.commit()
            
        except Exception as e:
            conn.rollback()
            print(f"Error creating database: {e}")
            raise
        finally:
            conn.close()
    
    def _create_apkg_archive(self, temp_dir: str, deck_name: str) -> str:
        """Create the final .apkg file by zipping the directory."""
        apkz_path = f"exports/{deck_name.replace(' ', '_')}_deck.apkg"
        
        # Ensure exports directory exists
        os.makedirs("exports", exist_ok=True)
        
        with zipfile.ZipFile(apkz_path, 'w', zipfile.ZIP_DEFLATED) as apkz:
            apkz.write(os.path.join(temp_dir, "collection.anki2"), "collection.anki2")
            
            # Add media directory if exists
            media_dir = os.path.join(temp_dir, "media")
            if os.path.exists(media_dir):
                apkz.write(media_dir, "media/")
        
        return apkz_path
    
    def export_quiz_as_anki(self, quiz: QuizOutput, filename: str = None) -> str:
        """
        Main method to export quiz as Anki deck.
        
        Args:
            quiz: QuizOutput to export
            filename: Optional custom filename
            
        Returns:
            Path to created .apkg file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"quiz_{timestamp}.apkg"
        
        deck_name = f"Quiz - {datetime.now().strftime('%Y-%m-%d')}"
        apkz_path = self.create_apkg(quiz, deck_name)
        
        return apkz_path