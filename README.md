# Taiwan Traffic Accident Data (A1 & A2)

This repository contains processed traffic accident records from Taiwan, covering the years 108 (2019) to 113 (2024). The dataset is split into two main categories:

- **A1**: Fatal accidents (致死車禍)  
- **A2**: Accidents involving only injuries (不含死亡之傷害事故)

Each row in the dataset represents a single accident event (rather than a single person), with columns indicating various attributes such as date/time, weather, road condition, and counts of people involved.

---

## Table of Contents

1. [Overview](#overview)  
2. [External Source](#external-source)  
3. [Data Processing and Tools Used](#data-processing-and-tools-used)  
4. [Data Composition and Amount](#data-composition-and-amount)  
5. [Data Collection Conditions](#data-collection-conditions)  
6. [Examples](#examples)  
7. [Final Remarks](#final-remarks)

---

## 1. Overview

This dataset provides a consolidated view of Taiwan’s traffic accidents by aggregating person-level information (from the original government open data) into accident-level records. The main objectives of this dataset are to facilitate:

- **Predictive modeling**: e.g., classifying accidents as fatal (A1) vs. injury-only (A2).  
- **Statistical analysis**: e.g., exploring correlations between road conditions and accident severity.

Each record corresponds to a single accident, providing key information such as date, time, weather, road condition, traffic signals, and counts of people/vehicles involved by category.

---

## 2. External Source

- **Source**: [政府資料開放平台 - 歷史交通事故資料](https://data.gov.tw/)  
- **Original Format**: Multiple CSV files, each row representing one person involved in an accident. If multiple people were involved, the accident data was repeated in multiple rows with some shared fields (date/time/location) and some differing (e.g., personal info, vehicle type).

---

## 3. Data Processing and Tools Used

1. **Original Data Download**  
   - CSV files were downloaded directly from the [政府資料開放平台](https://data.gov.tw/).

2. **Data Analysis**  
   - Inspected and confirmed the data formats and representations (e.g., column names, types).

3. **Data Combining and Cleaning**  
   - Data was originally split by year (and for A2, also by month).  
   - CSVs were merged into two categories (A1, A2).  
   - Missing or invalid values were removed to ensure data integrity.

4. **Mapping to Numeric Codes**  
   - Categorical labels (e.g., weather, lighting, road condition) were mapped to integer codes to facilitate machine learning and statistical modeling.

5. **Accident-Level Aggregation**  
   - Original rows were person-level, but to better predict accident severity or analyze accident-level features, data was aggregated by accident.  
   - Relevant attributes (e.g., counts of people by age range, vehicle types) were summed or otherwise combined into a single row per accident.

6. **Software and Environment**  
   - **Python** (pandas, scikit-learn) for data processing.  
   - **CSV** format for storing processed data.  
   - **Jupyter Notebooks** & Excel for code editing and data inspection.

7. **Hardware**  
   - Standard desktop/laptop with sufficient RAM to handle large CSV files.  
   - No specialized hardware (e.g., GPUs) required.

---

## 4. Data Composition and Amount

### 4.1 File Structure
```
dataset/  
├── train/   
│ ├── A1.csv  
│ └── A2.csv  
└── test/  
  ├── A1.csv  
  └── A2.csv
```

- **A1.csv**: Fatal accidents (years 108–113).  
- **A2.csv**: Injury-only accidents (years 108–113).

### 4.2 Rows and Columns

- **Rows**: Each row represents a single accident.  
- **Columns**:  

  1. `date`, `time`  
     - Accident date and time (`HHMMSS` format for time).  
  2. `weather`  
     - Mapped to integers, e.g., 晴 (0), 陰 (1), 雨 (2), 霧或煙 (3), 風 (4), 風沙 (5), 雪 (6), 強風 (7), 暴雨 (8).  
  3. `lighting`  
     - Mapped to integers, e.g., 有照明未開啟或故障 (0), 無照明 (1), 有照明且開啟 (2), 日間自然光線 (3), 夜間有照明 (4), 夜間無照明 (5), 晨或暮光 (6).  
  4. `speed_limit`  
     - The speed limit (in km/h) where the accident occurred.  
  5. `road_condition`  
     - Mapped to integers, e.g., 乾燥 (0), 濕潤 (1), 泥濘 (2), 油滑 (3), 冰雪 (4).  
  6. `traffic_sign` (or `traffic_signal`)  
     - Mapped to integers, e.g., 無號誌 (0), 閃光號誌 (1), 行車管制號誌(附設行人專用號誌) (2), 行車管制號誌 (3).  
  7. `male`, `female`  
     - Number of males and females involved.  
  8. `veh_*` (e.g. `veh_scooter`, `veh_car`, etc.)  
     - Count of each vehicle type involved.  
  9. `age_*` (e.g. `age_21~30`, `age_61~70`, etc.)  
     - Count of people in each age range.

### 4.3 Data Volume

- **A1**: 10,399 records (split ~70% in `train`, ~30% in `test`).  
- **A2**: 1,583,818 records (split ~70% in `train`, ~30% in `test`).

---

## 5. Data Collection Conditions

1. **Time Frame**  
   - Covers years 108 to 113 (2019–2024).
2. **Geographical Coverage**  
   - All accidents occurred in Taiwan.
3. **Accident Severity**  
   - **A1** (fatal)  
   - **A2** (injury-only)
4. **Filtering Criteria**  
   - Retained rows only where categorical columns matched predefined mappings (e.g., 天候名稱 in [晴, 陰, 雨, 霧或煙, 風, 風沙, 雪, 強風, 暴雨]).  
   - Excluded rows with invalid or missing data in these key columns.

---

## 6. Examples

Below is an example row from the **A1** category (fatal accident). The **A2** category follows the same format.

| date     | time  | weather | lighting | speed_limit | road_condition | traffic_signal | male | female |
|----------|-------|---------|----------|------------|---------------|----------------|------|--------|
| 20240130 | 61900 | 0       | 0        | 50         | 0             | 3              | 1    | 1      |

- **date/time**: Accident happened on 2024/01/30 at 06:19:00.  
- **weather**: 0 (晴)  
- **lighting**: 0 (有照明未開啟或故障)  
- **speed_limit**: 50 (km/h)  
- **road_condition**: 0 (乾燥)  
- **traffic_signal**: 3 (行車管制號誌)  
- **male/female**: 1 male, 1 female involved  

Additional columns for vehicles and age distribution:

| veh_Scooter | veh_Bus | veh_Pedestrian | veh_Truck | veh_Car | veh_Slow | veh_Small_Truck | veh_Full_trailer | veh_Tractor | veh_Semi_trailer | veh_Other | veh_Special | veh_Military |
|-------------|---------|----------------|-----------|---------|---------|-----------------|------------------|------------|------------------|-----------|------------|--------------|
| 1           | 0       | 0              | 0         | 1       | 0       | 0               | 0                | 0          | 0                | 0         | 0          | 0            |

| age_1~10 | age_11~20 | age_21~30 | age_31~40 | age_41~50 | age_51~60 | age_61~70 | age_71~80 | age_81~90 | age_91~100 | age_101~110 | age_111~120 |
|----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|------------|-------------|-------------|
| 0        | 0         | 1         | 0         | 0         | 0         | 1         | 0         | 0         | 0          | 0           | 0           |

- One person aged 21–30, and another aged 61–70.

---

## 7. Final Remarks

This documentation outlines the structure, source, and processing of the Taiwan Traffic Accident Dataset. It aims to provide clarity for researchers or data scientists who wish to use it for predictive modeling, statistical analysis, or any other form of data exploration. For additional details—such as more extensive mappings, year-by-year record counts, or deeper breakdowns of accident severities—please refer to the appendix or experiment sections.

> **Note**: For more information, please check report.pdf.  
and you can download raw_data folder here: https://gofile.me/7srmc/bhtAxWiQC
