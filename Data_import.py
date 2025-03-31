import kagglehub
import pandas as pd
import os
import numpy as np

path = kagglehub.dataset_download("impapan/student-performance-data-set")
inner_path = os.path.join(path, "student")

df_por = pd.read_csv(f"{inner_path}/student-por.csv", sep=";")
df_mat = pd.read_csv(f"{inner_path}/student-mat.csv", sep=";")

common_cols = ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 
               'Mjob', 'Fjob', 'reason', 'guardian', 'traveltime', 'studytime', 'failures', 
               'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 
               'romantic', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences']

df = df_por.merge(df_mat, how='outer', on=common_cols, suffixes=('_por', '_mat'))

df['przedmiot'] = 'oba'
df.loc[pd.isna(df['G1_por']), 'przedmiot'] = 'matematyka'
df.loc[pd.isna(df['G1_mat']), 'przedmiot'] = 'portugalski'

if 'przedmiot_por' in df.columns:
    df = df.drop(columns=['przedmiot_por'])
if 'przedmiot_mat' in df.columns:
    df = df.drop(columns=['przedmiot_mat'])

df['G3_avg'] = np.nan

mask_oba = df['przedmiot'] == 'oba'
df.loc[mask_oba, 'G3_avg'] = df.loc[mask_oba, ['G3_por', 'G3_mat']].mean(axis=1)

mask_por = df['przedmiot'] == 'portugalski'
df.loc[mask_por, 'G3_avg'] = df.loc[mask_por, 'G3_por']

mask_mat = df['przedmiot'] == 'matematyka'
df.loc[mask_mat, 'G3_avg'] = df.loc[mask_mat, 'G3_mat']

df.to_csv("student_data.csv", index=False)
print("DataFrame został zapisany jako student_data.csv")