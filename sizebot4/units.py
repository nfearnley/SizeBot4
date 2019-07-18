from pint import UnitRegistry
ureg = UnitRegistry()
ureg.default_format = "~P"
Q_ = ureg.Quantity

# x = 10 * ureg.meter
# x = 10 * ureg.parse_expression("meter")
# x = 10 * ureg("meter")
# x = Q_(10, "meter")
# x = Q_("10m")
# x_in_feet = Q_(x).to("feet")

# x.magnitude
# x.units

# f"{x:P}" == "10 meter"
# f"{x:~P}" == "10 m"

# ureg.default_format = "~P"
