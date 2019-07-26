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
      <b-tab title="About" active>
         <b-card-text>Introducing myself 👋 </b-card-text>
         <b-row>
         <b-card
           v-for="blob in blobs_about"
           style="max-width: 40rem; margin-left: 2rem"
           :title="blob.title"
           :img-src="blob.img_url"
           img-alt="Image"
           img-top
           tag="article"
           class="mb-2">
          <b-card-text>
             {{ blob.content }}
          </b-card-text>
          <b-card-footer>
              <b-link :href="blob.external_url">{{blob.external_url}}</b-link>
          </b-card-footer>
        </b-card>
        </b-row>
      </b-tab>
      <b-tab title="Serverless Computing">
         <b-card-text>So what exactly is serverless..?</b-card-text>
         <b-card
           v-for="blob in blobs_serverless"
           :title="blob.title"
           :img-src="blob.img_url"
           img-alt="Image"
           img-height="350px"
           img-top
           tag="article"
           class="mb-2">
          <b-card-text>
             {{ blob.content }}
          </b-card-text>
          <b-card-footer>
              <b-link :href="blob.external_url">{{blob.external_url}}</b-link>
          </b-card-footer>
        </b-card>
      </b-tab>
      <b-tab title="Recent Reads">
         <b-card-text>Here are some books and papers that I thought were worthwhile.</b-card-text>
         <b-card
           v-for="blob in blobs_readings"
           :title="blob.title"
           :img-src="blob.img_url"
           img-alt="Image"
           img-left
           tag="article"
           class="mb-2">
          <b-card-text>
             {{ blob.content }}
          </b-card-text>
          <b-card-footer>
              <b-link :href="blob.external_url">{{blob.external_url}}</b-link>
          </b-card-footer>
        </b-card>
      </b-tab>
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
         'blobs_about' : null,
         'blobs_serverless': null,
         'blobs_readings': null
      }
   },
   methods: {
       getBlobs() {
         const pathAbout = 'https://x00nzhadqi.execute-api.us-east-2.amazonaws.com/stage/about';
         const pathServerless = 'https://x00nzhadqi.execute-api.us-east-2.amazonaws.com/stage/serverless';
         const pathReadings = 'https://x00nzhadqi.execute-api.us-east-2.amazonaws.com/stage/readings';
         axios.get(pathAbout)
           .then((res) => {
             this.blobs_about = res.data.Items;
           })
           .catch((error) => {
             // eslint-disable-next-line
             console.error(error);
           });
         axios.get(pathServerless)
           .then((res) => {
             this.blobs_serverless = res.data.Items;
           })
           .catch((error) => {
             // eslint-disable-next-line
             console.error(error);
           });
         axios.get(pathReadings)
           .then((res) => {
             this.blobs_readings= res.data.Items;
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
