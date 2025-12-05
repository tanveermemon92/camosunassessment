# Camosun Program Area Enrollment Analysis (2020/21–2023/24)

## Overview

This project analyzes **Camosun College's program-area enrollment patterns** from 2020/21 to 2023/24 using data from the **BC Post-Secondary Central Data Warehouse "Standard Reports – Program Area Totals" (May 2025 submission)** and Camosun's public program information.[file:69][web:83]

**Goal:** Provide clear, leadership-ready insights and visuals for strategic planning.

## 🎯 Objectives

- Identify notable trends in Camosun's program-area enrollments (Health, Arts & Sciences, Business)
- Quantify growth/decline across years and program areas
- Visualize patterns for **non-technical leadership audience**
- Situate Camosun in broader BC/national sector context (international decline, health expansion)[file:69][web:80]

## 📁 Repository Structure

camosun_enrollment_analysis/
1.data_setup.py # Hard-coded program + sector data setup
2.analysis_metrics.py # Growth calculations + summary metrics
3. visuals.py # Chart creation (PNG outputs)
4. run_analysis.py # Orchestration script
5. README.md # Project documentation (this file)
6. data/ # (Optional) CSVs if you export data later

## 🛠️ File Breakdown

### `data_setup.py`
**Builds pandas DataFrames for:**
- Camosun program-area enrollments (2020/21–2023/24)
- Sector comparison table (BC colleges, universities, national average)[file:69][web:80]

### `analysis_metrics.py`
**Computes:**
- Student growth (absolute + %) by program area (2020/21 vs 2023/24)
- Summary stats: Health vs Arts & Sciences (health share of total enrollment)[file:69]

### `visuals.py`
**Generates PNG charts for reports:**
- 📈 **Line chart**: Key program trends over time
- 📊 **Clustered bar chart**: 2020/21 vs 2023/24 headcount by program
- 🥧 **Pie chart**: 2023/24 program mix
- 📉 **Bar chart**: International enrollment decline by institution/average[file:69][web:80]

### `run_analysis.py`
**Runs full pipeline:**
- Prints growth table + summary metrics to console
- Saves all charts to working directory

## ⚙️ Requirements

**Python 3.9+**
**Packages:**
- `pandas` (data handling)[web:83][web:80]
- `matplotlib` (basic charting)
pip install pandas matplotlib

## 🚀 How to Run

**From project root:**
python run_analysis.py

**Output:**
✅ Formatted growth table + health vs arts summary (terminal)  
✅ Chart PNGs: `program_trends.png`, `program_2020_vs_2023.png`, `program_mix_2023.png`, `sector_international_decline.png`

**Insert PNGs directly into Word, PowerPoint, or presentation tools.**

## 📊 Data Sources

1. **Program Area Totals**: "Standard Reports – Program Area Totals" PDF, BC Ministry of Post-Secondary Education & Future Skills, Post-Secondary Central Data Warehouse, May 2025 submission (Camosun College excerpt)[file:69]
2. **Camosun Context**: Public information about programs + strategic priorities from Camosun website[web:83]

*Code uses hard-coded values from Camosun section of Program Area report. Replace with CSV imports or database connections as needed.*[file:69][web:80]

## 🔮 Extending the Project

**Future enhancements:**
- Replace hard-coded data → CSVs from official reports
- Add filters/arguments to `run_analysis.py` (e.g., focus Health only)
- Export tables → CSV/Excel for non-technical users
- Mirror visuals in **Tableau** using same data structure for interactive dashboards

---

**Last Updated:** December 5, 2025  
**Data Period:** 2020/21–2023/24  
