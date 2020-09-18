<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                        安全退出
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    欢迎，{{users}}, 访问百知员工管理系统
                </h1>
                <table class="table">
                    <tr class="table_header">
                        <td>ID</td>
                        <td>Name</td>
                        <td>Photo</td>
                        <td>Salary</td>
                        <td>Age</td>
                        <td>Operation</td>
                    </tr>
                    <tr class="row1" v-for="(emp,index) in emp_list" :key="emp.id">
                        <td>{{emp.id}}</td>
                        <td>{{emp.emp_name}}</td>
                        <td><img :src="emp.img" style="height: 60px;"></td>
<!--                        <td>{{emp.img}}</td>-->
                        <td>{{emp.salary}}</td>
                        <td>{{emp.age}}</td>
                        <td><a href="javascript:(0);" @click="del_emp(emp.id)">删除员工</a>&nbsp;
                            <a href="javascript:(0);" @click="update_emp(emp.id)">更新员工</a>
                            <router-link :to="'/emp_update/'+emp.id">更新2</router-link>
                        </td>
                    </tr>

                </table>
                <p>
<!--                    <input type="button" class="el-button" value="添加员工"/>-->
                    <el-button type="success">
                        <router-link to="/emp_add">添加员工</router-link>
                    </el-button>
                </p>
            </div>
        </div>
        <div id="footer">
            <div id="footer_bg">
                ABC@126.com
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "emp_admin",
        data(){
            return {
                users:'',
                emp_list:[],
            }
        },
        methods:{
            find_emp(){
                    this.$axios.get("http://127.0.0.1:8000/app1/employee/").then(response=>{
                    this.emp_list = response.data.results;
                }).catch(error=>{

                })
            },
            del_emp(id){
                this.$axios({
                    url:'http://127.0.0.1:8000/app1/employee/',
                    method:'delete',
                    data:{
                        "id":id,
                    }
                }).then( response => {

                }).catch( response => {

                })
            },
            // update_emp(id){
            //
            // }
        },
        created() {
            let username = sessionStorage.getItem("users");
            if (username) {
                this.user_msg = username;
            } else {
                this.$message.error("请先登录");
                this.$router.push("/login");
            }
            // 在页面加载完成前获取员工数据并把值赋值给 data
            this.find_emp();
        }
    }
</script>

<style scoped>

</style>
