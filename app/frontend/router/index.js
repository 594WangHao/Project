import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

import Index from '../components/index.vue'


export default new VueRouter({
    routes: [

        {
            path: '/',
            component: Index,
            name: 'index'
        }, {
            path: '/equip/data/:id',
            component: r => require.ensure([], () => r(require('../components/equip/data.vue')), 'equip_data')
        }, {
            path: '/equip/info/:id',
            component: r => require.ensure([], () => r(require('../components/equip/info.vue')), 'equip_info')
        }

    ]
})
