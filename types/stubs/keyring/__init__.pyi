# https://github.com/jaraco/keyring/blob/master/keyring/core.py

from . import backend


def set_keyring(keyring: backend.KeyringBackend) -> None:
    ...


def get_keyring() -> backend.KeyringBackend:
    ...


def get_password(service_name: str, username: str) -> str:
    ...


def set_password(service_name: str, username: str, password: str) -> None:
    ...


def delete_password(service_name: str, username: str) -> None:
    ...
