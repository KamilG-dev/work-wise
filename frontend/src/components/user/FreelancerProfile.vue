<template>
    <div class="container">
        <UserNavbar />
        <Navbar />
        <div class="content">
            <div class="freelancer">
                <div class="freelancer-header">
                    <h1>{{ freelancer.display_name }}</h1>
                </div>
                <div class="freelancer-content">
                    <p>
                        {{ freelancer.description }}
                    </p>
                    <p>
                        Skills: {{ freelancer.skills }}
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import api from '@/api';
import UserNavbar from './UserNavbar.vue';
import Navbar from '../Navbar.vue';
import { type Freelancer } from '@/components/user/UserProfileContent.vue'

export default {
    name: 'FreelancerProfile',
    props: {
        id: {
            type: Number,
            required: true
        }
    },
    components: {
        UserNavbar,
        Navbar
    },
    data() {
        return {
            freelancer_id: this.id,
            freelancer: {} as Freelancer
        }
    },
    methods: {
        getFreelancer() {
            api.get(`/freelancer/${this.freelancer_id}`)
                .then(response => {
                    this.freelancer = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
        }
    },
    created() {
        this.getFreelancer();
    }

}
</script>

<style>
.freelancer {
    display: flex;
    flex-direction: column;
    align-items: baseline;
    width: 100%;
    height: 100%;
}
.freelancer-header {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100px;
    border-bottom: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 10px;
    font-size: 36px;
    font-weight: bold;
    text-transform: uppercase;
}
.freelancer-content {
    display: flex;
    flex-direction: column;
    align-items: baseline;
    text-align: left;
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    font-size: 24px;
    font-weight: normal;
    line-height: 1.5;
}
.freelancer-content p {
    border-bottom: 1px solid white;
    padding-bottom: 40px;
    margin-bottom: 10px;
    width: 100%;
}
</style>