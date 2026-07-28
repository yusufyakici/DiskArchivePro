"""
DiskArchive Pro v2
Folder Repository
"""

from app.models.folder import Folder
from app.repository.base_repository import BaseRepository


class FolderRepository(BaseRepository):

    TABLE_NAME = "folders"

    def __init__(self, db):

        super().__init__(db)

    # -------------------------------------------------
    # INSERT
    # -------------------------------------------------

    def add(self, folder: Folder):

        cursor = self.execute(
            """
            INSERT INTO folders
            (
                disk_id,
                parent_id,
                name,
                path,
                size,
                file_count,
                folder_count,
                created_at,
                modified_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                folder.disk_id,
                folder.parent_id,
                folder.name,
                folder.path,
                folder.size,
                folder.file_count,
                folder.folder_count,
                folder.created_at,
                folder.modified_at,
            ),
        )

        folder.id = cursor.lastrowid

        return folder

    # -------------------------------------------------
    # SAVE ALL
    # -------------------------------------------------

    def save_all(self, folders):

        from os.path import normcase, normpath

        folder_map = {}

        for folder in folders:

            saved = self.add(folder)

            folder_map[
                normcase(normpath(saved.path))
            ] = saved.id

        return folder_map

    # -------------------------------------------------
    # UPDATE PARENT IDS
    # -------------------------------------------------

    def update_parent_ids(self, folders):

        for folder in folders:

            self.execute(
                """
                UPDATE folders
                SET parent_id=?
                WHERE id=?
                """,
                (
                    folder.parent_id,
                    folder.id,
                ),
            )

    # -------------------------------------------------
    # GET BY ID
    # -------------------------------------------------

    def get_by_id(self, folder_id):

        row = self.fetchone(
            "SELECT * FROM folders WHERE id=?",
            (folder_id,),
        )

        return Folder(**dict(row)) if row else None

    # -------------------------------------------------
    # GET BY PATH
    # -------------------------------------------------

    def get_by_path(self, path):

        row = self.fetchone(
            """
            SELECT *
            FROM folders
            WHERE path=?
            """,
            (path,),
        )

        return Folder(**dict(row)) if row else None

    # -------------------------------------------------
    # GET ALL
    # -------------------------------------------------

    def get_all(self):

        rows = self.fetchall(
            """
            SELECT *
            FROM folders
            ORDER BY path
            """
        )

        return [
            Folder(**dict(row))
            for row in rows
        ]

    # -------------------------------------------------
    # GET LARGEST
    # -------------------------------------------------

    def get_largest(self, limit=10):

        rows = self.fetchall(
            """
            SELECT *
            FROM folders
            ORDER BY size DESC
            LIMIT ?
            """,
            (limit,),
        )

        return [
            Folder(**dict(row))
            for row in rows
        ]

    # -------------------------------------------------
    # SEARCH
    # -------------------------------------------------

    def search(self, keyword):

        rows = self.fetchall(
            """
            SELECT *
            FROM folders
            WHERE name LIKE ?
            ORDER BY name
            """,
            (f"%{keyword}%",),
        )

        return [
            Folder(**dict(row))
            for row in rows
        ]

    # -------------------------------------------------
    # EMPTY COUNT
    # -------------------------------------------------

    def empty_count(self):

        value = self.scalar(
            """
            SELECT COUNT(*)
            FROM folders
            WHERE file_count=0
              AND folder_count=0
            """
        )

        return value or 0

    # -------------------------------------------------
    # TOTAL SIZE
    # -------------------------------------------------

    def total_size(self):

        value = self.scalar(
            """
            SELECT SUM(size)
            FROM folders
            """
        )

        return value or 0

    # -------------------------------------------------
    # DELETE
    # -------------------------------------------------

    def delete(self, folder_id):

        self.delete_by_id(
            self.TABLE_NAME,
            folder_id,
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