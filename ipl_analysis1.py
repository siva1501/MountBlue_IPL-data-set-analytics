import pandas as pd
import matplotlib.pyplot as plt

deliveries = pd.read_csv("data/deliveries.csv")

rcb = deliveries[
    deliveries["batting_team"] == "Royal Challengers Bangalore"
]

top_batsmen = (
    rcb.groupby("batsman")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_batsmen)

top_batsmen.plot(kind="bar")

plt.title("Top 10 Batsmen for Royal Challengers Bangalore")
plt.xlabel("Batsman")
plt.ylabel("Total Runs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()