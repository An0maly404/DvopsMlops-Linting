import pytest


def normalize_username(username: str) -> str:
	return username.strip().lower()


def test_normalize_username_strips_whitespace_and_lowercases():
	assert normalize_username("  Alice.Smith  ") == "alice.smith"
