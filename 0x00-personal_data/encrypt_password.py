#!/usr/bin/env python3
"""
function that expects one string argument name password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    function that expects one string argument name password
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    function that expects 2 arguments and returns a boolean
    """
    password_bytes = password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password)
