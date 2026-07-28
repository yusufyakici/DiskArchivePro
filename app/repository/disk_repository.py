"""
DiskArchive Pro v2
Disk Repository
"""

from app.models.disk import Disk
from app.repository.base_repository import BaseRepository


class DiskRepository(BaseRepository):

    TABLE_NAME = "disks"

    def __init__(self, db):

        super().__init__(db)

    # -------------------------------------------------
    # INSERT
    # -------------------------------------------------

    def add(self, disk: Disk):

        cursor = self.execute(
            """
            INSERT INTO disks
            (
                label,
                drive_letter,
                serial_number,
                file_system,
                capacity,
                used_space,
                free_space,
                scan_date
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                disk.label,
                disk.drive_letter,
                disk.serial_number,
                disk.file_system,
                disk.capacity,
                disk.used_space,
                disk.free_space,
                disk.scan_date,
            ),
        )

        disk.id = cursor.lastrowid

        return disk

    # -------------------------------------------------
    # UPDATE
    # -------------------------------------------------

    def update(self, disk: Disk):

        self.execute(
            """
            UPDATE disks
            SET
                label=?,
                serial_number=?,
                file_system=?,
                capacity=?,
                used_space=?,
                free_space=?,
                scan_date=?
            WHERE drive_letter=?
            """,
            (
                disk.label,
                disk.serial_number,
                disk.file_system,
                disk.capacity,
                disk.used_space,
                disk.free_space,
                disk.scan_date,
                disk.drive_letter,
            ),
        )

        return disk

    # -------------------------------------------------
    # SAVE
    # -------------------------------------------------

    def save(self, disk: Disk):

        existing = self.get_by_drive(
            disk.drive_letter
        )

        if existing is None:

            return self.add(disk)

        disk.id = existing.id

        return self.update(disk)

    # -------------------------------------------------
    # GET BY ID
    # -------------------------------------------------

    def get_by_id(self, disk_id):

        row = self.fetchone(
            "SELECT * FROM disks WHERE id=?",
            (disk_id,),
        )

        return (
            Disk(**dict(row))
            if row
            else None
        )

    # -------------------------------------------------
    # GET BY DRIVE
    # -------------------------------------------------

    def get_by_drive(self, drive_letter):

        row = self.fetchone(
            """
            SELECT *
            FROM disks
            WHERE drive_letter=?
            """,
            (drive_letter,),
        )

        return (
            Disk(**dict(row))
            if row
            else None
        )

    # -------------------------------------------------
    # GET ALL
    # -------------------------------------------------

    def get_all(self):

        rows = self.fetchall(
            """
            SELECT *
            FROM disks
            ORDER BY drive_letter
            """
        )

        return [
            Disk(**dict(row))
            for row in rows
        ]

    # -------------------------------------------------
    # GET LAST SCANNED
    # -------------------------------------------------

    def get_last_scanned(self):

        row = self.fetchone(
            """
            SELECT *
            FROM disks
            ORDER BY scan_date DESC
            LIMIT 1
            """
        )

        return (
            Disk(**dict(row))
            if row
            else None
        )

    # -------------------------------------------------
    # DELETE
    # -------------------------------------------------

    def delete(self, disk_id):

        self.delete_by_id(
            self.TABLE_NAME,
            disk_id,
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