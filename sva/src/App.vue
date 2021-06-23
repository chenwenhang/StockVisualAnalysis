<template>
  <img alt="Vue logo" src="./assets/logo.png" />
  <h1>{{ msg }}</h1>
  <StockAnalysis />
</template>

<script setup>
import StockAnalysis from "./components/StockAnalysis.vue";
import * as echarts from 'echarts'
import { provide } from 'vue'

let msg = "股票可视化分析系统"
provide('ec',echarts)

// This starter template is using Vue 3 experimental <script setup> SFCs
// Check out https://github.com/vuejs/rfcs/blob/script-setup-2/active-rfcs/0000-script-setup.md
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
