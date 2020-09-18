<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
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
                    login
                </h1>
                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">
                            username:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="name" v-model="username"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            password:
                        </td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" name="pwd" v-model="pwd"/>
                        </td>
                    </tr>
                </table>
                <p>
                    <input type="submit" class="el-button" value="登录" @click="login"/>
                    &nbsp;&nbsp;
                    <router-link to="/register">注册</router-link>
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
        name: "login",
        data(){
            return {
                username:'',
                pwd:'',
            }
        },
        methods:{
            login(){
                this.$axios({
                    url:'http://127.0.0.1:8000/app1/users/',
                    params:{
                        username:this.username,
                        pwd:this.pwd,
                    }
                }).then(response =>{
                    if(response.data.message){
                        console.log(response.data.results['username'])
                        this.$message({
                            message:'登录成功，即将跳转到主页面',
                            type: 'success',
                            duration: 1000,
                            showClose: true,
                        })
                        let user = response.data.results['username'];
                        sessionStorage.setItem('users',user);
                        this.$router.push('emp_admin/')
                    }else {
                        this.$message.error("用户名或密码不对")
                    }
                }).catch(error =>{
                    console.log(error);
                })
            }
        }
    }
</script>

<style scoped>

</style>
