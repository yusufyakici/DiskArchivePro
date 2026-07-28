"""
DiskArchive Pro v2
Folder Model
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Folder:

    # -------------------------------------------------
    # Identity
    # -------------------------------------------------

    id: int | None = None

    disk_id: int = 0

    parent_id: int | None = None

    # -------------------------------------------------
    # Folder Information
    # -------------------------------------------------

    name: str = ""

    path: str = ""

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    size: int = 0

    file_count: int = 0

    folder_count: int = 0

    # -------------------------------------------------
    # Dates
    # -------------------------------------------------

    created_at: str = ""

    modified_at: str = ""

    # -------------------------------------------------
    # Helpers
    # -------------------------------------------------

    @property
    def is_root(self) -> bool:

        return self.parent_id is None

    @property
    def level(self) -> int:

        if not self.path:
            return 0

        path = self.path.replace("\\", "/")

        return len(
            [part for part in path.split("/") if part]
        )

    @property
    def has_files(self) -> bool:

        return self.file_count > 0

    @property
    def has_folders(self) -> bool:

        return self.folder_count > 0

    @property
    def is_empty(self) -> bool:

        return (
            self.file_count == 0
            and self.folder_count == 0
        )

    @property
    def total_items(self) -> int:

        return (
            self.file_count +
            self.folder_count
        )

    # -------------------------------------------------
    # String
    # -------------------------------------------------

    def __str__(self):

        return self.path

    # -------------------------------------------------
    # Representation
    # -------------------------------------------------

    def __repr__(self):

        return (
            f"Folder("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"files={self.file_count}, "
            f"folders={self.folder_count})"
        )