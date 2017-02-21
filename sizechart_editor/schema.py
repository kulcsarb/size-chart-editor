from marshmallow import Schema, fields, validates_schema, validates, ValidationError


class SizeChart(Schema):
    class Meta:
        strict = True

    name = fields.Str(required=True)
    designation = fields.Str()
    vendor = fields.Str()
    region = fields.Str()
    unit = fields.Str(required=True)
    url = fields.Url()

    @validates('unit')
    def validate_unit(self, data):
        if data not in ['cm', 'in']:
            raise ValidationError("unit must be either 'cm' or 'in'")
