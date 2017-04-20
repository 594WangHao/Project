import Vue from 'vue'
import Vuex from 'vuex'

import ajax from '../lib/ajax.js'

Vue.use(Vuex)

const state = {
    user:{},
    equip:{},
    equip_list:[]
}

const actions = {
    logout({commit, state}){
        ajax('GET', '/api/logout/')
        .then(function (data) {
            window.location.href = '/';
        })
    },
    get_equip_list({commit, state}){
        ajax('GET','/api/equip_list/')
        .then(function (data) {
            commit('GET_EQUIP_LIST',data)
        })
    }
}

const mutations = {
    GET_EQUIP_LIST(state, data){
        state.equip_list = data;
    },
    CURRENT_EQUIP(state, id){
        for (var i = 0; i < state.equip_list.length; i++) {
          if (state.equip_list[i]['id'] == id){
            state.equip = state.equip_list[i];
          }
        }
    }
}

export default new Vuex.Store({
    state,
    actions,
    mutations
})