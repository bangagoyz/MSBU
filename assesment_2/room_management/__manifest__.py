{
    'name': 'Room Booking Management',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Module for managing room bookings',
    'author': 'Your Company',
    'website': 'http://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/room_views.xml',
        'views/booking_views.xml'
        
    ],
    'installable': True,
    'application': True,
}