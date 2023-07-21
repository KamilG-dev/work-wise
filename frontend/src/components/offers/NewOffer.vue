<template>
    <div class="container">
        <UserNavbar></UserNavbar>
        <OfferForm v-if="isLoggedIn"></OfferForm>
        <div v-else>
            <h1>You need to be logged in to post new job offer.</h1>
            <router-link to="/login">Sign in</router-link>
        </div>
    </div>
</template>

<script lang="ts">
import OfferForm from './OfferForm.vue';
import UserNavbar from '@/components/user/UserNavbar.vue';
import { useUserStore } from '@/store/user';

export default {
    name: 'NewOffer',
    components: {
        OfferForm,
        UserNavbar
    },
    data() {
        return {
        }
    },
    computed: {
        user() {
            const userStore = useUserStore();
            return userStore.user!;
        },
        isLoggedIn() {
            const userStore = useUserStore();
            return userStore.isLoggedIn;
        },
    }
}
</script>

<style>

</style>