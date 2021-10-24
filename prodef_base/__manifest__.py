# -*- coding: utf-8 -*-
{
    'name': "Prodef base module",

    'summary': """
        Prodef Base module""",

    'description': """
        Prodef Base module
    """,

    'author': "Moad KHIDER",
    'website': "http://www.prodef.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','account'],
    'data': [
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        'views/report_invoice.xml',
        # 'views/instance_monitoring.xml',
        # 'views/server_config_admin.xml',
        # 'views/menu.xml',
        # 'data/cron_instances_create.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
