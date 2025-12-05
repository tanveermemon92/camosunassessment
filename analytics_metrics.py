# analysis_metrics.py
import pandas as pd
from data_setup import load_camosun_program_enrollment

def compute_program_growth():
    df = load_camosun_program_enrollment()
    df["2020-21"] = df["2020-21"].astype(float)
    df["2023-24"] = df["2023-24"].astype(float)

    df_growth = pd.DataFrame({
        "Program Area": df["Program Area"],
        "2020-21": df["2020-21"],
        "2023-24": df["2023-24"],
    })
    df_growth["Growth Students"] = df_growth["2023-24"] - df_growth["2020-21"]
    df_growth["Growth %"] = (
        df_growth["Growth Students"] / df_growth["2020-21"]
    ) * 100

    return df_growth.sort_values("Growth %", ascending=False)

def summarize_health_vs_others():
    df = load_camosun_program_enrollment()
    total_2023 = df["2023-24"].sum()
    health_2023 = df.loc[df["Program Area"] == "Health", "2023-24"].iloc[0]
    health_share = health_2023 / total_2023 * 100

    arts_2020 = df.loc[df["Program Area"] == "Arts and Sciences", "2020-21"].iloc[0]
    arts_2023 = df.loc[df["Program Area"] == "Arts and Sciences", "2023-24"].iloc[0]
    arts_growth_abs = arts_2023 - arts_2020
    arts_growth_pct = arts_growth_abs / arts_2020 * 100

    return {
        "health_2023_headcount": health_2023,
        "health_2023_share_pct": health_share,
        "arts_growth_abs": arts_growth_abs,
        "arts_growth_pct": arts_growth_pct,
    }
