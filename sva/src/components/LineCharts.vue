<template>
  <el-row>
    <el-date-picker
      v-model="dateRange"
      type="daterange"
      range-separator="至"
      start-placeholder="开始日期"
      end-placeholder="结束日期"
      value-format="YYYY-MM-DD"
      @change="changeDateRange"
      :default-value="[new Date(), new Date()]"
    >
      >
    </el-date-picker>
  </el-row>
  <el-row>
    <el-col :span="24"
      ><div id="myChart" :style="{ width: '100%', height: '400px' }"></div
    ></el-col>
  </el-row>
</template>

<script setup>
import { inject, onMounted, ref, onUpdated } from "vue";
import axios from "axios";
import moment from "moment";

let echarts = inject("ec"); //引入
let dateRange = ref([
  moment().subtract(7, "days").format("YYYY-MM-DD"),
  moment().format("YYYY-MM-DD"),
]);
let lineChartData = ref([]);

onMounted(() => {
  changeDateRange();
});

function changeDateRange() {
  let lineChartParam = localStorage.lineChartParam;
  let code = JSON.parse(localStorage.getItem("lineChartParam")).code;
  let startDate = dateRange.value[0];
  let endDate = dateRange.value[1];
  axios
    .get(
      "/api/stock/getBlocksInRange?code=" +
        code +
        "&start_date=" +
        startDate +
        "&end_date=" +
        endDate
    )
    .then((response) => {
      lineChartData.value = response.data.data;
      loadLineChart();
    });
}

function loadLineChart() {
  //需要获取到element,所以是onMounted的Hook
  let myChart = echarts.init(document.getElementById("myChart"));
  // 绘制图表
  myChart.setOption({
    xAxis: {
      type: "category",
      data: lineChartData.value.map((item) =>
        moment(item.date).format("YYYY-MM-DD")
      ),
    },
    yAxis: {
      type: "value",
    },
    series: [
      {
        data: lineChartData.value.map((item) => item.grade),
        type: "line",
        label: { normal: { show: true } },
      },
    ],
  });
  window.onresize = function () {
    //自适应大小
    myChart.resize();
  };
  setTimeout(() => {
    myChart.resize();
  }, 100);
}
</script>

<style></style>
