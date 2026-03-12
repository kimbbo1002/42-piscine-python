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
     
    # call data
    url = "https://github.com/chandanverma07/DataSets/blob/master/weight-height.csv"
    df = pd.read_csv("weight-height.csv")
    
    # data manipulation with pandas
    df_clean = df.dropna()
    df_clean['Gender'] = df_clean['Gender'].str.capitalize()
    df_clean = df_clean[df_clean['Gender'].isin(['Male', 'Female'])]

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

    plt.scatter(x_female, y_female, facecolors='none', edgecolors='pink', label='Female', s=50)
    plt.scatter(x_male, y_male, facecolors='none', edgecolors='lightblue', label='Male', s=50)

    plt.axvline(avg_height_male, color='blue', linestyle='--', linewidth=2, label='Male Avg Height/Weight')
    plt.axhline(avg_weight_male, color='blue', linestyle='--', linewidth=2)
    plt.axvline(avg_height_female, color='red', linestyle='--', linewidth=2, label='Female Avg Height/Weight')
    plt.axhline(avg_weight_female, color='red', linestyle='--', linewidth=2)

    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.title("Height and Weight by Gender with Averages")
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
        
main()