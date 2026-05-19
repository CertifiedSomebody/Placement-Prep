import sqlite3


class DatabaseManager:

    def __init__(self):

        self.connection = sqlite3.connect(
            "placementprep.db"
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    # =========================================
    # Create Tables
    # =========================================
    def create_tables(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS quiz_history (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                category TEXT,

                score INTEGER,

                total_questions INTEGER,

                played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.connection.commit()

    # =========================================
    # Save Quiz Result
    # =========================================
    def save_result(
        self,
        category,
        score,
        total_questions
    ):

        self.cursor.execute("""
            INSERT INTO quiz_history (
                category,
                score,
                total_questions
            )

            VALUES (?, ?, ?)
        """, (
            category,
            score,
            total_questions
        ))

        self.connection.commit()

    # =========================================
    # Get Quiz History
    # =========================================
    def get_history(self):

        self.cursor.execute("""
            SELECT
                category,
                score,
                total_questions,
                played_at

            FROM quiz_history

            ORDER BY played_at DESC
        """)

        return self.cursor.fetchall()