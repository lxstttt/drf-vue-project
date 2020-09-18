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
                        <a href="#">Main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    update Emp info:
                </h1>
                <form action="emplist.html" method="post">
                    <table cellpadding="0" cellspacing="0" border="0"
                           class="form_table">
                        <tr>
                            <td valign="middle" align="right">
                                id:
                            </td>
                            <td valign="middle" align="left">
                                {{$route.params.emp.id}}
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                name:
                            </td>
                            <td valign="middle" align="left">
                                <input type="text" class="inputgri" name="name" v-model="username"/>
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                photo:
                            </td>
                            <td valign="middle" align="left">
                                <input type="file" name="photo"/>
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                salary:
                            </td>
                            <td valign="middle" align="left">
                                <input type="text" class="inputgri" name="salary" v-model="salary"/>
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                age:
                            </td>
                            <td valign="middle" align="left">
                                <input type="text" class="inputgri" name="age" v-model="age"/>
                            </td>
                        </tr>
                    </table>
                    <p>
                        <input type="submit" class="button" value="Confirm" @click="update_emp"/>
                    </p>
                </form>
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
        name: "update",
        data() {
            return {
                username: '',
                salary: '',
                age: '',
            }
        },
        update_emp() {
            let file = this.$refs.photo.files[0];
            let formData = new FormData();
            formData.append("emp_name", this.emp_name);
            formData.append("salary", this.salary);
            formData.append("age", this.age)
            formData.append("img", this.$refs.photo.files[0])
            this.$axios({
                url: 'http://127.0.0.1:8000/app1/employee/',
                method: 'patch',
                data: formData,
                headers: {
                    "content-type": "multipart/form-data"
                },
            }).then(response => {
                console.log(response.data);
                if (response.data.message) {
                    this.$message({
                        message: '员工更新成功',
                        type: 'success',
                        duration: 1000,
                        showClose: true,
                    })
                    this.$router.push('/emp_admin');
                }
            }).catch(error => {
                console.log(error.message);
            })
        }

    }
</script>

<style scoped>

</style>
