"""
DiskArchive Pro v2
Disk Model
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Disk:

    # -------------------------------------------------
    # Identity
    # -------------------------------------------------

    id: int | None = None

    # -------------------------------------------------
    # Disk Information
    # -------------------------------------------------

    label: str = ""

    drive_letter: str = ""

    serial_number: str = ""

    file_system: str = ""

    # -------------------------------------------------
    # Capacity
    # -------------------------------------------------

    capacity: int = 0

    used_space: int = 0

    free_space: int = 0

    # -------------------------------------------------
    # Scan
    # -------------------------------------------------

    scan_date: str = ""

    # -------------------------------------------------
    # Helpers
    # -------------------------------------------------

    @property
    def used_percent(self) -> float:

        if self.capacity <= 0:
            return 0.0

        return round(
            (self.used_space / self.capacity) * 100,
            2,
        )

    @property
    def free_percent(self) -> float:

        if self.capacity <= 0:
            return 0.0

        return round(
            (self.free_space / self.capacity) * 100,
            2,
        )

    @property
    def is_scanned(self) -> bool:

        return bool(self.scan_date)

    # -------------------------------------------------
    # String
    # -------------------------------------------------

    def __str__(self):

        return f"{self.drive_letter} ({self.label})"

    # -------------------------------------------------
    # Representation
    # -------------------------------------------------

    def __repr__(self):

        return (
            f"Disk("
            f"id={self.id}, "
            f"drive_letter='{self.drive_letter}', "
            f"label='{self.label}', "
            f"capacity={self.capacity})"
        )