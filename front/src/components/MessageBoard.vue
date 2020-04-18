<template>
    <div id="messageBoard">
        <el-container>
            <el-header id="header">留言板</el-header>
            <div id="searchInput">
                <el-input
                        @keyup.enter.native="searchComments()"
                        placeholder="请输入内容"
                        prefix-icon="el-icon-search"
                        v-model="inputField">
                </el-input>
                <el-switch
                        @change="init()"
                        style="margin-top: 30px"
                        v-model="valueOpen"
                        active-text="按点赞数排序"
                        inactive-text="按时间排序">
                </el-switch>
            </div>
            <el-main>
                <div :key="item" class="text item" v-for="item in message">
                    <el-card class="box-card">
                        <div class="clearfix" slot="header" style="padding-bottom: 50px;position: relative">

                            <div class="block" @click="watchOtherPeople(item)">
                                <el-avatar :size="50" :src="item.avaUrl" class="myAva"></el-avatar>
                            </div>
                            <span class="msgTitle" v-text="item.name+'\xa0\xa0\xa0\xa0\xa0'+item.date"></span>
                            <el-link style="position: absolute;margin-top: 14px;right: 250px"
                                     @click="watchOldReply(item)">查看回复<i
                                    class="el-icon-view el-icon--right"></i></el-link>
                            <el-link @click="reply(item)" icon="el-icon-edit"
                                     style="position: absolute;margin-top: 14px;right: 150px">回复
                            </el-link>
                            <el-tooltip class="item" effect="dark" content="点个赞" placement="top-end">
                                <i @click="incLikeNum(item)" class="el-icon-top"></i>
                            </el-tooltip>
                            <span class="likeNum" v-text="item.likenum"></span>
                            <el-tooltip class="item" effect="dark" content="踩一下" placement="top-end">
                                <i @click="incDisLikeNum(item)" class="el-icon-bottom"></i>
                            </el-tooltip>
                            <span class="disLikeNum" v-text="item.dislikenum"></span>
                        </div>

                        <div>
                            <span v-text="item.content"></span>
                            <div class="reply-box" v-if="item.replyIsShow">
                                <ul class="infinite-list" style="overflow:auto">
                                    <li class="infinite-list-item" v-for="i in item.reply">
                                        <div class="block" @click="watchOtherPeople(i)" style="cursor: pointer;">
                                            <el-avatar :size="30" :src="i.avaUrl" class="myAva"></el-avatar>
                                        </div>
                                        <span class="reply-box-name" v-text="i.from_name"></span>
                                        <span class="reply-box-content"
                                              v-text="': '+i.content+'\xa0\xa0\xa0\xa0\xa0\xa0\xa0('+i.date+')'"></span>
                                        <el-link type="primary" @click="delMyReply(i)"
                                                 v-text="'\xa0\xa0\xa0'+'删除'"
                                                 v-if="i.from_name === username" :underline="false"></el-link>
                                    </li>
                                </ul>
                            </div>

                            <el-input
                                    :rows="5"
                                    placeholder="请输入回复内容,字数限制100字"
                                    minlength="1"
                                    maxlength="100"
                                    style="top: 8px"
                                    type="textarea"
                                    v-if="item.inputIsShow"
                                    v-model="newReply">
                            </el-input>
                            <el-button @click="replyOver(item)" icon="el-icon-check"
                                       style="left: 48%;position: relative;margin-top: 20px;"
                                       type="primary" v-if="item.inputIsShow"></el-button>
                        </div>
                    </el-card>
                </div>
            </el-main>
        </el-container>
        <el-pagination
                style="margin-top: 20px"
                background
                layout="prev, pager, next, jumper"
                :current-page="currentPage"
                :total=total
                @current-change="handleCurrentChange">
        </el-pagination>
    </div>
</template>

<script>
    export default {
        name: "MessageBoard",
        data() {
            return {
                valueOpen: false,
                count: 0,
                username: "",
                inputField: "",
                currentPage: 1,
                total: 0,
                dialogVisible: false,
                newReply: "",
                message: [
                    {
                        id: 0,
                        from_phonenumber: "",
                        likenum: 0,
                        dislikenum: 0,
                        avaUrl: "",
                        content: "",
                        date: "2020-02-23",
                        name: "忧郁的小乌龟",
                        reply: [],
                    },
                ],
            };
        },
        methods: {
            handleCurrentChange(val) {
                this.currentPage = val;
                let that = this;
                let formData = new FormData();
                formData.append("currentPage", that.currentPage);
                formData.append("value", that.valueOpen);
                this.axios({
                    method: "post",
                    url: "/watchMoreComments",
                    data: formData,
                })
                    .then(function (response) {
                            if (response.data.msg === "成功") {
                                that.message = response.data.pageNow;
                                that.total = 10 * parseInt(response.data.pageCount);
                            } else {
                                that.$message.error(response.data.msg);
                            }
                        },
                        function (err) {
                            console.log(err);
                        },
                    );
            },
            incLikeNum(item) {
                let that = this;
                let formData = new FormData();
                formData.append("commentsId", item.id);
                this.axios({
                    method: "post",
                    url: "/incLikeNum",
                    data: formData,
                })
                    .then(function (response) {
                            if (response.data.msg === "点赞成功") {
                                item.likenum += 1;
                            } else {
                                that.$message(response.data.msg);
                            }
                        },
                        function (err) {
                            console.log(err);
                            that.$message.error("你还没登录呢");
                        },
                    );
            },

            incDisLikeNum(item) {
                let that = this;
                let formData = new FormData();
                formData.append("commentsId", item.id);
                this.axios({
                    method: "post",
                    url: "/incDisLikeNum",
                    data: formData,
                })
                    .then(function (response) {
                            if (response.data.msg === "点踩成功") {
                                item.dislikenum += 1;
                            } else {
                                that.$message(response.data.msg);
                            }
                        },
                        function (err) {
                            console.log(err);
                            that.$message.error("你还没登录呢");
                        },
                    );
            },

            reply(item) {
                item.inputIsShow = true;
            },

            watchOldReply(item) {
                item.replyIsShow = !item.replyIsShow;
                let that = this;
                let formData = new FormData();
                formData.append("commentsId", item.id);
                this.axios({
                    method: "post",
                    url: "/watchReply",
                    data: formData,
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

            replyOver(item) {
                item.inputIsShow = false;
                let that = this;
                let formData = new FormData();
                let thisData = this.getNowFormatDate();
                formData.append("content", this.newReply);
                if (this.newReply.length === 0) {
                    this.$message({
                        message: "你没有输入任何消息",
                        type: "warning",
                    });
                } else {
                    formData.append("commentsId", item.id);
                    formData.append("date", thisData);
                    this.axios({
                        method: "post",
                        url: "/writeReply",
                        data: formData,
                    })
                        .then(function (response) {
                                let msg = response.data.msg;
                                if (msg === "评论成功") {
                                    let name = response.data.name;
                                    let tempItem = {
                                        from_name: name,
                                        content: that.newReply,
                                        date: thisData,
                                    };
                                    item.reply.push(tempItem);
                                    that.watchOldReply(item);
                                    that.$message({
                                        message: msg,
                                        type: "success",
                                    });
                                    that.newReply = "";
                                } else {
                                    that.$message.error(msg);
                                    that.newReply = "";
                                }
                            },
                            function (err) {
                                console.log(err);
                            },
                        );
                }
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

            init() {
                let that = this;
                let formData = new FormData();
                formData.append("value", this.valueOpen);
                this.axios({
                    method: "post",
                    url: "/watchComments",
                    data: formData,
                })
                    .then(function (response) {
                            that.message = response.data.pageNow;
                            that.total = 10 * parseInt(response.data.pageCount);
                            that.username = response.data.username;
                        },
                        function (err) {
                            console.log(err);
                        },
                    );
            },

            searchComments() {
                let that = this;
                let formData = new FormData();
                formData.append("inputField", this.inputField);
                this.axios({
                    method: "post",
                    url: "/searchComments",
                    data: formData,
                })
                    .then(function (response) {
                            console.log(response);
                            that.message = response.data.pageNow;
                        },
                        function (err) {
                            console.log(err);
                            that.$message.error("没有结果");
                        });
            },

            delMyReply(i) {
                let that = this;
                this.$confirm("此操作将永久删除该回复, 是否继续?", "提示", {
                    confirmButtonText: "确定",
                    cancelButtonText: "取消",
                    type: "warning",
                }).then(() => {
                    that.axios({
                        methods: "get",
                        url: "/delMyReply?id=" + i.id,
                    })
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

            watchOtherPeople(item) {
                let that = this;
                let theName;
                if (item.from_name) {
                     theName = item.from_name;
                } else {
                    theName = item.name;
                }
                let routeData = this.$router.resolve({
                    path: "/OtherPeople",
                    query: {
                        phoneNumber: item.from_phonenumber,
                        username: theName,
                        myName: that.username,
                    },
                });
                window.open(routeData.href, '_blank');

            },

        },
        mounted: function () {
            this.init();
        },
    };
</script>

<style scoped>
    #messageBoard {
        position: relative;
        width: 100%;
        height: 100%;

    }

    .el-header, .el-footer {
        background-color: #B3C0D1;
        color: #333;
        text-align: center;
        line-height: 60px;
        background-image: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    .box-card {
        line-height: 30px;
        margin-top: 30px;
        padding-bottom: 20px;
        position: relative;
    }

    .msgTitle {
        position: absolute;
        left: 0;
        margin-top: 14px;
        margin-left: 60px;
    }

    .myAva {
        position: absolute;
        left: 0;
        cursor: pointer;
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

    .reply-box {
        position: relative;
        width: 100%;
        height: 150px;
        overflow: auto;
        text-align: left;
        box-shadow: 0 -1px 1px 0 rgba(0, 0, 0, 0.1)
    }

    .infinite-list-item {
        list-style: none;
        margin-bottom: 10px;
    }

    #header {
        font-size: 30px;
        padding-top: 20px;
        padding-bottom: 75px;
        border-radius: 5px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
        background-image: linear-gradient(135deg, #f5f7fa 0%, #f5f7fa 100%);
    }

    #searchInput {
        line-height: 10px;
        margin-top: 20px;
        margin-bottom: -20px;
        width: 80%;
        transform: translate(10%, 0%);
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