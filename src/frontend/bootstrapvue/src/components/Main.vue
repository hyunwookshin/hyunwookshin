<template>
<div class="page-root">

  <!-- Top App Bar -->
  <header class="app-bar">
    <div class="app-bar-inner">
      <span class="app-bar-title">hyunwook shin</span>
      <div class="app-bar-actions">
        <b-btn href="https://github.com/hyunwookshin" class="tonal-btn" variant="primary">GitHub</b-btn>
        <b-btn href="https://www.linkedin.com/in/hwshin/" class="tonal-btn" variant="primary">LinkedIn</b-btn>
      </div>
    </div>
  </header>

  <!-- Hero -->
  <div class="hero-container">
    <b-img
      src="https://hyunwook.s3.us-east-2.amazonaws.com/images/servertop.png"
      fluid alt="Hero image"
      class="hero-img">
    </b-img>
  </div>

  <!-- Main content -->
  <div class="content-wrapper">
    <b-tabs content-class="tab-content-area" class="md-tabs">
      <b-tab title="Cloud &amp; AI" active>
        <div class="section-intro">
          <h2 class="section-heading">Cloud &amp; AI Posts</h2>
          <p class="section-body">
            Hello and welcome to my personal blog. Here I share topics related to my profession, industry trends, and hobbies.
            As a software engineer specializing in cloud technologies, you'll find articles about the cloud here.
            I update content periodically, so check back often.
            <br><a class="md-link" href="https://medium.com/@shincontact">Read on Medium</a>
          </p>
        </div>
        <div class="cards-grid">
          <b-card
            v-for="blob in blobs_cloud"
            v-bind:key="blob"
            :title="blob.title"
            :img-src="blob.img_url"
            img-alt="Image"
            tag="article"
            class="md-card">
            <b-card-text class="content">
              <span class="meta">Posted {{ blob.posted_date }}</span>
              <br><br>
              {{ blob.content }}
            </b-card-text>
            <b-card-footer class="card-footer-md">
              <b-link :href="blob.external_url" class="md-link footer-link">Read more</b-link>
            </b-card-footer>
          </b-card>
        </div>
      </b-tab>

      <b-tab title="Serverless">
        <div class="section-intro">
          <h2 class="section-heading">Serverless</h2>
          <p class="section-body">
            Serverless applications still need to run on servers in the cloud. Serverless architecture
            separates infrastructure from application logic, helping us build modular and maintainable software.
          </p>
        </div>
        <div class="cards-grid">
          <b-card
            v-for="blob in blobs_serverless"
            v-bind:key="blob"
            :title="blob.title"
            :img-src="blob.img_url"
            img-alt="Image"
            img-top
            tag="article"
            class="md-card">
            <b-card-text class="content">
              <span class="meta">{{ blob.posted_by }} · {{ blob.posted_date }}</span>
              <br><br>
              {{ blob.content }}
            </b-card-text>
            <b-card-footer class="card-footer-md">
              <b-link :href="blob.external_url" class="md-link footer-link">Read more</b-link>
            </b-card-footer>
          </b-card>
        </div>
      </b-tab>

      <b-tab title="Reading List">
        <div class="section-intro">
          <h2 class="section-heading">Recent Reading Favorites</h2>
        </div>
        <div class="cards-grid cards-grid--sm">
          <b-card
            v-for="blob in blobs_readings"
            v-bind:key="blob"
            :title="blob.title"
            :img-src="blob.img_url"
            img-alt="Image"
            img-top
            tag="article"
            class="md-card">
            <b-card-text class="content">
              <span class="meta">{{ blob.posted_by }} · {{ blob.posted_date }}</span>
              <br><br>
              {{ blob.content }}
            </b-card-text>
            <b-card-footer class="card-footer-md">
              <b-link :href="blob.external_url" class="md-link footer-link">Read more</b-link>
            </b-card-footer>
          </b-card>
        </div>
      </b-tab>

      <b-tab title="About">
        <div class="about-container">
          <b-img
            src="https://hyunwook.s3.us-east-2.amazonaws.com/images/profile3.jpg"
            rounded="circle"
            class="profile-img"
            alt="Profile photo">
          </b-img>
          <div class="about-cards">
            <b-card
              v-for="blob in blobs_about"
              v-bind:key="blob"
              :title="blob.title"
              tag="article"
              class="md-card">
              <b-card-text class="content">{{ blob.content }}</b-card-text>
            </b-card>
          </div>
        </div>
      </b-tab>
    </b-tabs>
  </div>

  <!-- Footer -->
  <footer class="site-footer">
    <p class="footer-text">Hyunwook Shin &copy; 2026</p>
  </footer>

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
/* ── Page root ─────────────────────────────────────── */
.page-root {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--md-surface-container-low);
}

/* ── Top App Bar ────────────────────────────────────── */
.app-bar {
  position: sticky;
  top: 0;
  z-index: 100;
  background-color: var(--md-surface);
  box-shadow: 0 1px 3px rgba(0,0,0,0.10), 0 2px 6px rgba(0,0,0,0.06);
}
.app-bar-inner {
  max-width: 1100px;
  margin: 0 auto;
  padding: 14px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.app-bar-title {
  font-family: 'Roboto', sans-serif;
  font-size: 1.4rem;
  font-weight: 500;
  letter-spacing: 0.01em;
  color: var(--md-on-surface);
}
.app-bar-actions {
  display: flex;
  gap: 10px;
}

/* ── Tonal Buttons ──────────────────────────────────── */
.tonal-btn,
.tonal-btn.btn-primary {
  background-color: var(--md-primary-container) !important;
  border-color: transparent !important;
  color: var(--md-on-primary-container) !important;
  border-radius: var(--md-shape-full) !important;
  font-family: 'Roboto', sans-serif !important;
  font-weight: 500 !important;
  font-size: 0.875rem !important;
  letter-spacing: 0.01em !important;
  padding: 6px 20px !important;
  transition: box-shadow 0.2s, background-color 0.2s !important;
}
.tonal-btn:hover,
.tonal-btn.btn-primary:hover {
  background-color: #DDD6FF !important;
  box-shadow: var(--md-elev-1) !important;
}

/* ── Hero ───────────────────────────────────────────── */
.hero-container {
  width: 100%;
  overflow: hidden;
  max-height: 200px;
}
.hero-img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  display: block;
}

/* ── Content wrapper ────────────────────────────────── */
.content-wrapper {
  max-width: 1100px;
  margin: 32px auto;
  padding: 0 24px;
  flex: 1;
  width: 100%;
}

/* ── MD3-style Tabs ─────────────────────────────────── */
</style>

<style>
/* Unscoped: override Bootstrap tab styles globally for this component */
.md-tabs .nav-tabs {
  border-bottom: 1px solid var(--md-outline-variant) !important;
  gap: 4px;
}
.md-tabs .nav-tabs .nav-link {
  border: none !important;
  border-radius: 0 !important;
  border-bottom: 3px solid transparent !important;
  color: var(--md-on-surface-variant) !important;
  font-family: 'Roboto', sans-serif !important;
  font-weight: 500 !important;
  font-size: 0.9rem !important;
  letter-spacing: 0.01em !important;
  padding: 12px 20px !important;
  transition: color 0.2s, background-color 0.15s !important;
  background-color: transparent !important;
  margin-bottom: -1px;
}
.md-tabs .nav-tabs .nav-link:hover {
  color: var(--md-primary) !important;
  background-color: rgba(103, 80, 164, 0.08) !important;
  border-radius: 4px 4px 0 0 !important;
}
.md-tabs .nav-tabs .nav-link.active {
  color: var(--md-primary) !important;
  font-weight: 600 !important;
  border-bottom: 3px solid var(--md-primary) !important;
  background-color: transparent !important;
}
.tab-content-area {
  padding-top: 12px !important;
}

/* ── Cards ──────────────────────────────────────────── */
.md-card {
  border-radius: var(--md-shape-lg) !important;
  border: 1px solid var(--md-outline-variant) !important;
  box-shadow: var(--md-elev-1) !important;
  background-color: var(--md-surface) !important;
  overflow: hidden;
  transition: box-shadow 0.2s, transform 0.2s !important;
}
.md-card:hover {
  box-shadow: var(--md-elev-2) !important;
  transform: translateY(-2px);
}
.md-card .card-title {
  font-family: 'Roboto', sans-serif !important;
  font-weight: 600 !important;
  font-size: 1rem !important;
  color: var(--md-on-surface) !important;
  margin-bottom: 0.5rem !important;
}
.md-card .card-footer.card-footer-md {
  background-color: var(--md-surface-container-low) !important;
  border-top: 1px solid var(--md-outline-variant) !important;
  padding: 10px 16px !important;
}
</style>

<style scoped>
/* ── Section intro ──────────────────────────────────── */
.section-intro {
  margin: 8px 0 24px;
}
.section-heading {
  font-family: 'Roboto', sans-serif;
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--md-on-surface);
  margin-bottom: 10px;
}
.section-body {
  font-size: 0.95rem;
  color: var(--md-on-surface-variant);
  line-height: 1.7;
  max-width: 680px;
}

/* ── Cards grid ─────────────────────────────────────── */
.cards-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: flex-start;
}
.cards-grid .md-card {
  flex: 0 1 calc(50% - 10px);
  max-width: 480px;
}
.cards-grid--sm .md-card {
  flex: 0 1 calc(33% - 14px);
  max-width: 320px;
}

/* ── Content text ────────────────────────────────────── */
.content {
  font-family: 'Roboto', sans-serif;
  font-size: 0.9rem;
  color: var(--md-on-surface-variant);
  line-height: 1.65;
}
.meta {
  font-size: 0.78rem;
  font-weight: 500;
  color: var(--md-outline);
  letter-spacing: 0.02em;
  text-transform: uppercase;
}

/* ── Links ───────────────────────────────────────────── */
.md-link {
  color: var(--md-primary) !important;
  text-decoration: none !important;
  font-weight: 500;
}
.md-link:hover {
  text-decoration: underline !important;
}
.footer-link {
  font-size: 0.85rem;
}

/* ── About tab ───────────────────────────────────────── */
.about-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
  padding-top: 16px;
}
.profile-img {
  width: 112px;
  height: 112px;
  object-fit: cover;
  border-radius: 50%;
  box-shadow: var(--md-elev-2);
  border: 4px solid var(--md-surface);
}
.about-cards {
  width: 100%;
  max-width: 700px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

/* ── Footer ──────────────────────────────────────────── */
.site-footer {
  background-color: var(--md-surface-container-high);
  border-top: 1px solid var(--md-outline-variant);
  text-align: center;
  padding: 28px 24px;
  margin-top: 48px;
}
.footer-text {
  font-family: 'Roboto', sans-serif;
  font-size: 0.85rem;
  color: var(--md-on-surface-variant);
  margin: 0;
  letter-spacing: 0.02em;
}

/* ── Responsive ──────────────────────────────────────── */
@media (max-width: 768px) {
  .app-bar-inner {
    padding: 12px 16px;
  }
  .app-bar-title {
    font-size: 1.1rem;
  }
  .content-wrapper {
    padding: 0 16px;
    margin: 20px auto;
  }
  .cards-grid .md-card,
  .cards-grid--sm .md-card {
    flex: 0 1 100%;
    max-width: 100%;
  }
}</style>
