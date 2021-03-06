import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],

  devServer: {
    localhost:"127.0.0.1",
    port:8000,
    // ๅๅไปฃ็
    proxy: {
        '/api': {
            target: 'http://127.0.0.1:8000/',
            changeOrigin: true,
            ws: true,
            rewrite: path => path.replace(/^\/api/, '')
        }
    }
  }

})
