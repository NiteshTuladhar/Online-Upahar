from django.contrib.gis.geoip2 import GeoIP2

def get_geo(ip):
    g = GeoIP2()
    city = g.city(ip)
    country = g.country(ip)
    lat, lon = g.lat_lon(ip)
    return country, city, lat, lon