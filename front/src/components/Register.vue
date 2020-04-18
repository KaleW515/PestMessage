<template>
    <div>
        <el-form :model="registerForm" :rules="rules" ref="registerForm" label-width="80px" class="registerBox">
            <h3 class="register-title">欢迎注册</h3>
            <el-form-item label="账号" prop="phoneNumber">
                <el-input v-model="registerForm.phoneNumber" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="用户名" prop="username">
                <el-input v-model="registerForm.username" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="pass">
                <el-input type="password" v-model="registerForm.pass" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="checkPass">
                <el-input type="password" v-model="registerForm.checkPass" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item class="myButton">
                <el-button class="register-button" type="primary" @click="submitForm('registerForm')">提交</el-button>
                <el-button class="register-button" @click="resetForm('registerForm')">重置</el-button>
                <el-button class="register-button" type="primary" @click="Login('registerForm')">登录</el-button>
            </el-form-item>
        </el-form>
        <el-dialog
                title="温馨提示"
                :visible.sync="dialogVisible"
                width="30%">
            <span>你填完了?</span>
            <span slot="footer" class="dialog-footer">
        <el-button class="button" type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
        </el-dialog>
    </div>
</template>

<script>
    import crypto from 'crypto'
    export default {
        data() {
            let validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'));
                }
                {
                    if (this.registerForm.checkPass !== '') {
                        this.$refs.registerForm.validateField('checkPass');
                    }
                    callback();
                }
            };
            let validatePass2 = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请再次输入密码'));
                } else if (value !== this.registerForm.pass) {
                    callback(new Error('两次输入密码不一致!'));
                } else {
                    callback();
                }
            };
            return {
                registerForm: {
                    phoneNumber: '',
                    username: '',
                    pass: '',
                    checkPass: '',
                },
                rules: {
                    phoneNumber: [
                        {required: true, message: '请输入账号', trigger: 'blur'},
                        {min: 11, max: 11, message: '长度必须为11位', trigger: 'blur'}
                    ],
                    username: [
                        {required: true, message: '请输入昵称', trigger: 'blur'},
                        {min: 3, max: 11, message: '位数在3-11位', trigger: 'blur'}
                    ],
                    pass: [
                        {required: true, message: '请输入密码', trigger: 'blur'},
                        {validator: validatePass, trigger: 'blur'}
                    ],
                    checkPass: [
                        {required: true, message: '请再次输入密码', trigger: 'blur'},
                        {validator: validatePass2, trigger: 'blur'}
                    ],
                },
                dialogVisible: false
            }
        },
        methods: {
            submitForm(formName) {
                let that = this;
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        let formData = new FormData();
                        let md5 = crypto.createHash("md5");
                        md5.update(this.registerForm.pass);
                        let password = md5.digest('hex');
                        formData.append('phoneNumber', this.registerForm.phoneNumber);
                        formData.append('username', this.registerForm.username);
                        formData.append('pass', password);
                        this.axios({
                            method: 'post',
                            url: '/register',
                            data: formData,
                        })
                            .then((response) => {
                                let msg = response.data.msg;
                                if (msg === '注册成功') {
                                    that.$message({
                                        message: msg,
                                        type: 'success'
                                    });
                                    that.$router.push('/Login');
                                } else {
                                    that.$message.error(msg);
                                }
                            })
                            .catch((error) => {
                                console.log(error)
                            })
                    } else {
                        this.dialogVisible = true;
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            },
            Login(formName) {
                this.$router.push('/Login');
            }
        }
    }
</script>

<style lang="scss" scoped>
    .registerBox {
        width: 600px;
        height: 400px;
        padding: 35px 65px 35px 35px;
        position: absolute;
        top: 40%;
        left: 50%;
        transform: translate(-50%, -50%);
        border: 1px solid #DCDFE6;
        border-radius: 5px;
        box-shadow: 0 0 2px #b1b4ba;
    }

    .register-title {
        text-align: center;
        position: relative;
        left: 3.5%;
        margin: 0 auto 40px auto;
        font-size: 40px;
        color: #303133;
    }

    .register-button {
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
        margin-top: 25px;
    }


</style>
