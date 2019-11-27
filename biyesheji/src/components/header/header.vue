<template>
    <div class="header">
        <el-row :span="24">
            <el-col :span="4" style="height: 80px">
               
            </el-col>
            <el-col :span="16" style="height: 80px">
                <el-row :span="24">
                    <el-col :span="24" style="line-height: 80px;float: right;">
                        <el-row :span="24">
                            <el-menu  class="el-menu-demo" mode="horizontal" @select="handleSelect" text-color="#fff" background-color="transparent" style="display:flex;height: 80px;justify-content: space-between;">
                                <el-menu-item index="1">
                                    <router-link :to="{name:'man'}" tag="div">
                                        <p style="margin-top:10px;">男士</p>
                                        
                                    </router-link>
                                </el-menu-item>
                                <el-menu-item index="2">
                                    <router-link :to="{name:'woman'}" tag="div">
                                        <p style="margin-top:10px;">女士</p>
                                        
                                    </router-link>
                                </el-menu-item>
                                <el-menu-item index="3">
                                    <img src="../../assets/logo.png" alt="">
                                </el-menu-item>
                                <el-menu-item index="4">
                                    <router-link :to="{name:'category'}" tag="div">
                                        <p style="margin-top:10px;">分类</p>
                                        
                                    </router-link>
                                </el-menu-item>
                                <el-menu-item index="5">
                                    <router-link :to="{name:'series'}" tag="div">
                                        <p style="margin-top:10px;">系列</p>
                                        
                                    </router-link>
                                </el-menu-item>
                                

                            </el-menu>
                        </el-row>
                    </el-col>
                </el-row>
            </el-col>
        </el-row>
        
    </div>
</template>

<script>
export default {
    name:'headers',
    data(){
            return {
                
            }
        },
        methods: {
            handleSelect() {
            }
        }
}
</script>

<style scoped>
   
    .header{
        width:100%;
        height:80px!important;
        background-color: #6c33e1;
        
    }
    
</style>