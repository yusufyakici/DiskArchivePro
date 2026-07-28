"""
DiskArchive Pro v2
Base Repository
"""

from abc import ABC


class BaseRepository(ABC):

    def __init__(self, db):

        self.db = db

    # -------------------------------------------------
    # EXECUTE
    # -------------------------------------------------

    def execute(self, sql, parameters=()):

        return self.db.execute(
            sql,
            parameters,
        )

    # -------------------------------------------------
    # EXECUTEMANY
    # -------------------------------------------------

    def executemany(self, sql, values):

        return self.db.executemany(
            sql,
            values,
        )

    # -------------------------------------------------
    # FETCH ONE
    # -------------------------------------------------

    def fetchone(self, sql, parameters=()):

        return self.db.fetchone(
            sql,
            parameters,
        )

    # -------------------------------------------------
    # FETCH ALL
    # -------------------------------------------------

    def fetchall(self, sql, parameters=()):

        return self.db.fetchall(
            sql,
            parameters,
        )

    # -------------------------------------------------
    # SCALAR
    # -------------------------------------------------

    def scalar(self, sql, parameters=()):

        return self.db.scalar(
            sql,
            parameters,
        )

    # -------------------------------------------------
    # BEGIN
    # -------------------------------------------------

    def begin(self):

        self.db.begin()

    # -------------------------------------------------
    # COMMIT
    # -------------------------------------------------

    def commit(self):

        self.db.commit()

    # -------------------------------------------------
    # ROLLBACK
    # -------------------------------------------------

    def rollback(self):

        self.db.rollback()

    # -------------------------------------------------
    # DELETE BY ID
    # -------------------------------------------------

    def delete_by_id(self, table, record_id):

        self.execute(
            f"DELETE FROM {table} WHERE id=?",
            (record_id,),
        )

    # -------------------------------------------------
    # DELETE ALL
    # -------------------------------------------------

    def delete_all(self, table):

        self.execute(
            f"DELETE FROM {table}"
        )

    # -------------------------------------------------
    # COUNT
    # -------------------------------------------------

    def count(self, table):

        value = self.scalar(
            f"SELECT COUNT(*) FROM {table}"
        )

        return value or 0

    # -------------------------------------------------
    # EXISTS
    # -------------------------------------------------

    def exists(self, table, field, value):

        return bool(
            self.scalar(
                f"""
                SELECT 1
                FROM {table}
                WHERE {field}=?
                LIMIT 1
                """,
                (value,),
            )
        )

    # -------------------------------------------------
    # INSERT MANY
    # -------------------------------------------------

    def insert_many(self, sql, values):

        if values:

            self.executemany(
                sql,
                values,
            )
    