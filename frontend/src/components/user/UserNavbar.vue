<template>
    <div class="top-navbar">
        <div class="top-navbar-left">
            <Header size="small" color="white" />
        </div>
        <div class="top-navbar-right">
            <div class="navbar-vert">
                <router-link to="/profile" class="profile-link"> {{ user.username }} </router-link>
                <button @click="submitLogout" class="navbar-button">Log out</button>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import api from '@/api';
import { useUserStore } from '@/store/user';

import Header from '@/components/Header.vue';

export default {
    name: 'UserNavbar',
    components: {
        Header
    },
    computed: {
        user() {
            const userStore = useUserStore();
            return userStore.user!;
        }
    },
    methods: {
        submitLogout() {
            api.delete(`/login/${this.user.id}`)
                .then((response) => {
                    console.log(response.data);
                })
                .catch((error) => {
                    console.log(error);
                });
            const userStore = useUserStore();
            userStore.logout();
            this.$router.push('/');
        }
    }
}

</script>
<style>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    min-height: 100vh;
    text-align: center;
    color: white;
}

.top-navbar {
    background-color: hsla(160, 100%, 37%, 1);
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 1rem;
}

.navbar-button {
    background-color: #222222;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    cursor: pointer;
}

.navbar-button:hover {
    background-color: #121212;
}

.navbar-vert {
    display: flex;
    height: 100%;
    flex-direction: column;
    justify-content: space-around;
}

.profile-link {
    color: white;
    font-size: 1.5rem;
    text-decoration: none;
}

.profile-link:hover {
    text-decoration: underline;
    cursor: pointer;
}</style>