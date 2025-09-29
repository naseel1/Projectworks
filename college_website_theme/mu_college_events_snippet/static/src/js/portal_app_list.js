odoo.define('sedd_website_snippets.website_portal_other_apps', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.SEDDPortalApps = publicWidget.Widget.extend({
    selector: '.sedd_apps_link_list, .sedd_main_quick_link_list',
    start() {
        let SEDDAppsList = this.el.querySelector('#sedd_apps_link_list')
        let SEDDQuickLink = this.el.querySelector('#sedd_main_quick_link_list')
        if (SEDDAppsList){
            this._rpc({
                route: '/internal/sedd_other_applications/',
                params:{}
            }).then(function (data1) {
                console.log("data", data1)
                let html = ``
                data1.forEach(sedd_app=>{
                    html += `
                        <div class="col-lg-2">
                            <a href=${sedd_app.link}>
                                <div class="card mt-3 mb-3 text-center">
                                    <i class="${sedd_app.icon_class ? sedd_app.icon_class : ''} ${sedd_app.icon ? sedd_app.icon : ''}"></i>
                                    <p>${sedd_app.name ? sedd_app.name : ''}</p>
                                </div>
                            </a>
                        </div>`
                })
                SEDDAppsList.innerHTML = html
            })
        }
        if (SEDDQuickLink){
            this._rpc({
                route: '/internal/sedd_quick_links/',
                params:{}
            }).then(function (data2) {
                let html = ``
                data2.forEach(sedd_quick_link=>{
                    html += `
                        <div class="col-lg-4">
                            <a href=${sedd_quick_link.link}>
                                <div class="card text-center">
                                    <i class="${sedd_quick_link.icon_class ? sedd_quick_link.icon_class : ''} ${sedd_quick_link.icon ? sedd_quick_link.icon : ''}"></i>
                                    <p>${sedd_quick_link.name ? sedd_quick_link.name : ''}</p>
                                </div>
                            </a>
                        </div>`
                })
                SEDDQuickLink.innerHTML = html
            })
        }
    },
});

return publicWidget.registry.SEDDPortalApps;

});