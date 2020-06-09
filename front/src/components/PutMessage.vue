<template>
    <div id="app">
        <el-container>
            <el-header id="header">在留言板上写出自己想说的话</el-header>
            <el-main>
                <div id="comments">
                    <el-input
                            id="commentsInput"
                            :rows="20"
                            placeholder="请输入回复内容,字数限制200字"
                            minlength="1"
                            maxlength="200"
                            style="top: 8px"
                            type="textarea"
                            v-model="myComments">
                    </el-input>
                    <el-button @click="commentsSubmit()" icon="el-icon-check"
                               style="left: 47%;position: relative;"
                               type="primary"></el-button>
                </div>
            </el-main>
        </el-container>
        <span>将自己的想说的话写到留言板上,欢迎和大家一起讨论</span>
    </div>
</template>

<script>
    export default {
        name: "PutMessage",
        data() {
            return {
                myComments: '',
            };
        },
        methods: {
            commentsSubmit() {
                let that = this;
                let formData = new FormData();
                formData.append('myComments', this.myComments);
                this.axios({
                    method: 'post',
                    url: '/write_message',
                    data: formData,
                })
                    .then(function (response) {
                            if (response.data.msg === '发表成功') {
                                that.$message.success(response.data.msg);
                                that.myComments = '';
                            } else {
                                that.$message.error(response.data.msg);
                                that.myComments = '';
                            }
                        },
                        function (err) {
                            console.log(err);
                        }
                    );
            },
        }
    };
</script>

<style scoped>
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

    #comments {
        position: relative;
        width: 70%;
        left: 50%;
        transform: translate(-50%, 0%);
    }

    #commentsInput {
        position: relative;
        width: 80%;
    }

</style>