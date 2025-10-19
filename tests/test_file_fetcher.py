import os
import pytest
from src.file_fetcher import FileFetcher
from src.exceptions import AccessDeniedError, NotFoundError


@pytest.fixture(autouse=True)
def clean_files():
    files = [
        "output/sample.csv",
        "output/latest.csv",
    ]
    for file in files:
        if os.path.exists(file):
            os.remove(file)


def test_correct_url():
    url = "https://oleksandr-fedoruk.com/wp-content/uploads/2025/10/sample.csv"
    FileFetcher.get_and_save_file(url, "sample.csv")
    assert os.path.exists("output/sample.csv") is True
    FileFetcher.get_and_save_file(url)
    assert os.path.exists("output/latest.csv") is True


def test_404_error(capsys):
    url = "https://mock.httpstatus.io/404"
    capsys.disabled = True
    with pytest.raises(NotFoundError):
        FileFetcher.get_and_save_file(url)
    assert os.path.exists("output/latest.csv") is False


def test_403_error(capsys):
    url = "https://mock.httpstatus.io/403"
    capsys.disabled = True
    with pytest.raises(AccessDeniedError):
        FileFetcher.get_and_save_file(url)
    assert os.path.exists("output/latest.csv") is False


def test_service_unavailable(capsys):
    url = "https://mock.httpstatus.io/503"
    capsys.disabled = True
    with pytest.raises(Exception):
        FileFetcher.get_and_save_file(url)
    assert os.path.exists("output/latest.csv") is False
