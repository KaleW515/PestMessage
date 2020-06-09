<template>
    <div id="home">
        <el-container id="container">
            <el-scrollbar style="height: 102%; background-color: #545C64;">
                <el-aside :width="asideWidth" style="overflow-x: hidden;">
                    <span id="title" v-if="!isCollapse">疫情信息平台</span>
                    <el-radio-group v-model="isCollapse" @change="haveChange" size="mini" fill="#545C64">
                        <el-radio-button :label="false">
                            <i class="el-icon-s-fold"></i>
                        </el-radio-button>
                        <el-radio-button :label="true">
                            <i class="el-icon-s-unfold"></i>
                        </el-radio-button>
                    </el-radio-group>
                    <el-menu
                            :collapse="isCollapse"
                            default-active="1-1"
                            :default-openeds="['1', '2']"
                            class="el-menu-vertical-demo"
                            @open="handleOpen"
                            @close="handleClose"
                            background-color="#545c64"
                            text-color="#fff"
                            active-text-color="#ffd04b">
                        <el-submenu index="1">
                            <template slot="title">
                                <i class="el-icon-news"></i>
                                <span>关于疫情</span>
                            </template>
                            <el-menu-item-group>
                                <el-menu-item index="1-1" @click="getPestData">最新信息</el-menu-item>
                                <el-menu-item index="1-2" @click="go_aboutVirus">关于病毒</el-menu-item>
                                <el-menu-item index="1-3" @click="go_messageBoard">留言板</el-menu-item>
                                <el-menu-item index="1-4" @click="go_donate">我要捐助</el-menu-item>
                                <el-menu-item index="1-5" @click="go_volunteer">志愿报名</el-menu-item>
                            </el-menu-item-group>
                        </el-submenu>
                        <el-submenu index="2">
                            <template slot="title">
                                <i class="el-icon-user"></i>
                                <span>个人主页</span>
                            </template>
                            <el-menu-item-group>
                                <el-menu-item index="2-1" @click="go_myPage">我的主页</el-menu-item>
                                <el-menu-item index="2-3" @click="go_putMessage">我有话说</el-menu-item>
                                <el-menu-item index="2-4" @click="outLogin">退出系统</el-menu-item>
                            </el-menu-item-group>
                        </el-submenu>
                    </el-menu>
                </el-aside>
            </el-scrollbar>
            <el-main id="body">
                <div v-if="msgIsShow">
                    <el-carousel :interval="4000" type="card" height="200px">
                        <el-carousel-item v-for="item in picUrl" :key="item">
                            <el-image :src=item>
                                <div slot="placeholder" class="image-slot">
                                    加载中<span class="dot">...</span>
                                </div>
                            </el-image>
                        </el-carousel-item>
                    </el-carousel>
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <span>全国疫情数据</span>
                        </div>
                        <div id="pestDataCard">
                            <div class="confirm">
                                <span>确诊:</span>
                                <el-tooltip :content="contrastYesData.confirmData" placement="bottom"
                                            effect="light">
                                    <span v-text="chinaPestData.confirmData"></span>
                                </el-tooltip>
                            </div>
                            <div class="suspect">
                                <span>疑似:</span>
                                <el-tooltip :content="contrastYesData.suspectData" placement="bottom"
                                            effect="light">
                                    <span v-text="chinaPestData.suspectData"></span>
                                </el-tooltip>
                            </div>
                            <div class="dead">
                                <span>死亡:</span>
                                <el-tooltip :content="contrastYesData.deadData" placement="bottom" effect="light">
                                    <span v-text="chinaPestData.deadData"></span>
                                </el-tooltip>
                            </div>
                            <div class="heal">
                                <span>治愈:</span>
                                <el-tooltip :content="contrastYesData.healData" placement="bottom" effect="light">
                                    <span v-text="chinaPestData.healData"></span>
                                </el-tooltip>
                            </div>
                        </div>
                    </el-card>
                    <el-card class="box-card" id="areaPestData">
                        <div slot="header" class="clearfix" id="areaPeatDataTitle">
                            <span v-text="curCity"></span>
                            <span>疫情数据</span>
                            <div id="select">
                                <el-select v-model="value" placeholder="请选择" @change="changeCity">
                                    <el-option
                                            v-for="item in cities"
                                            :key="item.value"
                                            :label="item.label"
                                            :value="item.value">
                                        <span style="float: left">{{ item.label }}</span>
                                    </el-option>
                                </el-select>
                            </div>
                        </div>
                        <div>
                            <div class="confirm">
                                <span>新增确诊:</span>
                                <span v-text="areaPestData.areaNewConfirmData"></span>
                            </div>
                            <div class="suspect">
                                <span>确诊:</span>
                                <span v-text="areaPestData.areaConfirm"></span>
                            </div>
                            <div class="dead">
                                <span>死亡:</span>
                                <span v-text="areaPestData.areaDeadData"></span>
                            </div>
                            <div class="heal">
                                <span>治愈:</span>
                                <span v-text="areaPestData.areaHealData"></span>
                            </div>
                        </div>
                    </el-card>
                    <div id="lineChart">
                    </div>
                </div>
                <router-view/>
            </el-main>

        </el-container>
    </div>
</template>

<script>
    import echarts from "echarts";
    import {mapMutations} from 'vuex';

    export default {
        name: "Home",
        data() {
            return {
                socket: "",
                isCollapse: false,
                asideWidth: "250px",
                charts: "",
                cityData: {},
                picUrl: [axios.defaults.baseURL + "/img/?id=1",
                    axios.defaults.baseURL + "/img/?id=2",
                    axios.defaults.baseURL + "/img/?id=3"],
                msgIsShow: true,
                e_confirmData: [],
                e_suspectData: [],
                e_healData: [],
                e_deadData: [],
                xData: [],
                chinaPestData: {
                    confirmData: 0,
                    suspectData: 0,
                    deadData: 0,
                    healData: 0,
                },
                contrastYesData: {
                    confirmData: "",
                    suspectData: "",
                    deadData: "",
                    healData: "",
                },
                areaPestData: {
                    areaNewConfirmData: 0,
                    areaConfirm: 0,
                    areaDeadData: 0,
                    areaHealData: 0,
                },
                curCity: "",
                cities: [{
                    value: "HuBei",
                    label: "湖北",
                }, {
                    value: "GuangDong",
                    label: "广东",
                }, {
                    value: "HeNan",
                    label: "河南",
                }, {
                    value: "ZheJiang",
                    label: "浙江",
                }, {
                    value: "HuNan",
                    label: "湖南",
                }, {
                    value: "AnHui",
                    label: "安徽",
                }, {
                    value: "JiangXi",
                    label: "江西",
                }, {
                    value: "JiangSu",
                    label: "江苏",
                }, {
                    value: "ChongQin",
                    label: "重庆",
                }, {
                    value: "ShanDong",
                    label: "山东",
                }, {
                    value: "SiChuan",
                    label: "四川",
                }, {
                    value: "HeLongJiang",
                    label: "黑龙江",
                }, {
                    value: "BeiJing",
                    label: "北京",
                }, {
                    value: "ShangHai",
                    label: "上海",
                }, {
                    value: "HeBei",
                    label: "河北",
                }, {
                    value: "FuJian",
                    label: "福建",
                }, {
                    value: "GuangXi",
                    label: "广西",
                }, {
                    value: "ShaXi",
                    label: "陕西",
                }, {
                    value: "YunNan",
                    label: "云南",
                }, {
                    value: "HaiNan",
                    label: "海南",
                }, {
                    value: "GuiZhou",
                    label: "贵州",
                }, {
                    value: "ShanXi",
                    label: "山西",
                }, {
                    value: "TianJin",
                    label: "天津",
                }, {
                    value: "LiaoNing",
                    label: "辽宁",
                }, {
                    value: "GanSu",
                    label: "甘肃",
                }, {
                    value: "JiLin",
                    label: "吉林",
                }, {
                    value: "XinJiang",
                    label: "新疆",
                }, {
                    value: "NeiMengGu",
                    label: "内蒙古",
                }, {
                    value: "NingXia",
                    label: "宁夏",
                }, {
                    value: "XiangGang",
                    label: "香港",
                }, {
                    value: "TaiWan",
                    label: "台湾",
                }, {
                    value: "QinHai",
                    label: "青海",
                }, {
                    value: "AoMen",
                    label: "澳门",
                }, {
                    value: "XiZang",
                    label: "西藏",
                }],
                value: "",
                lockReconnect: false,//是否真正建立连接
                timeout: 10 * 1000,//30秒一次心跳
                timeoutObj: null,//心跳倒计时
                serverTimeoutObj: null,//心跳倒计时
                timeOutNum: null,//断开 重连倒计时
            };
        },
        methods: {
            ...mapMutations(['setNewReplyNum', 'setNewLikeNum', 'setNewDisLikeNum']),

            handleOpen(key, keyPath) {
                console.log(key, keyPath);
            },

            handleClose(key, keyPath) {
                console.log(key, keyPath);
            },

            getPestData() {
                let that = this;
                this.$router.push("/home");
                this.msgIsShow = true;
                axios.get("/new_msg")
                    .then(function (response) {
                            that.chinaPestData.confirmData = response.data.totalData.confirm;
                            that.chinaPestData.suspectData = response.data.totalData.suspect;
                            that.chinaPestData.healData = response.data.totalData.heal;
                            that.chinaPestData.deadData = response.data.totalData.dead;
                            that.cityData = response.data.cityData;
                            that.changeContrastData(response);
                            that.initDrawData();
                            for (let key in response.data.dateTodayData) {
                                that.e_confirmData.unshift(response.data.dateTodayData[key].today.confirm.toString());
                                that.e_suspectData.unshift(response.data.dateTodayData[key].today.suspect.toString());
                                that.e_healData.unshift(response.data.dateTodayData[key].today.heal.toString());
                                that.e_deadData.unshift(response.data.dateTodayData[key].today.dead.toString());
                                that.xData.unshift(response.data.dateTodayData[key].date.toString().substring(5, 10));
                            }
                            that.mounted();
                        },
                        function (err) {
                            console.log(err);
                        });
            },

            changeCity(curCity) {
                let label = "";
                label = this.cities.find((item) => {
                    return item.value === curCity;
                });
                this.curCity = label.label;
                for (let key in this.cityData) {
                    if (key === this.curCity) {
                        this.areaPestData.areaConfirm = this.cityData[key].totalData.confirm;
                        this.areaPestData.areaNewConfirmData = this.cityData[key].todayData.confirm;
                        this.areaPestData.areaHealData = this.cityData[key].totalData.heal;
                        this.areaPestData.areaDeadData = this.cityData[key].totalData.dead;
                        if (this.areaPestData.areaNewConfirmData === "") {
                            this.areaPestData.areaNewConfirmData = "待更新";
                        }
                    }
                }
            },

            haveChange(nowBool) {
                nowBool === false ? this.asideWidth = "250px" : this.asideWidth = "65px";
            },

            initDrawData() {
                this.e_suspectData = [];
                this.e_confirmData = [];
                this.e_healData = [];
                this.e_deadData = [];
                this.xData = [];
            },

            changeContrastData(response) {
                let that = this;
                if (response.data.todayData.confirm === null) {
                    return;
                }
                if (response.data.todayData.confirm >= 0) {
                    that.contrastYesData.confirmData = "较昨日增长" + response.data.todayData.confirm.toString();
                } else {
                    that.contrastYesData.confirmData = "较昨日减少" + response.data.todayData.confirm.toString();
                }
                if (response.data.todayData.suspect >= 0) {
                    that.contrastYesData.suspectData = "较昨日增长" + response.data.todayData.suspect.toString();
                } else {
                    that.contrastYesData.suspectData = "较昨日减少" + response.data.todayData.suspect.toString();
                }
                if (response.data.todayData.heal >= 0) {
                    that.contrastYesData.healData = "较昨日增长" + response.data.todayData.heal.toString();
                } else {
                    that.contrastYesData.healData = "较昨日减少" + response.data.todayData.heal.toString();
                }
                if (response.data.todayData.dead >= 0) {
                    that.contrastYesData.deadData = "较昨日增长" + response.data.todayData.dead.toString();
                } else {
                    that.contrastYesData.deadData = "较昨日减少" + response.data.todayData.dead.toString();
                }
            },

            drawLine(id) {
                let that = this;
                this.charts = echarts.init(document.getElementById(id));
                this.charts.setOption({
                    title: {text: "全国疫情新增趋势"},
                    tooltip: {
                        trigger: "axis",
                    },
                    legend: {
                        data: ["新增确诊", "新增疑似", "新增治愈", "新增死亡"],
                    },

                    grid: {
                        left: "3%",
                        right: "3%",
                        bottom: "5%",
                        containLabel: true,
                    },

                    toolbox: {
                        feature: {
                            saveAsImage: {},
                        },
                    },
                    xAxis: {
                        type: "category",
                        name: "日期",
                        boundaryGap: false,
                        data: this.xData,

                    },
                    yAxis: {
                        name: "数量",
                        type: "value",
                    },

                    series: [
                        {
                            name: "新增确诊",
                            type: "line",
                            stack: "确诊总量",
                            data: this.e_confirmData,
                        },
                        {
                            name: "新增疑似",
                            type: "line",
                            stack: "疑似总量",
                            data: this.e_suspectData,
                        },
                        {
                            name: "新增治愈",
                            type: "line",
                            stack: "治愈总量",
                            data: this.e_healData,
                        },
                        {
                            name: "新增死亡",
                            type: "line",
                            stack: "死亡总量",
                            data: this.e_deadData,
                        },
                    ],
                });
            },
            go_aboutVirus() {
                this.msgIsShow = false;
                this.$router.push("/about-virus");
            },

            go_volunteer() {
                this.msgIsShow = false;
                this.$router.push("/volunteer");
            },

            go_donate() {
                this.msgIsShow = false;
                this.$router.push("/donation");
            },

            go_messageBoard() {
                this.msgIsShow = false;
                this.$router.push("/message-board");
            },

            go_myPage() {
                this.msgIsShow = false;
                this.$router.push("/my-page");
            },

            go_revisePwd() {
                this.msgIsShow = false;
                this.$router.push("/revise-pwd");
            },

            go_putMessage() {
                this.msgIsShow = false;
                this.$router.push("/put-message");
            },

            mounted() {
                this.$nextTick(function () {
                    this.drawLine("lineChart");
                });
            },

            outLogin() {
                this.$confirm("退出后再登录需要重新输入密码, 是否继续?", "提示", {
                    confirmButtonText: "确定",
                    cancelButtonText: "取消",
                    type: "warning",
                }).then(() => {
                    this.$message({
                        type: "success",
                        message: "退出成功!",
                    });
                    axios.get("/logout")
                        .then(function (response) {
                                console.log(response);
                                localStorage.clear();
                            },
                            function (err) {
                                console.log(err);
                            });
                    this.$router.push("/Login");
                }).catch(() => {
                    this.$message({
                        type: "info",
                        message: "已取消退出",
                    });
                });
            },

            initSocket: function () {
                if (typeof (WebSocket) === "undefined") {
                    alert("您的浏览器不支持socket");
                } else {
                    this.socket = new WebSocket("ws://127.0.0.1:8000/push_msg/" + localStorage.getItem('username'));
                    this.socket.onopen = this.open;
                    this.socket.onerror = this.error;
                    this.socket.onmessage = this.getMessage;
                    this.socket.onclose = this.close;
                }
            },

            open: function () {
                console.log("success");
                this.start();
            },
            error: function () {
                console.log("failed");
                this.reconnect();
            },
            getMessage: function (msg) {
                try {
                    if (msg.data === 'heartBeat') {
                        this.reset();
                        return;
                    }
                } catch (e) {
                    console.log(e);
                }
                let res = JSON.parse(msg.data);
                let _this = this;
                if (res.newReplyNum !== this.$store.state.newReplyNum) {
                    _this.setNewReplyNum({newReplyNum: res.newReplyNum});
                }
                if (res.newLikeNum !== this.$store.state.newLikeNum) {
                    _this.setNewLikeNum({newLikeNum: res.newLikeNum});
                }
                if (res.newDisLikeNum !== this.$store.state.newDisLikeNum) {
                    _this.setNewDisLikeNum({newDisLikeNum: res.newDisLikeNum});
                }
                this.reset();
            },
            send: function (msg) {
                this.socket.send(msg);
            },
            close: function () {
                console.log("closed");
                this.reconnect();
            },
            reconnect() {//重新连接
                let that = this;
                if (that.lockReconnect) {
                    return;
                }
                that.lockReconnect = true;
                that.timeOutNum = setTimeout(function () {
                    that.initSocket();
                    that.lockReconnect = false;
                }, 5000);
            },
            reset() {
                let that = this;
                clearTimeout(that.timeoutObj);
                clearTimeout(that.serverTimeoutObj);
                that.start();
            },
            start() {
                let self = this;
                self.timeoutObj && clearTimeout(self.timeoutObj);
                self.serverTimeoutObj && clearTimeout(self.serverTimeoutObj);
                self.timeoutObj = setTimeout(function () {
                    if (self.socket.readyState == 1) {
                        self.socket.send("heartBeat");
                    } else {
                        self.reconnect();
                    }
                    self.serverTimeoutObj = setTimeout(function () {
                        self.socket.close();
                    }, self.timeout);
                }, self.timeout);
            },
        },

        mounted() {
            this.$nextTick(function () {
                this.drawLine("lineChart");
                this.getPestData();
            });

            this.initSocket();
        },

        watch: {
            "$store.state.newReplyNum"(val) {
                if (val !== 0) {
                    this.$notify({
                        title: "消息提示",
                        message: "刚刚有人回复了你",
                        duration: 0,
                    });
                }
            },
            "$store.state.newLikeNum"(val) {
                if (val !== 0) {
                    this.$notify({
                        title: "消息提示",
                        message: "刚刚有人赞了你",
                        duration: 0,
                    });
                }
            },
            "$store.state.newDisLikeNum"(val) {
                if (val !== 0) {
                    this.$notify({
                        title: "消息提示",
                        message: "刚刚有人踩了你",
                        duration: 0,
                    });
                }
            },
        },
    };
</script>

<style scoped>
    #home {
        width: 100%;
        height: 100%;
        overflow: hidden;
    }

    #container {
        position: absolute;
        width: 100%;
        height: 100%;
        overflow: hidden;
        margin-top: -8px;
        margin-left: -8px;
    }

    #title {
        font-size: 30px;
        color: white;
    }

    #body {
        position: relative;
        overflow-x: hidden;
        height: 100%;
        width: 80%;
        left: -1px;
        border: 1px solid white;
        line-height: 100px;
        text-align: center;
    }

    .el-aside {
        background-color: #545C64;
        color: #333;
        text-align: center;
        line-height: 100px;
    }

    #pestDataCard {
        position: relative;
        width: 100%;
        height: 100%;
    }

    #areaPeatDataTitle {
        height: 160px;
    }

    #select {
        position: relative;
        transform: translate(80%, -100%);
    }

    #areaPestData {
        position: relative;
        top: 30px;
    }

    .clearfix {
        text-align: left;
        font-size: 30px;
    }

    .confirm {
        position: absolute;
        width: 25%;
    }

    .suspect {
        position: absolute;
        width: 25%;
        left: 25%;
    }

    .dead {
        position: absolute;
        width: 25%;
        left: 50%;
    }

    .heal {
        position: relative;
        width: 25%;
        left: 75%;
    }

    #lineChart {
        position: relative;
        width: 100%;
        height: 500px;
        top: 60px;
    }

    body > .el-container {
        margin-bottom: 40px;
    }

    .el-container:nth-child(5) .el-aside,
    .el-container:nth-child(6) .el-aside {
        line-height: 260px;
    }

    .el-container:nth-child(7) .el-aside {
        line-height: 320px;
    }

</style>
