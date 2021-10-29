# -*- coding: utf-8 -*-
{
    'name': "La Team Nutra APPS",

    'summary': """
        Install this module to install all La Team Nutra apps dependance""",

    'description': """
        Install this module to install all La Team Nutra apps dependance
    """,

    'author': "RANDRIANASOLO Jean Robert",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'rtmg_backend_theme',
        'rtmg_conf',
        'rtmg_web_patch',
        'ltn_base',
        'ltn_product',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'sequence': -50,
}
