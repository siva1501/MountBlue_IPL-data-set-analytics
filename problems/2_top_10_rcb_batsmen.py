import csv
import matplotlib.pyplot as plt


batsman_runs = {}

with open("data/deliveries.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["batting_team"] == "Royal Challengers Bangalore":
            batsman = row["batsman"]
            runs = int(row["batsman_runs"])

            if batsman not in batsman_runs:
                batsman_runs[batsman] = 0

            batsman_runs[batsman] += runs


sorted_batsmen = sorted(
    batsman_runs.items(),
    key=lambda item: item[1],
    reverse=True
)

top_10 = sorted_batsmen[:10]

batsmen = []
runs = []

for batsman, total_runs in top_10:
    batsmen.append(batsman)
    runs.append(total_runs)
    print(batsman, total_runs)


# Create plot
plt.figure(figsize=(12, 6))

plt.bar(batsmen, runs)

plt.xlabel("Batsmen")
plt.ylabel("Total Runs")
plt.title("Top 10 Batsmen for Royal Challengers Bangalore")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()