# -*- coding: utf-8 -*-
# Made for Odoo Online. See Odoo LICENSE file for full copyright and licensing details.

{
    'name': '[JOS] Automated Payment on Successful Payment TX',
    'category': 'Accounting',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
This custom module for Odoo Online automatically creates an account.payment
record on successful payment transactions (from payment acquirer). For Authorize.net ONLY.
        """,
    'depends': ['base','payment_authorize','account_accountant','base_action_rule'],
    'data': [
        'data/fields_actions.xml',
        'data/views.xml',

    ],
    'installable': True,
    'application': True,
}
