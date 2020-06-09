<template>
    <div id="app">
        <el-container>
            <el-header id="header">个人信息</el-header>
            <el-main>
                <div id="myMessage">
                    <div>
                        <el-link icon="el-icon-edit" style="position: absolute; right: 20px" :underline="false" @click="dialogFormVisible = true">修改密码
                        </el-link>
                    </div>
                    <el-tooltip content="点击此处上传头像,为不影响视觉效果,请尽量上传宽高比一致的图像" placement="bottom" effect="light">
                        <el-upload
                                class="avatar-uploader"
                                :show-file-list="false"
                                :on-success="handleAvatarSuccess"
                                :before-upload="beforeAvatarUpload">
                            <img v-if="imageUrl" :src="imageUrl" class="avatar"
                                 style="width: 200px; height: 200px;">
                            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                        </el-upload>
                    </el-tooltip>
                    <el-divider></el-divider>
                    <div class="block">
                        <el-avatar :size="15" :src="volunteerLogoUrl" v-if="isVolunteer"></el-avatar>
                        <el-divider></el-divider>
                    </div>
                    <el-tooltip content="点击此处修改签名" placement="bottom" effect="light">
                <span v-text="'签名: '" @click="changeMySignature()"
                      style="cursor: pointer; outline: none"></span>
                    </el-tooltip>
                    <span v-text="signature" style="margin-left: 60px"></span>
                    <el-divider></el-divider>
                    <span v-text="'姓名: '"></span>
                    <span v-text="name" style="margin-left: 60px"></span>
                    <el-divider></el-divider>
                    <span v-text="'留言数: '"></span>
                    <span v-text="MessageNum" style="margin-left: 80px"></span>
                    <el-divider></el-divider>
                    <span v-text="'收到的赞: '"></span>
                    <span v-text="likeNum" style="margin-left: 70px"></span>
                    <el-divider></el-divider>
                    <span v-text="'收到的踩: '"></span>
                    <span v-text="disLikeNum" style="margin-left: 75px"></span>
                    <el-divider></el-divider>
                    <el-badge :value="newLikeNum" :max="99" class="item">
                        <el-button size="small" @click="openMyMessageReply()">新的赞</el-button>
                    </el-badge>
                    <el-badge :value="newReplyNum" :max="99" class="item">
                        <el-button size="small" @click="openMyMessageReply()">新的回复</el-button>
                    </el-badge>
                    <el-badge :value="newDisLikeNum" :max="99" class="item">
                        <el-button size="small" @click="openMyMessageReply()">新的踩</el-button>
                    </el-badge>
                    <div :key="item" class="text item" v-for="item in message" v-if="myMessageIsShow">

                        <el-card class="box-card">
                            <div class="clearfix" slot="header" style="padding-bottom: 50px; position: relative">

                                <div class="block">
                                    <el-avatar :size="50" :src="item.avaUrl" class="myAva"></el-avatar>
                                </div>
                                <span class="msgTitle" v-text="item.name+' '+item.date"></span>
                                <el-link icon="el-icon-edit" class="del" @click="deleteMyComment(item)">删除</el-link>
                                <el-link style="position: absolute;margin-top: 14px;right: 160px"
                                         @click="watchOldReply(item)">
                                    查看回复<i
                                        class="el-icon-view el-icon--right"></i></el-link>
                                <i class="el-icon-top"></i>
                                <span class="likeNum" v-text="item.likenum"></span>
                                <i class="el-icon-bottom"></i>
                                <span class="disLikeNum" v-text="item.dislikenum"></span>
                            </div>
                            <div>
                                <span v-text="item.content"></span>
                                <div class="reply-box" v-if="item.replyIsShow">
                                    <ul class="infinite-list" style="overflow:auto">
                                        <li class="infinite-list-item" v-for="i in item.reply">
                                            <div class="block">
                                                <el-avatar :size="30" :src="i.avaUrl" class="myAva"></el-avatar>
                                            </div>
                                            <span class="reply-box-name" v-text="i.from_name"></span>
                                            <span class="reply-box-content"
                                                  v-text="': '+i.content+'\xa0\xa0\xa0\xa0\xa0\xa0\xa0('+i.date+')'"></span>
                                        </li>
                                    </ul>
                                </div>
                            </div>

                        </el-card>
                    </div>
                    <el-pagination
                            style="margin-top: 20px"
                            v-if="myMessageIsShow"
                            background
                            layout="prev, pager, next, jumper"
                            :current-page="currentPage"
                            :total=total
                            page-size=5
                            @current-change="handleCurrentChange">
                    </el-pagination>
                </div>
            </el-main>
        </el-container>
        <el-dialog title="修改密码" :visible.sync="dialogFormVisible">
            <el-form ref="reviseForm" :model="reviseForm" :rules="rules" label-width="80px">
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
                <el-form-item style="margin-left: 50%;transform: translate(-40%, 0%)">
                    <el-button type="primary" style="margin-right: 50px"
                               @click="reviseSub('reviseForm')">提交
                    </el-button>
                    <el-button @click="resetForm('reviseForm')">重置
                    </el-button>
                </el-form-item>
            </el-form>
        </el-dialog>
    </div>
</template>

<script>
    import {mapMutations} from 'vuex';
    import crypto from "crypto";

    export default {
        name: "MyPage",
        data() {
            let validatePwd = (rule, value, callback) => {
                if (value === "") {
                    callback(new Error("请再次输入密码"));
                } else if (value !== this.reviseForm.newPwd) {
                    callback(new Error("两次输入密码不一致!"));
                } else {
                    callback();
                }
            };
            return {
                name: '',
                imageUrl: axios.defaults.baseURL + '/my_ava',
                phoneNumber: '',
                signature: '',
                MessageNum: 0,
                likeNum: 0,
                disLikeNum: 0,
                newReplyNum: '',
                newLikeNum: '',
                newDisLikeNum: '',
                total: 0,
                currentPage: 0,
                volunteerLogoUrl: axios.defaults.baseURL + '/vol_logo',
                myMessageIsShow: false,
                isVolunteer: false,
                message: [],
                dialogFormVisible: false,
                reviseForm: {
                    oldPwd: "",
                    newPwd: "",
                    checkNewPwd: "",
                },
                rules: {
                    oldPwd: [
                        {required: true, message: "请输入原密码", trigger: "blur"},
                    ],
                    newPwd: [
                        {required: true, message: "请输入新密码", trigger: "blur"},
                    ],
                    checkNewPwd: [
                        {required: true, message: "请重复新密码", trigger: "blur"},
                        {validator: validatePwd, trigger: "blur"},
                    ],
                },
            };
        },
        methods: {
            ...mapMutations(['noticeInit']),
            watchOldReply(item) {
                item.replyIsShow = !item.replyIsShow;
                let that = this;
                axios.get('/reply?commentsId=' + item.comment_id)
                    .then(function (response) {
                            if (response.data.msg === '没有回复') {
                                that.$message('没有回复');
                            } else {
                                item.reply = response.data;
                            }
                        },
                        function (err) {
                            console.log(err);
                        },
                    );
            },
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
            outLogin() {
                localStorage.clear();
                axios.get('/logout')
                    .then(function (response) {
                            console.log(response);
                        },
                        function (err) {
                            console.log(err);
                        });
                this.$router.push('/Login');
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            },
            handleCurrentChange(val = 1) {
                this.currentPage = val;
                let that = this;
                let formData = new FormData();
                formData.append('currentPage', that.currentPage);
                this.axios({
                    method: 'post',
                    url: '/personal_comments',
                    data: formData,
                })
                    .then(function (response) {
                            if (response.data.msg === '成功') {
                                that.message = response.data.pageNow;
                                that.total = 5 * response.data.pageCount;
                            } else {
                                that.$message.error(response.data.msg);
                            }
                        },
                        function (err) {
                            console.log(err);
                        },
                    );
            },

            openMyMessageReply() {
                let _this = this;
                this.myMessageIsShow = !this.myMessageIsShow;
                _this.noticeInit({newReplyNum: 0, newDisLikeNum: 0, newLikeNum: 0});
                let that = this;
                let formData = new FormData();
                formData.append('currentPage', '1');
                this.axios({
                    method: 'post',
                    url: '/personal_comments',
                    data: formData,
                })
                    .then(function (response) {
                            that.message = response.data.pageNow;
                            that.total = 5 * response.data.pageCount;
                            that.newLikeNum = '';
                            that.newDisLikeNum = '';
                            that.newReplyNum = '';
                        },
                        function (err) {
                            console.log(err);
                        },
                    );
            },

            init() {
                let that = this;
                this.axios({
                    method: 'get',
                    url: '/my_info',
                })
                    .then(function (response) {
                            that.name = response.data.data.name;
                            that.phoneNumber = response.data.data.phoneNumber;
                            that.MessageNum = response.data.data.commentsNum;
                            that.likeNum = response.data.data.likeNum;
                            that.disLikeNum = response.data.data.disLikeNum;
                            that.signature = response.data.data.signature;
                            if (response.data.data.isVolunteer === '1') {
                                that.isVolunteer = true;
                            } else {
                                that.isVolunteer = false;
                            }
                            if (response.data.data.newReplyNum !== 0) {
                                that.newReplyNum = response.data.data.newReplyNum;
                            }
                            if (response.data.data.newLikeNum !== 0) {
                                that.newLikeNum = response.data.data.newLikeNum;
                            }
                            if (response.data.data.newDisLikeNum !== 0) {
                                that.newDisLikeNum = response.data.data.newDisLikeNum;
                            }
                        },
                        function (err) {
                            console.log(err);
                        },
                    );
            },

            deleteMyComment(item) {
                let that = this;
                this.$confirm('此操作将永久删除该留言, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning',
                }).then(() => {
                    axios.delete('/personal_comments?commentId=' + item.comment_id)
                        .then(function (response) {
                                if (response.data.msg == '成功') {
                                    that.$message({
                                        type: 'success',
                                        message: '删除成功!',
                                    });
                                    that.openMyMessageReply();
                                } else {
                                    that.$message(response.data.msg);
                                }
                            },
                            function (err) {
                                console.log(err);
                            },
                        );

                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除',
                    });
                });
            },

            getNowFormatDate() {
                let date = new Date();
                let seperator1 = "-";
                let year = date.getFullYear();
                let month = date.getMonth() + 1;
                let strDate = date.getDate();
                if (month >= 1 && month <= 9) {
                    month = "0" + month;
                }
                if (strDate >= 0 && strDate <= 9) {
                    strDate = "0" + strDate;
                }
                let currentDate = year + seperator1 + month + seperator1 + strDate;
                return currentDate;
            },

            handleAvatarSuccess(res, file) {
                this.imageUrl = URL.createObjectURL(file.raw);
            },

            beforeAvatarUpload(file) {
                const isLt2M = file.size / 1024 / 1024 < 2;
                let _this = this;
                if (!isLt2M) {
                    this.$message.error('上传头像图片大小不能超过 2MB!');
                } else {
                    let fd = new FormData();
                    fd.append('file', file);
                    fd.append("fileName", file.name)
                    axios.post('/my_ava', fd)
                        .then(function (response) {
                            _this.$message.success('上传成功');
                        }, function (error) {
                            console.log(error);
                        });
                }
                return isLt2M;
            },

            changeMySignature() {
                let that = this;
                this.$prompt('请输入新的签名', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    inputPlaceholder: '不超过50字',
                    inputPattern: /^.{1,50}$/,
                    inputErrorMessage: '签名格式不正确',
                }).then(({value}) => {
                    let formData = new FormData();
                    formData.append('value', value);
                    that.axios({
                        method: 'post',
                        url: '/signature',
                        data: formData,
                    })
                        .then(function (response) {
                                that.$message({
                                    type: 'success',
                                    message: '修改成功,你的签名: ' + value,
                                });
                                that.signature = value;
                            },
                            function (err) {
                                console.log(err);
                            });
                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '取消输入',
                    });
                });
            },


        },
        mounted: function () {
            this.init();
        },
    };
</script>

<style scoped>
    #myMessage {
        position: relative;
        width: 70%;
        height: auto;
        transform: translate(-50%, 0%);
        background-color: white;
        padding: 70px;
        border-radius: 9px;
        left: 50%;
        line-height: 15px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    }

    #app {
        position: relative;
        width: 100%;
        height: auto;
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

    .el-button {
        width: 100px;
        height: 40px;
        margin-left: 30px;
    }

    .box-card {
        line-height: 30px;
        margin-top: 30px;
        padding-bottom: 20px;
    }

    .infinite-list-item {
        list-style: none;
        margin-bottom: 10px;
    }

    .el-badge__content {
        position: absolute;
        margin-right: 30px;
    }

    .msgTitle {
        position: absolute;
        left: 0;
        margin-top: 14px;
        margin-left: 60px;
    }

    .reply-box {
        position: relative;
        width: 100%;
        height: 150px;
        overflow: auto;
        text-align: left;
        box-shadow: 0 -1px 1px 0 rgba(0, 0, 0, 0.1)
    }

    .el-icon-top {
        position: absolute;
        right: 80px;
        margin-right: 20px;
        transform: translate(50%, 50%);
        cursor: pointer;
        margin-top: 14px;
    }

    .el-icon-bottom {
        position: absolute;
        right: 0px;
        margin-right: 20px;
        transform: translate(50%, 50%);
        cursor: pointer;
        margin-top: 14px;
    }

    .likeNum {
        position: absolute;
        right: 80px;
        transform: translate(50%, 3%);
        margin-top: 14px;
    }

    .disLikeNum {
        position: absolute;
        right: 0;
        transform: translate(50%, 3%);
        margin-top: 14px;
    }

    .del {
        position: absolute;
        right: 300px;
        margin-top: 14px;
    }

    .myAva {
        position: absolute;
        left: 0;
    }

    .reply-box-name {
        color: #EB7347;
        position: absolute;
        left: 0;
        margin-left: 50px;
    }

    .reply-box-content {
        left: 0;
        margin-left: 130px;
    }

</style>