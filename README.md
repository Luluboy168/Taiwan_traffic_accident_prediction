# Taiwan Traffic Accident Dataset Documentation

This repository contains a processed version of the Taiwan Traffic Accident data obtained from the [政府資料開放平台 (Taiwan Government Open Data Portal)](https://data.gov.tw/dataset/12197). The dataset has been prepared for improved predictive modeling by consolidating accident records into single rows.

---

## Table of Contents

- [Overview](#overview)
- [External Source](#external-source)
- [Data Composition](#data-composition)
  - [File Structure](#file-structure)
  - [Rows and Columns](#rows-and-columns)
  - [Data Volume](#data-volume)
- [Data Collection Conditions](#data-collection-conditions)
- [Data Processing and Tools Used](#data-processing-and-tools-used)
- [Original vs. Consolidated Format](#original-vs-consolidated-format)
- [Usage Notes and Limitations](#usage-notes-and-limitations)
- [Citation and Contact](#citation-and-contact)

---

## Overview

This dataset provides records of traffic accidents in Taiwan, categorized into:

- **A1**: Fatal accidents  
- **A2**: Accidents involving only injuries

Each record in the processed dataset corresponds to one accident event. Various accident attributes, such as weather conditions, light conditions, vehicle types, and age groups, are recorded as integers for easier analysis and modeling.

---

## External Source

- **Source**: [政府資料開放平台](https://data.gov.tw/dataset/12197)
- **Original Format**: CSV files containing detailed accident reports **in Chinese**.

  The original data is organized in a **one-person-per-row format**, where each row represents an individual involved in an accident (e.g., driver, passenger, pedestrian). This means that for accidents involving multiple persons, there are multiple rows with the same accident date, time, and location but different details for each person.

---

## Data Composition

### File Structure

The dataset is divided into two categories and further organized by year:  
```
dataset/  
├─ A1  
│ ├─ 108_A1.csv  
│ ├─ 109_A1.csv  
│ ├─ 110_A1.csv  
│ ├─ 111_A1.csv  
│ ├─ 112_A1.csv  
│ └─ 113_A1.csv  
└─ A2  
├─ 108_A2.csv  
├─ 109_A2.csv  
├─ 110_A2.csv  
├─ 111_A2.csv  
├─ 112_A2.csv  
└─ 113_A2.csv
```

- **A1** folder: Fatal accidents across different years.
- **A2** folder: Injury-only accidents for the same years.

### Rows and Columns

After processing, each row in the dataset represents a **single accident**. The following integer-typed columns are included:

1. `發生日期` (Accident Date)
2. `發生時間` (Accident Time)
3. `天候名稱` (Weather) – mapped to integer codes
4. `光線名稱` (Light Condition) – mapped to integer codes
5. `速限-第1當事者` (Speed Limit for the First Party Involved)
6. `路面狀況-路面狀態名稱` (Road Surface Condition) – mapped to integer codes
7. `號誌-號誌種類名稱` (Traffic Signal Type) – mapped to integer codes
8. `male` (Number of Males Involved)
9. `female` (Number of Females Involved)
10. `veh_機車` (Number of Motorcycles)
11. `veh_大客車` (Number of Large Passenger Vehicles)
12. `veh_人` (Number of Pedestrians)
13. `veh_大貨車` (Number of Large Trucks)
14. `veh_小客車(含客、貨兩用)` (Number of Small Passenger/Cargo Vehicles)
15. `veh_慢車` (Number of Slow-Moving Vehicles)
16. `veh_小貨車(含客、貨兩用)` (Number of Small Trucks)
17. `veh_全聯結車` (Number of Full-Trailer Trucks)
18. `veh_曳引車` (Number of Tractor Trucks)
19. `veh_半聯結車` (Number of Semi-Trailer Trucks)
20. `veh_其他車` (Number of Other Vehicles)
21. `veh_特種車` (Number of Special-Purpose Vehicles)
22. `veh_小貨車` (Number of Small Trucks)
23. `veh_軍車` (Number of Military Vehicles)
24. `age_1~10` (Number of People Aged 1–10)
25. `age_11~20` (Number of People Aged 11–20)
26. `age_21~30` (Number of People Aged 21–30)
27. `age_31~40` (Number of People Aged 31–40)
28. `age_41~50` (Number of People Aged 41–50)
29. `age_51~60` (Number of People Aged 51–60)
30. `age_61~70` (Number of People Aged 61–70)
31. `age_71~80` (Number of People Aged 71–80)
32. `age_81~90` (Number of People Aged 81–90)
33. `age_91~100` (Number of People Aged 91–100)
34. `age_101~110` (Number of People Aged 101–110)
35. `age_111~120` (Number of People Aged 111–120)

### Data Volume

- **Rows**: Each processed row corresponds to a single accident event. In contrast, the original data had multiple rows per accident if several individuals were involved.
- **Columns**: All columns are stored as integer types after the mapping process.
- **Overall Size**: Each CSV file may contain thousands of accident records. The complete dataset (across multiple years and categories) includes tens of thousands of accident events.

---

## Data Collection Conditions

- **Time Frame**: Data covers years 108 to 113 in the Minguo calendar (approximately 2019 to 2024 in the Gregorian calendar).
- **Geographical Coverage**: All accidents reported occurred within Taiwan.
- **Accident Severity**: Two distinct categories:
  - **A1**: Fatal accidents
  - **A2**: Accidents involving injuries only
- **Filtering Criteria**:
  - Only records that match predefined mapping criteria (e.g., 天候名稱, 光線名稱, 路面狀況-路面狀態名稱, 號誌-號誌種類名稱) are retained.
  - Rows with missing or unrecognized text in the mapping columns are excluded.

---

## Data Processing and Tools Used

1. **Original Data Download**  
   - The CSV files were downloaded directly from the [政府資料開放平台](https://data.gov.tw/dataset/12197).

2. **Mapping to Numeric Codes**  
   - A Python function `mapping(df)` was used to convert textual descriptions to integer codes. For example:
     ```python
     def mapping(df):
         # Mapping for weather conditions
         weather_map = {
             '晴': 0,
             '陰': 1,
             '雨': 2,
             '霧或煙': 3,
             '風': 4,
             '風沙': 5,
             '雪': 6,
             '強風': 7,
             '暴雨': 8
         }
         df = df[df['天候名稱'].isin(weather_map.keys())]
         df['天候名稱'] = df['天候名稱'].map(weather_map)

         # Mapping for light conditions
         light_map = {
             '有照明未開啟或故障': 0,
             '無照明': 1,
             '有照明且開啟': 2,
             '日間自然光線': 3,
             '夜間(或隧道、地下道、涵洞)有照明': 4,
             '夜間(或隧道、地下道、涵洞)無照明': 5,
             '晨或暮光': 6
         }
         df = df[df['光線名稱'].isin(light_map.keys())]
         df['光線名稱'] = df['光線名稱'].map(light_map)

         # Similar mapping processes for other textual columns...
         
         return df
     ```

3. **Software and Environment**  
   - **Python (Pandas)** was used for data cleaning, mapping, and aggregation.
   - **CSV** format was maintained for the processed dataset.
   - Code editing and data inspection were performed using IDEs like Visual Studio Code.

4. **Hardware**  
   - Standard desktop or laptop computers with sufficient RAM to handle large CSV files.

---

## Original vs. Consolidated Format

- **Original Data**:  
  The CSV files originally contained one row per person involved in an accident. This meant that if multiple individuals were involved in a single accident (e.g., driver, passengers, pedestrians), there were multiple rows with the same accident date/time/location details but different personal information.

- **Consolidated Data (This Dataset)**:  
  In the processed dataset, rows that share the same accident date and time are grouped together into one row. This aggregation summarizes:
  - **Vehicle Involvement**: The count of different types of vehicles involved.
  - **Demographic Information**: The aggregated counts of individuals (by gender and age group).
  
  This consolidation creates an accident-level record that is more suitable for predictive modeling and statistical analysis, ultimately leading to improved model performance.

---

## Usage Notes and Limitations

- **Data Completeness**:  
  Some rows are filtered out if they do not meet the mapping criteria (e.g., unexpected or missing textual values).

- **Interpretation of Codes**:  
  - The integer codes used for weather, light conditions, road surface conditions, and traffic signal types are based on custom mappings. Refer to the mapping dictionaries in the code for interpretation.

- **Granularity**:  
  - Each row represents an entire accident event. Analyses requiring individual-level details (e.g., per-person behavior) will need to refer back to the original dataset.

- **Privacy**:  
  - The dataset contains aggregated counts and does not include personal identifying information.

---

## Citation and Contact

- **Citation**:  
  If you use or publish findings based on this dataset, please cite the Taiwan Government Open Data Portal and reference the dataset [政府資料開放平台, dataset ID: 12197](https://data.gov.tw/dataset/12197).

- **Contact**:  
  For questions regarding the original data or this processing methodology, please consult the data provider’s contact information on the Taiwan Government Open Data Portal or refer to this documentation.

---

