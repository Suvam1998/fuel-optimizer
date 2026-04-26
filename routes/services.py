import pandas as pd
import polyline

# -------------------------------
# LOAD DATA (FAST, STATIC)
# -------------------------------
fuel_data = pd.read_csv("data/fuel_with_coords.csv")

# -------------------------------
# ROUTE (SIMPLE LINE)
# -------------------------------
def get_route(start, end):
    coords = []

    steps = 50
    for i in range(steps + 1):
        lat = start[0] + (end[0] - start[0]) * i / steps
        lon = start[1] + (end[1] - start[1]) * i / steps
        coords.append([lon, lat])

    distance = 2500  # dummy miles
    return coords, distance


# -------------------------------
# GREEDY (PRICE-BASED)
# -------------------------------
def optimal_fuel_stops(route):
    stops = []

    cheapest = fuel_data.sort_values("price").iloc[0]

    for i in range(10, len(route), 10):
        stops.append({
            "lat": route[i][1],
            "lon": route[i][0],
            "price": float(cheapest["price"])
        })

    return stops


# -------------------------------
# COST
# -------------------------------
def calculate_cost(distance, stops):
    MPG = 10
    gallons = distance / MPG

    avg_price = (
        sum(s["price"] for s in stops) / len(stops)
        if stops else fuel_data["price"].mean()
    )

    return gallons * avg_price


# -------------------------------
# POLYLINE
# -------------------------------
def encode_polyline(route):
    latlon = [(p[1], p[0]) for p in route]
    return polyline.encode(latlon)