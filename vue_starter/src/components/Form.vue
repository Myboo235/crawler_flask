<template>
    <div class="p-10">
        <form class="mx-auto text-primary text-white">
        <div class="mb-10 flex flex-col gap-2">
            <label for="title" class="mb-2 text-2xl">Title</label>
            <input type="text" id="title" class="bg-secondary border border-gray-300 rounded-lg placeholder-[#4b3f2f] w-full p-5" placeholder="Your title" v-model="title"/>
        </div>
        <div class="mb-5 flex flex-col gap-2">
            <label class="mb-2 text-2xl" for="image">Upload image</label>

            <input class="w-full rounded-lg cursor-pointer bg-secondary p-5 placeholder-[#4b3f2f]" aria-describedby="image_blog" id="user_avatar" type="text" placeholder="Your image url or file path" v-model="file">

            <div class="mt-1 text-sm text-gray-500 dark:text-gray-300" id="image_blog">A blog picture is useful to attract viewer user </div>
        </div>
        <div class="mb-5 flex flex-col gap-2">
            <label class="mb-2 text-2xl" for="content">Content</label>
            <textarea type="text" id="content" class="rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full p-5 bg-secondary placeholder-[#4b3f2f]" rows="20" placeholder="Your blog go here ..." v-model="content"/>
        </div>
        </form>
        <button class="text-secondary bg-primary border-secondary border-2 hover:text-primary hover:bg-secondary rounded-lg p-4 justify-self-end" @click="onSubmit()">Submit your blog 🚀</button>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const title = ref("")
const file = ref("")
const content = ref("")

const onSubmit = () => {
    console.log(title.value)
    console.log(file.value)
    console.log(content.value)
}
</script>

<style lang="scss" scoped>

</style>