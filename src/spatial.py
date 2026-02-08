import math
import csv
class Point:
    def __init__(self, id, lon, lat, name=None, tag=None):
        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        
        if not (-90 <= lat <= 90):
            raise ValueError("Latitude must be between -90 and 90")

        self.id = id
        self.lon = lon
        self.lat = lat
        self.name = name
        self.tag = tag

    # ------------------------------------------------------------------
    # Instance methods (behavior belongs to the object)
    # ------------------------------------------------------------------

    def to_tuple(self) -> tuple[float,float]:
        """
        Return the coordinate as a (lon, lat) tuple.
        """
        return (self.lon, self.lat)
    
    def distance_to(self,other):
        return Point.haversine_m(self.lon, self.lat, other.lon, other.lat)
    
# ------------------------------------------------------------------
    # Static method (pure spatial math)
    # ------------------------------------------------------------------

    @staticmethod
    def haversine_m(
        lon1: float, lat1:float, lon2:float, lat2:float
       )   -> float:
        """
        Compute the Haversine Distance between tow lon/lat pairs in meters.

        Static method because it does not depend on object state.
        """

        R = 6_371_000.0 # Earth radius in meters

        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = math.sin(dphi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda/2)**2
        c = 2 * math.asin(math.sqrt(a))

        distance = R * c
        return distance
    

    # ------------------------------------------------------------------
        # Class method (constructing objects from data)
        # ------------------------------------------------------------------

    @classmethod
    def from_row(cls, row):
        return cls( 
            id=str(row["id"]),
            lon=float(row["lon"]),
            lat=float(row["lat"]),
            name=row.get("name"),
            tag=row.get("tag"),
        )

    def is_poi(self):
        return (self.tag or "").lower() == "poi"
    
import csv
from typing import List, Tuple
from spatial import Point 

class PointSet:
    def __init__(self, points: List[Point] = None):
        """
        Initialize a PointSet with a list of Point objects.
        """
        self.points = points if points is not None else []


    @classmethod
    def from_csv(cls, path: str) -> "PointSet":
        """
        Reads a CSV file
        """
        points = []
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    point = Point.from_row(row)
                    points.append(point)
                except Exception as e:
                 
                    print(f"Skipping invalid row: {row}, reason: {e}")
        return cls(points)


    def count(self) -> int:
        return len(self.points)


    def bbox(self) -> Tuple[float, float, float, float]:
        if not self.points:
            return (0.0, 0.0, 0.0, 0.0) 
        lons = [p.lon for p in self.points]
        lats = [p.lat for p in self.points]
        return (min(lons), min(lats), max(lons), max(lats))


    def filter_by_tag(self, tag: str) -> "PointSet":
      
        filtered_points = [p for p in self.points if (p.tag or "").lower() == tag.lower()]
        return PointSet(filtered_points)

    def __repr__(self):
        return f"PointSet({len(self.points)} points)"


                              
