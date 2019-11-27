<template>
    <div class="category">
         
        <el-breadcrumb separator="/">

            <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item><a href="/">分类</a></el-breadcrumb-item>
            <el-breadcrumb-item>上衣</el-breadcrumb-item>
        </el-breadcrumb>
        <div class="buju">

        
            <div class="jiansuo">
                <div class="shaixuan">
                    <h5>我的筛选</h5>
                    <p style="font-size:10px;color:#ccc;">重置筛选</p>
                    
                </div>
                    <div style="padding-bottom:10px;border-bottom:1px solid #ccc;">
                        <div class="shaixuan1">
                        <div class="shaixuan2"><p>上衣</p><p>x</p></div>
                        <div class="shaixuan2"><p>男装</p><p>x</p></div> 
                    </div>
                    <div class="shaixuan1">
                        <div class="shaixuan2"><p>短袖</p><p>x</p></div>
                        <div class="shaixuan2"><p>国潮</p><p>x</p></div> 
                    </div>
                </div>
                <div class="sex">
                    <p><strong>性别</strong></p>
                    <div style="padding-top:5px;">
                        <div style="float:left;padding:5px 5px 5px 18px;">男士</div>
                        <div style="float:left;padding:5px 5px 5px 10px;">女士</div>

                    </div>
                    
                </div>
                <div class="sex">
                    <p><strong>分类</strong></p>
                    <div style="padding-top:5px;">
                        <div style="float:left;padding:5px 5px 5px 18px;">上衣</div>
                        <div style="float:left;padding:5px 5px 5px 10px;">下装</div>

                    </div>
                    
                </div>
                <div class="sex">
                    <p><strong>类型</strong></p>
                    <div style="padding-top:5px;">
                        <div style="float:left;padding:5px 5px 5px 18px;">夹克</div>
                        <div style="float:left;padding:5px 5px 5px 10px;">卫衣</div>
                        <div style="float:left;padding:5px 5px 5px 18px;">短袖</div>
                        <div style="float:left;padding:5px 5px 5px 10px;">衬衫</div>

                    </div>
                    
                </div>
                <div class="fengge">
                    <p><strong>风格</strong></p>
                    <div style="padding-top:5px;">
                        <div style="float:left;padding:5px 5px 5px 18px;">纯色</div>
                        <div style="float:left;padding:5px 5px 5px 10px;">国潮</div>
                        <div style="float:left;padding:5px 5px 5px 18px;">工装</div>
                        <div style="float:left;padding:5px 5px 5px 10px;">复古</div>
                        <div style="float:left;padding:5px 5px 5px 18px;">日系</div>
                        <div style="float:left;padding:5px 5px 5px 10px;">美式</div>

                    </div>
                    
                </div>
                <div class="xilie">
                    <p><strong>产品系列</strong></p>
                    <div style="padding-top:10px;font-size:12px">
                        <div style="padding:5px 5px 5px 18px;">ZERO GRAVITY</div>
                        <div style="padding:5px 5px 5px 18px;">STREENATIONAL TIDE</div>
                        <div style="padding:5px 5px 5px 18px;">AMERICAN STYLE TOOLING</div>
                        

                    </div>
                    
                </div>
                

                
                
            </div>
            <div class="goods">
                <h2>[37 件商品]</h2>
                <el-dropdown>
                    <span class="el-dropdown-link">
                        请选择商品排列方式<i class="el-icon-arrow-down el-icon--right"></i>
                    </span>
                    <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item>价格</el-dropdown-item>
                        <el-dropdown-item>综合</el-dropdown-item>
                        <el-dropdown-item>销售量</el-dropdown-item>
                        
                    </el-dropdown-menu>
                </el-dropdown>
                <div class="xiangqing2">
                    
                    <div style="padding:15px 30px;">
                        <div style="width:250px;">
                            <img src="../../assets/yifu1.png" alt="" style="width:100%;">
                        </div>
                        <p style="color:red;padding:10px 15px;">STREENATIONAL TIDE</p>
                        <p style="padding:5px 15px"><strong>19SS美式工装衬衫打印花卫衣</strong></p>
                        <div style="border-bottom:2px solid red;width:30px;margin:5px 15px"></div>
                        <p style="padding:5px 15px"><strong>1699.00</strong><font size='1'>RMB</font></p>
                        <router-link :to="{name:'xiangqing'}">
                            <div style="width:120px;height:30px;text-align:center;line-height:30px;background:#6c33e1;border-radius:25px;color:white;margin:0 auto;">结算</div>
                        </router-link>
                    </div>
                    <div style="padding:15px 30px;">
                        <div style="width:250px;">
                            <img src="../../assets/yifu1.png" alt="" style="width:100%;">
                        </div>
                        <p style="color:red;padding:10px 15px;">STREENATIONAL TIDE</p>
                        <p style="padding:5px 15px"><strong>19SS美式工装衬衫打印花卫衣</strong></p>
                        <div style="border-bottom:2px solid red;width:30px;margin:5px 15px"></div>
                        <p style="padding:5px 15px"><strong>1699.00</strong><font size='1'>RMB</font></p>
                        <router-link :to="{name:'xiangqing'}">
                            <div style="width:120px;height:30px;text-align:center;line-height:30px;background:#6c33e1;border-radius:25px;color:white;margin:0 auto;">结算</div>
                        </router-link>
                    </div>
                    
                 
                </div>
                <div class="xiangqing2">
                    
                    <div style="padding:15px 30px;">
                        <div style="width:250px;">
                            <img src="../../assets/yifu1.png" alt="" style="width:100%;">
                        </div>
                        <p style="color:red;padding:10px 15px;">STREENATIONAL TIDE</p>
                        <p style="padding:5px 15px"><strong>19SS美式工装衬衫打印花卫衣</strong></p>
                        <div style="border-bottom:2px solid red;width:30px;margin:5px 15px"></div>
                        <p style="padding:5px 15px"><strong>1699.00</strong><font size='1'>RMB</font></p>
                        <router-link :to="{name:'xiangqing'}">
                            <div style="width:120px;height:30px;text-align:center;line-height:30px;background:#6c33e1;border-radius:25px;color:white;margin:0 auto;">结算</div>
                        </router-link>
                    </div>
                    <div style="padding:15px 30px;">
                        <div style="width:250px;">
                            <img src="../../assets/yifu1.png" alt="" style="width:100%;">
                        </div>
                        <p style="color:red;padding:10px 15px;">STREENATIONAL TIDE</p>
                        <p style="padding:5px 15px"><strong>19SS美式工装衬衫打印花卫衣</strong></p>
                        <div style="border-bottom:2px solid red;width:30px;margin:5px 15px"></div>
                        <p style="padding:5px 15px"><strong>1699.00</strong><font size='1'>RMB</font></p>
                        <router-link :to="{name:'xiangqing'}">
                            <div style="width:120px;height:30px;text-align:center;line-height:30px;background:#6c33e1;border-radius:25px;color:white;margin:0 auto;">结算</div>
                        </router-link>
                    </div>
                     
                 
                </div>
                <!-- 分页 -->
                <el-pagination
                size="medium"
                :page-size="20"
                :pager-count="11"
                layout="prev, pager, next"
                :total="1000">
                </el-pagination>
            </div>
        </div>


       
    </div>
</template>
<script>
export default {
    name:'',
    mounted(){
            let that =this
              this.$axios.get("/category").then(res=>res.data).then(function (data) {
                  if(data.code == 200){

                      alert(data.data)
                      that.tableData = data.data
                  }
              }).catch(function (error) {
                  alert(error)
              })
        },
    
}
</script>

<style>
    .category{
        padding: 20px 300px;
    }
    /* .buju{
        display: flex;
        justify-content:space-between;
    } */
    .shaixuan{
        
        display: flex;
        justify-content:space-between;
    }
    .jiansuo{
        width:200px;
        height:auto;
        padding: 20px 0;
        float: left;
    }
    .shaixuan1{
        padding: 10px 10px 5px;
        display: flex;
        justify-content:space-between;
        
    }
    .shaixuan1 div{
        width:50px;
        height:24px;
        border-radius: 10px;
        background-color:#6c33e1;
        color:white;
        font-size: 12px;
        /* text-align: center; */
        line-height: 24px;
        
    }
    .shaixuan2{
        padding: 0 6px;
        display: flex;
        justify-content:space-between;
    }
    .sex{
        height: 55px;
        padding:10px 0;
        font-size: 14px;
        border-bottom: 1px solid #ccc;
        
    }
    .fengge{
        height: 80px;
        padding:10px 0;
        font-size: 14px;
        border-bottom: 1px solid #ccc;
        
    }
    .xilie{
        height: 95px;
        padding:10px 0;
        font-size: 14px;
        /* border-bottom: 1px solid #ccc; */
    }
    .goods{
        float: left;
        margin-left: 80px;
        padding:20px 0;
        }
    .el-dropdown{
        padding:10px;
    }
    .xiangqing2{
        width: 100%;
        display: flex;
        justify-content:space-between;
    }
</style>