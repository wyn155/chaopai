<template>
    <div class="main">
        <el-carousel :interval="4000" type="card" height="400px">
            <el-carousel-item v-for="item in 3" :key="item">
            <!-- <h3 class="medium">{{ item }}</h3> -->
            </el-carousel-item>
        </el-carousel>
        <div style="padding:20px 0;">
            <Xilie></Xilie>
        </div>
        <div style="padding:20px 0;">
            <Renqi></Renqi>
        </div>
        <!-- <div style="padding:20px 0;">
            <Yugao></Yugao>
        </div> -->

    </div>
</template>
<script>
import Xilie from '@/components/xilietuijian/xilietuijian.vue'
import Renqi from '@/components/renqidanpin/renqidanpin.vue'
// import Yugao from '@/components/xinpinyugao/xinpinyugao.vue'
export default {
    name:'mains',
    components:{
        Xilie,Renqi,
       
    },
    data(){
        return {
            
        }
    }
}
</script>

<style scoped>
    .main{
        padding:30px 150px;
        background-color: rgb(223, 223, 223);
    }
    .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background:url('../../assets/goods/daohang.jpg');
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background:url('../../assets/goods/daohang.jpg');
  }
 
</style>