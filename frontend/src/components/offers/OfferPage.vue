<template>
    <div class="container">
        <UserNavbar></UserNavbar>
        <div class="content">
            <div class="offer">
                <div class="offer-header">
                    <div class="offer-header-item">
                        <h1>Title: {{ offer?.title }}</h1>
                    </div>
                    <div class="offer-header-item">
                        <span>Author: {{ offer?.author.display_name }}</span>
                        <span>Posted at: {{ formatDate(offer?.posted_at) }}</span>
                        <span>Price: {{ offer?.price }}</span>
                    </div>

                </div>
                <div class="offer-content offer-element">
                    <p>
                        {{ offer?.description }}
                    </p>
                </div>
                <div class="offer-submissions offer-element">
                    <h2>Submissions: {{ offer?.submissions.length }}</h2>
                    <div v-for="submission in offer?.submissions" :key="submission.id" class="submission">
                            <div class="submission-header">
                                <div class="submission-header-item">
                                    <router-link :to="{path: '/freelancer/' + submission.freelancer.user_id}"> <h3>{{ submission.freelancer.display_name }}</h3></router-link>
                                </div>
                                <div class="submission-header-item">
                                    <span>Posted at: {{ formatDate(submission.posted_at) }}</span>
                                    <span>Price: {{ submission.price }}</span>
                                </div>
                            </div>
                            <div class="submission-content">
                                <p>
                                    {{ submission.description }}
                                </p>
                            </div>
                    </div>
                </div>
                <div class="post-submission offer-element">
                    <div class="post-submission-header">
                        <h1>Post a new submission</h1>
                    </div>
                    <div class="post-submission-content">
                        <textarea name="submission-content" id="submission-content" cols="30" rows="10"
                            v-model="subcontent"></textarea>
                        <div class="post-submission-side">
                            <div class="input-group">
                                <label for="price"><h3>Price</h3></label>
                                <input type="number" step="0.1" name="price" v-model="subprice">
                            </div>

                            <button class="button" @click="postSubmission">Submit</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import api from '@/api';
import UserNavbar from '../user/UserNavbar.vue';
import { useOfferStore, type Offer } from '@/store/offer';

export default {
  name: 'OfferPage',
  components: {
    UserNavbar
  },
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      offerId: this.id,
      offer: null as Offer | null,
      subcontent: '',
      subprice: 0.0
    };
  },
  methods: {
    formatDate(date: string | undefined): string {
        if(!date){
            return '';
        }
      const options: Intl.DateTimeFormatOptions = {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      };
      return new Date(date).toLocaleDateString(undefined, options);
    },
    postSubmission() {
      if (this.subcontent.length > 0) {
        api
          .post(`/submission/${this.offerId}`, {
            description: this.subcontent,
            price: this.subprice
          })
          .then(response => {
            console.log(response);
            this.subcontent = '';
            this.subprice = 0;
            this.updateOffer();
          })
          .catch(error => {
            console.log(error);
          });
      }
    },
    updateOffer() {
      api
        .get(`/offer/${this.offerId}`)
        .then(response => {
          const offer = response.data as Offer;
          useOfferStore().updateOffer(offer);
          this.offer = offer;
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  created() {
    this.updateOffer();
  }
};

</script>

<style>
.offer {
    display: flex;
    flex-direction: column;
    align-items: baseline;
    width: 100%;
    height: 100%;
}

.offer-element {
    padding-bottom: 40px;
    margin-bottom: 10px;
    border-bottom: 1px solid white;
    width: 100%;
}

.offer-header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    
    padding-bottom: 40px;
    margin-bottom: 10px;
    width: 100%;
}

.offer-header-item {
    display: flex;
    flex-direction: column;
}

.offer-header-item span {
    text-align: right;
}

.offer-content {
    display: flex;
    font-size: 18px;
    text-align: start;
}

.offer-submissions {
    display: flex;
    flex-direction: column;
    align-items: baseline;
    width: 100%;
}
.submission {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    border: 1px solid white;
    width: 100%;
    padding: 24px;
    margin-top: 20px;
}
.submission-header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 20px;
}
.submission-header-item{
    display: flex;
    flex-direction: column;
}
.submission-header-item span {
    text-align: right;
}
.submission-content {
    display: flex;
    align-items: baseline;
    width: 100%;
}
.post-submission {
    display: flex;
    flex-direction: column;
    align-items: baseline;
}

.post-submission-header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 20px;
}

.post-submission-content {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
}
.post-submission-side {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.post-submission textarea {
    resize: none;
    width: 80%;
    background-color: #222222;
    color: white;
    font-size: 18px;
}
.input-group {
    display: flex;
    flex-direction: column;
}
.input-group input {
    background-color: #222222;
    color: white;
    padding: 6px;
}
</style>