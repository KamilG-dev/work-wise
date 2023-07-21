<template>
    <div class="home">
        <Header></Header>
        <div class="content">
            <div class="blocks">
                <div class="block">
                    <h2>About Us</h2>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Maiores alias dignissimos enim ex dolores
                        excepturi sed, aliquid, commodi impedit aut quasi magnam labore et accusamus blanditiis a
                        perspiciatis atque mollitia?
                        Nemo, unde? Obcaecati asperiores eos error odit, soluta animi, aspernatur amet excepturi doloribus,
                        reiciendis iure nam suscipit sed accusantium nobis beatae maiores omnis id fugit nulla corporis.
                        Rem, amet eaque!
                        Odio accusamus itaque, officia ex laborum exercitationem, neque sint facilis nulla harum molestias
                        delectus aspernatur perspiciatis ipsam dolorem non fugiat! Fuga minima temporibus sequi numquam,
                        consequuntur suscipit cum pariatur consectetur.
                        Expedita rem consequatur eligendi, earum soluta voluptas porro sint impedit adipisci amet sit nobis
                        tempore assumenda delectus cupiditate, reiciendis voluptatibus blanditiis cumque temporibus?
                        Asperiores, officia. Neque impedit doloremque itaque laudantium.
                        Recusandae culpa adipisci nihil voluptate magnam provident delectus aut, natus placeat corrupti
                        temporibus ipsa harum sint animi molestiae commodi aspernatur assumenda eligendi aperiam totam.
                        Dolore culpa fuga ad iste dolor!</p>
                </div>
                <div class="block">
                    <h2>Latest Job Offers</h2>
                    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laudantium harum deleniti architecto
                        recusandae sequi earum, obcaecati quis dolorem, sed quibusdam officiis doloribus quisquam repellat
                        tenetur porro at blanditiis nihil mollitia?
                        Quam distinctio eius ab iusto dolorum! Recusandae corporis perferendis doloribus animi ab reiciendis
                        cupiditate perspiciatis aperiam harum, accusamus voluptatum accusantium similique nemo id ad neque
                        aliquid ratione in natus consectetur?
                        Quasi, harum illo placeat, quis nostrum consectetur error voluptatem aliquid ab cum quidem saepe
                        enim esse ratione atque aperiam inventore provident sit ea. Fugit eos harum a soluta similique
                        numquam.
                        Quae non voluptatum recusandae. Iusto similique, deserunt commodi placeat temporibus voluptatum
                        adipisci saepe reprehenderit reiciendis quod animi rem obcaecati laudantium natus perferendis
                        ducimus molestiae. Ex maxime sunt quidem voluptatem cumque?
                        Harum neque veritatis culpa repudiandae nemo vel provident fugit, rerum in inventore officiis
                        excepturi pariatur a, earum dignissimos quis id aperiam ipsa doloremque animi ex ea! Reprehenderit
                        fuga eos nemo.</p>
                </div>
                <div class="block">
                    <h2>Join us today!</h2>
                    <div class="join-buttons">
                        <router-link to="/login" class="cta-button">Login</router-link>
                        <router-link to="/register" class="cta-button">Register</router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import Header from '@/components/Header.vue';

export default {
    name: 'HomeGuest',
    components: {
        Header,
    }
};

</script>

<style>
.home {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    min-height: 100vh;
    text-align: center;
    width: 100%;
}


.content {
    flex-grow: 1;
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.home h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

.blocks {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}

.block {
    margin-top: 50px;
    box-sizing: border-box;
    width: 100%;
    margin-bottom: 50px;
    /* Add margin-bottom between blocks */
}

.join-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 20px;
}

.join-buttons {
    align-content: center;
    gap: 10px;
}

.cta-button {
    display: inline-block;
    padding: 10px 20px;
    margin: 10px;
    background-color: #e67e22;
    color: #fff;
    text-decoration: none;
    border-radius: 4px;
    transition: background-color 0.3s ease;
}

.cta-button:hover {
    background-color: #d35400;
}
</style>
