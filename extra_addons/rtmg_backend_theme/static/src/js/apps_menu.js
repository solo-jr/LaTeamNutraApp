odoo.define('rtmg_backend_theme.AppsMenu', function (require) {
var AppsMenu = require('web.AppsMenu');
var AppsMenu = AppsMenu.include({
    events: _.extend({}, AppsMenu.prototype.events, {
        'click .fullhome': '_onclick_fullhome',
    }),
    _onclick_fullhome: function(e){
        $('.full').first().click();
        console.log($('.full').get())
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
    },
    init: function (parent, menuData) {
        this._super.apply(this, arguments);
        this._apps = _.map(menuData.children, function (appMenuData) {
            return {
                actionID: parseInt(appMenuData.action.split(',')[1]),
                menuID: appMenuData.id,
                name: appMenuData.name,
                xmlID: appMenuData.xmlid,
                icon: appMenuData.web_icon_data,
            };
        });
    },
    start: function () {
        this._super();
        var $dropdownMenu =  this.$('.dropdown-menu');
        var $contentMenuApp =  this.$('.content-menu-app');
        function configAppSize(){
            if($dropdownMenu.attr('class').includes('show')){
                $dropdownMenu.css('width', window.innerWidth+'px');
                $dropdownMenu.css('height', (window.innerHeight - $('header > .o_main_navbar').outerHeight())+'px');
//                var topValue = ($dropdownMenu.height()-$contentMenuApp.height())/2;
//                topValue = (topValue>0)?topValue:0;
//                $contentMenuApp.css('top', topValue+'px');
            }
            else {
                $dropdownMenu.css('width', '0px');
                $dropdownMenu.css('height', '0px');0
            }
        }
        var configAfterShow= function(e){
            for(var i in e) {
                var mutation = e[i];
                if (mutation.type == 'attributes'
                    && ['class'].includes(mutation.attributeName)
                ) {
                    configAppSize()
                }
            }
        };
        window.onresize = function(e){
            configAppSize();
//            window.location.reload();
        }
        var onAppShow = new MutationObserver(configAfterShow)
        onAppShow.observe($dropdownMenu.get()[0], {attributes: true})
//        window.innerHeight -= 50;
//        $('.buttonsfull').css('top', (window.innerHeight + 5) +'px');
//        $('.buttonsfull').css('display', 'block');
    },
});
return AppsMenu;
});
