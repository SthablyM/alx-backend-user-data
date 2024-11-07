#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated:
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    filter_datum that returns the log message obfuscated
    """
    return re.sub(
            f"({'|'.join(fields)})=[^{separator}]+",
            lambda m: f"{m.group().split('=')[0]}={redaction}", message
            )
