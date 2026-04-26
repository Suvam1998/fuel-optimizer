import pandas as pd
def enrich_with_coordinates():
    import os

    CACHE_FILE = "data/fuel_with_coords.csv"

    # ✅ if cache exists → use it instantly
    if os.path.exists(CACHE_FILE):
        print("Using cached coordinates...")
        return pd.read_csv(CACHE_FILE)

    print("Generating coordinates (one-time)...")

    df = pd.read_csv("data/fuel_prices.csv")
    df.columns = [c.strip().lower() for c in df.columns]

    df.rename(columns={
        "retail price": "price"
    }, inplace=True)

    from geopy.geocoders import Nominatim
    import time

    geolocator = Nominatim(user_agent="fuel_optimizer")

    lats, lons = [], []

    for i, row in df.iterrows():
        address = f"{row.get('address','')}, {row.get('city','')}, {row.get('state','')}"

        try:
            location = geolocator.geocode(address, timeout=5)
            if location:
                lats.append(location.latitude)
                lons.append(location.longitude)
            else:
                lats.append(None)
                lons.append(None)
        except:
            lats.append(None)
            lons.append(None)

        # 🔥 speed boost (reduce delay)
        if i % 5 == 0:
            time.sleep(1)

    df["latitude"] = lats
    df["longitude"] = lons

    df.dropna(subset=["latitude", "longitude"], inplace=True)

    df.to_csv(CACHE_FILE, index=False)

    print("Saved coordinates to cache.")

    return df