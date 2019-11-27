<template>
    <div class="shopcar">
        <div class="list">
            <el-steps :active="active" finish-status="success" simple style="margin-top: 20px">
                <el-step title="购物车" ></el-step> 
                <el-step title="确认订单" ></el-step>
                <el-step title="付款方式" ></el-step>
                <el-step title="订单完成" ></el-step>
            </el-steps>
            <!-- 步骤条 -->
        <div v-if="active===0">
            <Shopcar></Shopcar>
        </div>
        <div v-if="active===1">
            <Order></Order>
        </div>
        <div v-if="active===2">
            <Pay></Pay>
        </div>
        <div v-if="active===3">
            <Success></Success>
        </div>
        
        
        
        
        <!-- 列表 -->
        
        
        

        <el-button v-if="active==0 ||active==1||active==2" style="margin-top: 12px;background-color:blueviolet;border-radius:15px;color:white;" @click="next">结算</el-button>
        <Tuijian></Tuijian>

    
            </div>
        
    </div>
</template>

<script>
import Shopcar from '@/components/shopping/shopping.vue'
import Order from '@/components/order/order.vue'
import Pay from '@/components/pay/pay.vue'
import Success from '@/components/success/success.vue'
import Tuijian from '@/components/baokuantuijian/baokuantuijian.vue'
export default {
    name:'',
    components:{
        Tuijian,Shopcar,Order,Pay,Success
    },
    data(){
        return {
            active: 0,
        }
    },
    methods: {
      next() {
        if (this.active++ > 2) this.active = 0;
      }
    }
}
</script>

<style scoped>
    .shopcar{
        
        padding:30px 300px;
    }
    .el-steps--simple{
        background-color:transparent;
    }
   
</style>