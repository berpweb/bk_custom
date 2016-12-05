# -*- coding: utf-8 -*-

from openerp.osv import osv


class product_template(osv.osv):
    _inherit = 'product.template'

    _defaults = {
        'list_price': 0,
    }