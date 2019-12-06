<template>
    <div class="login-box">
        <el-row :span="24" style="padding: 0 50px;height: 96px;line-height: 96px">
            <el-col :span="6" class="logo-box">
                <i class="iconfont icon-dianying"></i>
                <span>潮牌</span>
            </el-col>
        </el-row>
<!--        登录-->
        <el-card class="login-right">
            <el-row :span="24" style="padding: 30px 30px 20px 30px">
                <p>注册</p>
                <el-form :model="ruleForm" :rules="rules" status-icon ref="ruleForm">

                    <el-form-item prop="username">
                        <el-input placeholder="请输入用户名" clearable v-model="ruleForm.username" style="width: 284px;"></el-input>
                    </el-form-item>

                    <el-form-item prop="password">
                        <el-input placeholder="请输入密码" clearable v-model="ruleForm.password" type="password" style="width: 284px"></el-input>
                    </el-form-item>

                    <el-form-item prop="passwordyes">
                        <el-input placeholder="请确认密码" clearable v-model="ruleForm.passwordyes" type="password" style="width: 284px"></el-input>
                    </el-form-item>
                    <router-link :to="{name:'login'}">
                        <el-button type="danger" style="width:284px" @click="onSubmit('ruleForm')">注册</el-button>
                    </router-link>

                </el-form>
                <el-row :span="24">
                    <el-col :span="24" class="ty-box">注册即代表同意
                        <a href="https://www.xinpianchang.com/aboutus/responsibility">《用户协议》</a>
                    </el-col>
                </el-row>

            </el-row>
            <el-row :span="24" class="btn-box">
                <el-col :span="24">
                    <router-link :to="{name:'login'}" tag="span">已有账号？登录</router-link>
                </el-col>
            </el-row>

        </el-card>
    </div>
</template>

<script>
    // @ is an alias to /src
    // import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'login',
        components: {
            // HelloWorld
        },
        data(){
            return {
                ruleForm:{
                    username:'',
                    password:''
                },
                rules:{
                    username:[
                        { required: true, message: '请输入用户名',trigger:'blur'},
                        { min: 2, max: 20, message: '名字太长，请重新输入', trigger: 'blur' }
                    ],
                    password:[
                        { required: true, message: '请输入密码',trigger:'blur'},
                        { min: 6, message: '密码长度在6位以上', trigger: 'blur' }
                    ],
                    passwordyes:[
                        { required: true, message: '请确认密码',trigger:'blur'},
                    ]
                }
            }
        },
        methods:{
            onSubmit(formName){
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.$message({
                            message: '注册成功',
                            type: 'success',
                        });
                        this.$router.push({name:"index"});
                    } else {
                        this.$message.error('注册失败');
                        return false;
                    }
                });
            }
        },
    }
</script>
<style>
    .login-box{
        width: 100%;
        height: 750px;
        background: url("../../assets/goods/bj.png") no-repeat;
        background-size: cover;
        background-position: 50%;
        position: relative;
    }
    /*    登录*/
    .login-right{
        width: 360px;
        height: 415px;
        float: right;
        /*padding: 30px;*/
        box-sizing: border-box;
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        margin: auto;
        background: white;
        border-radius: 4px;
    }
    .login-right p{
        width: 284px;
        height: 40px;
        color: #33475F;
        font-size: 16px;
        line-height: 40px;
        margin: 0 auto;
    }
    .el-card__body{
        padding: 0!important;
    }
    .ty-box{
        color: #9e9e9e;
        font-size: 12px;
        text-align: left;
        margin: 16px 0 ;
    }
    .ty-box a{
        text-decoration: none;
        color: #3791f6;
    }
    .i-box{
        display: flex;
        justify-content: space-around;
    }
    .i-box .el-col{
        cursor: pointer;
    }
    .i-box a{
        font-size: 20px;
        color: #9E9E9E;
        text-decoration: none;
    }
    .btn-box{
        border-top: 1px solid #f0f0f0;
        background: #fafafa;
        height: 46px;
        line-height: 46px;
        color: #9e9e9e!important;
        font-size: 14px;
    }
    .btn-box span{
        cursor: pointer;
    }
    .btn-box span:hover{
        color: #e74b3b;
    }
    .logo-box{
        color: white;
        font-size: 24px;
        text-align: left;
        font-family: "微软雅黑";
    }
    .logo-box i{
        font-size: 44px;
        margin-right: 8px;
    }
</style>
