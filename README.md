# ETL Pipeline for CSV Processing

This project implements a simple, memory-efficient ETL (Extract, Transform, Load) pipeline in Python. The application fetches a CSV file from a URL, processes its contents, and separates the data into two distinct output files based on data validity.

The core of the project is a generator-based pipeline that processes the source file row-by-row, ensuring minimal memory consumption even with very large datasets.

## Features

*   **File Fetching**: Downloads a file from a specified URL using the `requests` library.
*   **Error Handling**: Gracefully handles common HTTP errors, such as `404 Not Found` and `403 Access Denied`.
*   **Memory-Efficient ETL**:
    *   **Extract**: Reads the input CSV file one row at a time.
    *   **Transform**: Validates each row. If a row contains missing values (represented by `-`), it's marked as invalid. For valid rows, it calculates the sum and average of the numerical values.
    *   **Load**: Writes the processed data into two separate files:
        *   `values.csv`: Contains the ID, sum, and average for all valid rows.
        *   `missing.csv`: Contains the ID and the column indices of missing data for all invalid rows.
*   **Performance-Timed**: The main execution function is timed using a simple decorator.
*   **Dependency Management**: Uses Poetry for managing project dependencies and packaging.
*   **Tested**: Includes a suite of `pytest` tests for the ETL and file-fetching logic.

## Installation

1.  **Install Poetry**: If you don't have Poetry, follow the instructions on the official website.

2.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <your-repository-url>
    cd <repository-folder>
    ```
3.  **Install dependencies**: Navigate to the project root and run:
    ```bash
    poetry install
    ```

## Usage

To run the complete ETL process, execute the `main.py` script from the root of the project:

```bash
poetry run main
```

This will:
1.  Download the `sample.csv` file from the hardcoded URL in `main.py`.
2.  Save it to the project's root directory.
3.  Process the file and generate `values.csv` and `missing.csv` in the root directory.
4.  Print the total execution time.

### Running Tests

To run the tests for this project:

```bash
poetry run pytest -v
```


### Building the Project

To build the distributable packages (source archive and wheel):

```bash
poetry build
```

The built packages will be located in the `dist/` directory.

## Project Structure

```
.
├── pyproject.toml
├── poetry.lock
├── README.md
├── LICENSE
├── output/
│   ├── missing.csv
│   ├── values.csv
│   └── latest.csv
├── src/
│   └── poetry/
│       ├── __init__.py
│       ├── decorators.py
│       ├── etl.py
│       ├── exceptions.py
│       ├── file_fetcher.py
│       └── main.py
└── tests/
    ├── __init__.py
    ├── test_decorators.py
    └── test_file_fetcher.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
