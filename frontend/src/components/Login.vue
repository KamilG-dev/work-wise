<template>
    <div class="login">
        <div class="header-container">
            <Header />
        </div>
        <h1>Login</h1>
        <form @submit.prevent="submitLogin">
            <div class="form-group">
                <label for="login">Username or Email</label>
                <input type="text" id="login" v-model="login" />
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" v-model="password" />
            </div>
            <button type="submit">Login</button>
        </form>
        <p>Don't have an account? <router-link to="/register">Sign up</router-link></p>
        <p v-if="error" class="error">{{ error }}</p>
    </div>
</template>
  
<script lang="ts">
import Header from '@/components/Header.vue';
import { useUserStore } from '@/store/user';
import { setAuthHeader } from '@/api';
import api from '@/api';

export default {
    name: 'Login',
    data() {
        return {
            login: '',
            password: '',
            error: ''
        };
    },
    components: {
        Header,
    },
    methods: {
        submitLogin() {
            const userStore = useUserStore();

            api.post(`/login`, {
                login: this.login,
                password: this.password,
            }).then((response) => {
                if (response.status === 200) {
                    userStore.setAccessToken(response.data.access_token);
                    userStore.setUser(response.data.user);
                    setAuthHeader(userStore.accessToken);
                    this.$router.push('/');
                }
            }).catch((error) => {
                console.error(error);
                this.error = error.response.data.message;
            });
        }
    }
};
</script>
  
<style>
.login {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    text-align: center;
}

.header-container {
    margin-bottom: 30px;
}

.login form {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 300px;
    margin-bottom: 20px;
}

.login h1 {
    letter-spacing: 1ch;
    margin-bottom: 30px;
}

.login .form-group {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-bottom: 10px;
}

.login label {
    font-size: 16px;
    margin-bottom: 5px;
}

.login input {
    width: 100%;
    padding: 8px;
    border-radius: 4px;
    border: 1px solid #ddd;
    background-color: #222222;
    color: #fff;
    margin-bottom: 12px;
}

.login button {
    padding: 10px 20px;
    background-color: #e67e22;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.login button:hover {
    background-color: #d35400;
}

.login p {
    font-size: 14px;
    margin-top: 10px;
}

.login p router-link {
    color: #e67e22;
    text-decoration: underline;
}
.error {
    color: red;
}
</style>
  