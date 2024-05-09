<script>
import Circle from './Circle.vue';

export default {
    setup() {
        const title = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quae, ea.";
        const thumb = "https://cdn.pixabay.com/photo/2023/05/16/13/14/ai-generated-7997537_1280.jpg";
        const content = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi quasi eligendi eos aliquam autem debitis exercitationem iure at culpa, voluptates vitae provident quod rerum unde vero explicabo deserunt, velit sequi.";
        const time = "1/13/2024";
        const author = "Clare Moreo";
        const avatar = "https://cdn.pixabay.com/photo/2023/05/16/13/14/ai-generated-7997537_1280.jpg";
        return {
            title, thumb, content, time, author, avatar
        };
    },
    components: { Circle }
}
</script>


<template>
    <div class="bg-tertiary relative py-[5rem]">
        <div class="">
            <h2 class="px-8 pb-8 text-6xl font-bold lg:my-[4rem] cursor-pointer">Top Article.</h2>
            <div class="px-4 lg:px-8 grid md:grid-cols-2 justify-center items-center gap-[5rem] md:gap-y-[5rem] lg:w-3/4">
                <div v-for="i in 4">
                    <div class="grid grid-cols-2 duration-300] group " v-motion-fade-visible-once>
                        <div class="grid grid-rows-3 gap-5 cursor-pointer ">
                            <div class="bg-white rounded-l-[1rem] p-[0.67rem] lg:text-sm text-lg row-span-3 group-hover:bg-primary group-hover:text-white duration-300 shadow-lg shadow-black">
                                <p>{{ title }}</p>
                                <span class="lg:pt-4">{{ time }}</span>
                            </div>
                            <button class="row-span-1 mt-auto mb- flex justify-center items-center bg-secondary mx-4 rounded-[2rem] hover:scale-105 transition-all duration-200 cursor-pointer group border-2 border-primary shadow-lg shadow-black">
                                <p class="flex items-center px-5 py-1">
                                    View more 
                                </p>
                                <div class="">
                                    <v-icon name="bi-arrow-up-right" class="bg-black rounded-[10rem] text-[#e6a349] mr-1 p-[0.1rem]" />
                                </div>
                            </button>
                    
                        </div>
                        <div class="bg-white group-hover:bg-primary p-4 rounded-r-[1rem] rounded-b-[1rem] h-full flex justify-center duration-300 shadow-[0_5px_15px] [clip-path:inset(-10px_-10px_-10px_0px)]">
                            <img v-bind:src="thumb" alt="" class="rounded-[1rem] object-cover group-hover:scale-105 duration-500 ">
                        </div>
                    </div>
                </div>
                
            </div>
        </div>
        
        <div class="absolute top-20 right-0 hidden lg:block ">
            <img src="../assets/astronaut.png" alt="" class="bounce z-[2]">
        </div>
        
    </div>
</template>



<style scoped>
    .bounce{
        animation: bounce 2s ease infinite;
    }
    @keyframes bounce{
        0%{
            transform: translateY(0);
        }
        50%{
            transform: translateY(-1.5rem);
        }
        100%{
            transform: translateY(0);
        }
    }
</style>