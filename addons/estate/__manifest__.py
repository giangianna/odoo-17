{
    'name': "Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Gian Gianna Pallan Pallas",
    'category': 'App',
    'description': """
        This module is used to learn basic odoo 17 technical
    """,
    'application': True,
    'data': [
        # security
        'security/ir.model.access.csv',  
        
        # templates
        # 'data/templates/example_email_template.xml',  

        # views
        'views/estate_property.xml',
        'views/estate_property_type.xml',
        'views/estate_property_offer.xml',
        'views/menu.xml', # the order position matter!
        
        # Load initial Data
        'data/estate.property.csv',
        # Schedulers
        'views/schedulers/estate_property_scheduler.xml'
    ]
}