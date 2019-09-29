from datetime import date, timedelta

from astral import Location


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
    location = Location((local_name, region, latitude, longitude, time_zone, elevation))
    return {"Nascer do sol": location.sunrise(resh_date),
            "Meio-dia solar": location.solar_noon(resh_date),
            "Pôr do sol": location.sunset(resh_date),
            "Meia-noite solar": location.solar_midnight(resh_date + timedelta(days=1))}
