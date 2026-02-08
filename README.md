# GmE 205 Lab 2: Simple Spatial Objects in Python (Reflection)
## Object vs Geometry
### How did modeling points as objects change the way you thought about the data compared to treating them as rows in a table?
### Modeling points as objects lets each point store its data and behaviors. This makes the data more readable and organized. Using a PointSet allows collection-level operations like counting points or filtering by tag, which would be more cumbersome with plain rows.



## Responsibility
### Which behaviors belonged in Point, which belonged in PointSet, and which belonged in the runner script? Give one concrete example.
### For points, storing the coordinates (lat,long) and validating it (e.g., latitude between -90 and 90). For Point Set, the behavior it belong is computing the bounding box of the set of points. Lastly, reading the CSV data is an example of behaior of running scripts.

## Modeling Insight
### How did separating geometry, meaning, and behavior make the spatial logic easier (or harder) to understand?
### Separating geometry (Point), meaning (PointSet), and behavior (runner) clarifies spatial logic by giving each part a focused and separated and a role that is easy to understand. For example, Point handles the coordinates and incorporating it to a Point Set, it gives meaning the the set of points which can be managed and operated which then be process by runer scripts by giving the pointset a behavior. In this way, you can already know what you should modify depending on what you needed because the roles are very clear and distinct respectively. 
