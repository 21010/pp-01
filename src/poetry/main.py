from poetry.etl import ETL
from poetry.file_fetcher import FileFetcher
from poetry.decorators import stopwatch


@stopwatch
def main():
    # 1. Pobieranie pliku i zapis do pliku lokalnego
    # adres url pliku
    URL = "https://oleksandr-fedoruk.com/wp-content/uploads/2025/10/sample.csv"
    # nazwa pliku lokalnego
    file_name = URL.split("/")[-1]
    # pobieranie pliku
    FileFetcher.get_and_save_file(URL, file_name)

    # 2. Wczytywanie, transformacja i ładowanie danych
    etl = ETL(
        input_file="output/sample.csv",
        values_file="output/values.csv",
        missing_file="output/missing.csv",
    )

    etl.run_etl()


if __name__ == "__main__":
    main()
