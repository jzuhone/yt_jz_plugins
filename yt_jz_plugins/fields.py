import numpy as np
from yt.fields.field_plugin_registry import register_field_plugin
from yt.utilities.physical_constants import mp, qp, me, clight
from yt.utilities.physical_ratios import primordial_H_mass_fraction
from yt.units import radian

RMconst = radian*qp**3/(2.*np.pi*me*me*clight**4)

@register_field_plugin
def setup_jz_fields(registry, ftype = "gas", slice_info = None):

    def _density_squared(field, data):
        return data["density"]**2
    registry.add_field((ftype, "density_squared"), sampling_type="cell",
                       function=_density_squared, units="g**2/cm**6")

    def _vfield(ax):
        def _velocity_squared(field, data):
            return data["velocity_%s" % ax]**2
        return _velocity_squared

    for ax in "xyz":
        registry.add_field(("gas", "velocity_%s_squared" % ax),
                           sampling_type="cell", function=_vfield(ax),
                           units="cm**2/s**2")

    def _n_e(field, data) :
        if data.has_field_parameter("mue"):
            mue = data.get_field_parameter("mue")
        else:
            mue = 2.0/(1.0+primordial_H_mass_fraction)
        return data["density"]/(mue*mp)
    registry.add_field(("gas", "n_e"), sampling_type="cell",
                       function=_n_e, units="cm**-3")

    def _RMfield(ax):
        def _RM(field, data):
            rm = RMconst*data["magnetic_field_%s" % ax]*data["n_e"]
            rm.convert_to_units("radian/m**2/cm")
            return rm
        return _RM

    for ax in "xyz":
        registry.add_field(("gas", "rotation_measure_%s" % ax),
                           sampling_type="cell", function=_RMfield(ax),
                           units="radian*m**2/cm")
