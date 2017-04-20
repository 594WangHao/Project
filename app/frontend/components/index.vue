<template>
    <md-layout>
        <md-table style="flex:1">
            <md-table-header>
                <md-table-row>
                    <md-table-head>名称</md-table-head>
                    <md-table-head>车间</md-table-head>
                    <md-table-head>机位</md-table-head>
                    <md-table-head>测点数</md-table-head>
                    <md-table-head>AB线</md-table-head>
                    <md-table-head>添加时间</md-table-head>
                    <md-table-head>操作</md-table-head>
                </md-table-row>
            </md-table-header>
            <md-table-body>
                <md-table-row v-for="equip in equip_list" :key="equip.id">
                    <md-table-cell>{{equip.name}}</md-table-cell>
                    <md-table-cell>{{equip.workshop}}</md-table-cell>
                    <md-table-cell>{{equip.seat}}</md-table-cell>
                    <md-table-cell>{{equip.points.length}}</md-table-cell>
                    <md-table-cell>{{equip.abline}}</md-table-cell>
                    <md-table-cell>{{equip.add_time.split(' ')[0]}}</md-table-cell>
                    <md-table-cell>
                        <router-link :to="'/equip/data/'+ equip.id" class="md-primary md-mini">频谱数据</router-link>
                        <router-link :to="'/equip/info/' + equip.id" class="md-primary md-mini">详细信息</router-link>
                    </md-table-cell>
                </md-table-row>
            </md-table-body>
        </md-table>
    </md-layout>
</template>
<script>
    import {
        mapState
    } from 'vuex'
    export default {
        computed: mapState({
            equip_list: state => state.equip_list
        }),

    }
</script>
