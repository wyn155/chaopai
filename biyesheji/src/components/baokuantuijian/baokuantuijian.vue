<template>
    <div class="baokuantuijian">
        <p style="text-align:center;font-size:24px;color:#e70909;">爆款推荐</p>
        <p style="text-align:center;font-size:14px;color:#e70909;padding:3px 0;font-family:'微软雅黑'">Explosion recommendation</p>
        <div class="tuijian">
            <div class="information">
                <div class="im">
                    <img src="../../assets/tuijian2.jpg" alt="" style="width:100%;">
                    <span style="padding:5px 0;color:red;font-size:14px;">ZERO GRAVRY</span>
                    <span style="padding:5px 10px;color:red;font-size:14px;">/ 系列 /</span>
                    <div class="hengxian"></div>
                    <p style="padding:15px 0;font-size:13px;">19SS美式街头印花卫衣</p>
                    <span style="font-size:22px;">1399.00</span>
                    <span style="font-size:8px;padding:0 10px;">RMB</span>
                    <div class="purchase">购买</div>
                    
                </div>
                <div class="im">
                    <img src="../../assets/tuijian3.jpg" alt="" style="width:100%;">
                    <span style="padding:5px 0;color:red;font-size:14px;">ZERO GRAVRY</span>
                    <span style="padding:5px 10px;color:red;font-size:14px;">/ 系列 /</span>
                    <div class="hengxian"></div>
                    <p style="padding:15px 0;font-size:13px;">19SS美式街头印花卫衣</p>
                    <span style="font-size:22px;">1399.00</span>
                    <span style="font-size:8px;padding:0 10px;">RMB</span>
                    <div class="purchase">购买</div>
                </div>
                <div class="im">
                    <img src="../../assets/tuijian4.jpg" alt="" style="width:100%;">
                    <span style="padding:5px 0;color:red;font-size:14px;">ZERO GRAVRY</span>
                    <span style="padding:5px 10px;color:red;font-size:14px;">/ 系列 /</span>
                    <div class="hengxian"></div>
                    <p style="padding:15px 0;font-size:13px;">19SS美式街头印花卫衣</p>
                    <span style="font-size:22px;">1399.00</span>
                    <span style="font-size:8px;padding:0 10px;">RMB</span>
                    <div class="purchase">购买</div>
                </div>
            </div>
        </div>
        <el-pagination layout="prev, pager, next" :total="40" style="text-align:center;"></el-pagination>
    </div>
</template>

<script>
export default {
    name:'',
}
</script>

<style scoped>
    .baokuantuijian{
        
        padding:100px 0 0 0;
    }
    .information{
        display: flex;
        justify-content: space-between;
    }
    .im{
        width:280px;

    }
    .hengxian{
        margin-top:10px;
        width:25px;
        border-bottom: 3px solid red;
    }
    .purchase{
        width:80px;
        height:30px;
        border-radius: 15px;
        background-color: blueviolet;
        color: white;
        text-align: center;
        line-height: 30px;
        float: right;
    }
    .tuijian{
        padding:20px 0;
    }
</style>