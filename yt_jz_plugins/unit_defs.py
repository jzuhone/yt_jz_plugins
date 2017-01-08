import numpy as np
import yt

# Angle units

yt.define_unit("revolution", (2.0*np.pi, "radian"))
yt.define_unit("chandra_pixel", (0.492, "arcsec"))

# Time units

yt.define_unit("week", (7.0, "day"))
yt.define_unit("fortnight", (14.0, "day"))

# Force and energy

yt.define_unit("cal", (4.184e7, "erg"))
yt.define_unit("g0", (9.80665e2, "cm/s**2"))

# Metric units

yt.define_unit("L", (1000.0, "cm**3"), prefixable=True)
yt.define_unit("t", (1.0, "Mg"), prefixable=True)

# Imperial units

yt.define_unit("inch", (1.0/12.0, "ft"))
yt.define_unit("yard", (3.0, "ft"))
yt.define_unit("slug", (1.0, "lbf*s**2/ft"))
yt.define_unit("ton", (2000.0, "lbm"))
yt.define_unit("oz", (1.0/16.0, "lbm"))
yt.define_unit("mph", (1.0, "mile/hr"))
yt.define_unit("psi", (1.0, "lbf/inch**2"))

# US volumes

yt.define_unit("pt_US", (473.176473, "cm**3"))
yt.define_unit("fl_oz_US", (1.0/16.0, "pt_US"))
yt.define_unit("cp_US", (0.5, "pt_US"))
yt.define_unit("qt_US", (2.0, "pt_US"))
yt.define_unit("gal_US", (8.0, "pt_US"))

# Nautical

yt.define_unit("knot", (1.151, "mph"))
yt.define_unit("nautical_mile", (1.852, "km"))
