from .unit_lut import unit_symbol_lut
from yt.units.unit_object import default_unit_registry
from . import fields

for k, v in unit_symbol_lut.items():
    default_unit_registry.add(k, *v)
