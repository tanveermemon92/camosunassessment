Camosun Program Area Enrollment Analysis (2020/21–2023/24)
Overview
This project analyzes Camosun College’s program‑area enrollment patterns from 2020/21 to 2023/24 using data from the BC Post‑Secondary Central Data Warehouse “Standard Reports – Program Area Totals” (May 2025 submission) and Camosun’s public program information. The goal is to provide clear, leadership‑ready insights and visuals for strategic planning.​​

Objectives
Identify notable trends in Camosun’s program‑area enrollments (e.g., Health, Arts & Sciences, Business).​

Quantify growth/decline across years and program areas.

Visualize these patterns for a non‑technical leadership audience.

Situate Camosun in the broader BC and national sector context (e.g., international enrollment decline, health‑program expansion).​​

Repository Structure
Suggested structure:

text
camosun_enrollment_analysis/
├── data_setup.py              # Hard‑coded program and sector data setup
├── analysis_metrics.py        # Growth calculations and summary metrics
├── visuals.py                 # Chart creation (PNG outputs)
├── run_analysis.py            # Orchestration script
├── README.md                  # Project documentation (this file)
└── data/                      # (Optional) CSVs if you export data later
data_setup.py

Builds pandas DataFrames for:

Camosun program‑area enrollments (2020/21–2023/24).

Sector comparison table (BC colleges, universities, national average).​​

analysis_metrics.py

Computes:

Student growth (absolute and %) by program area between 2020/21 and 2023/24.

Summary stats for Health vs Arts & Sciences (e.g., health share of total enrollment).​

visuals.py

Generates PNG charts suitable for reports:

Line chart: key program trends over time.

Clustered bar chart: 2020/21 vs 2023/24 headcount by program.

Pie chart: 2023/24 program mix.

Bar chart: international enrollment decline by institution/average.​​

run_analysis.py

Runs the full pipeline:

Prints growth table and summary metrics to the console.

Saves all charts to the working directory.

Requirements
Python 3.9+ (or similar)

Packages:

pandas (data handling)​

matplotlib (basic charting)

Install dependencies:

bash
pip install pandas matplotlib
How to Run
From the project root:

bash
python run_analysis.py
This will:

Output a formatted growth table and health vs arts summary in the terminal.

Create chart image files (e.g., program_trends.png, program_2020_vs_2023.png, program_mix_2023.png, sector_international_decline.png).

You can insert these PNGs directly into Word, PowerPoint, or other presentation tools.

Data Sources
Program Area Totals: “Standard Reports – Program Area Totals” PDF, BC Ministry of Post‑Secondary Education & Future Skills, Post‑Secondary Central Data Warehouse, May 2025 submission (Camosun College excerpt).​

Camosun Context: Public information about Camosun’s programs and strategic priorities from its website.​

The code currently uses hard‑coded values copied from the Camosun portion of the Program Area report; you can later replace these with CSV imports or direct database connections if needed.​​

Extending the Project
Ideas for extensions:

Replace hard‑coded data with CSVs downloaded or transcribed from the official reports.

Add filters/arguments in run_analysis.py (e.g., focus only on Health vs all others).

Export tables to CSV or Excel for sharing with non‑technical users.

Mirror visuals in Tableau using the same data structure for interactive dashboards.
