from bson import json_util as json

from flask import current_app, request
from flask_jwt import current_identity, _jwt_required
from flask_restful import reqparse, Resource

import pymongo

from xians import permissions


class Resource(Resource):
    model = None
    permissions = {
        'CREATE': permissions.AUTHORIZED,
        'READ': permissions.ANY,
        'UPDATE': permissions.AUTHORIZED,
        'DELETE': permissions.AUTHORIZED
    }
    default_fields = []
    default_sort = [('_id', pymongo.DESCENDING)]

    def _user(self, operation):
        if self.permissions.get(operation, False) is permissions.AUTHORIZED:
            return current_identity['_id']
        return None

    def path(self, path):
        if path is not None:
            return path.replace('/', '.')
        return None

    def check_permissions(self, operation):
        if self.permissions[operation] is permissions.AUTHORIZED:
            _jwt_required(current_app.config['JWT_DEFAULT_REALM'])

    def get(self, path=None, **match):
        self.check_permissions('READ')

        path = self.path(path)
        fields, sort = self.get_query()

        return self.model.search(_user=self._user('READ'),
                                 fields=fields,
                                 sort=sort,
                                 path=path,
                                 **match)

    def post(self, _id=None):
        document = json.loads(request.data)

        if _id is not None:
            self.check_permissions('UPDATE')
            _user = self._user('UPDATE')
        else:
            self.check_permissions('CREATE')
            _user = self._user('CREATE')

        headers = {}

        _id = self.model.upsert(document, _id=_id, _user=_user)
        success = _id is not False

        if success:
            headers['Location'] = '%s/%s' % (request.url, _id)
            message = "Document upserted successfully."
            code = 201
        else:
            message = "Couldn't upsert a document."
            code = 409

        return {'success': success, 'message': message}, code, headers

    def patch(self, _id, path=None):
        document = json.loads(request.data)

        self.check_permissions('UPDATE')

        path = self.path(path)
        headers = {}
        _id = self.model.upsert(document, _id=_id, _user=self._user('UPDATE'),
                                path=path)
        success = _id is not False

        if success:
            message = "Document updated successfully."
            code = 201
        else:
            message = "Couldn't update a document."
            code = 409

        return {'success': success, 'message': message}, code, headers

    def delete(self, _id, path=None):
        self.check_permissions('DELETE')

        path = self.path(path)
        success = self.model.delete(_id=_id, _user=self._user('DELETE'),
                                    path=path)
        if success:
            message = "Document removed successfully."
            code = 200
        else:
            message = "Couldn't remove a document."
            code = 404

        return {'success': success, 'message': message}, code

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
