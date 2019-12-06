<template>
    <div class="person">
        <el-breadcrumb separator="/">

            <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item><a href="/">个人中心</a></el-breadcrumb-item>
            
        </el-breadcrumb>

        <div class="buju">
            <div class="left-box">
                <div class="touxiang">
                    <el-avatar :size='100' src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
                    <p style="margin-top:10px;"><strong>-994</strong></p>
                    <!-- <el-progress :percentage="50"></el-progress> -->
                </div>
                <div class="neirong">
                      <div class="order">
                        <p style="font-size:16px;padding:5px 0;"><strong>订单中心</strong></p>
                        <!-- <P style="font-size:14px;">ORDER CENTER</p> -->
                        <p style="padding:5px 0;font-size:14px;">全部订单</p>
                        <p style="padding:5px 0;font-size:14px;">待支付订单</p>
                        <p style="padding:5px 0;font-size:14px;">待收货订单</p>
                      </div>
                      <div class="serve">
                        <p style="font-size:16px;padding:5px 0;"><strong>我的服务</strong></p>
                        <p style="padding:5px 0;font-size:14px;">收获地址管理</p>
                        <p style="padding:5px 0;font-size:14px;">退款和售后</p>
                        <p style="padding:5px 0;font-size:14px;">我的购物车</p>
                        <p style="padding:5px 0;font-size:14px;">我关注的商品</p>
                        <p style="padding:5px 0;font-size:14px;">我的优惠</p>
                      </div>
                      <div class="infrom">
                        <p style="font-size:16px;padding:5px 0;"><strong>我的信息</strong></p>
                        <p style="padding:5px 0;font-size:14px;">个人信息</p>
                        <p style="padding:5px 0;font-size:14px;">账户安全</p>
                        <p style="padding:5px 0;font-size:14px;">我的尺码</p>
                        <p style="padding:5px 0;font-size:14px;">账号绑定</p>

                      </div>
                    </div>
                 </div>
            <div class="right-box">
                <div style="margin:25px 20px;font-size:24px;">个人信息</div>
                <div class="touxiang">
                    <el-avatar :size='100' src="img" class="el-icon-camera-solid"></el-avatar>
                    
                </div>
                <el-form ref="form" :model="form" label-width="200px">
                  <el-form-item label="昵称：">
                    <el-input v-model="form.name" style="width:300px;"></el-input>
                  </el-form-item>
                  <el-form-item label="真实姓名：">
                    <el-input v-model="form.real" style="width:300px;"></el-input>
                  </el-form-item>
                  <el-form-item label="生日：">
                    <el-input v-model="form.birth" style="width:300px;"></el-input>
                  </el-form-item>
                  <el-form-item label="手机号：">
                    <el-input v-model="form.phone" style="width:300px;"></el-input>
                  </el-form-item>
                  <el-form-item label="性别：">
                    <el-radio-group v-model="form.sex">
                      <el-radio label="男"></el-radio>
                      <el-radio label="女"></el-radio>
                    </el-radio-group>
                  </el-form-item>



                </el-form>
            </div>
        </div>
        <div>
          <Tuijian></Tuijian>
        </div>

    </div>
</template>

<script>
import Tuijian from '@/components/baokuantuijian/baokuantuijian.vue'
export default {

    name:'',
    components:{
      Tuijian,
    },
    data() {
      return {
        value1: '',
        img:'',
        form: {
          name: '',
          real:'',
          birth:'',
          phone:'',
          sex:'',
        }
      }
    },
    methods: {
      onSubmit() {
        // console.log('submit!');
      }
    }
}
</script>

<style scoped>
    .person{
        padding: 30px 300px;
    }
    .buju{
        display: flex;
        justify-content: space-between;
        padding-top: 30px;
    }
    .left-box{
        box-shadow: 5px 5px 10px 3px rgba(0, 0, 0, 0.1);
        width:200px;
        height:auto;
    }
    .touxiang{
        margin:20px auto;
        text-align: center;
    }
    .right-box{
        box-shadow: 5px 5px 10px 3px rgba(0, 0, 0, 0.1);
        width:650px;
        height:auto;
    }
    .el-icon-camera-solid{
      font-size: 40px;
    }
    .neirong{
      padding:15px 0 15px 50px;
    }
    .serve{
      padding-top:20px;
    }
    .infrom{
      padding-top:20px;
    }
    
</style>