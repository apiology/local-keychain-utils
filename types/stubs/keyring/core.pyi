# https://github.com/jaraco/keyring/blob/master/keyring/core.py

from . import backend


def load_keyring(keyring_name: str) -> backend.KeyringBackend:
    ...
