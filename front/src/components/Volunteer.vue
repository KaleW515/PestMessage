<template>
    <div id="app">
        <el-container>
            <el-header id="header">快速报名成为志愿者</el-header>
            <el-main>
                <div id="volunteer">
                    <el-form :model="volunteerForm" :rules="rules" ref="ruleForm" label-width="100px"
                             class="demo-ruleForm">
                        <el-form-item label="姓名" prop="name">
                            <el-input v-model="volunteerForm.name"></el-input>
                        </el-form-item>
                        <el-form-item label="联系电话" prop="phoneNumber">
                            <el-input v-model="volunteerForm.phoneNumber"></el-input>
                        </el-form-item>
                        <el-form-item label="QQ" prop="qq">
                            <el-input v-model="volunteerForm.qq"></el-input>
                        </el-form-item>
                        <el-form-item label="空闲时间段" required>
                            <el-col :span="11">
                                <el-form-item prop="date1">
                                    <el-time-picker placeholder="选择时间" v-model="volunteerForm.date1"
                                                    style="width: 100%;"></el-time-picker>
                                </el-form-item>
                            </el-col>
                            <el-col class="line" :span="2">-</el-col>
                            <el-col :span="11">
                                <el-form-item prop="date2">
                                    <el-time-picker placeholder="选择时间" v-model="volunteerForm.date2"
                                                    style="width: 100%;"></el-time-picker>
                                </el-form-item>
                            </el-col>
                        </el-form-item>

                        <el-form-item label="是否医护人员" prop="isDoctor">
                            <el-switch v-model="volunteerForm.isDoctor"></el-switch>
                        </el-form-item>

                        <el-form-item label="自身优势" prop="advantage">
                            <el-checkbox-group v-model="volunteerForm.advantage">
                                <el-checkbox label="会应急救护" name="type"></el-checkbox>
                                <el-checkbox label="有志愿经历" name="type"></el-checkbox>
                                <el-checkbox label="懂医学知识" name="type"></el-checkbox>
                                <el-checkbox label="其他" name="type"></el-checkbox>
                            </el-checkbox-group>
                        </el-form-item>

                        <el-form-item label="申请感言" prop="words">
                            <el-input type="textarea" v-model="volunteerForm.words" :rows="5"
                                      placeholder="填写申请感言,最多不超过100个字符"></el-input>
                        </el-form-item>
                        <el-form-item class="myButton">
                            <el-button class="Vol-button" type="primary" @click="submitForm('ruleForm')">立即提交
                            </el-button>
                            <el-button class="Vol-button" @click="resetForm('ruleForm')">重置</el-button>
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
                volunteerForm: {
                    name: '',
                    phoneNumber: '',
                    qq: '',
                    date1: '',
                    date2: '',
                    isDoctor: false,
                    advantage: [],
                    words: ''
                },
                rules: {
                    name: [
                        {required: true, message: '请输入姓名', trigger: 'blur'},
                    ],
                    phoneNumber: [
                        {required: true, message: '请输入联系电话', trigger: 'blur'},
                        {min: 11, max: 11, message: '长度为11个字符', trigger: 'blur'}
                    ],
                    qq: [
                        {required: true, message: '请输入QQ', trigger: 'blur'},
                        {min: 4, max: 10, message: '长度为4到11之间', trigger: 'blur'}
                    ],
                    date1: [
                        {type: 'date', required: true, message: '请选择时间', trigger: 'change'}
                    ],
                    date2: [
                        {type: 'date', required: true, message: '请选择时间', trigger: 'change'}
                    ],
                    type: [
                        {type: 'array', required: true, message: '请至少选择自身优势', trigger: 'change'}
                    ],
                    desc: [
                        {required: true, message: '请填写申请感言', trigger: 'blur'},
                        {max: 100, message: '最多100个字符', trigger: 'blur'}
                    ]
                }
            };
        },
        methods: {
            submitForm(formName) {
                let that = this;
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        let formData = new FormData();
                        for (let key in this.volunteerForm) {
                            formData.append(key, this.volunteerForm[key]);
                        }
                        this.axios({
                            method: 'post',
                            url: '/toBeVolunteer',
                            data: formData,
                        })
                            .then(function (response) {
                                    let msg = response.data.msg;
                                    if (msg === '注册成功') {
                                        that.$message({
                                            message: '恭喜你，报名成功!',
                                            type: 'success'
                                        });
                                    } else {
                                        that.$message({
                                            message: '报名失败',
                                            type: 'error'
                                        });
                                    }
                                },
                                function (err) {
                                    console.log(err);
                                }
                            );
                    } else {
                        return false;
                    }
                });
            },

            resetForm(formName) {
                this.$refs[formName].resetFields();
            },
        }
    };
</script>

<style scoped>
    #volunteer {
        position: relative;
        width: 70%;
        left: 50%;
        transform: translate(-50%, 0%);
        background-color: white;
        padding: 60px 60px 90px 60px;
        margin-top: 20px;
        border-radius: 9px;
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

    .Vol-button {
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