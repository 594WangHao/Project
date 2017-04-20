<template>
    <md-card>
        <md-card-area>
            <md-card-header>
                <div class="md-title">{{equip.name}}</div>
                <div class="md-subheading">车间: {{equip.workshop}}</div>
                <div class="md-subheading">机位: {{equip.seat}}</div>
                <div class="md-subheading">测点数: {{equip.point_number}}</div>
                <div class="md-subheading">AB线: {{equip.abline}}</div>
                <div class="md-subheading">添加时间: {{equip.add_time.split(' ')[0]}}</div>
            </md-card-header>
            <md-card-content>
                {{equip.remarks}}
            </md-card-content>
        </md-card-area>
        <md-card-actions>
            <md-button :href="'#/equip/data/' + equip.id" class="md-primary">频谱数据
                <md-icon>chart_donut</md-icon>
            </md-button>
            <!-- <md-button>返回</md-button> -->
        </md-card-actions>
    </md-card>
</template>
<script>
    import {
        mapState
    } from 'vuex'
    export default {
        computed: mapState({
            equip: state => state.equip
        }),
        created(){
            this.$store.commit('CURRENT_EQUIP', this.$route.params.id)
        }
    }
</script>
