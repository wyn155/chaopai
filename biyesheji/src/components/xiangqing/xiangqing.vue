<template>
    <div class="xiangqing">
        <el-breadcrumb separator="/">
            
            <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item><a href="/">分类</a></el-breadcrumb-item>
            <el-breadcrumb-item><strong>上衣</strong></el-breadcrumb-item>
            <el-breadcrumb-item><strong>19SS美式工装衬衫打印花卫衣</strong></el-breadcrumb-item>
        </el-breadcrumb>
        <div class="fenbu">
            <div class="dahezi">
                <div class="datupian">
                    <img src="../../assets/goods/shop1.jpg" alt="" style="height: 100%;">
                </div>
                <div class="xiaotupian">
                    <img src="../../assets/goods/shop1-1.jpg" alt="" style="padding-top:20px;">
                    <img src="../../assets/goods/shop1-1.jpg" alt="" style="padding-top:20px;">
                    <img src="../../assets/goods/shop1-1.jpg" alt="" style="padding-top:20px;">
                </div>
            </div>
            <div class="describe">
                <h1>19SS街头国潮纯色卫衣</h1>
                <h1 style="padding:15px 0;">19SS Street Guochao Pure-color Sanitary Clothes</h1>
                <div class="hengxian"></div>
                <div class="wenzi">他是采用最基础的版型设计，直筒的宽松剪裁，带来了丝丝休闲运动的风格，不挑身材，中心化的设计，无论男女都可选择</div>
            
                <div class="yanse">
                     <div style="font-size:20px;line-height:40px;"><strong>颜 色</strong></div>
                    <div style="width:40px;height:40px;border-radius:50%;background-color:blue;margin:0 20px;"></div>
                    <div style="width:40px;height:40px;border-radius:50%;background-color:green;margin:0 20px;"></div>
                    <div style="width:40px;height:40px;border-radius:50%;background-color:pink;margin:0 20px;"></div>
                </div>
                <div class="size">
                    <div style="font-size:20px;line-height:40px;width: 50px;">尺 码</div>
                    <div style="margin-top:5px;margin-left:15px;width:50px;height:20px;border-radius:15px;border:3px solid #ccc;text-align:center;line-height:20px;">M</div>
                    <div style="margin-top:5px;margin-left:15px;width:50px;height:20px;border-radius:15px;border:3px solid #ccc;text-align:center;line-height:20px;">L</div>
                    <div style="margin-top:5px;margin-left:15px;width:50px;height:20px;border-radius:15px;border:3px solid #ccc;text-align:center;line-height:20px;">XL</div>
                    <div style="margin-top:5px;margin-left:15px;width:50px;height:20px;border-radius:15px;border:3px solid #ccc;text-align:center;line-height:20px;">XXL</div>
                </div>
                <div class="num">
                    <div style="font-size:20px;line-height:40px;padding-right:20px;">数 量</div>
                    <el-input-number v-model="num" @change="handleChange" size="small" style="margin-top:5px;" :min="1"></el-input-number>
                    <div style="line-height:40px;padding-left:20px;">库存8件</div>
                </div>
                <div style="margin-top:10px;width:160px;height:50px;border-radius:20px;text-align:center;line-height:50px;color:white;background-color:#6c33e1">立即购买</div>
               
            </div>
        </div>
        
    </div>
</template>

<script>
export default {
    name:'',
    data(){
        return {
            num: 1
        }
    },
     methods: {
      handleChange() {
        // alert(value);
      }
    }
}
</script>
 
<style scoped>
    .xiangqing{
        padding:30px 300px;  
    }
    .fenbu{
        display: flex;
        justify-content:space-between;
    }
    .datupian{
        padding-top: 50px;
        height: 600px;
    }
    .xiaotupian{
        
        width:163px;
        height:auto;
        margin-top: 90px;
        margin-left: 20px;
        
    }
    .dahezi{
        width: 660px;
        display: flex;
        justify-content: space-between;
        
       
    }
    .describe{
        padding-top:50px;
        margin-left: 50px;
    }
    .hengxian{
        margin:20px 0;
        width:50px;
        border-bottom: 5px solid #000;
        
    }
    .wenzi{
        color: #ccc;
        padding:30px 0;
        font-size: 14px;
    }
    .yanse{
        margin:20px 0 20px;
        display: flex;
        justify-content: flex-start;
    }
    .size{
        display: flex;
        justify-content: flex-start;
        padding:10px 20px 30px 0;
        
    }
    .num{
        display: flex;
        justify-content: flex-start;
        padding:15px 20px 30px 0;
    }
</style>