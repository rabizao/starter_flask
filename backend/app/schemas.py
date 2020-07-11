import marshmallow as ma


class JobSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    name = ma.fields.String()


class JobQueryArgsSchema(ma.Schema):
    name = ma.fields.String()
