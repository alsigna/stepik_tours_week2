import data


def departures(request):
    return {"departures": data.departures}


def title(request):
    return {"title": data.title}
