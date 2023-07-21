<template>
    <div class="container">
        <UserNavbar />
        <Navbar />
        <div class="content">
            <div v-for="freelancer in freelancers" :key="freelancer.id" class="card" @click="goToFreelancer(freelancer.user_id)">
                <div class="card-body">
                    <div class="card-image">
                        <img :src="imagePath(freelancer.profile_pic)" alt="avatar">
                    </div>
                    <div class="card-title">
                        {{ freelancer.display_name }}
                    </div>
                    <div class="card-description">
                        {{ freelancer.description.substring(0, 300) }}
                        <span v-if="freelancer.description.length > 300">...</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import api from '@/api';
import UserNavbar from './UserNavbar.vue';
import Navbar from '@/components/Navbar.vue';
import { type Freelancer } from '@/components/user/UserProfileContent.vue'
import { imagePath } from '@/image';

export default {
    name: 'FreelancerView',
    components: {
        UserNavbar,
        Navbar
    },
    data() {
        return {
            freelancers: [] as Freelancer[],
        }
    },
    methods: {
        imagePath,
        getFreelancers() {
            api.get(`/freelancer`)
                .then(response => {
                    this.freelancers = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },
        goToFreelancer(user_id: number) {
            this.$router.push({
                path: `/freelancer/${user_id}`
            });
        }    
    },
    created() {
        this.getFreelancers();
    }

}
</script>

<style>
.card {
    display: flex;
    flex-direction: row;
    width: 100%;
    margin: 10px;
    background-color: #222222;
    cursor: pointer;
}
.card-image {
    flex: 1;
}
.card-image img {
    max-width: 100%;
    max-height: 100%;
    object-fit: cover; /* Maintain aspect ratio and cover the entire .card-image */
}
.card-name {
    width: 20%;
    height: 100%;
    text-align: left;
    background-color: #333333;
    padding: 20px;
    display: flex;
    justify-content: center;
    align-self: center;
}

.card-description {
    width: 80%;
    text-align: left;
    margin: 20px;
    height: 100%;
}
</style>