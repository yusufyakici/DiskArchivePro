"""
DiskArchive Pro v2
File Repository
"""

from collections import Counter

from app.models.file import File
from app.repository.base_repository import BaseRepository
from app.utils.logger import Logger


class FileRepository(BaseRepository):

    TABLE_NAME = "files"

    def __init__(self, db):

        super().__init__(db)

    # -------------------------------------------------
    # INSERT
    # -------------------------------------------------

    def add(self, file: File):

        cursor = self.execute(
            """
            INSERT INTO files
            (
                disk_id,
                folder_id,
                name,
                extension,
                full_path,
                size,
                created_at,
                modified_at,
                hash
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                file.disk_id,
                file.folder_id,
                file.name,
                file.extension,
                file.full_path,
                file.size,
                file.created_at,
                file.modified_at,
                file.hash,
            ),
        )

        file.id = cursor.lastrowid

        return file

    # -------------------------------------------------
    # INSERT MANY
    # -------------------------------------------------

    def add_many(self, files):

        if not files:
            return

        for file in files:

            try:

                self.add(file)

            except Exception:

                print("=" * 60)
                print("HATALI DOSYA")
                print("Name      :", file.name)
                print("Path      :", file.full_path)
                print("Disk ID   :", file.disk_id)
                print("Folder ID :", file.folder_id)
                print("=" * 60)

                raise
    # -------------------------------------------------
    # GET BY ID
    # -------------------------------------------------

    def get_by_id(self, file_id):

        row = self.fetchone(
            """
            SELECT *
            FROM files
            WHERE id=?
            """,
            (file_id,),
        )

        if row is None:

            return None

        return File(**dict(row))

    # -------------------------------------------------
    # GET ALL
    # -------------------------------------------------

    def get_all(self):

        rows = self.fetchall(
            """
            SELECT *
            FROM files
            ORDER BY full_path
            """
        )

        return [

            File(**dict(row))

            for row in rows

        ]

    # -------------------------------------------------
    # SEARCH
    # -------------------------------------------------

    def search(self, filters):

        sql = """
        SELECT *
        FROM files
        WHERE 1=1
        """

        parameters = []

        if filters.get("name"):

            sql += " AND name LIKE ?"

            parameters.append(
                f"%{filters['name']}%"
            )

        if filters.get("extension"):

            sql += " AND extension=?"

            parameters.append(
                filters["extension"]
            )

        if filters.get("min_size") is not None:

            sql += " AND size>=?"

            parameters.append(
                filters["min_size"]
            )

        if filters.get("max_size") is not None:

            sql += " AND size<=?"

            parameters.append(
                filters["max_size"]
            )

        if filters.get("date"):

            sql += " AND created_at LIKE ?"

            parameters.append(
                f"{filters['date']}%"
            )

        sql += " ORDER BY size DESC"

        rows = self.fetchall(
            sql,
            tuple(parameters),
        )

        return [

            File(**dict(row))

            for row in rows

        ]

    # -------------------------------------------------
    # GET LARGEST
    # -------------------------------------------------

    def get_largest(self, limit=10):

        rows = self.fetchall(
            """
            SELECT *
            FROM files
            ORDER BY size DESC
            LIMIT ?
            """,
            (limit,),
        )

        return [

            File(**dict(row))

            for row in rows

        ]

    # -------------------------------------------------
    # TOTAL SIZE
    # -------------------------------------------------

    def total_size(self):

        value = self.scalar(
            """
            SELECT SUM(size)
            FROM files
            """
        )

        return value or 0

    # -------------------------------------------------
    # EMPTY COUNT
    # -------------------------------------------------

    def empty_count(self):

        value = self.scalar(
            """
            SELECT COUNT(*)
            FROM files
            WHERE size=0
            """
        )

        return value or 0

    # -------------------------------------------------
    # EXTENSION STATISTICS
    # -------------------------------------------------

    def extension_statistics(self):

        return self.fetchall(
            """
            SELECT
                extension,
                COUNT(*) AS file_count,
                SUM(size) AS total_size
            FROM files
            GROUP BY extension
            ORDER BY file_count DESC
            """
        )

    # -------------------------------------------------
    # DELETE
    # -------------------------------------------------

    def delete(self, file_id):

        self.delete_by_id(
            self.TABLE_NAME,
            file_id,
        )

    # -------------------------------------------------
    # DELETE ALL
    # -------------------------------------------------

    def clear(self):

        self.delete_all(
            self.TABLE_NAME,
        )

    # -------------------------------------------------
    # COUNT
    # -------------------------------------------------

    def count(self):

        return super().count(
            self.TABLE_NAME,
        )