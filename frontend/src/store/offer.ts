import { defineStore } from 'pinia';
import { type User } from './user';
import { type Freelancer } from '@/components/user/UserProfileContent.vue';

export interface Submission {
    id: number;
    freelancer: Freelancer;
    description: string;
    price: number;
    posted_at: string;
}

export interface Offer {
    id: number;
    title: string;
    description: string;
    posted_at: string;
    price: number;
    author: User;
    submissions: Submission[];
}

export const useOfferStore = defineStore('offer', {
    state() {
        return {
            offers: [] as Offer[]
        }
    },
    actions: {
        setOffers(offers: Offer[]) {
            this.offers = offers;
        },
        updateOffer(offer: Offer) {
            this.offers = this.offers.map(o => o.id === offer.id? offer : o);
        },
        addOffers(offers: Offer[]) {
            this.offers.push(...offers);
        },
        getOffer(id: number) {
            return this.offers.find(offer => offer.id === id);
        }
    },
    persist: true,
});