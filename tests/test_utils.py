# mypy: disable-error-code="no-untyped-def"


import json
from unittest.mock import mock_open, patch

from src.utils import read_json


def test_read_json_success():
    """Тест успешного чтения корректного JSON."""
    mock_data = [{"id": 1, "name": "test"}]
    json_str = json.dumps(mock_data)

    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=json_str)):
            result = read_json("fake_path.json")
            assert result == mock_data
            assert isinstance(result, list)


def test_read_json_file_not_found(capsys):
    """Тест поведения, если файл не существует."""
    with patch("os.path.exists", return_value=False):
        result = read_json("missing.json")
        assert result == []


def test_read_json_invalid_format(capsys):
    """Тест поведения при некорректном JSON."""
    invalid_json = "{ 'bad': data }"  # Одинарные кавычки и лишние символы

    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=invalid_json)):
            result = read_json("bad.json")
            assert result == []


def test_read_json_unexpected_error(capsys):
    """Тест обработки непредвиденных ошибок (например, кодировка)."""
    with patch("os.path.exists", return_value=True):
        # Имитируем ошибку при попытке чтения
        with patch("builtins.open", side_effect=Exception("Disk error")):
            result = read_json("error.json")
            assert result == []
