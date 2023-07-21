import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import Home from './components/Home.vue';
import Login from './components/Login.vue';
import Register from './components/register/Register.vue';
import UserProfile from '@/components/user/UserProfile.vue';
import NewOffer from '@/components/offers/NewOffer.vue';
import OfferPage from '@/components/offers/OfferPage.vue';
import FreelancerProfile from '@/components/user/FreelancerProfile.vue';
import FreelancerView from '@/components/user/FreelancerView.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/register',
      name: 'Register',
      component: Register,
    },
    {
      path: '/profile',
      name: 'Profile',
      component: UserProfile
    },
    {
      path: '/offer',
      name: 'Offer',
      component: NewOffer
    },
    {
      path: '/offer/:id',
      name: 'OfferPage',
      component: OfferPage,
      props: route => ({ id: Number(route.params.id) })
    },
    {
      path: '/freelancer',
      name: 'FreelancerView',
      component: FreelancerView,
    },
    {
      path: '/freelancer/:id',
      name: 'FreelancerProfile',
      component: FreelancerProfile,
      props: route => ({ id: Number(route.params.id) })
    }
],

});
export default router;