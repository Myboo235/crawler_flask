<script setup>
import axios from 'axios';
import { ref } from 'vue'
import Astronaut from './Astronaut.vue'
// import Carousel from './Carousel.vue'

import { useRoute, useRouter } from 'vue-router'
import { FwbCarousel } from 'flowbite-vue'
import { FwbAlert } from 'flowbite-vue'


const route = useRoute()
const router = useRouter()

const title = ref("");
const imgs = ref([]);
const content = ref("");
const error_msg = ref("none")

const id = (route.params.id)
axios.get(`http://localhost:5000/data/${id}`)
    .then(response => {
        const responseData = response.data;
        title.value = responseData.title;
        content.value = responseData.content;

        responseData.img.map((i) => {
            imgs.value.push({ "src": i })
        })

    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });

const deleteArticle = () => {
    error_msg.value = "none"
    axios.post('http://localhost:5000/delete', {
        "_id": id,
    })
        .then(response => {
            router.push('/');
        })
        .catch(error => {
            console.error('Error fetching data:', error);
            error_msg.value = error
        });
}
</script>


<template>
    <div class="fixed w-full px-[1rem] top-10 z-[100]" v-if="error_msg !== 'none'">
        <fwb-alert border type="danger" closable>
            {{ error_msg }}
        </fwb-alert>
    </div>
    <div class="bg-tertiary relative py-[2rem] xl:px-[10rem] 2xl:px-[30rem]">
        <div class="mx-[2rem] py-[1rem] px-[2rem] bg-white rounded-3xl relative">
            <div class="flex cursor-pointer bg-primary rounded-xl text-secondary items-center">
                <h2 class="p-8 text-4xl lg:text-6xl font-bold lg:my-[4rem] text-secondary">{{ title }}</h2>
                <div class="ml-auto flex flex-col gap-2">
                    <button id = "update_btn"  class="mr-4 px-2 bg-secondary text-primary h-[2rem] min-w-[5rem] rounded-lg">
                        <RouterLink :to="'/update/' + $route.params.id">
                            update
                        </RouterLink>
                    </button>
                    <button id = "delete_btn" class="ml-auto mr-4 px-2 bg-red-400 text-primary h-[2rem] min-w-[5rem] rounded-lg"
                    
                        @click="deleteArticle">
                        delete
                    </button>
                </div>
            </div>
            <div class="w-full h-1 my-4 bg-primary" />

            <fwb-carousel :pictures="imgs"/>
            <!-- <img v-bind:src="image" alt="" class="rounded-[1rem] object-cover group-hover:scale-105 duration-500 "> -->
            <div class="w-full h-1 my-4 bg-primary" />
            <div class="h-[50vh] overflow-auto mt-4">
                <div class="mt-4" v-for="c in content">
                    <p>
                        {{ c }}
                    </p>
                </div>
            </div>

        </div>
    </div>
    <div>
        <Astronaut />
    </div>
</template>




<style scoped>
.bounce {
    animation: bounce 2s ease infinite;
}

@keyframes bounce {
    0% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-1.5rem);
    }

    100% {
        transform: translateY(0);
    }
}
</style>