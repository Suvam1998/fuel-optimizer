# 🚗 Fuel Optimizer API

## 📌 Overview

Fuel Optimizer is a Django-based backend system that computes optimal fuel stops along a route based on fuel prices and vehicle constraints. It also provides an interactive map visualization for better understanding of the route and stops.

## ✨ Features

* 📍 Route generation between start and end points
* ⛽ Fuel stop optimization (cost-efficient strategy)
* 💰 Total fuel cost calculation (based on 10 MPG)
* 🗺️ Interactive map with route + fuel stops
* 🔗 Polyline encoding for efficient frontend rendering
* 🐳 Fully Dockerized for easy setup and deployment
* ⚡ No runtime dependency on external APIs (fast & reliable)

---

## 🧠 Approach

* The original dataset lacked geographic coordinates
* Data was **preprocessed into latitude/longitude format**
* A **greedy strategy** is used to select fuel stops
* The route is represented as a polyline for lightweight transfer

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Data Processing:** Pandas
* **Frontend:** Leaflet.js (map visualization)
* **Deployment:** Docker

---

## 📁 Project Structure

```
fuel-optimizer/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── data/
│   ├── fuel_prices.csv
│   └── fuel_with_coords.csv
│
├── templates/
│   └── map.html
│
├── fuel_optimizer/
├── routes/
└── manage.py
```

---

## 🚀 Getting Started

### 🔧 Run with Docker

```bash
docker-compose up --build
```

Open in browser:

```
http://localhost:8000/
```

---

## 📡 API Usage

### Endpoint

```
POST /api/optimize/
```

### Request Body

```json
{
  "start": [40.7128, -74.0060],
  "end": [34.0522, -118.2437]
}
```

### Response

```json
{
  "distance": 2500,
  "fuel_stops": [
    { "lat": 41.0, "lon": -87.6, "price": 3.2 }
  ],
  "total_cost": 800,
  "polyline": "encoded_string_here"
}
```
## ⚠️ Notes

* The dataset was preprocessed to include coordinates to avoid runtime geocoding delays
* A simplified routing approach is used to ensure reliability without external APIs
* The system is designed to be easily extendable with real-world routing services

## 🎯 Future Improvements

* Integrate real routing APIs (OpenRouteService / Google Maps)
* Use spatial indexing (KD-tree) for faster nearest-station lookup
* Improve optimization using distance-aware fuel strategy
* Add React-based frontend

##👨‍💻 Author

Suvam Sankar Kar
