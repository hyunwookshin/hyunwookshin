<template>
<div>
<b-row class="header">
   <b-col cols="7" class="toptitle"><h2>hyunwook shin _</h2></b-col>
   <b-col cols="3" class="links">
      <b-btn href="https://github.com/hyunwookshin" class="githubButton" variant="primary">GitHub</b-btn>
   </b-col>
</b-row>
<div id="centered">
   <b-img
      thumbnail
      src="https://hyunwook.s3.us-east-2.amazonaws.com/images/profile3.jpg"
      id="profile"
      v-bind="mainProps"
      rounded="circle"
      style="width: 8rem; height: 8rem"
      alt="Circle image">
   </b-img>
</div>
<b-img
   src="https://hyunwook.s3.us-east-2.amazonaws.com/images/servertop.png"
   fluid alt="Responsive image"
   style="width: 100%; max-height: 15rem">
</b-img>
<div class="wrapper">
   <b-tabs content-class="mt-3" justified>
      <b-tab title="Cloud Posts" active>
         <b-card-text class="text-left section" >
            <h3>Recent Cloud Posts</h3>
            Hello and welcome to my personal blog. Here, I regularly share a variety of topics related to my profession, industry trends, and my hobbies. As a software engineer specializing in cloud technologies, you'll find intriguing articles about the cloud under the first tab. I update the content periodically, so check back often for new insights and discussions.

            You can also check out my Medium page <a href="https://medium.com/@shincontact">here</a>.
         </b-card-text>
         <b-row align-h="center">
         <b-card
           v-for="blob in blobs_cloud"
           v-bind:key="blob"
           :title="blob.title"
           :img-src="blob.img_url"
           style="max-width: 40rem; margin-left: 2rem"
           img-alt="Image"
           tag="article"
           class="mb-2 text-left">
          <b-card-text class="content">
             Posted on {{ blob.posted_date }} &#128197;
             <br><br>
             {{ blob.content }}
          </b-card-text>
          <b-card-footer>
              <b-link :href="blob.external_url">{{blob.external_url}}</b-link>
          </b-card-footer>
        </b-card>
        </b-row>
      </b-tab>
      <b-tab title="Serverless">
         <b-card-text class="text-left section" >
            <h3>Serverless</h3>
            Serverless applications still need to run on servers somewhere in the cloud environments. Accordingly, serverless architecture is not immune to
            standard problems such as scale issues, security vulnerabilities, compatibility and networking issues. But overall, serverless architecture
            separates infrastructure/platform from the application logic, and that separation helps us build modular and maintainabile software.
         </b-card-text>
         <b-row align-h="center">
         <b-card
           v-for="blob in blobs_serverless"
           v-bind:key="blob"
           :title="blob.title"
           :img-src="blob.img_url"
           style="max-width: 40rem; margin-left: 2rem"
           img-alt="Image"
           img-height="350px"
           img-top
           tag="article"
           class="mb-2 text-left">
          <b-card-text class="content">
             {{ blob.posted_by }} | {{ blob.posted_date }} &#128197; <br><br>
             {{ blob.content }}
          </b-card-text>
          <b-card-footer>
              <b-link :href="blob.external_url">{{blob.external_url}}</b-link>
          </b-card-footer>
        </b-card>
        </b-row>
      </b-tab>
      <b-tab title="Recent Readings">
         <b-card-text class="text-left section" ><h3>Recent Reading Favorites</h3></b-card-text>
         <b-card-group columns>
         <b-card
           v-for="blob in blobs_readings"
           v-bind:key="blob"
           :title="blob.title"
           :img-src="blob.img_url"
           img-alt="Image"
           img-width="200px"
           style="max-width: 20rem; margin-left: 1rem"
           img-top
           tag="article"
           class="mb-2 text-left">
          <b-card-text class="content">
             {{ blob.posted_by }} | {{ blob.posted_date }} &#128197; <br><br>
             {{ blob.content }}
          </b-card-text>
          <b-card-footer>
              <b-link :href="blob.external_url">{{blob.external_url}}</b-link>
          </b-card-footer>
        </b-card>
        </b-card-group>
      </b-tab>
      <b-tab title="About">
         <b-card
           v-for="blob in blobs_about"
           v-bind:key="blob"
           :title="blob.title"
           :img-src="blob.img_url"
           img-alt="Image"
           border-variant="light"
           img-bottom
           tag="article"
           class="mb-2 text-left">
          <b-card-text class="content">
             {{ blob.content }}
          </b-card-text>
        </b-card>
      </b-tab>
   </b-tabs>
</div>
<b-row class="footer">
   <b-col cols="12" class="footerInner">
      <p>Hyunwook Shin 2024</p>
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
         'progress': true,
         'blobs_about' : null,
         'blobs_serverless': null,
         'blobs_readings': null,
         'blobs_cloud': null
      }
   },
   methods: {
       getBlobs() {
         const pathAbout = 'https://spflqnjnzf.execute-api.us-east-2.amazonaws.com/stage/about';
         const pathServerless = 'https://spflqnjnzf.execute-api.us-east-2.amazonaws.com/stage/serverless';
         const pathReadings = 'https://spflqnjnzf.execute-api.us-east-2.amazonaws.com/stage/readings';
         const pathCloud = 'https://spflqnjnzf.execute-api.us-east-2.amazonaws.com/stage/cloud';
         function compare(blob1, blob2) {
            if (blob1.posted_date < blob2.posted_date) {
               return 1;
            }
            if (blob1.posted_date > blob2.posted_date) {
               return -1;
            }
            return 0;
         }
         axios.get(pathAbout)
           .then((res) => {
             var blobs = res.data.Items;
             this.blobs_about = blobs.sort(compare);
             // Since this is the landing tab finish progress bar if done here
             this.progress = false
           })
           .catch((error) => {
             // eslint-disable-next-line
             console.error(error);
           });
         axios.get(pathServerless)
           .then((res) => {
             var blobs = res.data.Items;
             this.blobs_serverless = blobs.sort(compare);
           })
           .catch((error) => {
             // eslint-disable-next-line
             console.error(error);
           });
         axios.get(pathReadings)
           .then((res) => {
             var blobs = res.data.Items;
             this.blobs_readings = blobs.sort(compare);
           })
           .catch((error) => {
             // eslint-disable-next-line
             console.error(error);
           });
         axios.get(pathCloud)
           .then((res) => {
             var blobs = res.data.Items;
             this.blobs_cloud = blobs.sort(compare);
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
.toptitle {
   margin: 1em 1em;
   margin-left: 12%;
   text-align: left;
   font-family: Montserrat, "Calibri Light", Arial, Helvetica, sans-serif;
}
.header {
   margin-top: 1em;
   background-color: white;
   color: gray;
}
.footer {
   padding-top: 4em;
   padding-bottom: 4em;
   background-color: black;
   color: gray;
}
.title, .githubButton {
   margin: 1em 1em;
   text-align: left;
   font-family: Montserrat, "Calibri Light", Arial, Helvetica, sans-serif;
}
.section{
   margin-top: 2rem;
}
.links {
   text-align: right;
}
.content {
  font-family: "Open Sans", "Calibri Light", Arial, Helvetica, sans-serif;
}
.wrapper {
   margin-top: 1em;
   margin-left: 12%;
   margin-right: 12%;
}
#centered {
   position: absolute;
   top: 9rem;
   left: 50%;
   z-index: 3;
}
#profile {
   position: relative;
   left: -4rem;
   z-index: 3;
}
</style>
