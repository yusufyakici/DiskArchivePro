"""
DiskArchive Pro v2
Search Parser
"""

import re


class SearchParser:

    def __init__(self):

        self.filters = {}

    # -------------------------------------------------
    # PARSE
    # -------------------------------------------------

    def parse(self, text):

        self.filters = {

            "name": None,
            "extension": None,
            "disk": None,
            "min_size": None,
            "max_size": None,
            "date": None,

        }

        if not text:

            return self.filters

        words = text.strip().split()

        for word in words:

            word = word.strip()

            # ext:pdf

            if word.startswith("ext:"):

                ext = word[4:].lower()

                if ext and not ext.startswith("."):

                    ext = "." + ext

                self.filters["extension"] = ext

                continue

            # disk:D

            if word.startswith("disk:"):

                self.filters["disk"] = word[5:].upper()

                continue

            # name:test

            if word.startswith("name:"):

                self.filters["name"] = word[5:]

                continue

            # size>100MB

            if word.startswith("size>"):

                self.filters["min_size"] = self.parse_size(
                    word[5:]
                )

                continue

            # size<2GB

            if word.startswith("size<"):

                self.filters["max_size"] = self.parse_size(
                    word[5:]
                )

                continue

            # date:2026

            if word.startswith("date:"):

                self.filters["date"] = word[5:]

                continue

            # Normal Search

            if self.filters["name"] is None:

                self.filters["name"] = word

        return self.filters

    # -------------------------------------------------
    # SIZE PARSER
    # -------------------------------------------------

    def parse_size(self, value):

        value = value.strip().upper()

        match = re.fullmatch(
            r"([\d\.]+)(B|KB|MB|GB|TB)?",
            value,
        )

        if not match:

            return None

        number = float(match.group(1))

        unit = match.group(2) or "B"

        multipliers = {

            "B": 1,
            "KB": 1024,
            "MB": 1024 ** 2,
            "GB": 1024 ** 3,
            "TB": 1024 ** 4,

        }

        return int(number * multipliers[unit])