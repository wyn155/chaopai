<template>
    <div>
        <el-table ref="multipleTable"  :data="tableData" tooltip-effect="dark" style="width: 1200px;margin-top:20px" @selection-change="handleSelectionChange">
            <el-table-column type="selection" align="center" width="90" label="全选"></el-table-column>
            <el-table-column align="center" label="商品图片" width="250" prop='img'>
                <template slot-scope="scope">
                    <img :src="scope.row.img" alt="">
                </template>
            </el-table-column>
            <el-table-column label="商品描述" align="center" width="130">
                <template slot-scope="scope">
                    <p style=""><strong>{{ scope.row.name }}</strong></p>
                    <p>{{ scope.row.describe }}</p>
                </template>

            </el-table-column>
            <el-table-column prop="color" align="center" label="颜色" width="150"></el-table-column>
            <el-table-column align="center" label="尺码" width="130">
<!--                <template slot-scope="scope">-->
<!--                    <p>W:{{ scope.row.W }}</p>-->
<!--                    <p>H:{{ scope.row.H }}</p>-->
<!--                    <p>L:{{ scope.row.L }}</p>-->
<!--                </template>-->
            </el-table-column>

            <el-table-column align="center" label="数量" width="150">
                <template scope="scope">
                <el-input-number v-model="scope.row.num1" @change="changeCount(scope.row)" style="width:100px;" size="mini">
                    <el-button slot="prepend" @click="changeQuantity(scope.row,-1)"><i class="el-icon-minus"></i></el-button>
                    <el-button slot="append" @click="changeQuantity(scope.row,1)"><i class="el-icon-plus"></i></el-button>
                </el-input-number>
                </template>
            </el-table-column>
            <el-table-column align="center" label="单价" width="150">
                <template slot-scope="scope">
                    <p style="font-size:16px;"><strong>{{ scope.row. price}}</strong><font size=0.5>RMB</font></p>

                </template>
            </el-table-column>
            <el-table-column align="center" label="总价" width="150">
                <template slot-scope="scope">
                    <p style="font-size:16px;padding-top:70px;"><strong>{{ scope.row.total}}</strong><font size=0.5>RMB</font></p>
                    <el-button type="text" size="small" class="el-icon-delete" style="padding-top:50px;">删除</el-button>

                </template>
            </el-table-column>



        </el-table>
        <div style="width:1200px;height:100px;">
            <div style="float:left;font-size:12px;padding:50px 0 0 15px;">3个结果</div>
            <div style="float:right;padding:50px 0 0 15px;font-size:40px;color:red">
                {{monkey}}<font size=2 color=black>RMB</font>

            </div>
            <div style="float:right;font-size:12px;padding:50px 0 0 15px;">
                <p style="font-size:16px;">应付金额:</p>
                <p>Total payable</p>
            </div>
            <div style="float:right;font-size:16px;padding:50px 50px 0 15px;">运费：<font size=6>300.00</font><font size=2>RMB</font></div>
        </div>


    </div>
</template>
<script>
export default {
    name:'shopping',
    component:{

    },
    data() {
      return {
        monkey:3146.00,
        // describe:'POANG-波昂'+'\n'+'有效',
        // color:"红色",
        // num1:1,


        tableData:[
          {
            name:'POANG-波昂',
            describe:'摇椅 北欧风',
            color:"桦木贴面，基尼萨淡米色",
            W:'59cm',
            H:"23cm",
            L:"87cm",
            num1:'1',
            price:'13451',
            // total:'13451',
            // img:require('../../assets/yifu.png'),

          },
        ],
        multipleSelection: []
      };
    },
    methods: {
    //     handleClick(row) {
    //     // console.log(row);
    //   },
      toggleSelection(rows) {
        if (rows) {
          rows.forEach(row => {
            this.$refs.multipleTable.toggleRowSelection(row);
          });
        } else {
          this.$refs.multipleTable.clearSelection();
        }
      },
      handleSelectionChange(val) {
        this.multipleSelection = val;
      },
    changeQuantity(row, type){
          if( type > 0 ){
            row.count++;
          }else{
            row.count > 1 ? row.count--: row.count = 1;
          }
          this.changeCount(row);
        },
        //数量文本框值改变
        changeCount (row) {
            if(null == row.count || row.count == ""){
              row.count=1;
            }
            row.total = (row.count * row.price).toFixed(2);//保留两位小数
               // alert(row.total+" = "+ row.count +" * "+ row.price)
            //增加商品数量也需要重新计算商品总价
         },
      handleChange() {
          // let val = this.value;
          // alert(val)
        // console.log(value);
      },

    },
    // mounted(){
    //         let that =this
    //           this.$axios.get("/api/shopcar/").then(res=>res.data).then(function (data) {
    //               if(data.code == 200){
    //                   alert(data.data)
    //                   that.tableData = data.data
    //               }
    //           }).catch(function (error) {
    //               alert(error)
    //           })
    //
    //
    //     },
}
</script>

<style scoped>
    .el-input-number__increase{
        border-radius: 50%;
        background-color: aqua;
    }
    .el-table .cell {
            /* word-wrap: break-word; */
            text-align: center;
            white-space: pre-line;/*保留换行符*/
        }
</style>