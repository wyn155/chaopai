<template>
    <div class="index-box">
      <el-container>
          
              <el-header>
                  <Header></Header>
              </el-header>
              <el-main>
                  <router-view></router-view>
              </el-main>
              <el-footer>
                  <Footer></Footer>
              </el-footer>
          
      </el-container>
    </div>
</template>

<script>
import Header from '@/components/header/header.vue'
import Footer from '@/components/footer/footer.vue'


export default {
    name:"index",
    components:{
        Header,Footer,
    }
}
</script>

<style>
    .el-header{
        padding: 0;
        height:80px!important;
    }
    .index-box{
        width:100%;
        height:auto;
    }
    .el-main{
        padding:0;
    }
     .el-footer{
      padding: 0;
  }


    
</style>