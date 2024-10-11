##############################################################################
# Copyright (c) 2024 braintec AG (https://braintec.com)
# All Rights Reserved
#
# Licensed under the Odoo Proprietary License v1.0 (OPL).
# See LICENSE file for full licensing details.
##############################################################################


from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    saml_provider_id = fields.Many2one(
        "auth.saml.provider", string="Default SAML Provider"
    )
