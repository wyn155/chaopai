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
            <el-row :span="24" style="padding: 30px">
                <p>用户登录</p>
                <el-form :model="ruleForm" :rules="rules" status-icon ref="ruleForm">

                    <el-form-item prop="username">
                        <el-input placeholder="请输入用户名" clearable v-model="ruleForm.username" style="width: 284px;"></el-input>
                    </el-form-item>

                    <el-form-item prop="password">
                        <el-input placeholder="请输入密码" clearable v-model="ruleForm.password" type="password" style="width: 284px"></el-input>
                    </el-form-item>
                    
                        <el-button type="danger" style="width:284px" @click="onSubmit('ruleForm')">登录</el-button>
                    
                </el-form>
                <el-row :span="24">
                    <el-col :span="24" class="wj-box">忘记密码</el-col>
                </el-row>
                <el-row :span="24" style="height: 46px;line-height: 46px">
                    <el-col :span="24">
                        <el-row :span="24" class="i-box">
                            <el-col :span="4">
                                <el-tooltip class="item" effect="dark" content="微博" placement="top">
                                    <a href="https://weibo.com/login.php" class="iconfont icon-weibo"></a>
                                </el-tooltip>
                            </el-col>
                            <el-col :span="4">
                                <el-tooltip class="item" effect="dark" content="微信" placement="top">
                                    <a href="https://open.weixin.qq.com/connect/qrconnect?appid=wx07b48066de7e5abe&redirect_uri=https://passport.xinpianchang.com/get-weixin-code.php?redirect_uri%3Dhttps://passport.xinpianchang.com/api/user-center/user/login/connect?connect_type%253Dwechat%2526redirect_uri%253Dhttps://passport.xinpianchang.com/connect/v2/callback?redirect_uri%25253Dhttps%2525253A%2525252F%2525252Fpassport.xinpianchang.com%2525252Flogin%2525253Fredirect_uri%2525253Dhttp%252525253A%252525252F%252525252Fwww.vmovier.com%252525252F%25252526type%2525253Dpassword%252526bind%25253D%252525E2%2525259C%25252598%252526type%25253Dwechat%2526client_name%253Dbrowser%2526type%253Dlogin&response_type=code&scope=snsapi_login#wechat_redirect" class="iconfont icon-weixin1"></a>
                                </el-tooltip>
                            </el-col>
                            <el-col :span="4">
                                <el-tooltip class="item" effect="dark" content="QQ" placement="top">
                                    <a href="https://graph.qq.com/oauth2.0/show?which=Login&display=pc&client_id=100467464&redirect_uri=https%3A%2F%2Fpassport.xinpianchang.com%2Fget-weixin-code.php%3Fredirect_uri%3Dhttps%253A%252F%252Fpassport.xinpianchang.com%252Fapi%252Fuser-center%252Fuser%252Flogin%252Fconnect%253Fconnect_type%253Dqq%2526redirect_uri%253Dhttps%253A%252F%252Fpassport.xinpianchang.com%252Fconnect%252Fv2%252Fcallback%253Fredirect_uri%25253Dhttps%2525253A%2525252F%2525252Fpassport.xinpianchang.com%2525252Flogin%2525253Fredirect_uri%2525253Dhttp%252525253A%252525252F%252525252Fwww.vmovier.com%252525252F%25252526type%2525253Dpassword%252526bind%25253D%252525E2%2525259C%25252598%252526type%25253Dqq%2526client_name%253Dbrowser%2526type%253Dlogin&response_type=code&scope=get_user_info" class="iconfont icon-icon"></a>
                                </el-tooltip>
                            </el-col>
                            <el-col :span="4">
                                <el-tooltip class="item" effect="dark" content="邮箱" placement="top">
                                    <a href="https://mail.163.com/" class="iconfont icon-youxiang"></a>
                                </el-tooltip>
                            </el-col>
                        </el-row>
                    </el-col>
                </el-row>
            </el-row>
            <el-row :span="24" class="btn-box">
                <el-col :span="24">
                    <router-link :to="{name:'logon'}" tag="span">没有账号？注册</router-link>
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
                    ]
                }
            }
        },
        methods:{
            onSubmit(formName){
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.$message({
                            message: '登录成功',
                            type: 'success',
                        });
                        this.$router.push({name:"index"});
                    } else {
                        this.$message.error('登录失败');
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
        background: url("../../assets/bj.png") no-repeat;
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
    .wj-box{
        color: #9e9e9e;
        font-size: 14px;
        text-align: right;
        margin: 16px 0 ;
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
