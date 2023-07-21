<template>
<div class="content">
      <div class="block">
        <h1>Latest job offers</h1>
        <div v-for="offer in offers" :key="offer.id">
          <div class="card" @click="goToOffer(offer.id)">
            <div class="card-body">
              <div class="card-content">
                <div class="card-title">{{ offer.title }}</div>
                <p class="card-description">
                    {{ offer.description.substring(0, 300) }}
                    <span v-if="offer.description.length > 300">...</span>
                </p>
              </div>
            </div>
            <div class="card-meta">
              <small class="text-muted">{{ offer.author.display_name }}</small>
              <small class="text-muted">{{ formatDate(offer.posted_at) }}</small>
              <small class="text-muted">Submissions: {{ offer.submissions.length }}</small>
              <span class="card-price">Price: {{ offer.price }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>     
</template>

<script lang="ts">
import api from '@/api';
import { type Offer, type Submission, useOfferStore } from '@/store/offer';
import type { User } from '@/store/user';


export default {
    name: 'Offers',
    data() {
    return {
      offers: [] as Offer[],
    }
  },
  methods: {
    formatDate(date: string): string {
      const options: Intl.DateTimeFormatOptions = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
      };
      return new Date(date).toLocaleDateString(undefined, options);
    },
    goToOffer(id: number) {
      this.$router.push(`/offer/${id}`);
    },
    loadOffers() {
      api.get('offer')
        .then(response => {
          this.offers = [];
          response.data.forEach((element: any) => {
            this.offers.push({
              id: element.id,
              title: element.title,
              description: element.description,
              posted_at: element.posted_at,
              price: element.price,
              author: element.author as User,
              submissions: element.submissions as Submission[]
            });
          });
          useOfferStore().setOffers(this.offers);
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  mounted() {
    this.loadOffers();
  }
}

</script>

<style>
.card {
  width: 100%;
  background-color: #222222;
  padding: 24px;
  margin-top: 20px;
  display: flex;
  flex-direction: row;
  /* Set flex-direction to row */
  cursor: pointer;
}

.card:hover {
  background-color: #333333;

}
.card-content {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.card-title {
  font-weight: bold;
  margin-right: 10px;
  align-self: flex-start;
  /* Align the title to the top left corner */
  margin-bottom: 10px;
}

.card-body {
  display: flex;
  flex-grow: 1;
}

.card-description {
  text-align: left;
}

.card-meta {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  /* Align the meta content to the bottom */
  align-items: flex-end;
  flex-shrink: 0;
  /* Align the meta content to the right */
}

.card-meta small {
  margin-bottom: 5px;
}
</style>