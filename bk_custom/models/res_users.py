# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class res_users(osv.osv):
    _inherit = 'res.users'

    _defaults = {
        'notify_email': 'none',
        'email': 'test@test.com'
    }