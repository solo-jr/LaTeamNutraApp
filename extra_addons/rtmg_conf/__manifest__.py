# -*- coding: utf-8 -*-
{
    'name': "La Team Nutra Configuration",

    'summary': """
        Launch the default configurations of the La Team Nutra application""",

    'description': """
        Launch the default configurations of the La Team Nutra application
    """,

    'author': "RANDRIANASOLO Jean Robert",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['ltn_base',
                # 'product',
                # 'account',
                # 'sale_stock',
                ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/res_config_settings.xml',
        'views/views.xml',
        'data/company_infos.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'sequence': -49,
}
