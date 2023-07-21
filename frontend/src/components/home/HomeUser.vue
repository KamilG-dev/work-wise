<template>
  <div class="container">
    <UserNavbar />
    <Navbar />
    <OffersView />
  </div>
</template>
  
<script lang="ts">
import { useUserStore, type User } from '@/store/user';
import Header from '@/components/Header.vue';
import UserNavbar from '@/components/user/UserNavbar.vue';
import Navbar from '../Navbar.vue';
import OffersView from '../offers/OffersView.vue';

export default {
  name: 'HomeUser',
  components: {
    Header,
    UserNavbar,
    Navbar,
    OffersView
  },
  
  computed: {
    user() {
      const userStore = useUserStore();
      return userStore.user!;
    },
  },
  

};
</script>

<style>

.button {
  border: none;
  border-radius: 4px;
  padding: 10px 20px;
  background-color: rgb(0, 151, 101);
  cursor: pointer;
}
.blue{
  background-color: rgb(0, 151, 201);
}

</style>