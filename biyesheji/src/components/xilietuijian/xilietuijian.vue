<template>
    <div class="xilie">
        <div class="tuijian">
            <strong>
                <span>系</span>
                <span>列</span>
                <span>推</span>
                <span>荐</span>
                
            </strong>
            <!-- <p style="text-align:center;"><strong>SERIESRECOMMENDATION</strong></p> -->
        </div>
        <div style="height:150px;">

        </div>
        <div class="contain">
            <div class="hezi">
                <img src="../../assets/goods/tuijian1.png" alt="" style="position:absolute;left:20px;top:-100px;">
            </div>
            <div class="xiangqing">
                <h3>19SS初代多色宗教拼接卫衣</h3>
                <p style="padding:10px 0;font-size:14px;">19SS初代多色宗教拼接卫衣</p>
                <p style="padding:10px 0;font-size:14px;">
                    他是采用最基础的版型设计，直筒的宽松剪裁，带来了丝丝休闲运动的风格，不挑身材，中心化的设计，无论男女都可选择。
                </p>
                <div style="display: flex;justify-content: space-around;padding-top:80px;">
                    <div style="width:50px;height:20px;border-radius:15px;border:2px solid darkgray;text-align:center;display:inline-block;">卫衣</div>
                    <div style="width:50px;height:20px;border-radius:15px;border:2px solid darkgray;text-align:center;display:inline-block;">纯色</div>
                    <div style="width:50px;height:20px;border-radius:15px;border:2px solid darkgray;text-align:center;display:inline-block;">春夏</div>
                </div>
                <router-link :to="{name:'xiangqing'}">
                    <div class="chakan">
                        查看详情
                    </div>
                </router-link>
            </div>
        </div>
        

        
    </div>
</template>
<script>
export default {
    name:'',
}
</script>

<style scoped>
    .xilie{
        /* background-color: white; */
        padding: 30px 180px;
    }
    .tuijian{
        margin: 0 auto;
        background: url(../../assets/goods/no1.png) no-repeat;
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
    .hezi{
        width:300px;
        height:300px;
        background-color: #2f22e9;
        
    }
    .contain{
        padding-top:100px;
        position: relative;
        display: flex;
        justify-content: space-around;
        padding: 50px 0;
    }
    .xiangqing{
        
        padding-left: 150px;
        

    }
    .chakan{
        width:150px;
        height:50px;
        border-radius: 30px;
        background-color:#2f22e9;
        text-align: center;
        line-height: 50px;
        color: white;
        float:right;
        margin-top: 30px;
    }
</style>