{
    'name': "BK Custom",

    'summary': """
        This module is used to customize the point of sale""",

    'version': '8.0.1.0.0',
    'category': 'Point Of Sale',
    'author': 'BusinessERPWeb <businesserpweb@gmail.com>',
    'application': True,
    'installable': True,
    'depends':['point_of_sale',
               'sales_team'],
    'data': [
            "wizard/pos_session_opening.xml",
            "security/pos_security_view.xml",
            "security/ir.model.access.csv",
            "views/res_users_view.xml",
            "views/main_sub_menu.xml",
            "views/point_of_sale_view.xml",
            "views/pos_order_view.xml",
            "views/product_template_view.xml",
            "views/bk_search_view.xml",
             ],
    'demo': [],
    'qweb': [],
}
