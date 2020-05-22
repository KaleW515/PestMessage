<template>
    <div id="app">
        <el-container>
            <el-header id="header">个人信息</el-header>
            <el-main>
                <div id="myMessage">
                    <el-image :src="imageUrl" style="width: 200px; height: 200px;">
                        <div slot="placeholder" class="image-slot">
                            加载中<span class="dot">...</span>
                        </div>
                    </el-image>
                    <el-divider></el-divider>
                    <div class="block">
                        <el-avatar :size="15" :src="volunteerLogoUrl" v-if="isVolunteer"></el-avatar>
                        <el-divider></el-divider>
                    </div>
                    <span v-text="'签名: '+signature"></span>
                    <el-divider></el-divider>
                    <span v-text="'姓名: '+name"></span>
                    <el-divider></el-divider>
                    <span v-text="'留言数: '+MessageNum"></span>
                    <el-divider></el-divider>
                    <span v-text="'收到的赞: '+likeNum"></span>
                    <el-divider></el-divider>
                    <span v-text="'收到的踩: '+disLikeNum"></span>
                    <el-divider></el-divider>
                    <el-badge :value="newReplyNum" :max="99" class="item">
                        <el-button size="small" @click="openMyMessageReply()">他的留言</el-button>
                    </el-badge>
                    <div :key="item" class="text item" v-for="item in message" v-if="myMessageIsShow">

                        <el-card class="box-card">
                            <div class="clearfix" slot="header" style="padding-bottom: 50px; position: relative">

                                <div class="block">
                                    <el-avatar :size="50" :src="item.avaUrl" class="myAva"></el-avatar>
                                </div>
                                <span class="msgTitle" v-text="item.name+' '+item.date"></span>
                                <el-link
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
                                            <el-link type="primary" @click="delMyReply(i)"
                                                     v-text="'\xa0\xa0\xa0'+'删除'"
                                                     v-if="i.from_name === myName" :underline="false"></el-link>
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
    </div>
</template>

<script>
    export default {
        name: "OtherPeople",
        data() {
            return {
                myName: "",
                name: "",
                imageUrl: "",
                signature: "",
                MessageNum: 0,
                likeNum: 0,
                disLikeNum: 0,
                newReplyNum: "",
                total: 0,
                currentPage: 0,
                volunteerLogoUrl: axios.defaults.baseURL + "/vol_logo",
                myMessageIsShow: false,
                isVolunteer: false,
                message: [],
            };
        },
        methods: {
            watchOldReply(item) {
                item.replyIsShow = !item.replyIsShow;
                let that = this;
                this.axios({
                    method: "get",
                    url: "/reply?commentsId=" + item.comment_id,
                })
                    .then(function (response) {
                            if (response.data.msg === "没有回复") {
                                that.$message("没有回复");
                            } else {
                                item.reply = response.data;
                            }
                        },
                        function (err) {
                            console.log(err);
                        },
                    );
            },

            handleCurrentChange(val) {
                this.currentPage = val;
                let that = this;
                let formData = new FormData();
                formData.append("currentPage", that.currentPage);
                formData.append('phoneNumber', this.$route.query.phoneNumber);
                this.axios({
                    method: "post",
                    url: "/personal_comments",
                    data: formData,
                })
                    .then(function (response) {
                            if (response.data.msg === "成功") {
                                that.message = response.data.pageNow;
                                that.total = 5 * parseInt(response.data.pageCount);
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
                this.myMessageIsShow = !this.myMessageIsShow;
                let that = this;
                let formData = new FormData();
                formData.append("currentPage", '1');
                formData.append('userId', this.$route.query.userId);
                this.axios({
                    method: "post",
                    url: "/personal_comments",
                    data: formData,
                })
                    .then(function (response) {
                            that.message = response.data.pageNow;
                            that.total = 5 * parseInt(response.data.pageCount);
                        },
                        function (err) {
                            console.log(err);
                        },
                    );
            },

            init() {
                let that = this;
                this.axios({
                    method: "get",
                    url: "/people_info/" + this.$route.query.userId + '/',
                })
                    .then(function (response) {
                        console.log(response)
                            that.myName = response.data.data.myName;
                            that.name = response.data.data.name;
                            that.phoneNumber = response.data.data.phoneNumber;
                            that.MessageNum = response.data.data.commentsNum;
                            that.likeNum = response.data.data.likeNum;
                            that.disLikeNum = response.data.data.disLikeNum;
                            that.signature = response.data.data.signature;
                            that.imageUrl = axios.defaults.baseURL + "/people_ava/" + that.$route.query.username;
                            if (response.data.data.isVolunteer === "1") {
                                that.isVolunteer = true;
                            } else {
                                that.isVolunteer = false;
                            }
                        },
                        function (err) {
                            console.log(err);
                        },
                    );
            },

            delMyReply(i) {
                let that = this;
                this.$confirm("此操作将永久删除该回复, 是否继续?", "提示", {
                    confirmButtonText: "确定",
                    cancelButtonText: "取消",
                    type: "warning",
                }).then(() => {
                    axios.delete("/reply?id=" + i.reply_id)
                        .then(function (response) {
                            if (response.data.msg === "成功") {
                                that.$message({
                                    type: "success",
                                    message: "删除成功!",
                                });
                            }
                        }, function (err) {
                            console.log(err);
                        });
                }).catch(() => {
                    that.$message({
                        type: "info",
                        message: "已取消删除",
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
        text-align: center;
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