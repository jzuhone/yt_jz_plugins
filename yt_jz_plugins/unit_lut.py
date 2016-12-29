import numpy as np
from yt.units import dimensions
from yt.utilities.physical_ratios import sec_per_day, sec_per_hr, cm_per_km

grams_per_pound = 453.59237
cm_per_ft = 30.48
cm_per_mile = cm_per_ft*5280.0
cc_per_us_pint = 473.176473
erg_per_calorie = 4.184e7
g0 = 9.80665e2

unit_symbol_lut = {

    # Angle units

    "revolution": (2.*np.pi, dimensions.angle),
    "chandra_pixel": (0.492*np.pi/648000.0, dimensions.angle),

    # Time units

    "week": (sec_per_day*7.0, dimensions.time),
    "fortnight": (sec_per_day*14.0, dimensions.time),

    # Metric units

    "L": (1000.0, dimensions.volume),
    "tonne": (1.0e6, dimensions.mass),

    # Imperial units

    "inch": (cm_per_ft/12., dimensions.length),
    "yard": (cm_per_ft*3., dimensions.length),
    "slug": (grams_per_pound*g0/cm_per_ft, dimensions.mass),
    "ton": (grams_per_pound*2000.0, dimensions.mass),
    "oz": (grams_per_pound/16.0, dimensions.mass),
    "mph": (cm_per_mile/sec_per_hr, dimensions.velocity),
    "psi": (grams_per_pound*g0*144./cm_per_ft**2, dimensions.pressure),

    # US volumes

    "fl_oz_US": (cc_per_us_pint/16.0, dimensions.volume),
    "cp_US": (cc_per_us_pint/2.0, dimensions.volume),
    "pt_US": (cc_per_us_pint, dimensions.volume),
    "qt_US": (cc_per_us_pint*2.0, dimensions.volume),
    "gal_US": (cc_per_us_pint*8.0, dimensions.volume),

    # Nautical

    "knot": (1.151*cm_per_mile/sec_per_hr, dimensions.velocity),
    "nautical_mile": (1.852*cm_per_km, dimensions.length),

    # Force and energy

    "cal": (erg_per_calorie, dimensions.energy),
    "g0": (g0, dimensions.acceleration),

}
