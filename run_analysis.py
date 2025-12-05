# run_analysis.py
from analysis_metrics import compute_program_growth, summarize_health_vs_others
from visuals import (
    plot_program_trends,
    plot_2020_vs_2023_bar,
    plot_2023_pie,
    plot_sector_decline,
)

def main():
    growth = compute_program_growth()
    print("=== Program Growth (2020-21 to 2023-24) ===")
    print(growth.to_string(index=False))

    summary = summarize_health_vs_others()
    print("\n=== Health vs Arts & Sciences Summary ===")
    for k, v in summary.items():
        print(f"{k}: {v:.2f}" if isinstance(v, float) else f"{k}: {v}")

    plot_program_trends()
    plot_2020_vs_2023_bar()
    plot_2023_pie()
    plot_sector_decline()
    print("\nCharts saved as PNG files in the current folder.")

if __name__ == "__main__":
    main()
