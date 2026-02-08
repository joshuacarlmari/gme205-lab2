from spatial import Point
p = Point("A", 121.0, 14.6)
print(p.id, p.lon, p.lat)

q = Point("X", 120, 14)
print(q.id, q.lon, q.lat)

p = Point("A", 121.0, 14.6)
print(p.id, p.lon, p.lat)
print(p.to_tuple())

dist = p.distance_to(q)
print(dist)