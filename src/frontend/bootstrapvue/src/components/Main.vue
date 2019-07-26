<template>
<div>
<b-row class="header">
   <b-col cols="7" class="title"><h1>Hyunwook Shin</h1></b-col>
   <b-col cols="3" class="links">
      <b-btn href="https://github.com/hyunwookshin/hyunwookshin" class="githubButton" variant="primary">GitHub</b-btn>
   </b-col>
</b-row>
<b-card no-body>
   <b-tabs card>
      <b-tab title="About me in 100 words" active>
         <b-card-text>Time for me to introduce myself.</b-card-text>
         <b-card
           v-for="blob in blobs"
           :title="blob.title"
           :img-src="blob.img_url"
           img-alt="Image"
           img-top
           tag="article"
           class="mb-2">
          <b-card-text>
             {{ blob.content }}
              <b-link :href="blob.external_url">{{blob.external_url}}</b-link>
          </b-card-text>
        </b-card>
      </b-tab>
      <b-tab title="Serverless Computing">
         <b-card-text>Although intimidating at first, I began really like the serverless idea.</b-card-text>
      </b-tab>
      <b-tab title="Recent Reads">
         <b-card-text>Here are some books and papers that I thought were worthwhile.</b-card-text>
      </b-tab>
      <b-tab title="Cloud Articles">
         <b-card-text>Here are some cloud articles bookmarked.</b-card-text>
      </b-tab>
      <b-tab title="Tweets Feed">
         <b-card-text>Here are some videos bookmarked.</b-card-text>
      </b-tab>
      <b-tab title="Food Places">
         <b-card-text>Here are some nice food places I have tried</b-card-text>
      </b-tab>
   </b-tabs>
</b-card>
<b-row class="footer">
   <b-col cols="12" class="footerInner">
      <p>Hyunwook Shin 2019</p>
   </b-col>
</b-row>
</div>
</template>
<script>
import axios from 'axios';
export default {
   name: 'Main',
   data() {
      return {
         'blobs' : null,
      }
   },
   methods: {
       getBlobs() {
         const path = 'https://x00nzhadqi.execute-api.us-east-2.amazonaws.com/stage/about';
         axios.get(path)
           .then((res) => {
             this.blobs = res.data.Items;
           })
           .catch((error) => {
             // eslint-disable-next-line
             console.error(error);
           });
       },
  },
  created() {
       this.getBlobs();
  },
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
