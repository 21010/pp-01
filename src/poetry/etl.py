from pathlib import Path
import csv


class ETL:
    def __init__(self, input_file: str, values_file: str, missing_file: str):
        self.input_file = Path(input_file).resolve()
        self.values_file = Path(values_file).resolve()
        self.missing_file = Path(missing_file).resolve()

    def _extract(self):
        with open(self.input_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                yield [cell.strip() for cell in row]

    def _transform(self, lines_iterator):
        for line in lines_iterator:
            row_id = line[0]

            missing_indices = [i for i, value in enumerate(line) if value == "-"]

            if missing_indices:
                yield ("missing", (row_id, missing_indices))
            else:
                numbers = [float(val) for val in line[1:]]
                total_sum = sum(numbers)
                average = total_sum / len(numbers) if numbers else 0

                yield ("valid", (row_id, total_sum, average))

    def _load(self, transform_iterator):
        with (
            open(self.values_file, "w", newline="", encoding="utf-8") as f_values,
            open(self.missing_file, "w", newline="", encoding="utf-8") as f_missing,
        ):
            values_writer = csv.writer(f_values)
            missing_writer = csv.writer(f_missing)

            # Zapis nagłówków do plików wyjściowych
            values_writer.writerow(["idx", "sum", "avg"])
            missing_writer.writerow(["idx", "missing_idxs"])

            # Przetwarzanie danych z generatora 'transform' i zapis
            for record_type, data in transform_iterator:
                if record_type == "valid":
                    row_id, total_sum, average = data
                    values_writer.writerow(
                        [row_id, f"{total_sum:.2f}", f"{average:.2f}"]
                    )
                elif record_type == "missing":
                    row_id, indices = data

                    indices_str = ", ".join(map(str, indices))
                    missing_writer.writerow([row_id, indices_str])

    def run_etl(self):
        # E: Extract
        lines_generator = self._extract()
        # T: Transform
        transformed_generator = self._transform(lines_generator)
        # L: Load
        self._load(transformed_generator)
