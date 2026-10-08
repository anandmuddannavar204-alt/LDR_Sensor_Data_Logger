import csv
import statistics
from pathlib import Path
import matplotlib.pyplot as plt

# Locate the project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "Data" / "ldr_data.csv"
RESULTS_DIR = PROJECT_DIR / "Results"
RESULTS_DIR.mkdir(exist_ok=True)

# Read the sensor data without Pandas
groups = {}

with open(DATA_FILE, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        condition = row["Condition"].strip()
        time_seconds = float(row["Time_ms"]) / 1000
        value = int(row["LDR_Value"])

        groups.setdefault(condition, []).append(
            (time_seconds, value)
        )

# Calculate sensor statistics
summary_file = RESULTS_DIR / "ldr_summary.csv"

with open(summary_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Condition", "Count", "Minimum",
        "Maximum", "Mean", "Median"
    ])

    for condition, readings in groups.items():
        values = [value for _, value in readings]

        count = len(values)
        minimum = min(values)
        maximum = max(values)
        average = statistics.mean(values)
        median = statistics.median(values)

        print(f"\nCondition: {condition}")
        print(f"Number of readings: {count}")
        print(f"Minimum: {minimum}")
        print(f"Maximum: {maximum}")
        print(f"Average: {average:.2f}")

        writer.writerow([
            condition, count, minimum, maximum,
            f"{average:.2f}", f"{median:.2f}"
        ])

# Generate the graph
plt.figure(figsize=(10, 5))

for condition, readings in groups.items():
    times = [time for time, value in readings]
    values = [value for time, value in readings]

    plt.plot(times, values, marker="o", label=condition)

plt.title("LDR Sensor Readings Under Different Light Conditions")
plt.xlabel("Time (seconds)")
plt.ylabel("LDR Sensor Value")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

graph_file = RESULTS_DIR / "ldr_light_conditions.png"
plt.savefig(graph_file, dpi=200)
plt.close()

print("\nAnalysis completed successfully!")
print("Summary saved:", summary_file)
print("Graph saved:", graph_file)