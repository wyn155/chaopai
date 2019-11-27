<template>
    <div class="xilie">
        <div class="tuijian">
            <strong>
                <span>人</span>
                <span>气</span>
                <span>单</span>
                <span>品</span>
            </strong>

        </div>
        <div style="padding:30px 0">
            <el-carousel :interval="4000" type="card" height="500px">
            <el-carousel-item v-for="item in 3" :key="item">
            <h3 class="medium"></h3>
            </el-carousel-item>
        </el-carousel>
        </div>
        <div style="width:150px;height:40px;border-radius:20px;;background-color:rgb(147, 12, 236);text-align:center;line-height:40px;color:white;margin:0 auto;">
            单品详情
        </div>
        
        
        
    </div>
</template>
<script>
export default {
    name:'',
}
</script>

<style scoped>
    .tuijian{
        margin: 0 auto;
        background: url(../../assets/no1.png) no-repeat;
        width: 250px;
        height:70px;
    }
    .tuijian {
        text-align: center;
        line-height: 70px;
    }
    .tuijian span{
        padding-right: 30px;
        color: rgb(126, 20, 20);
    }
    .el-carousel__item h3 {
        margin: 0 auto;
        color: #475669;
        font-size: 14px;
        /* opacity: 0.75; */
        line-height: 200px;
        margin: 0;
        
    }
  
  .el-carousel__item:nth-child(2n) {
    background:url("../../assets/daohang2.jpg") no-repeat;
    background-size: contain;
    background-position: 100px ;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background:url("../../assets/daohang2.jpg") no-repeat;
    background-size: contain;
    background-position: 100px ;


  }
  .medium{
      width:300px;
  }
  .el-carousel__mask{
      
      background-color: transparent;
  }
</style>