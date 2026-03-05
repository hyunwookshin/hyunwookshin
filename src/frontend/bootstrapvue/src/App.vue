<template>
  <div id="app">
      <Main/>
  </div>
</template>

<script>
import Main from './components/Main.vue'

export default {
  name: 'app',
  components: {
     Main
  }
}
</script>

<style>
:root {
  --md-primary: #6750A4;
  --md-primary-container: #EADDFF;
  --md-on-primary: #FFFFFF;
  --md-on-primary-container: #21005D;
  --md-surface: #FFFBFE;
  --md-surface-container: #F3EDF7;
  --md-surface-container-low: #F7F2FA;
  --md-surface-container-high: #ECE6F0;
  --md-on-surface: #1C1B1F;
  --md-on-surface-variant: #49454F;
  --md-outline: #79747E;
  --md-outline-variant: #CAC4D0;
  --md-shape-sm: 8px;
  --md-shape-md: 12px;
  --md-shape-lg: 16px;
  --md-shape-xl: 28px;
  --md-shape-full: 50px;
  --md-elev-1: 0 1px 2px rgba(0,0,0,0.06), 0 1px 3px rgba(0,0,0,0.08);
  --md-elev-2: 0 2px 6px rgba(0,0,0,0.1), 0 4px 10px rgba(0,0,0,0.07);
  --md-elev-3: 0 4px 12px rgba(0,0,0,0.12), 0 8px 20px rgba(0,0,0,0.08);
}

* {
  box-sizing: border-box;
}

body {
  background-color: var(--md-surface-container-low) !important;
  font-family: 'Roboto', Helvetica, Arial, sans-serif !important;
  color: var(--md-on-surface) !important;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app {
  font-family: 'Roboto', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--md-on-surface);
  min-height: 100vh;
}
</style>
