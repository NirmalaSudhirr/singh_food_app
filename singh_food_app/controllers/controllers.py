# -*- coding: utf-8 -*-
import json
import json.decoder
from odoo import http
from odoo.http import request

from odoo.http import content_disposition, dispatch_rpc, request, serialize_exception as _serialize_exception, Response

class SinghFoodAppSession(http.Controller):

    @http.route('/web/get_session_info', type='json', auth="none")
    def get_session_info(self):
        request.session.check_security()
        request.uid = request.session.uid
        request.disable_db = False
        return request.env['ir.http'].session_info()

    @http.route('/web/authenticate', type='json', auth="none")
    def authenticate(self, db, login, password, base_location=None):
        request.session.authenticate(db, login, password)
        return request.env['ir.http'].session_info()
        
    @http.route('/api/get_categories', type="http", auth="public", website=True, method=['POST'], csrf=False)
    def get_categories(self):
        categories_rec = request.env['foodapp.categories'].sudo().search([])
        categories = []
        for rec in categories_rec:
            vals = {
                'id': rec.id,
                'name': rec.name,
                'image':rec.image.decode('utf-8'),

            }
            categories.append(vals)
        #print("categories List--->", categories)
        data = {'status': 200, 'response': categories, 'message': 'Done All Categiries Returned'}
        return json.dumps(data)



