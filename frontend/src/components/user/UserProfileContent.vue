<template>
    <div class="user-profile-content">
        <!-- Tab navigation -->
        <div class="tab-navigation">
            <div v-for="(tab, index) in tabs" :key="index"
                :class="{ active: activeTab === tab, disabled: activeTab !== tab }" @click="activeTab = tab"
                class="tab-item">
                {{ tab }}
            </div>
        </div>

        <!-- Content section -->
        <div class="content-section">
            <div v-if="activeTab === 'Freelancer'" class="tab-content">          
                <div class="tab-main-content">
                    <div class="display-name">
                        <h1>Display name</h1>
                        <input type="text" name="display_name" class="big-input" v-model="name">
                        <button v-if="diff()" class="button">Apply</button>
                    </div>
                    <h1 v-if="freelancer">Your Freelancer Profile</h1>
                    <h1 v-else>
                        Create your freelancer profile to start posting submissions for offers.
                    </h1>
                    <div class="form-group">
                        <label for="description">Description:</label>
                        <textarea name="description" id="description" cols="30" rows="10" v-model="description"></textarea>
                    </div>
                    <div class="form-group">
                        <label for="skills">Skills:</label>
                        <input type="text" name="skills" id="skills" v-model="skills">
                    </div>
                    <div class="form-group">
                        <button class="button blue mt-5" @click="save_freelancer()">Save</button>
                    </div>
                </div>
            </div>
            <div v-if="activeTab === 'Pictures'" class="tab-content">
                <div class="tab-cols-content">
                    <div class="tab-col">
                        <div class="upload-pic">
                            <h2>Upload picture</h2>
                            <ImageUploadForm @uploaded="load_images"/>
                        </div>
                    </div>
                <div class="tab-col">
                    <h2>Chose profile picture</h2>
                    <div class="images-container">
                        <div v-for="image in images" :key="image.id" class="image-item">
                            <img :src="imagePath(image.url)">
                            <button class="button red" @click="remove_image(image.id)">Remove</button>
                        </div>
                    </div>
                </div>
                </div>
            </div>
            <div v-if="activeTab === 'Messages'" class="tab-content">
                f<!-- User activity history content -->
            </div>
        </div>
    </div>
</template>
  
<script lang="ts">
import api from '@/api';
import { useUserStore } from '@/store/user';
import ImageUploadForm from '../ImageUploadForm.vue';
import { imagePath, type Image } from '@/image';

export interface Freelancer {
    id: number;
    user_id: number
    description: string;
    display_name: string;
    skills: string;
    profile_pic: string;
}

export default {
    name: 'UserProfileContent',
    components: {
        ImageUploadForm
    },
    data() {
        return {
            tabs: ['Freelancer', 'Pictures', 'Messages'],
            activeTab: 'Freelancer',
            freelancer: null as Freelancer | null,
            images: [] as Image[],
            skills: '',
            description: '',
            name: ''
        }
    },
    computed: {
        user() {
            const userStore = useUserStore();
            return userStore.user!;
        }
    },
    mounted() {
        this.load_freelancer();
        this.name = this.user?.display_name;

        this.load_images();
    },
    methods: {
        imagePath,
        load_freelancer() {
            api.get(`freelancer/${this.user.id}`)
                .then(response => {
                    this.freelancer = response.data as Freelancer;
                    this.skills = this.freelancer!.skills;
                    this.description = this.freelancer!.description;
                })
                .catch(error => {
                    console.log(error);
                    if (error.response.status === 404) {
                        this.freelancer = null;
                    }
                });
        },
        save_freelancer() {
            api.post(`freelancer/${this.user.id}`,
                {
                    description: this.description,
                    skills: this.skills,
                }).
                then(response => {
                    console.log(response.data);
                    this.load_freelancer();
                })
                .catch(error => {
                    console.log(error);
                });
        },
        load_images() {
            api.get(`user/${this.user.id}/images`)
              .then(response => {
                    this.images = response.data;
                })
              .catch(error => {
                    console.log(error);
                });
        },
        remove_image(id: number) {
            api.delete(`image/${id}`)
            .then(response => {
                this.load_images();
            })
            .catch(error => {
                console.log(error);
            })
        },
        diff() {
            return this.name !== this.freelancer?.display_name;
        }
    }
}
</script>
  
<style>
.red {
    background-color: red;
}
h2 {
    margin-bottom: 20px;
}
.user-profile-content {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    height: 100%;
    width: 100%;
}

.tab-navigation {
    display: flex;
    background-color: #181818;
    border-radius: 25px 25px 0 0;
}

.tab-navigation .tab-item {
    flex: 1;
    padding: 16px;
    text-align: center;
    cursor: pointer;
    margin-right: 20px;
    /* Add spacing between tabs */
}

.tab-navigation .tab-item:last-child {
    margin-right: 0;
    /* Remove margin from the last tab */
}

.tab-navigation>div {
    flex: 1;
    padding: 16px;
    text-align: center;
    cursor: pointer;
    border-radius: 25px 25px 0 0;
}

.tab-navigation>div.active {
    background-color: #282828;
    font-weight: bold;
    border-radius: 25px 25px 0 0;
}

.tab-navigation>div.disabled {
    background-color: #d8d8d8;
    color: #777777;
}
.tab-content h1{
    font-size: 48px;
    font-weight: bold;
}
.tab-main-content {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    width: 90%;
    margin: 0 auto;
    margin-top: 20px;
}
.tab-cols-content {
    display: flex;
    flex-direction: row;
    width: 100%;
    margin-top: 20px;
}
.tab-col {
    width: 50%;
}
.display-name {
    display: flex;
    flex-direction: row;
    width: 100%;
    justify-content: center;
    align-items: center;
    margin-bottom: 40px;
    border-bottom: 1px solid white;
}
.display-name *{
    margin: 0 10px;
}
.tab-main-content label {
    font-size: large;
}

.content-section {
    flex-grow: 1;
    background-color: #282828;
    border-radius: 0 0 8px 8px;
    padding: 16px;
    height: 100%;
}

#description {
    resize: none;
    font-size: 24px;
}

#skills {
    font-size: 24px;
}

.save-button {
    width: fit-content;
    padding: 12px 24px;
    margin-top: 20px;
    font-size: 24px;
    background-color: blue;
    border: none;
    border-radius: 4px;
}

.save-button:hover {
    background-color: #00a2ff;
    cursor: pointer;
}
.big-input {
    padding: 12px 0px;
    font-size: 24px;
}

.form-group {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.form-group textarea, .form-group input {
    background-color: #222222;
    color: white;
    width: 100%;
}
input {
    background-color: #222222;
    color: white;
}
.form-group * {
    margin-bottom: 10px;
}
.images-container {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}
.image-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    margin: 0 10px;
}
.image-item img{
    width: 160px;
    height: 160px;
}
</style>
  