import requests
import pandas as pd
from pathlib import Path

CONSTANTS = {"RESULTS_DIR": Path(__file__).parent}


class constants:
    RESULTS_DIR = Path(__file__).parent


def save_some_data():
    df = pd.DataFrame([[1, 3], [2, 4], [3, 5]])
    df.to_csv(CONSTANTS["RESULTS_DIR"] / "output.csv", index=False)


def check_resource_availability():
    iiasa_pages = [
        "data.ece.iiasa.ac.at",
        "mis5.iiasa.ac.at",
        "iiasa.ac.at",
        "data.ece.iiasa.ac.at/ngfs",
        "wiki.ece.iiasa.ac.at",
    ]
    all_online = all(
        requests.get(f"https://{page}").status_code == 200 for page in iiasa_pages
    )

    return all_online


if __name__ == "__main__":
    save_some_data()
    print(check_resource_availability())
