<template>
    <div id="app">
        <el-container>
            <el-header id="header">捐助物资</el-header>
            <el-main>
                <div id="donation">
                    <el-form :model="donateForm" :rules="rules" ref="ruleForm" label-width="100px"
                             class="demo-ruleForm">
                        <el-form-item label="姓名" prop="name">
                            <el-input v-model="donateForm.name"></el-input>
                        </el-form-item>

                        <el-form-item label="联系电话" prop="phoneNumber">
                            <el-input v-model="donateForm.phoneNumber"></el-input>
                        </el-form-item>

                        <el-form-item label="捐赠口罩" prop="maskNum">
                            <el-input-number v-model="donateForm.maskNum" :step="10" :min="0"></el-input-number>
                            <span style="margin-left: 25%">盒</span>
                        </el-form-item>

                        <el-form-item label="捐赠防护服" prop="proSuitNum">
                            <el-input-number v-model="donateForm.proSuitNum" :step="10" :min="0"></el-input-number>
                            <span style="margin-left: 25%">件</span>
                        </el-form-item>

                        <el-form-item label="捐赠医用酒精" prop="alcoholNum">
                            <el-input-number v-model="donateForm.alcoholNum" :step="2" :min="0"></el-input-number>
                            <span style="margin-left: 25%">瓶</span>
                        </el-form-item>

                        <el-form-item label="捐赠方便食品" prop="instantNum">
                            <el-input-number v-model="donateForm.instantNum" :step="2" :min="0"></el-input-number>
                            <span style="margin-left: 25%">箱</span>
                        </el-form-item>

                        <el-form-item label="捐赠矿泉水" prop="waterNum">
                            <el-input-number v-model="donateForm.waterNum" :step="2" :min="0"></el-input-number>
                            <span style="margin-left: 25%">箱</span>
                        </el-form-item>

                        <el-form-item class="myButton">
                            <el-button class="Don-button" type="primary" @click="submitForm('ruleForm')">立即提交
                            </el-button>
                            <el-button class="Don-button" @click="resetForm('ruleForm')">重置</el-button>
                        </el-form-item>
                    </el-form>
                </div>
            </el-main>
        </el-container>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                donateForm: {
                    name: '',
                    phoneNumber: '',
                    maskNum: 0,
                    proSuitNum: 0,
                    alcoholNum: 0,
                    instantNum: 0,
                    waterNum: 0,
                },
                rules: {
                    name: [
                        {required: true, message: '请输入姓名', trigger: 'blur'},
                    ],
                    phoneNumber: [
                        {required: true, message: '请输入联系电话', trigger: 'blur'},
                        {min: 11, max: 11, message: '长度为11个字符', trigger: 'blur'},
                    ],
                },
            };
        },
        methods: {
            submitForm(formName) {
                let that = this;
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        let formData = new FormData();
                        for (let key in this.donateForm) {
                            formData.append(key, this.donateForm[key]);
                        }
                        this.axios({
                            method: 'post',
                            url: '/donation',
                            data: formData,
                        })
                            .then(function (response) {
                                    that.$notify({
                                        title: '成功',
                                        message: '您的捐赠信息我们已经记录下来,如果有需要将在稍微与您取得联系,感谢您的爱心',
                                        type: 'success',
                                    });
                                },
                                function (err) {
                                    console.log(err);
                                },
                            );
                    } else {
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            },
        },
    };
</script>

<style scoped>
    #donation {
        position: relative;
        width: 70%;
        left: 50%;
        transform: translate(-50%, 0%);
        background-color: white;
        padding: 60px 60px 90px 60px;
        border-radius: 9px;
        margin-top: 20px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    }

    #app {
        position: relative;
        width: 100%;
        height: 100%;
    }

    #header {
        font-size: 30px;
        padding-top: 20px;
        padding-bottom: 75px;
        border-radius: 5px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
        background-image: linear-gradient(135deg, #f5f7fa 0%, #f5f7fa 100%);
    }

    .el-header, .el-footer {
        background-color: #B3C0D1;
        color: #333;
        text-align: center;
        line-height: 60px;
        background-image: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    .Don-button {
        position: relative;
        margin-right: 60px;
    }

    .myButton {
        position: absolute;
        left: 50%;
        text-align: center;
        transform: translate(-50%, 0%);
        margin-top: 10px;
    }
</style>