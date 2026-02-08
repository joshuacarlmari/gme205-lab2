import os
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from spatial import PointSet

# Paths

csv_path = "data/point.csv" 
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(csv_path)

points = PointSet.from_csv("data/point.csv")

num_rows, num_cols = df.shape

print("===DATA INSPECTION REPORT===")

print("\nBasic Information")
print("-----------------")

print(f"Total points: {points.count()}")
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")
print(f"Column names: {list(df.columns)}")


bbox = points.bbox()
print(f"Bounding box: {bbox}")  
print("\n")
print("Total Points by Tag")
print("-----------------")
pois = points.filter_by_tag("POI")
print(f"POIs count with POI: {pois.count()}")

pois = points.filter_by_tag("building")
print(f"POIs count with Building: {pois.count()}")

pois = points.filter_by_tag("school")
print(f"POIs count with School: {pois.count()}")

pois = points.filter_by_tag("gate")
print(f"POIs count with Gate: {pois.count()}")

pois = points.filter_by_tag("road")
print(f"POIs count with Road: {pois.count()}")



# Scatter Plot

plt.figure(figsize=(8, 6))
lons = [p.lon for p in points.points]
lats = [p.lat for p in points.points]

plt.scatter(lons, lats, c='red', alpha=0.6)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Spatial Distribution of Points of UP Landmarks")
plt.grid(True)

ax = plt.gca() 
ax.xaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_major_formatter(ScalarFormatter())
ax.ticklabel_format(useOffset=False)

# Save
fig_path = os.path.join(output_dir, "lab2_preview.png")
plt.savefig(fig_path, dpi=300)
plt.close()
print(f"Scatter plot saved to {fig_path}")


# Summary Report

summary = {
    "total_points": points.count(),
    "bounding_box": {
        "min_lon": bbox[0],
        "min_lat": bbox[1],
        "max_lon": bbox[2],
        "max_lat": bbox[3],
    }
}

json_path = os.path.join(output_dir, "lab2_report.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=4)

print(f"Summary report saved to {json_path}")