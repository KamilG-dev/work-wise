<template>
    <div class="image-uploader">
        <label for="file-input" class="file-input-label">
            <span v-if="!selectedFile">Choose an Image</span>
            <span v-else>Selected: {{ selectedFile.name }}</span>
            <input id="file-input" type="file" @change="onFileChange" accept="image/*" ref="fileInput">
        </label>
        <button @click="uploadImage" :disabled="!selectedFile" class="button">Upload</button>
        <div class="image-preview" v-if="selectedFile">
            <img :src="imageUrl" alt="Selected Image">
        </div>
    </div>
</template>
  
<script lang="ts">
import api from '@/api';

export default {
    name: 'ImageUploader',
    data() {
        return {
            selectedFile: null as null | File,
            imageUrl: '',
        };
    },
    methods: {
        onFileChange(event: Event) {
            const inputElement = event.target as HTMLInputElement;
            if (inputElement.files && inputElement.files.length > 0) {
                this.selectedFile = inputElement.files[0];
                this.imageUrl = URL.createObjectURL(this.selectedFile);
            }
        },
        uploadImage() {
            if (!this.selectedFile) {
                alert('Please select an image before uploading.');
                return;
            }

            const formData = new FormData();
            formData.append('file', this.selectedFile);

            api.post('/image', formData)
                .then(response => {
                    console.log(response);
                    this.$emit('uploaded', response);
                })
                .catch(error => {
                    console.error(error);
                });
        },
    },
};
</script>
  
<style lang="scss">
.image-uploader {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
}

.file-input-label {
    display: inline-block;
    padding: 1rem 2rem;
    border: 2px solid #007bff;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.2s;
}

.file-input-label:hover {
    background-color: #f2f2f2;
}

.file-input-label input[type="file"] {
    display: none;
}

.image-preview {
    width: 300px;
    height: 300px;
    overflow: hidden;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.image-preview img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>
  