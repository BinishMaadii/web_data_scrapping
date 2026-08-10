############### ############ ########################  ################################################
####### This is a piece of code for my Google site page, where I can show the timeline of my work
############################################################################################################


import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# 1. Replaced "Present" with dynamic today's date & fixed typo
today_str = pd.Timestamp.today().strftime('%Y-%m-%d')

data = [
    {"Task": "ATLAS Qualification task", "Start": "2017-07-01", "End": "2018-12-31", "Color": "#1E6BFF"},
    {"Task": "PhD", "Start": "2019-01-01", "End": "2025-09-30", "Color": "#F3C536"},
    {"Task": "Data Science Postdoc", "Start": "2023-01-01", "End": "2023-12-31", "Color": "#FF8C32"},
    {"Task": "Break/Holidays", "Start": "2025-10-01", "End": "2025-11-30", "Color": "#7BCD9B"},
    {"Task": "Lerne Deutsch A1-B2", "Start": "2025-12-01", "End": "2026-05-31", "Color": "#B266FF"},
    {"Task": "DrivenData", "Start": "2026-06-01", "End": today_str, "Color": "#FF3399"},
]

df = pd.DataFrame(data)
df['Start'] = pd.to_datetime(df['Start'])
df['End'] = pd.to_datetime(df['End'])

# Reverse order so top-most task in image appears at the top
df = df.iloc[::-1].reset_index(drop=True)

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

y_positions = range(len(df))
