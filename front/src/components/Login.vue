<template>
    <div>
        <el-form ref="loginForm" :model="loginForm" :rules="rules" label-width="80px" class="login-box">
            <h3 class="login-title">欢迎登录</h3>
            <el-form-item label="账号" prop="phoneNumber" class="item-input">
                <el-input type="text" placeholder="请输入账号" v-model="loginForm.phoneNumber" auto-complete="off"/>
            </el-form-item>
            <el-form-item label="密码" prop="password" class="item-input">
                <el-input type="password" placeholder="请输入密码" v-model="loginForm.password" auto-complete="off"/>
            </el-form-item>
            <el-form-item label="验证码" prop="captcha">
                <el-row>
                    <el-col :span="12">
                        <el-input type="text" placeholder="请输入验证码" v-model="loginForm.captcha" auto-complete="off"/>
                    </el-col>
                    <el-col :span="12">
                        <img :src=captchaUrl alt="点击换一张" id="id_captcha" @click="getCaptcha"
                             style="position: absolute;right: 0px">
                    </el-col>
                </el-row>
                <input v-model="captchaHashKey" type="hidden" id="id_captcha_0">
            </el-form-item>
            <el-form-item class="myButton">
                <el-button class="login-button" type="primary" @click="onSubmit('loginForm')">提交</el-button>
                <el-button class="login-button" @click="resetForm('loginForm')">重置</el-button>
                <el-button class="login-button" type="primary" @click="register('loginForm')">注册</el-button>
            </el-form-item>
        </el-form>

        <el-dialog
                title="温馨提示"
                :visible.sync="dialogVisible"
                width="30%">
            <span>请填好账号和密码</span>
            <span slot="footer" class="dialog-footer">
        <el-button class="button" type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
        </el-dialog>
    </div>
</template>

<script>
    import crypto from 'crypto';
    import {mapMutations} from 'vuex';
    import JSEncrypt from 'jsencrypt';

    export default {
        name: "Login",
        data() {
            return {
                salt: '',
                captchaUrl: '',
                captchaHashKey: '',
                loginForm: {
                    phoneNumber: '',
                    password: '',
                    captcha: '',
                },
                userToken: '',
                rules: {
                    phoneNumber: [
                        {required: true, message: '账号不可为空', trigger: 'blur'},
                        {min: 11, max: 11, message: "长度必须为11个字符", trigger: "blur"},
                    ],
                    password: [
                        {required: true, message: '密码不可为空', trigger: 'blur'},
                    ],
                    captcha: [
                        {required: true, message: '验证码不可为空', trigger: 'blur'},
                    ],
                },

                dialogVisible: false,
            };
        },
        methods: {
            ...mapMutations(['changeLogin']),
            onSubmit: function (formName) {
                let that = this;
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.axios({
                            method: 'post',
                            url: '/salt',
                        })
                            .then(function (response) {
                                that.salt = response.data.salt;
                                let publicKey = "-----BEGIN PUBLIC KEY-----\n" +
                                    "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDOikBHakQyUwIVjiMsFwVVdvFX\n" +
                                    "PcZD3ph8Fcv4Ftl0Jhe5/McNB+w34vAui1k8d28J+42xuCTb8kKteGWOdXl9aPWX\n" +
                                    "ZE07+6fnZO3u/T6AC8WFU80haTBz6a0rDWnHPkYrkazRJkqUBjcNMlUSttWNYJfZ\n" +
                                    "SqyV0/rKHa6fK0dDTwIDAQAB\n" +
                                    "-----END PUBLIC KEY-----";
                                let jse = new JSEncrypt();
                                jse.setPublicKey(publicKey);
                                let formData = new FormData();
                                let md5 = crypto.createHash("md5");
                                md5.update(that.loginForm.password);
                                let password = md5.digest('hex');
                                password += that.salt;
                                password = jse.encrypt(password);
                                formData.append('phoneNumber', that.loginForm.phoneNumber);
                                formData.append('password', password);
                                formData.append('captcha', that.loginForm.captcha);
                                formData.append('captchaHashKey', that.captchaHashKey);
                                that.axios({
                                    method: 'post',
                                    url: '/login',
                                    data: formData,
                                })
                                    .then((response) => {
                                        let msg = response.data.msg;
                                        if (msg !== '登录成功') {
                                            that.$message.error(msg);
                                            return;
                                        }
                                        that.userToken = response.data.token;
                                        that.changeLogin({Authorization: that.userToken});
                                        that.$message({
                                            message: msg,
                                            type: 'success',
                                        });
                                        that.$router.push('/MainPage');
                                    })
                                    .catch((error) => {
                                        console.log(error);
                                    });
                                console.log(response.data.salt);
                            }, function (err) {
                                console.log(err);
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

            register() {
                this.$router.push("/Register");
            },

            getCaptcha() {
                let that = this;
                this.axios({
                    method: 'get',
                    url: '/refreshCaptcha',
                })
                    .then(function (response) {
                            that.captchaUrl = axios.defaults.baseURL + response.data.imageUrl;
                            that.captchaHashKey = response.data.hashKey;
                        },
                        function (err) {
                            console.log(err);
                        });
            },
        },
        mounted() {
            this.getCaptcha();
        },
    };
</script>

<style lang="scss" scoped>
    .login-box {
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

    .item-input {
        padding-bottom: 10px;
    }

    .login-title {
        text-align: center;
        position: relative;
        left: 3.5%;
        margin: 0 auto 40px auto;
        font-size: 40px;
        color: #303133;
    }

    .login-button {
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
        margin-top: 68px;
    }


</style>
