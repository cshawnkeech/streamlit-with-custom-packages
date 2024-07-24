"""
Some constants
"""
# Location of the Springfield Conservation Nature Center
LAT = 37.12809805179428
LNG = -93.23978460381035

FORECAST_POINT_LOCATION_ENDPOINT = f"https://api.weather.gov/points/{
    LAT},{LNG}"
KS_ALERTS_ENDPOINT = "https://api.weather.gov/alerts/active?area=KS"
