
# https://pyastronomy.readthedocs.io/en/latest/pyaslDoc/aslDoc/eq2hor.html

# PyAstronomy.pyasl.hadec2altaz(ha, dec, lat, ws=False, radian=False)

    # Convert hour angle and declination into horizon (alt/az) coordinates.
    # Parameters:

    # ha : float or array

        # Local apparent hour angle in DEGREES.
    # dec : float or array

        # Local apparent declination in DEGREES.
    # lat : float or array

        # Local latitude in DEGREES.
    # radian : boolean, optional

        # If True, the result is returned in radian instead of in degrees (default is False).
    # ws : boolean, optional

        # Set this to True, if the azimuth shall be measured West from South. Default is to measure azimuth East from North.

    # Returns:

    # Altitude : list

        # A list holding the Local Apparent Altitude [deg].
    # Apparent Azimuth : list

        # The Local Apparent Azimuth [deg].


# As per Meeus, J. (1998). p. 92 the algorithms all assume azimuth measured west from south
# thus ws (west south) is true

from __future__ import print_function, division
from PyAstronomy import pyasl
import datetime
import numpy as np
import math

import sys

try:
    dec = float(sys.argv[2])
    lat = float(sys.argv[3])
    ha = float(sys.argv[1])

except:
    # Latitude of the observer (here Hamburger Sternwarte)
    lat = +53.48

    # Declination of object
    dec = 30.

    # Hour angle 0. means transiting the local meridian.
    ha = 0.

print("ha dec lat radians: ", math.radians(ha), math.radians(dec), math.radians(lat))

altaz = pyasl.hadec2altaz(ha, dec, lat, radian=True, ws=True)

print("alt", altaz[0], "az", altaz[1])



