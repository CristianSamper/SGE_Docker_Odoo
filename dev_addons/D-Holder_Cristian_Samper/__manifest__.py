#-*- coding: utf-8 -*-
{
    'name':"Gestión D-Holder",

    'summary':"Modulo utilizado para gestionar la Empresa D-Holder"
        """Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description':"Módulo utilizado para gestionar la empresa D-Holder"
        """Long description of module's purpose
            """,
    'author'"Cristian Samper Muñoz",
    'website':"",

    #Categories can be used to filter modules in modules listing
    #Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    #for the full list
    'category':'Uncategorized',
    'version':'0.1',

    #any module necesary for this one to work correctly
    'depends':['base'],

    #always loades
    'data':[
        'security/ir.model.access.csv',
        'views/views_Cristian.xml',
        'views/templates.xml',
    ],
    #only loades in demonstration mode
    'demo':[
        'demo/demo.xml',
    ],
}