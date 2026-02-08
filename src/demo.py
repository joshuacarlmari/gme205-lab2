from spatial import Point


p = Point("A", 121.0, 14.6)
print(p.id, p.lon, p.lat)
print(p.to_tuple())

q = Point("X", 150, 14)
print(q.id, q.lon, q.lat)

distance = p.distance_to(q)

print(f"p → q: {distance:.2f} m")
