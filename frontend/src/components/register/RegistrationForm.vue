<template>
    <div>
        <form @submit.prevent="register">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" v-model="username" />
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" v-model="email" />
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" v-model="password" />
            </div>
            <div class="form-group">
                <label for="confirm-password">Confirm Password</label>
                <input type="password" id="confirm-password" v-model="confirmPassword" />
            </div>
            <button type="submit">Register</button>
        </form>
        <p>Already have an account? <router-link to="/login">Sign in</router-link></p>
        <p v-if="error" class="error">{{ error }}</p>
    </div>
</template>

<script lang="ts">
import api from '@/api';

export default {
    name: 'RegistrationForm',
    data() {
        return {
            username: '',
            email: '',
            password: '',
            confirmPassword: '',
            error: '',
            registered: false,
        };
    },
    methods: {
        register() {
            if (this.password !== this.confirmPassword) {
                // Password and Confirm Password don't match, handle error
                return;
            }

            const userData = {
                username: this.username,
                email: this.email,
                password: this.password,
            };

            api
                .post(`/register`, userData)
                .then((response) => {
                    console.log(response);
                    this.$emit('register-success')
                })
                .catch((error) => {
                    console.error(error);
                    if (error.response && error.response.data && error.response.data.message) {
                        this.error = error.response.data.message; // Set the error message from the response
                    } else {
                        this.error = 'Registration failed. Please try again later.';
                    }
                });
        },
    },
}

</script>
