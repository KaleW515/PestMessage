<template>
    <div id="revise">
        <div id="revise-box">
            <el-form ref="reviseForm" :model="reviseForm" :rules="rules" label-width="80px">
                <h3 id="revise-title">修改密码</h3>
                <el-form-item label="旧密码" prop="oldPwd" class="pwd-input">
                    <el-input type="password" placeholder="请输入原始密码" v-model="reviseForm.oldPwd" auto-complete="off"/>
                </el-form-item>
                <el-form-item label="新密码" prop="newPwd" class="pwd-input">
                    <el-input type="password" placeholder="请输入新密码" v-model="reviseForm.newPwd" auto-complete="off"/>
                </el-form-item>
                <el-form-item label="重复密码" prop="checkNewPwd" class="pwd-input">
                    <el-input type="password" placeholder="请重复新密码" v-model="reviseForm.checkNewPwd"
                              auto-complete="off"/>
                </el-form-item>
                <el-form-item class="myButton">
                    <el-button class="revise-button" type="primary"
                               @click="reviseSub('reviseForm')">提交
                    </el-button>
                    <el-button class="revise-button" @click="resetForm('reviseForm')">重置
                    </el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
    import crypto from 'crypto';

    export default {
        name: "RevisePwd",
        data() {
            let validatePwd = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请再次输入密码'));
                } else if (value !== this.reviseForm.newPwd) {
                    callback(new Error('两次输入密码不一致!'));
                } else {
                    callback();
                }
            };
            return {

                reviseForm: {
                    oldPwd: "",
                    newPwd: "",
                    checkNewPwd: '',
                },
                rules: {
                    oldPwd: [
                        {required: true, message: '请输入原密码', trigger: 'blur'},
                    ],
                    newPwd: [
                        {required: true, message: '请输入新密码', trigger: 'blur'},
                    ],
                    checkNewPwd: [
                        {required: true, message: '请重复新密码', trigger: 'blur'},
                        {validator: validatePwd, trigger: 'blur'}
                    ],
                },
            };
        },
        methods: {
            reviseSub(formName) {
                let that = this;
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        let formData = new FormData();
                        let md5 = crypto.createHash("md5");
                        md5.update(this.reviseForm.oldPwd);
                        let oldPwd = md5.digest('hex');
                        let newMd5 = crypto.createHash("md5");
                        newMd5.update(this.reviseForm.newPwd);
                        let newPwd = newMd5.digest('hex');
                        formData.append('oldPwd', oldPwd);
                        formData.append('newPwd', newPwd);
                        this.axios({
                            method: 'post',
                            url: '/revise',
                            data: formData,
                        })
                            .then((response) => {
                                let msg = response.data.msg;
                                if (msg === '修改成功') {
                                    that.$message({
                                        message: msg + ',去重新登录吧',
                                        type: 'success'
                                    });
                                    that.outLogin();
                                    that.$router.push('/Login');
                                } else {
                                    this.$message.error(msg);
                                }
                            })
                            .catch((error) => {
                                console.log(error);
                            });
                    } else {
                        this.dialogVisible = true;
                        return false;
                    }
                });
            },

            resetForm(formName) {
                this.$refs[formName].resetFields();
            },

            outLogin() {
                localStorage.clear();
                this.axios.get('/logout')
                    .then(function (response) {
                            console.log(response);
                        },
                        function (err) {
                            console.log(err);
                        });
                this.$router.push('/Login');
            }
        }
    };
</script>

<style scoped>
    #revise {
        position: relative;
        width: 100%;
        height: 100%;
    }

    #revise-title {
        font-size: 40px;
        position: relative;
        text-align: center;
        margin-bottom: 30px;
    }

    #revise-box {
        position: relative;
        width: 50%;
        height: 50%;
        top: 45%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: white;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
        padding: 70px;
        border-radius: 9px;
    }

    .revise-button {
        position: relative;
        margin-right: 60px;
        padding-left: 30px;
        padding-right: 30px;
    }

    .myButton {
        position: relative;
        left: 50%;
        text-align: center;
        transform: translate(-50%, 0%);
        margin-top: 60px;
    }

</style>