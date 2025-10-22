import datetime


def stopwatch(func):
    def wrapper(*args, **kwargs):
        print(
            f"Start procesu ETL - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        result = func(*args, **kwargs)
        print(
            f"Koniec procesu ETL - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        return result

    return wrapper
