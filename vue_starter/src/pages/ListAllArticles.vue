<template>
    <div class="flex justify-center flex-col bg-[#292523] overflow-y-hidden">
        <Navbar />
        <h2 class="text-white px-8 text-6xl font-bold lg:my-[4rem] cursor-pointer">All Article.</h2>
        <div class="min-h-[80vh] grid xl:grid-cols-4 md:grid-cols-2 w-full gap-4 mt-[4rem] mb-[8rem] px-[4rem]">
            <div v-for="a in articles" >
                <RouterLink :to="'/article/'+a._id.$oid">
                    <div class="p-5 bg-secondary rounded-xl cursor-pointer">
                        <h5 class="text-2xl font-bold tracking-tight text-gray-900 dark:text-white h-[4rem]">
                            {{ a.title.slice(0, 40)}}....
                        </h5>
                        <img :src="a.img[0]" alt="" class="h-[10rem] w-full object-cover my-4">
                        <p class="font-normal text-gray-700 dark:text-gray-400 h-[5rem]">
                            {{ a.content.join("").slice(0, 100) }}....
                        </p>
                    </div>
                </RouterLink>
                
            </div>
        </div>
        <Footer />
        <div>
            <!-- <custom-cursor 
            :targets="['img', 'a', 'button', 'your-hover-class']" 
            :circleColor="'#3468C0'"
            :circleColorHover="'#2f2f2f'" 
            :dotColor="'#3468C0'" 
            :dotColorHover="'lightgray'"
            :hoverSize="1.8"
            :clientWith="2"
            ></custom-cursor> -->
        </div>
    </div>
</template>

<script setup>
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';
import { ref } from 'vue'
import axios from 'axios';

const articles = ref([]);

axios.get('http://localhost:5000/')
    .then(response => {
        articles.value = response.data
        console.log(response.data)
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
</script>

<style lang="scss" scoped></style>