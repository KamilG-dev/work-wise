<template>
    <div class="navbar">
      <div class="navbar-header">
        <h1>Looking for a freelancer?</h1>
      </div>
      <div class="navbar-bottom">
        <button class="button" @click="goToNewOffer">
          + Post Job Offer
        </button>
        <button class="button blue" @click="goToFreelancers">
          Freelancers
        </button>
      </div>
    </div>
</template>

<script lang="ts">

export default {
    name: 'Navbar',
    methods: {
        goToNewOffer() {
            this.$router.push('/offer');
        },
        goToFreelancers() {
            this.$router.push('/freelancer');
        }
    }
}
</script>

<style>
.navbar {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 40px;
}
.navbar-header {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  margin-bottom: 20px;
}
.navbar-bottom {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
}
.navbar-bottom button {
  margin: 0 10px;
}
.button {
  border: none;
  border-radius: 4px;
  padding: 10px 20px;
  background-color: rgb(0, 151, 101);
  cursor: pointer;
}
</style>