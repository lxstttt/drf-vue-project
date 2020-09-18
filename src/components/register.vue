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
                    注册
                </h1>
                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">
                            用户名:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="username" v-model="username"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            真实姓名:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="name" v-model="real_name"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            密码:
                        </td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" name="pwd" v-model="pwd"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            性别:
                        </td>
                        <td valign="middle" align="left">
                            男
                            <input type="radio" class="inputgri" name="sex" @click="gender=0" value="m"
                                   checked="checked"/>
                            女
                            <input type="radio" class="inputgri" name="sex" @click="gender=1" value="f"/>
                        </td>
                    </tr>

                </table>
                <p>
                    <input type="submit" class="button" value="注册" @click="register"/>
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
        name: "register",
        data() {
            return {
                username: '',
                real_name: '',
                pwd: '',
                gender: 0,
            }
        },
        methods: {
            register() {
                //  发起注册请求
                this.$axios({
                    url: "http://127.0.0.1:8000/app1/users/",
                    method: "post",
                    data: {
                        username: this.username,
                        password: this.pwd,
                        real_name: this.real_name,
                        gender: this.gender,
                    },
                }).then(response => {
                    if (response.data.message) {
                        console.log(response.data.message)
                        this.$message({
                            message: '恭喜你，注册成功,即将跳转到登录页面',
                            type: 'success',
                            duration: 1000,
                            showClose: true,
                        });
                        // 跳转至登录页面
                        this.$router.push("/login")
                    }
                }).catch(error => {
                    console.log(error.message);
                    this.$message.error('用户名已存在或者密码错误');
                })
            },
        }
    }
</script>

<style scoped>

</style>
