# -*- coding: utf-8 -*-
from GoogleMercatorProjection import LatLng
from PyQt4.QtGui import QColor

# LOCATION(S)
# Further radar configuration (zoom, marker location)
#  can be completed under the RADAR section
primary_coordinates = 48.129214, -1.644476  # Change to your Lat/Lon

wuprefix = 'http://api.wunderground.com/api/'
# Location for weather report
wulocation = LatLng(primary_coordinates[0], primary_coordinates[1])
# Default radar location
primary_location = LatLng(primary_coordinates[0], primary_coordinates[1])
noaastream = 'http://audioplayer.wunderground.com:80/tim273/edina'
background = 'images/bb.jpg'
squares1 = 'images/squares1-kevin.png'
squares2 = 'images/squares2-kevin.png'
icons = 'icons-darkwhite'
textcolor = '#ffffff'
clockface = 'images/clockface3-darkwhite.png'
hourhand = 'images/hourhand.png'
minhand = 'images/minhand.png'
sechand = 'images/sechand.png'

digital = 0             # 1 = Digtal Clock, 0 = Analog Clock

digitalcolor = "#154018"
digitalformat = "{0:%I:%M\n%S %p}"  # The format of the time
digitalsize = 200
# The above example shows in this way:
#  https://github.com/n0bel/PiClock/blob/master/Documentation/Digital%20Clock%20v1.jpg
# ( specifications of the time string are documented here:
#  https://docs.python.org/2/library/time.html#time.strftime )

# digitalformat = "{0:%I:%M}"
# digitalsize = 250
# The above example shows in this way:
#  https://github.com/n0bel/PiClock/blob/master/Documentation/Digital%20Clock%20v2.jpg


# 0 = English, 1 = Metric
metric = 1

# 0 = Clock disabled, 1 Clock enabled
clockEnabled = 1

# 0 = Weather disabled, 1 Weather enabled
weatherEnabled = 1

# 0 = Radar disabled, 1 Radar enabled
radarEnabled = 0

# minutes
radar_refresh = 10

# minutes
weather_refresh = 30

# Wind in degrees instead of cardinal 0 = cardinal, 1 = degrees
wind_degrees = 1

# Depreciated: use 'satellite' key in radar section, on a per radar basis
# if this is used, all radar blocks will get satellite images
satellite = 0

# Font attribute applied globally
fontattr = 'font-weight: bold; '

# These are to dim the radar images, if needed.
dimcolor = QColor('#103125')
dimcolor.setAlpha(192)

# Language Specific wording
# Weather Undeground Language code
#  (https://www.wunderground.com/weather/api/d/docs?d=language-support&MR=1)
wuLanguage = "FR"

# The Python Locale for date/time (locale.setlocale)
#  '' for default Pi Setting
# Locales must be installed in your Pi.. to check what is installed
# locale -a
# to install locales
# sudo dpkg-reconfigure locales
DateLocale = ''

# Language specific wording
LPressure = "Pression "
LHumidity = u"Humidité "
LWind = "Vent "
Lgusting = " gusting "
LFeelslike = "Ressenti "
LPrecip1hr = " Pr 1hr:"
LToday = "Aujourd'hui: "
LSunRise = "Lever soleil:"
LSet = " Coucher: "
LMoonPhase = " Phase de lune:"
LInsideTemp = u"Température intérieure "
LRain = " Pluie: "
LSnow = " Neige: "


# RADAR
# By default, primary_location entered will be the center and marker of all
# radar images.
# To update centers/markers, change radar sections below the desired lat/lon as:
# -FROM-
# primary_location,
# -TO-
# LatLng(44.9764016,-93.2486732),
radar1 = {
    'center': primary_location,  # the center of your radar block
    'zoom': 7,  # this is a google maps zoom factor, bigger = smaller area
    'satellite': 0,  # 1 => show satellite images instead of radar(colorized IR)
    'markers': (   # google maps markers can be overlayed
        {
            'location': primary_location,
            'color': 'red',
            'size': 'small',
        },          # dangling comma is on purpose.
    )
}


radar2 = {
    'center': primary_location,
    'zoom': 11,
    'satellite': 0,
    'markers': (
        {
            'location': primary_location,
            'color': 'red',
            'size': 'small',
        },
    )
}


radar3 = {
    'center': primary_location,
    'zoom': 7,
    'satellite': 0,
    'markers': (
        {
            'location': primary_location,
            'color': 'red',
            'size': 'small',
        },
    )
}

radar4 = {
    'center': primary_location,
    'zoom': 11,
    'satellite': 0,
    'markers': (
        {
            'location': primary_location,
            'color': 'red',
            'size': 'small',
        },
    )
}
