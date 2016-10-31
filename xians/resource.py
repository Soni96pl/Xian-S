from flask_restful import reqparse, Resource


class Resource(Resource):
    default_fields = []
    default_sort = []

    def get_query(self):
        parser = reqparse.RequestParser()
        parser.add_argument('fields')
        parser.add_argument('sort')
        args = parser.parse_args()

        if args['fields']:
            fields = args['fields'].split(',')
        else:
            fields = self.default_fields

        if args['sort']:
            sort = map(
                lambda f: (f[1:], -1) if f[0] == '-' else (f, 1),
                args['sort'].split(',')
            )
        else:
            sort = self.default_sort

        return (fields, sort)
