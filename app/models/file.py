"""
DiskArchive Pro v2
File Model
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class File:

    # -------------------------------------------------
    # Identity
    # -------------------------------------------------

    id: int | None = None

    disk_id: int = 0

    folder_id: int = 0

    # -------------------------------------------------
    # File Information
    # -------------------------------------------------

    name: str = ""

    extension: str = ""

    full_path: str = ""

    # -------------------------------------------------
    # Size
    # -------------------------------------------------

    size: int = 0

    # -------------------------------------------------
    # Dates
    # -------------------------------------------------

    created_at: str = ""

    modified_at: str = ""

    # -------------------------------------------------
    # Hash
    # -------------------------------------------------

    hash: str = ""

    # -------------------------------------------------
    # Helpers
    # -------------------------------------------------

    @property
    def filename(self) -> str:

        return Path(self.full_path).name

    @property
    def directory(self) -> str:

        return str(
            Path(self.full_path).parent
        )

    @property
    def suffix(self) -> str:

        return Path(
            self.full_path
        ).suffix.lower()

    @property
    def is_hidden(self) -> bool:

        return self.name.startswith(".")

    @property
    def is_empty(self) -> bool:

        return self.size == 0

    @property
    def formatted_size(self) -> str:

        size = float(self.size)

        units = (
            "B",
            "KB",
            "MB",
            "GB",
            "TB",
            "PB",
        )

        for unit in units:

            if size < 1024:

                return f"{size:.2f} {unit}"

            size /= 1024

        return f"{size:.2f} PB"

    # -------------------------------------------------
    # String
    # -------------------------------------------------

    def __str__(self):

        return self.full_path

    # -------------------------------------------------
    # Representation
    # -------------------------------------------------

    def __repr__(self):

        return (
            f"File("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"size={self.size}, "
            f"extension='{self.extension}')"
        )