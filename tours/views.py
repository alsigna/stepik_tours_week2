import random

import data
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render


def custom_404(request, exception):
    """Custom handler for 404 status code."""

    return HttpResponseNotFound("Page Not Found")


def custom_500(request):
    """Custom handler for 500 status code."""

    return HttpResponseServerError("Internal Server Error")


def main_view(request):
    """View for Main Page. Displays 6 random tours."""

    random_numbers = random.sample(range(1, len(data.tours) + 1), 6)
    random_tours = {tour_id: data.tours[tour_id] for tour_id in random_numbers}

    return render(
        request=request,
        template_name="tours/index.html",
        context={
            "subtitle": data.subtitle,
            "description": data.description,
            "tours": random_tours,
        },
    )


def departure_view(request, dep_code):
    """View for tours by departure.

    Args:
        dep_code (str): departure code

    Raises:
        Http404: in case of un-existed departure
    """

    departure = data.departures.get(dep_code, None)

    if not departure:
        raise Http404

    tours_by_departure = {
        tour_id: tour_info for tour_id, tour_info in data.tours.items() if tour_info["departure"] == dep_code
    }
    prices = [i["price"] for i in tours_by_departure.values()]
    nights = [i["nights"] for i in tours_by_departure.values()]

    return render(
        request=request,
        template_name="tours/departure.html",
        context={
            "tours": tours_by_departure,
            "details": {
                "departure": departure,
                "price_max": max(prices),
                "price_min": min(prices),
                "night_max": max(nights),
                "night_min": min(nights),
            },
        },
    )


def tour_view(request, tour_id):
    """View for specifc tour.

    Args:
        tour_id (int): tour identifier

    Raises:
        Http404: in case of un-existed tour
    """
    tour = data.tours.get(tour_id, None)

    if not tour:
        raise Http404

    return render(
        request=request,
        template_name="tours/tour.html",
        context={
            "tour": tour,
            "departure": data.departures[tour["departure"]],
        },
    )
