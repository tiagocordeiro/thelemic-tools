from datetime import date, timedelta

from astral import LocationInfo
from astral.location import Location


def resh_hours(local_name, region, latitude, longitude, time_zone, elevation, resh_date=date.today()):
    """
    :param local_name: str
    :param region: str
    :param latitude: str
    :param longitude: str
    :param time_zone: str
    :param elevation: int
    :param resh_date: date
    :return: dict
    """
    city = LocationInfo(local_name, region, time_zone, latitude, longitude)

    location = Location(city)
    return {"Nascer do sol": location.sunrise(resh_date, observer_elevation=elevation),
            "Meio-dia solar": location.noon(resh_date),
            "Pôr do sol": location.sunset(resh_date, observer_elevation=elevation),
            "Meia-noite solar": location.midnight(resh_date + timedelta(days=1))}
