<template>
    <div class="container">
        <UserNavbar />
        <div class="content">
            <UserProfileContent />
        </div>
    </div>
</template>


<script lang="ts">
import UserNavbar from '@/components/user/UserNavbar.vue'
import UserProfileContent from './UserProfileContent.vue';
import { useUserStore } from '@/store/user';

export default {
    name: 'UserProfile',
    components: {
        UserNavbar,
        UserProfileContent
    },
    computed: {
        user() {
            const userStore = useUserStore();
            return userStore.user!;
        }
    }
};
</script>


<style></style>