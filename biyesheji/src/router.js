import Vue from 'vue'
import Router from 'vue-router'
// import Home from './views/Home.vue'
// import Login from './views/login/login.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',//mode history代表，路由不再显示hash
  base: process.env.BASE_URL,//代表着是基本的路由请求的路径。
  routes: [
    {
      path:'/',
      name:'index',
      component: () => import('./views/index/index.vue'),
      redirect: '/shouye' ,
    //   meta:{
    //     requiresAuth:true,
      //  登录验证
      
//       //元信息元数据
      children:[
          {
            path: 'shouye',
            name: 'shouye',// 首页
            component: () => import('./views/shouye/shouye.vue'),
          },
        {
          path:"man",
          name:"man",
          component:()=>import('./components/man/man.vue'),
        },
        
        {
            path:'woman',
            name:'woman',
            component:()=>import('./components/woman/woman.vue'),
        },
        {
            path:'category',
            name:'category',
            component:()=>import('./components/category/category.vue'),
        },
        {
          path:'category/xiangqing',
          name:'xiangqing',
          component:()=>import('./components/xiangqing/xiangqing.vue'),
        },
        {
            path:'series',
            name:'series',
            component:()=>import('./components/series/series.vue'),
        },
        {
            path:'logon',
            name:'logon',
            component:()=>import('./components/logon/logon.vue')
        },
        {
          path:'login',
          name:'login',
          component:()=>import('./components/logon/login.vue')
      },
      {
          path:'person',
          name:'person',
          component:()=>import('./views/person/person.vue')
      },
          {
          path:'shopping',
          name:'shopping',
          component:()=>import('./views/shopping/shopping.vue')
      },

  ]
    }]
})
