"""
DiskArchive Pro v2
Formatter Utilities
"""

from datetime import datetime


# -------------------------------------------------
# SIZE
# -------------------------------------------------

def format_size(size):

    """
    Byte değerini okunabilir hale çevirir.
    """

    if size is None:
        return "0 B"

    try:
        size = float(size)
    except (TypeError, ValueError):
        return "0 B"

    units = [
        "B",
        "KB",
        "MB",
        "GB",
        "TB",
        "PB",
    ]

    index = 0

    while size >= 1024 and index < len(units) - 1:

        size /= 1024

        index += 1

    if index == 0:
        return f"{int(size)} {units[index]}"

    return f"{size:.2f} {units[index]}"


# -------------------------------------------------
# NUMBER
# -------------------------------------------------

def format_number(value):

    """
    Sayıları binlik ayırıcı ile gösterir.
    """

    try:
        return f"{int(value):,}".replace(",", ".")
    except Exception:
        return "0"


# -------------------------------------------------
# DATE
# -------------------------------------------------

def format_date(value):

    """
    Tarihi okunabilir hale getirir.
    """

    if not value:
        return ""

    if isinstance(value, datetime):
        return value.strftime("%d.%m.%Y")

    return str(value)


# -------------------------------------------------
# DATETIME
# -------------------------------------------------

def format_datetime(value):

    """
    Tarih + saat formatı.
    """

    if not value:
        return ""

    if isinstance(value, datetime):
        return value.strftime("%d.%m.%Y %H:%M:%S")

    return str(value)


# -------------------------------------------------
# DURATION
# -------------------------------------------------

def format_duration(seconds):

    """
    Saniyeyi HH:MM:SS formatına çevirir.
    """

    if seconds is None:
        return "00:00:00"

    seconds = int(seconds)

    hours = seconds // 3600

    minutes = (seconds % 3600) // 60

    seconds = seconds % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"


# -------------------------------------------------
# PERCENT
# -------------------------------------------------

def format_percent(value, total):

    """
    Yüzde hesaplar.
    """

    if total == 0:
        return "0%"

    return f"{(value / total) * 100:.2f}%"


# -------------------------------------------------
# YES / NO
# -------------------------------------------------

def format_bool(value):

    return "Evet" if value else "Hayır"