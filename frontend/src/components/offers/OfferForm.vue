<template>       
<div class="container">
    <form v-on:submit.prevent="postOffer()">
        <div class="form-group">
            <label for="name">Title</label>
            <input type="text" class="form-control" id="name" v-model="offer.title">
        </div>
        <div class="form-group">
            <label for="price">Price</label>
            <input type="text" class="form-control" id="price" v-model="offer.price">
        </div>
        <div class="form-group">
            <label for="description">Description</label>
            <textarea class="form-control" id="description" rows="3" v-model="offer.description"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</div>
</template>

<script lang="ts">
import { useUserStore } from '@/store/user';
import api from '@/api';

export default {
    name: 'OfferForm',
    data() {
        return {
            offer: {
                title: '',
                description: '',
                price: 0,
            },
        }
    },
    computed: {
        user() {
            const userStore = useUserStore();
            return userStore.user!;
        },
    },
    methods: {
        postOffer() {
            api.post('offer', this.offer)
            .then(response => {
                console.log(response);
            })
            .catch(error => {
                console.log(error);
            });
        }
    }
}
</script>

<style>

</style>