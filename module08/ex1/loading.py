import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from importlib.metadata import version


def check_dependencies() -> None:
    print("\nChecking dependencies:")
    try:
        print(f"[OK] pandas ({version('pandas')}) - Data manipulation ready")
    except Exception:
        raise ValueError(f"[KO] pandas is missing")

    try:
        print(f"[OK] numpy ({version('numpy')}) - Numeric computation ready")
    except Exception:
        raise ValueError("[KO] numpy is missing")

    try:
        print(f"[OK] requests ({version('requests')}) - Network access ready")
    except Exception:
        raise ValueError("[KO] requests is missing")

    try:
        print(f"[OK] matplotlib ({version('matplotlib')}) - Visualization ready")
    except Exception:
        raise ValueError("[KO] matplotlib is missing")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...")
    try:
        check_dependencies()
    except Exception as e:
        print(e)

    data = [
        ["Gender", "Height", "Weight"],
        ["Male", 73.847017017515, 241.893563180437],
        ["Male", pd.NA, 162.310472521300],
        ["Male", 74.1101053917849, 212.7408555565],
        ["Male", 71.7309784033377, 220.042470303077],
        ["Male", 69.8817958611153, 206.349800623871],
        ["Male", 67.2530156878065, 152.212155757083],
        ["Male", 68.7850812516616, 183.927888604031],
        ["Male", 68.3485155115879, 167.971110489509],
        ["Male", 67.018949662883, 175.92944039571],
        ["Male", 63.4564939783664, 156.399676387112],
        ["Male", 71.1953822829745, 186.604925560358],
        ["Male", 71.6408051192206, 213.741169489411],
        ["Male", 64.7663291334055, 167.127461073476],
        ["Male", 69.2830700967204, 189.446181386738],
        ["Male", 69.2437322298112, 186.434168021239],
        ["Male", 67.6456197004212, 172.186930058117],
        ["Male", 72.4183166259878, 196.028506330482],
        ["Male", 63.974325721061, 172.883470208780],
        ["Male", 69.6400598997523, 185.983957573130],
        ["Female", 58.9107320370127, 102.088326367840],
        ["Female", 65.2300125077128, 141.305822601420],
        ["Female", 63.3690037584139, 131.041402692995],
        ["Female", 64.4799974256081, 128.171511221632],
        ["Female", 61.7930961472815, 129.781407047572],
        ["Female", 65.9680189539591, 156.802082613991],
        ["Female", 62.8503786429821, 114.969038250962],
        ["Female", 65.6521564350254, 165.083001212576],
        ["Female", 61.8902337378544, 111.676199211845],
        ["Female", 63.6778681520585, pd.NA],
        ["Female", 68.1011722359871, 166.575660760601],
        ["Female", 61.7988785298549, 106.233686988457],
        ["Female", 63.3714589617276, 128.118169123676],
        ["Female", 58.8958863500041, 101.682613361014],
        ["Female", 58.4382490995692, 98.1926209281421],
        ["Female", 60.809798678611, 126.915463276282],
        ["Female", 70.1286528332314, 151.254270351714],
        ["Female", 62.2574296463807, 115.797393408160],
        ["Female", 61.7350902197, 107.866872355221],
        ["Female", 63.0595566947049, 145.589929145704],
    ]
    header = data[0]
    rows = data[1:]
    df = pd.DataFrame(rows, columns=header)
    print(df.head())

    # data manipulation with pandas
    df_clean = df.dropna()
    df_clean['Gender'] = df_clean['Gender'].str.capitalize()
    df_clean = df_clean[df_clean['Gender'].isin(['Male', 'Female'])]
    print(df_clean.head())

    male_mask = df_clean['Gender'] == 'Male'
    female_mask = df_clean['Gender'] == 'Female'

    x_male = df_clean['Height'][male_mask]
    y_male = df_clean['Weight'][male_mask]

    x_female = df_clean['Height'][female_mask]
    y_female = df_clean['Weight'][female_mask]

    # numerical computation with numpy
    avg_height_male = np.mean(x_male)
    avg_weight_male = np.mean(y_male)

    avg_height_female = np.mean(x_female)
    avg_weight_female = np.mean(y_female)

    # plotting with matplotlib
    plt.figure(figsize=(10,6))

    plt.scatter(x_female, y_female, facecolors='none', edgecolors='red', label='Female', s=50)
    plt.scatter(x_male, y_male, facecolors='none', edgecolors='blue', label='Male', s=50)

    plt.axvline(avg_height_male, color='lightblue', linestyle='--', linewidth=2, label='Male Avg Height/Weight')
    plt.axhline(avg_weight_male, color='lightblue', linestyle='--', linewidth=2)
    plt.axvline(avg_height_female, color='pink', linestyle='--', linewidth=2, label='Female Avg Height/Weight')
    plt.axhline(avg_weight_female, color='pink', linestyle='--', linewidth=2)

    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.title("Height and Weight by Gender with Averages")
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: 'matrix_analysis.png'")


if __name__ == "__main__":
    main()
