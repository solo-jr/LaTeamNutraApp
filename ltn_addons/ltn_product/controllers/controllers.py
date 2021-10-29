# -*- coding: utf-8 -*-
# from odoo import http


# class LtnProduct(http.Controller):
#     @http.route('/ltn_product/ltn_product/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ltn_product/ltn_product/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ltn_product.listing', {
#             'root': '/ltn_product/ltn_product',
#             'objects': http.request.env['ltn_product.ltn_product'].search([]),
#         })

#     @http.route('/ltn_product/ltn_product/objects/<model("ltn_product.ltn_product"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ltn_product.object', {
#             'object': obj
#         })
