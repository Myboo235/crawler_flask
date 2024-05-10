<template>
    <div class="fixed w-full px-[1rem] top-10" v-if="error_msg !== 'none' ">
        <fwb-alert border type="danger">
            {{ error_msg }}
          </fwb-alert>
    </div>
    <div class="p-10">
        <form class="mx-auto text-primary text-white">
        <div class="mb-10 flex flex-col gap-2">
            <label for="title" class="mb-2 text-2xl">Title</label>
            <input type="text" id="title" class="bg-secondary border border-gray-300 rounded-lg placeholder-[#4b3f2f] w-full p-5" placeholder="Your title" v-model="title"/>
        </div>
        <div class="mb-5 flex flex-col gap-2">
            <label class="mb-2 text-2xl" for="image">Upload image</label>

            <textarea class="w-full rounded-lg cursor-pointer bg-secondary p-5 placeholder-[#4b3f2f]" aria-describedby="image_blog" id="user_avatar" type="text" placeholder="Your image url or file path" v-model="imgs" />

            <div class="mt-1 text-sm text-gray-500 dark:text-gray-300" id="image_blog">A blog picture is useful to attract viewer user, each url image split by a `enter`</div>
        </div>
        <div class="mb-5 flex flex-col gap-2">
            <label class="mb-2 text-2xl" for="content">Content</label>
            <textarea type="text" id="content" class="rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full p-5 bg-secondary placeholder-[#4b3f2f]" rows="20" placeholder="Your blog go here ..." v-model="content"/>
        </div>
        </form>
        <button class="text-secondary bg-primary border-secondary border-2 hover:text-primary hover:bg-secondary rounded-lg p-4 justify-self-end" @click="onSubmit()" v-if="props.type !== 'update'" > 
            Submit your blog 🚀
        </button>
        <button class="text-secondary bg-primary border-secondary border-2 hover:text-primary hover:bg-secondary rounded-lg p-4 justify-self-end" @click="onSubmit()" v-else> 
            Update your blog 🚀
        </button>

    </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue'
import { useRoute , useRouter } from 'vue-router'
import { FwbAlert } from 'flowbite-vue'

const route = useRoute()
const router = useRouter()
const title = ref("")
const imgs = ref("")
const content = ref("")
const error_msg = ref("none")

const id = (route.params.id)
const props = defineProps(["type"])
console.log(props.type)

if(props.type === "update"){
    axios.get(`http://localhost:5000/${id}`)
    .then(response => {
          const responseData = response.data;
          console.log(response.data)
          title.value = responseData.title;
          content.value = responseData.content.join("\n");
          imgs.value = responseData.img.join("\n");



          console.log(imgs.value);
    })
        .catch(error => {
          console.error('Error fetching data:', error);
    });
}

const onSubmit = () => {
    let self = this;
    console.log(title.value)
    console.log(imgs.value.split("\n"))
    console.log(content.value.split("\n"))
    if (props.type === "update"){
        axios.post('http://localhost:5000/update',{
        "_id" : id,
        "title" : title.value,
        "img": imgs.value.split("\n"),
        "content" : content.value.split("\n")

        })
        .then(response => {
            console.log(response.data);
            router.push('/');
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            error_msg.value = error
        });
    }else{
        axios.post('http://localhost:5000/create',{
        "title" : title.value,
        "img": imgs.value.split("\n"),
        "content" : content.value.split("\n")

        })
        .then(response => {
            console.log(response.data);
            router.push('/');
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            error_msg.value = error
        });
    }
    
}
</script>

<style lang="scss" scoped>

</style>