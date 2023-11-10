#!/usr/bin/python3
"""Contains all models used in the app."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
