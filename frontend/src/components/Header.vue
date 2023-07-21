<template>
    <div :class="{'header': true, 'header-small': size === 'small'}">
        <router-link to="/" :class="{'home-link': true, 'white': color === 'white'}">
            <h1>WorkWise</h1>
            <p>Find the best job opportunities!</p>
        </router-link>
    </div>
</template>

<script lang="ts">
export default {
    name: 'Header',
    props: {
        size: String,
        color: String
    }
}
</script>

<style>
.header {
    font-size: 48px;
    color: #fff;
    padding: 20px;
}
.header-small {
    font-size: 24px;
    color: #fff;
    padding: 10px;
}
.header h1 {
    margin-bottom: 10px;
    letter-spacing: 1ch;
}
.header-small h1 {
    margin-bottom: 5px;
    letter-spacing: 1ch;
}
.white{
    color: #fff !important;
}
.header p {
    font-size: 18px;
    letter-spacing: 1ch;
}
.header-small p {
    font-size: 14px;
    letter-spacing: 1ch;
}
</style>