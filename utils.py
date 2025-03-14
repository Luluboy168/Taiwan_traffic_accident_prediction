import pandas as pd

def mapping(df):
    mapping = {
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
    
    df = df[df['天候名稱'].isin(mapping.keys())]
    df['天候名稱'] = df['天候名稱'].map(mapping)

    mapping = {
        '有照明未開啟或故障': 0,
        '無照明': 1,
        '有照明且開啟': 2,
        '日間自然光線': 3,
        '夜間(或隧道、地下道、涵洞)有照明': 4,
        '夜間(或隧道、地下道、涵洞)無照明': 5,
        '晨或暮光': 6

    }

    df = df[df['光線名稱'].isin(mapping.keys())]
    df['光線名稱'] = df['光線名稱'].map(mapping)

    mapping = {
        '乾燥': 0,
        '濕潤': 1,
        '泥濘': 2,
        '油滑': 3,
        '冰雪': 4
    }

    df = df[df['路面狀況-路面狀態名稱'].isin(mapping.keys())]
    df['路面狀況-路面狀態名稱'] = df['路面狀況-路面狀態名稱'].map(mapping)

    mapping = {
        '無號誌': 0,
        '閃光號誌': 1,
        '行車管制號誌(附設行人專用號誌)': 2,
        '行車管制號誌': 3
    }

    df = df[df['號誌-號誌種類名稱'].isin(mapping.keys())]
    df['號誌-號誌種類名稱'] = df['號誌-號誌種類名稱'].map(mapping)


    df['當事者區分-類別-大類別名稱-車種'] = df['當事者區分-類別-大類別名稱-車種'].str.strip()
    mapping = {
    "機車": "Scooter",
    "大客車": "Bus",
    "人": "Pedestrian",
    "大貨車": "Truck",
    "小客車(含客、貨兩用)": "Car",
    "慢車": "Slow",
    "小貨車(含客、貨兩用)": "Small_Truck",
    "全聯結車": "Full_trailer",
    "曳引車": "Tractor",
    "半聯結車": "Semi_trailer",
    "其他車": "Other",
    "特種車": "Special",
    "小貨車": "Small_Truck",
    "軍車": "Military"
    }

    df = df[df['當事者區分-類別-大類別名稱-車種'].isin(mapping.keys())]
    df['當事者區分-類別-大類別名稱-車種'] = df['當事者區分-類別-大類別名稱-車種'].map(mapping)


    return df