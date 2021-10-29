# -*- coding: utf-8 -*-
{
    'name': "ROOTTSMG BACKEND THEME",

    'summary': """
        By installing this module, your community odoo backend theme changes""",

    'description': """
        By installing this module, your community odoo backend theme changes
    """,

    'author': "RANDRIANASOLO Jean Robert",
    'website': "http://www.roottsmg.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'theme',
    'version': '14.1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'web',
    ],

    # always loaded
    'data': [
        'views/templates.xml',
        'views/web_client.xml',
    ],
    # only loaded in demonstration mode
    'qweb': [
        'views/menu.xml',
    ],
    'images': [
        'static/description/img/banner_presentation.png',
        'static/description/img/demo_screenshot.gif',
        'static/description/img/screen-shot3.png',
        'static/description/img/cap1.png',
        'static/description/img/cap2.png',
        'static/description/img/cap3.png',
        'static/description/img/cap4.png',
        'static/description/img/cap5.png',
        'static/description/img/cap6.png',
    ],
    'sequence': -27,
    'application': True,
    'license': 'OPL-1',
    'price': '10',
    'currency': 'EUR',
    'support': 'randrianasolojeanrobert@yahoo.fr',
}
