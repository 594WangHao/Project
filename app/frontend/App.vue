<template>
    <div>
        <md-toolbar>
            <h2 class="md-title" style="flex:1"><a href="/">过程设备远程监测系统</a></h2>
            <md-button href="/admin">设备&amp;用户管理</md-button>
            <md-avatar>
                <img src="https://placeimg.com/64/64/people/8" alt="People">
            </md-avatar>
            <md-button class="md-button" @click.native="logout">
                退出
                <md-icon>exit_to_app</md-icon>
            </md-button>
        </md-toolbar>
        <router-view></router-view>
    </div>
</template>
<script>
    import {
        mapState
    } from 'vuex'
    export default {
        methods: {
            toggleLeftSidenav() {
                this.$refs.leftSidenav.toggle();
            },
            logout() {
                console.log('logout')
                this.$store.dispatch('logout')
            },
        },
        created() {
            this.$store.dispatch('get_equip_list')
        },
        computed: mapState({
            equip_list: state => state.equip_list,
            // user: state => state.user,
        })
    }
</script>
<style lang="less">
    .md-theme-default.md-toolbar{
        a{
            color:#fff !important;

            &:hover{
                text-decoration: none;
            }
        }
        color:#fff !important;
    }
</style>