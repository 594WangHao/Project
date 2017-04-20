<template>
    <md-tabs>
        <md-tab :id="point.number" :md-label="'测点' + point.number" v-for="point in equip.points">
            <vue-chart :columns="columns" :rows="rows" :options="options"></vue-chart>
        </md-tab>
    </md-tabs>
</template>
<script>
    import {
        mapState
    } from 'vuex'
    import ajax from '../../lib/ajax.js'
    export default {
        data() {
                return {
                    columns: [{
                        'type': 'string',
                        'label': '时间'
                    }, {
                        'type': 'number',
                        'label': '振幅'
                    }],
                    rows: [],
                    options: {
                        title: '频谱图',
                        // colors: ['#f44336'],
                        // #f44336 红
                        // #ffeb3b 黄
                        hAxis: {
                            title: '时间',

                        },
                        vAxis: {
                            title: '振幅'
                        }
                    }
                }

            },
            computed: mapState({
                equip: state => state.equip,
            }),
            created() {
                this.$store.commit('CURRENT_EQUIP', this.$route.params.id);


                for (let i = 0; i < this.equip.points.length; i++) {
                    let point = this.equip.points[i]
                    // setInterval(() =>{
                    //     var url = '/api/equip_data_vue_charts/equip=' + this.equip.id + '&point=' + point.id + '&start='+
                    //     ajax('GET', url).then(function(data) {
                    //         console.log(data)
                    //     })
                    // }, 1000)

                }


            },
            methods: {
                changeTab(point_id) {
                    console.log('sss')
                    console.log(point_id)
                }
            }
    }
</script>
