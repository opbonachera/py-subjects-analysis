import json
import pandas as pd
import matplotlib.pyplot as plt

with open("data.json", "r", encoding="utf-8") as f:
    json_data = json.load(f)

data = pd.DataFrame(json_data["data"])

data["Fecha"] = pd.to_datetime(data["Fecha"])
data["Año"] = data["Fecha"].dt.year
data["Nota"] = pd.to_numeric(data["Nota"], errors="coerce")

average_per_year = data.groupby("Año")["Nota"].mean()
counts_per_year = data["Año"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
bars = average_per_year.plot(
    kind="bar",
    title="Grade Average per Year",
    ylabel="Average Grade",
    xlabel="Year",
)

for bar in bars.patches:
    height = bar.get_height()
    bars.annotate(
        f"{height:.2f}",
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 3),
        textcoords="offset points",
        ha="center",
        va="bottom",
        fontsize=9,
        color="black",
    )

plt.tight_layout()


def func(pct, allvalues):
    absolute = int(round(pct / 100. * allvalues.sum()))
    return f"{absolute}\n({pct:.1f}%)"


plt.figure(figsize=(8, 5))
counts_per_year.plot(
    kind="pie",
    title="Subjects per Year",
    autopct=lambda pct: func(pct, counts_per_year),
    ylabel="Subjects",
)

plt.tight_layout()
plt.show()
