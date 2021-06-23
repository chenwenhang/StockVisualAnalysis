<template>
  <el-row>
    <el-col :span="2"><div class="grid-content"></div></el-col>
    <el-col :span="20">
      <div class="grid-content">
        <el-row>
          <el-upload
            action="http://127.0.0.1:8000/api/stock/uploadBlock?type=excel"
            :on-success="handleUploadSuccess"
            multiple
            name="file"
            :limit="3"
            :on-exceed="handleExceed"
            :file-list="fileList"
          >
            <el-button>上传板块</el-button> </el-upload
          >&nbsp;&nbsp;
          <el-upload
            action="http://127.0.0.1:8000/api/stock/uploadStrength?type=excel"
            :on-success="handleUploadSuccess"
            multiple
            name="file"
            :limit="3"
            :on-exceed="handleExceed"
            :file-list="fileList"
          >
            <el-button>上传强度</el-button>
          </el-upload>
        </el-row>
        <el-tabs @tab-click="changeView">
          <el-tab-pane label="板块" name="first"></el-tab-pane>
          <el-tab-pane label="强度" name="second"></el-tab-pane>
        </el-tabs>
        <div v-show="showOption">
          <el-table :data="blockTableData" stripe style="width: 100%">
            <el-table-column prop="code" label="代码" sortable>
            </el-table-column>
            <el-table-column prop="name" label="名称" sortable>
            </el-table-column>
            <el-table-column prop="RPS250" label="RPS250" sortable>
            </el-table-column>
            <el-table-column prop="RPS120" label="RPS120" sortable>
            </el-table-column>
            <el-table-column prop="RPS60" label="RPS60" sortable>
            </el-table-column>
            <el-table-column prop="RPS30" label="RPS30" sortable>
            </el-table-column>
            <el-table-column prop="RPS10" label="RPS10" sortable>
            </el-table-column>
            <el-table-column prop="grade" label="分数" sortable>
            </el-table-column>
            <el-table-column
              prop="date"
              label="日期"
              :formatter="dateFormat"
              sortable
            >
            </el-table-column>
            <el-table-column align="right" width="200">
              <template #header>
                <div class="block">
                  <el-date-picker
                    v-model="blockDate"
                    @change="getBlocks"
                    type="date"
                    style="width: 90%"
                    placeholder="选择日期"
                  >
                  </el-date-picker>
                </div>
              </template>
              <template #default="scope">
                <el-button
                  size="mini"
                  @click="showBlockTrend(scope.$index, scope.row)"
                  >查看趋势</el-button
                >
              </template>
            </el-table-column>
          </el-table>
        </div>

        <el-dialog
          :title="'【' + lineChartParam.name + '】 板块趋势'"
          v-if="lineChartVisible"
          v-model="lineChartVisible"
          :width="'80%'"
        >
          <LineCharts />
        </el-dialog>

        <div v-show="!showOption">
          <el-table :data="strengthTableData" stripe style="width: 100%">
            <el-table-column prop="industry" label="行业" sortable>
            </el-table-column>
            <el-table-column prop="count" label="数量" sortable>
            </el-table-column>
            <el-table-column prop="total" label="总数" sortable>
            </el-table-column>
            <el-table-column prop="grade" label="分数" sortable>
            </el-table-column>
            <el-table-column
              prop="date"
              label="日期"
              :formatter="dateFormat"
              sortable
            >
            </el-table-column>
            <el-table-column align="right">
              <template #header>
                <div class="block">
                  <el-date-picker
                    v-model="strengthDate"
                    @change="getStrengths"
                    type="date"
                    placeholder="选择日期"
                  >
                  </el-date-picker>
                </div>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </div>
    </el-col>
    <el-col :span="2"><div class="grid-content"></div></el-col>
  </el-row>
</template>

<script setup>
import { defineProps, reactive, ref } from "vue";
import LineCharts from "./LineCharts.vue";
import { ElMessage } from 'element-plus'
import axios from "axios";
import moment from "moment";

let blockTableData = ref([]);
let strengthTableData = ref([]);
let strengthDate = ref(moment().format("YYYY-MM-DD"));
let blockDate = ref(moment().format("YYYY-MM-DD"));
let fileList = [];
let showOption = ref(true);
let search = null;
let lineChartVisible = ref(false);
let lineChartParam = ref({});

getStrengths(moment().format("YYYY-MM-DD"));
getBlocks(moment().format("YYYY-MM-DD"));

function showBlockTrend(index, row) {
  lineChartParam.value = {
    code: row.code,
    name: row.name,
  };
  lineChartVisible.value = true;
  localStorage.setItem("lineChartParam", JSON.stringify(lineChartParam.value));
}

function getStrengths() {
  axios
    .get(
      "/api/stock/getStrengths?date=" +
        moment(strengthDate.value).format("YYYY-MM-DD")
    )
    .then((response) => {
      strengthTableData.value = response.data.data;
    });
}

function getBlocks() {
  axios
    .get(
      "/api/stock/getBlocks?date=" +
        moment(blockDate.value).format("YYYY-MM-DD")
    )
    .then((response) => {
      blockTableData.value = response.data.data;
    });
}

function changeView() {
  showOption.value = !showOption.value;
}

function dateFormat(row, column) {
  let date = row[column.property];
  if (date == undefined) {
    return "";
  }
  return moment(date).format("YYYY-MM-DD");
}

function handleUploadSuccess(file, fileList) {
  ElMessage.success({
    message: "上传成功！",
    type: "success",
  });
}

function handleExceed(files, fileList) {
  this.$message.warning(
    `当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${
      files.length + fileList.length
    } 个文件`
  );
}

function beforeRemove(file, fileList) {
  return this.$confirm(`确定移除 ${file.name}？`);
}
</script>

<style scoped>
a {
  color: #42b983;
}
</style>
