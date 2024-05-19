<script>
import Circle from './Circle.vue';
import Astronaut from './Astronaut.vue'
import axios from 'axios';
import {ref} from 'vue'

export default {
    setup() {
        const articles = ref([]);

        axios.get('http://localhost:5000/')
            .then(response => {
                articles.value = response.data.slice(0,6)
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });

        return {
         articles
        };
    },
    components: { Circle , Astronaut }
}
</script>


<template>
    <div class="bg-tertiary relative py-[5rem]">
        <div class="">
            <div class=" w-full flex justify-center mb-8">
                <RouterLink to="/create" class="px-[2rem] xl:px-[8rem] py-[2rem] bg-gradient-to-r from-secondary to-pink-200 border-white border-2 rounded-2xl text-2xl hover:scale-105 duration-500 transition text-white hover:to-pink-400">
                    <button >
                         Click here to create new blog 🚀
                    </button>
                </RouterLink>
            </div>
            <h2 class="px-8 pb-8 text-6xl font-bold lg:my-[4rem] cursor-pointer">Top Article.</h2>
            <div class="px-4 lg:px-8 grid md:grid-cols-2 justify-center items-center gap-[5rem] md:gap-y-[5rem] lg:w-3/4">
                <div v-for="a in articles">
                    <div class="grid grid-cols-2 duration-300] group " v-motion-fade-visible-once>
                        <div class="grid grid-rows-3 gap-5 cursor-pointer ">
                            <div class="bg-white rounded-l-[1rem] p-[0.67rem] lg:text-sm text-lg row-span-3 group-hover:bg-primary group-hover:text-white duration-300 shadow-lg shadow-black">
                                <p>{{ a.title }}</p>
                                <!-- <span class="lg:pt-4">{{ time }}</span> -->
                            </div>
                            <button id = "view_more">
                                <RouterLink :to="'/article/'+a._id.$oid" class="row-span-1 mt-auto mb- flex justify-center items-center bg-secondary mx-4 rounded-[2rem] hover:scale-105 transition-all duration-200 cursor-pointer group border-2 border-primary shadow-lg shadow-black">
                                    <p class="flex items-center px-5 py-1"
                                        >
                                        View more
                                    </p>
                                    <div class="">
                                        <v-icon name="bi-arrow-up-right" class="bg-black rounded-[10rem] text-[#e6a349] mr-1 p-[0.1rem]" />
                                    </div>
                                </RouterLink>
                            </button>
                    
                        </div>
                        <div class="bg-white group-hover:bg-primary p-4 rounded-r-[1rem] rounded-b-[1rem] h-full flex justify-center duration-300 shadow-[0_10px_15px] [clip-path:inset(-10px_-10px_-10px_0px)]">
                            <img v-bind:src="a.img[0]" alt="" class="rounded-[1rem] object-cover group-hover:scale-105 duration-500 h-[10rem] w-[12rem]">
                        </div>
                    </div>
                </div>
                
            </div>
            <div class="flex justify-center m-8">
                <RouterLink to="/articles" class="px-[2rem] xl:px-[8rem] py-[1rem] bg-gradient-to-r from-secondary to-blue-200 border-white border-2 rounded-2xl text-xl hover:scale-105 duration-500 transition text-white hover:to-blue-400">
                    <button >
                         View all blog
                    </button>
                </RouterLink>
            </div>
        </div>
        
        <Astronaut />
        
    </div>
</template>



<style scoped>

</style>