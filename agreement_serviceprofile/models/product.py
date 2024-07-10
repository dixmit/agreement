# Copyright (C) 2019 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_serviceprofile = fields.Boolean(
        string="Create Service Profiles",
        help="""If True, this product will create a service profile on the
         agreement when the sales order is confirmed.""",
    )

    @api.depends("is_serviceprofile")
    def _compute_type(self):
        for record in self:
            if record.is_serviceprofile:
                record.type = "service"
            else:
                super(ProductTemplate, self)._compute_type()

        return True


class ProductProduct(models.Model):
    _inherit = "product.product"

    is_serviceprofile = fields.Boolean(
        string="Create Service Profiles",
        help="""If True, this product will create a service profile on the
         agreement when the sales order is confirmed.""",
    )

    @api.depends("is_serviceprofile")
    def _compute_type(self):
        for record in self:
            if record.is_serviceprofile:
                record.type = "service"
            else:
                super(ProductProduct, self)._compute_type()

        return True
