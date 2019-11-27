<template>
    <div class="order">
        <img src="../../assets/xuhao.png" alt="" style="width:180px;">
        <div class="address">
            <div class="address1">
                <div class="ad">
                    <span style="padding-right:10px;">山西省</span>
                    <span>太原市</span>
                </div>
                <p style="margin:10px 0;font-size:14px;">小店区平阳路学府街凯通大厦五层503</p>
                <div class="xx">
                    <div style="float:left;">李嘉豪</div>
                    <div style="float:right;font-size:18px;"><strong>13994255634</strong></div>
                </div>
                <div class="gn">
                    <div style="float:right;color:red">删除</div>
                    <!-- <div style="width:2px;height:12px;background-color:#ccc;line-height:12px;float:right;"></div> -->
                    <div style="float:right;margin-right:30px;">编辑</div>
                </div>
            </div>
            <div class="address2">
                <div class="ad">
                    <span style="padding-right:10px;">山西省</span>
                    <span>太原市</span>
                </div>
                <p style="margin:10px 0;font-size:14px;">小店区平阳路学府街凯通大厦五层503</p>
                <div class="xx">
                    <div style="float:left;">李嘉豪</div>
                    <div style="float:right;font-size:18px;"><strong>13994255634</strong></div>
                </div>
                <div class="gn">
                    <div style="float:right;color:red">删除</div>
                    <!-- <div style="width:2px;height:12px;background-color:#ccc;line-height:12px;float:right;"></div> -->
                    <div style="float:right;margin-right:30px;">编辑</div>
                </div>  
            </div>
            <div class="address2 el-icon-plus">
                
            </div>
        </div>
        <img src="../../assets/xuhao2.png" alt=""  style="width:200px;padding:30px 0;">
        <el-table :data="tableData" style="width: 100%;" align='center'>
            <el-table-column prop="date" label="商品" width="190" align='center'>
                <template slot-scope="scope">
                    <img :src="scope.row.img" alt="" style="height:120px;">
                    <p>{{ scope.row.name }}</p>
                </template>
            </el-table-column>
            <el-table-column prop="color" label="颜色" width="180" align='center'></el-table-column>
            <el-table-column prop="size" label="尺码" width="180" align='center'></el-table-column>
            <el-table-column prop="sum" label="数量" width="180" align='center'></el-table-column>
            <el-table-column prop="price" label="价格" width="180" align='center'></el-table-column>
    </el-table>
    <div class="total">
        合计:{{}}
    </div>
    </div>
</template>
<script>
export default {
    name:'',
    data(){
        return{
            tableData:[
                {
                    img:require('../../assets/list2.jpg'),
                    name:'港风小清新英文刺绣卫衣',
                    color:'红色',
                    size:'xl',
                    sum:'18',
                    price:'1399.00'
                },
                {
                    img:require('../../assets/list2.jpg'),
                    name:'港风小清新英文刺绣卫衣',
                    color:'红色',
                    size:'xl',
                    sum:'18',
                    price:'1399.00'
                },
            ]
        }
    }

}
</script>
<style scoped>
    .order{
        padding:40px 0;
    }
    .address{
        
        padding:40px;
        
    }
    .address1{
        width: 200px;
        height:120px;
        border-radius: 20px;
        box-shadow: 5px 5px 10px 3px rgba(0, 0, 0, 0.1);
        border-left: 20px solid hsl(263, 95%, 48%);
        padding:20px 15px;
        float: left;
    }
    .address2{
        width: 200px;
        height:120px;
        margin-left: 20px;
        border-radius: 20px;
        box-shadow: 5px 5px 10px 3px rgba(0, 0, 0, 0.1);
        /* border-left: 20px solid hsl(263, 95%, 48%); */
        padding:20px 15px;
        float: left;
    }
    .ad{
        font-size: 14px;
    }
    .xx{
        font-size:20px;
        padding:20px 0;
    }
    .gn{
        font-size: 12px;
        float: right;
    }
    .el-icon-plus{
        text-align: center;
        line-height: 120px;
        font-size: 60px;
        color: hsl(263, 95%, 48%);
    }
</style>