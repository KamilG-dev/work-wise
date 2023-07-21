<template>
    <div class="register">
        <div class="header-container">
            <Header />
        </div>
        <h1>Register</h1>
        <RegistrationForm v-if="!registered" @register-success="handleRegisterSuccess" />
        <RegistrationSuccess v-else />
    </div>
</template>

<script lang="ts">
import Header from '@/components/Header.vue'
import RegistrationForm from '@/components/register/RegistrationForm.vue'
import RegistrationSuccess from '@/components/register/RegistrationSuccess.vue'

export default {
    name: 'Register',
    components: {
        Header,
        RegistrationForm,
        RegistrationSuccess
    },
    data() {
        return {
            registered: false
        }
    },
    methods: {
        handleRegisterSuccess() {
            this.registered = true
        }
    }
}
</script>

<style>
.register {
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

.register form {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 300px;
    margin-bottom: 20px;
}

.register h1 {
    letter-spacing: 1ch;
    margin-bottom: 30px;
}

.register .form-group {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    margin-bottom: 10px;
}

.register label {
    font-size: 16px;
    margin-bottom: 5px;
}

.register input {
    width: 100%;
    padding: 8px;
    border-radius: 4px;
    border: 1px solid #ddd;
    background-color: #222222;
    color: #fff;
    margin-bottom: 12px;
}

.register button {
    padding: 10px 20px;
    background-color: #e67e22;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.register button:hover {
    background-color: #d35400;
}

.register p {
    font-size: 14px;
    margin-top: 10px;
}

.register p router-link {
    color: #e67e22;
    text-decoration: underline;
}

.error {
    color: red;
}
.success {
    color: green;
}
</style>