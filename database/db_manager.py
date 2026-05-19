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

                percentage REAL,

                played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        self.connection.commit()

        # =========================================
        # Safe Migration
        # =========================================
        try:

            self.cursor.execute("""
                ALTER TABLE quiz_history
                ADD COLUMN percentage REAL
            """)

            self.connection.commit()

        except:

            pass

    # =========================================
    # Save Quiz Result
    # =========================================
    def save_result(
        self,
        category,
        score,
        total_questions
    ):

        percentage = round(
            (score / total_questions) * 100,
            2
        )

        self.cursor.execute("""
            INSERT INTO quiz_history (
                category,
                score,
                total_questions,
                percentage
            )

            VALUES (?, ?, ?, ?)
        """, (
            category,
            score,
            total_questions,
            percentage
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
                percentage,
                played_at

            FROM quiz_history

            ORDER BY played_at DESC
        """)

        return self.cursor.fetchall()

    # =========================================
    # Total Quizzes Played
    # =========================================
    def get_total_quizzes(self):

        self.cursor.execute("""
            SELECT COUNT(*)
            FROM quiz_history
        """)

        return self.cursor.fetchone()[0]

    # =========================================
    # Average Percentage
    # =========================================
    def get_average_score(self):

        self.cursor.execute("""
            SELECT AVG(percentage)
            FROM quiz_history
        """)

        result = self.cursor.fetchone()[0]

        if result is None:

            return 0

        return round(result, 2)

    # =========================================
    # Category Attempts
    # =========================================
    def get_category_stats(self):

        self.cursor.execute("""
            SELECT
                category,
                COUNT(*)

            FROM quiz_history

            GROUP BY category
        """)

        return self.cursor.fetchall()

    # =========================================
    # Best Performing Category
    # =========================================
    def get_best_category(self):

        self.cursor.execute("""
            SELECT
                category,
                AVG(percentage) as avg_percentage

            FROM quiz_history

            GROUP BY category

            ORDER BY avg_percentage DESC

            LIMIT 1
        """)

        result = self.cursor.fetchone()

        if result:

            return result[0]

        return "-"

    # =========================================
    # Highest Score
    # =========================================
    def get_highest_score(self):

        self.cursor.execute("""
            SELECT MAX(percentage)
            FROM quiz_history
        """)

        result = self.cursor.fetchone()[0]

        if result is None:

            return 0

        return round(result, 2)

    # =========================================
    # Recent Activity
    # =========================================
    def get_recent_activity(self, limit=5):

        self.cursor.execute("""
            SELECT
                category,
                percentage,
                played_at

            FROM quiz_history

            ORDER BY played_at DESC

            LIMIT ?
        """, (limit,))

        return self.cursor.fetchall()