from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

from .services import get_route, optimal_fuel_stops, calculate_cost, encode_polyline


def map_view(request):
    return render(request, "map.html")


@api_view(["POST"])
def optimize_route(request):
    start = request.data.get("start")
    end = request.data.get("end")

    if not start or not end:
        return Response({"error": "start and end required"}, status=400)

    route, distance = get_route(start, end)
    stops = optimal_fuel_stops(route)
    cost = calculate_cost(distance, stops)

    return Response({
        "distance": round(distance, 2),
        "fuel_stops": stops,
        "total_cost": round(cost, 2),
        "polyline": encode_polyline(route)
    })