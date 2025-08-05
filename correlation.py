import pandas as pd

data = pd.read_csv("materias.csv").convert_dtypes()

data["Fecha"] = pd.to_datetime(data["Fecha"])
data["Año"] = data["Fecha"].dt.year
data["Nota"] = pd.to_numeric(data["Nota"], errors="coerce")

avg_grade_per_year = data.groupby("Año")["Nota"].mean()

subjects_count_per_year = data["Año"].value_counts().sort_index()

correlation = avg_grade_per_year.corr(subjects_count_per_year)

print("Average Grade per Year:")
print(avg_grade_per_year)
print("\nSubjects Passed per Year:")
print(subjects_count_per_year)
print(f"\nCorrelation between average grade and subjects passed per year: {correlation:.3f}")

import matplotlib.pyplot as plt

fig, ax1 = plt.subplots(figsize=(10, 6))

color = 'tab:blue'
ax1.set_xlabel('Year')
ax1.set_ylabel('Average Grade', color=color)
ax1.plot(avg_grade_per_year.index, avg_grade_per_year.values, marker='o', color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('Subjects Passed', color=color)
ax2.plot(subjects_count_per_year.index, subjects_count_per_year.values, marker='s', linestyle='--', color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Average Grade and Subjects Passed per Year')
plt.show()
