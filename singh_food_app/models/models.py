from odoo import fields, models, api

# Adding Categories model for singh food app.
class Categories (models.Model):

    # Holds the name of the table in database
    _name = 'foodapp.categories'

    # Holds the description of the table in database
    _description = 'Model for storing categories of the food app and do CRUD operations.'

    # Sorts the categories descending order with the time of registration.
    _order = "create_date desc"

    # Adding a filed (column) for the food app category. Char is varchar or string with a
    # small length.
    name = fields.Char(required=True,translate=True)

    # Adding a filed (column) for the image of the author which stores binary data for any
    # file format.
    image = fields.Binary()

    # Adding a filed (column) for the reverse relation of the publisher with the book which
    # stores all the books ids that the publisher had published. Note: postgres stores ids
    # but odoo displays them as a list of books records in his views which is nice.
   # products = fields.One2many("foodapp.products","categories")


