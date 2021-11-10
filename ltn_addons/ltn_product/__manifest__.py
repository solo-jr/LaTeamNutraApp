# -*- coding: utf-8 -*-
{
    'name': "LTN Product",

    'summary': """
        Manage LTN Producct""",

    'description': """
        Manage LTN Producct
    """,

    'author': "RANDRIANASOLO Jean Robert",
    'website': "http://www.roottsmg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'ltn_base',
        'product',
        'uom',
        'contacts',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/thematic_views.xml',
        'views/partner_views.xml',
        'views/favorites_views.xml',
        'views/assets.xml',
        'report/product_report.xml',
        'views/product_send_mail.xml',
        # 'views/templates.xml',
        'data/ir_cron.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
