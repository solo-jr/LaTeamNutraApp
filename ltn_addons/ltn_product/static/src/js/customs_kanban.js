odoo.define('ltn_product.customs_kanban', function (require) {
'use strict';

var KanbanRecord = require('web.KanbanRecord');

KanbanRecord.include({
    _openRecord: function () {
//        if (this.selectionMode !== true && this.modelName === 'ltn.thematic' &&
        if (['ltn.thematic', 'res.partner'].includes(this.modelName) &&
            this.$(".link_for_product a").length) {
            this.$('.link_for_product a').first().click();
        } else {
            this._super.apply(this, arguments);
        }
    },
});

});