# -*- coding: utf-8 -*-

from openerp.osv import osv


class product_template(osv.osv):
    _inherit = 'product.template'
    
    def write(self, cr, uid, ids, vals, context=None):
        if 'available_in_pos' in vals:
            vals['active'] = vals['available_in_pos']
        return super(product_template, self).write(cr, uid, ids, vals, context=context)

    _defaults = {
        'list_price': 0,
    }