import csv
import matplotlib.pyplot as plt

# Get 2015 match IDs
match_ids = []

with open("data/matches.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["season"] == "2015":
            match_ids.append(row["id"])


# Store bowler runs and balls
bowlers = {}

with open("data/deliveries.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["match_id"] in match_ids:
            bowler = row["bowler"]

            if bowler not in bowlers:
                bowlers[bowler] = [0, 0]

            # Runs conceded by bowler
            runs = int(row["total_runs"])

            # Don't count byes and leg-byes as bowler runs
            runs -= int(row["bye_runs"])
            runs -= int(row["legbye_runs"])

            bowlers[bowler][0] += runs

            # Count legal balls
            if int(row["wide_runs"]) == 0 and int(row["noball_runs"]) == 0:
                bowlers[bowler][1] += 1


# Calculate economy rate
economy = []

for bowler in bowlers:
    runs = bowlers[bowler][0]
    balls = bowlers[bowler][1]

    if balls > 0:
        economy_rate = runs * 6 / balls
        economy.append([bowler, economy_rate])


# Sort by economy rate
economy.sort(key=lambda x: x[1])


# Take top 10
top_10 = economy[:10]


# Print results
for bowler, rate in top_10:
    print(bowler, round(rate, 2))


# Prepare chart data
names = []
rates = []

for bowler, rate in top_10:
    names.append(bowler)
    rates.append(rate)


# Bar chart
plt.bar(names, rates)

plt.title("Top 10 Economical Bowlers in IPL 2015")
plt.xlabel("Bowlers")
plt.ylabel("Economy Rate")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
