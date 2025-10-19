import requests

from requests.exceptions import HTTPError, RequestException
from src.exceptions import NotFoundError, AccessDeniedError


class FileFetcher:
    @staticmethod
    def get_and_save_file(url: str, file_name: str = "latest.csv"):

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            with open(f"output/{file_name}", "wb") as f:
                f.write(response.content)

        except HTTPError as http_err:
            if http_err.response.status_code == 404:
                raise NotFoundError(f"File not found at {url}") from http_err
            elif http_err.response.status_code == 403:
                raise AccessDeniedError(f"Access denied for {url}") from http_err
            else:
                raise http_err
        except RequestException as req_err:
            raise req_err
