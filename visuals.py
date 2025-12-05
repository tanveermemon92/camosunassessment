# visuals.py
import pandas as pd
import matplotlib.pyplot as plt
from data_setup import load_camosun_program_enrollment, load_sector_comparison

plt.style.use("seaborn-v0_8")

def plot_program_trends(output_path="program_trends.png"):
    df = load_camosun_program_enrollment()
    df_long = df.melt(
        id_vars="Program Area",
        value_vars=["2020-21", "2021-22", "2022-23", "2023-24"],
        var_name="Year",
        value_name="Headcount",
    )

    focus_programs = [
        "Arts and Sciences",
        "Health",
        "Business and Management",
        "Personal Improvement and Leisure",
    ]
    df_focus = df_long[df_long["Program Area"].isin(focus_programs)]

    fig, ax = plt.subplots(figsize=(8, 5))
    for program in focus_programs:
        sub = df_focus[df_focus["Program Area"] == program]
        ax.plot(sub["Year"], sub["Headcount"], marker="o", label=program)

    ax.set_title("Camosun Program Headcount Trends (2020/21–2023/24)")
    ax.set_xlabel("Academic Year")
    ax.set_ylabel("Student Headcount")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path, dpi=300)

def plot_2020_vs_2023_bar(output_path="program_2020_vs_2023.png"):
    df = load_camosun_program_enrollment()
    fig, ax = plt.subplots(figsize=(9, 5))

    x = range(len(df))
    width = 0.35

    ax.bar(
        [i - width/2 for i in x],
        df["2020-21"],
        width=width,
        label="2020-21",
    )
    ax.bar(
        [i + width/2 for i in x],
        df["2023-24"],
        width=width,
        label="2023-24",
    )

    ax.set_xticks(list(x))
    ax.set_xticklabels(df["Program Area"], rotation=45, ha="right")
    ax.set_ylabel("Student Headcount")
    ax.set_title("Camosun Headcount by Program: 2020/21 vs 2023/24")
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_path, dpi=300)

def plot_2023_pie(output_path="program_mix_2023.png"):
    df = load_camosun_program_enrollment()
    labels = df["Program Area"]
    sizes = df["2023-24"]

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90,
    )
    ax.set_title("Camosun Program Mix (2023/24)")
    ax.axis("equal")
    fig.tight_layout()
    fig.savefig(output_path, dpi=300)

def plot_sector_decline(output_path="sector_international_decline.png"):
    df = load_sector_comparison()
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(df["Institution"], df["International Decline %"], color="#c0392b")
    ax.set_ylabel("International Enrollment Change (%)")
    ax.set_title("International Enrollment Decline – BC & National Context")
    ax.axhline(0, color="black", linewidth=0.8)
    plt.xticks(rotation=30, ha="right")
    fig.tight_layout()
    fig.savefig(output_path, dpi=300)
