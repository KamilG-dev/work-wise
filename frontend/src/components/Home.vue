<template>
    <HomeGuest v-if="!isLoggedIn"/>
    <HomeUser v-else/>
</template>
  
<script lang="ts">
import HomeGuest from '@/components/home/HomeGuest.vue';
import HomeUser from '@/components/home/HomeUser.vue';

import { useUserStore } from '@/store/user';

export default {
    name: 'Home',
    components: {
        HomeGuest,
        HomeUser,
    },
    computed: {
        isLoggedIn() {
            const userStore = useUserStore();
            return userStore.isLoggedIn;
        },
        user() {
            const userStore = useUserStore();
            return userStore.user!;
        },
    },
};
</script>
  
