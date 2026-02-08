from spatial import PointSet


points = PointSet.from_csv("data/point.csv")


print(f"Total points: {points.count()}")


bbox = points.bbox()
print(f"Bounding box: {bbox}")  # (min_lon, min_lat, max_lon, max_lat)


pois = points.filter_by_tag("POI")
print(f"POIs count: {pois.count()}")