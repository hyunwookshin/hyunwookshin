<template>
<div>
<b-row class="header">
   <b-col cols="7" class="title"><h1>Hyunwook Shin</h1></b-col>
   <b-col cols="3" class="links">
      <b-btn class="githubButton" variant="primary">GitHub</b-btn>
   </b-col>
</b-row>
<b-row class="footer">
   <b-col cols="12" class="footerInner">
      <p>Hyunwook Shin 2019</p>
   </b-col>
</b-row>
</div>
</template>
<script>
   export default {
      name: 'Main',
      data() {
         return {
         }
      }
   }
</script>
<style scoped>
.header, .footer {
   background-color: #39324B;
   color: white;
}
.footercInner {
   text-align: center;
   color: white;
}
.title, .githubButton {
   margin: 6px 6px;
   text-align: left;
}
.links {
   text-align: right;
}
</style>
