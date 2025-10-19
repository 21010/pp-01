from src.etl import ETL
from src.file_fetcher import FileFetcher
from src.decorators import stopwatch


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
        input_file="sample.csv",
        values_file="values.csv",
        missing_file="missing.csv",
    )

    etl.run_etl()


if __name__ == "__main__":
    main()
