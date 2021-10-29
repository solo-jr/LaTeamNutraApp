# -*- coding: utf-8 -*-
{
    'name': "ROOTTSMG WEB PATCH",

    'summary': """
        With this module you can personalize the signature of odoo in the website and the title of the back office""",

    'description': """
        With this module you can personalize the signature of odoo in the website and the title of the back office
    """,

    'author': "RANDRIANASOLO Jean Robert",
    'website': "http://www.roottsmg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'website',
    'version': '14.1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'web',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # data
        'data/web_patch_value.xml',
        # view
        'views/templates.xml',
        'views/res_config_settings_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'images': [
        'static/description/img/cap2.png',
        'static/description/img/cap3.png',
        'static/description/img/cap1_screenshot.png',
    ],
    'sequence': -27,
    'application': True,
    'license': 'OPL-1',
    'price': '10',
    'currency': 'EUR',
    'support': 'randrianasolojeanrobert@yahoo.fr',
}
