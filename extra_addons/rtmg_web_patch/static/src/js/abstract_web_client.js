odoo.define('rtmg_web_patch.AbstractWebClientInherit', function (require) {
var rpc = require('web.rpc');
var AbstractWebClient = require('web.AbstractWebClient');
var AbstractWebClientInherit = AbstractWebClient.include({
    init: function (parent) {
        var self = this;
        this._super(parent);
        rpc.query({
            model: 'rtmg.web.patch',
            method: 'get_global_name',
            args: [],
        }).then(function (title){
            self.set('title_part', {"zopenerp": title});
        });
    }
});
return AbstractWebClientInherit;
});
