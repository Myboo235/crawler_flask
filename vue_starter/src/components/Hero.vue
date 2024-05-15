<template>
    <div class="bg-[#d5ccbb] p-5 rounded-t-[2rem] relative z-5">
        <div
            class="bg-white lg:bg-transparent p-2 pb-10 rounded-[2rem] flex flex-col lg:flex-row gap-4 lg:gap-0 min-h-[30rem]">
            <div class="px-4 pt-4 lg:p-0 lg:pl-[5rem] lg:pt-[5rem] rounded-[2rem] relative lg:w-[100vw] ">
                <img src="https://cdn.pixabay.com/photo/2023/05/16/13/14/ai-generated-7997537_1280.jpg" alt=""
                    class="object-cover lg:rounded-[1rem] rounded-[2rem] shadow-md shadow-black">

            </div>


            <div class="lg:flex lg:flex-col lg:w-1/2 justify-center gap-5 relative">
                <div
                    class="xl:bg-white/70 lg:py-5 rounded-[2rem] lg:pl-5 lg:absolute lg:-left-[5rem] lg:max-w-[30rem] lg:border-2 lg:border-primary lg:shadow-lg lg:shadow-black">
                    <div class="px-4 flex">
                        <!-- <div>Trending now</div> -->
                        <!-- <div class="ml-auto">1/13/2024</div> -->
                    </div>
                    <div class="px-4 lg:flex lg:flex-col gap-5">
                        <h3 class="text-xl md:text-2xl xl:text-4xl lg:text-3xl font-bold text-primary hover:opacity-80 cursor-pointer transition-all duration-500">
                            Welcome to our AI-generated space blog
                        </h3>
                    
                        <p class="xl:font-[300]">
                            Welcome to the fascinating world of space exploration, brought to you by artificial intelligence. Join me on an extraordinary journey through the vast expanse of the universe, where AI algorithms analyze and generate captivating content about celestial wonders. From stunning nebulae to mysterious black holes, we will delve into the secrets and beauty that lie beyond the boundaries of our planet. Embark on an interstellar adventure as we explore the cosmos and uncover the marvels that await us, all through the power of AI technology.
                        </p>
                    </div>

                    <!-- <div class="px-4 flex items-center gap-2 cursor-pointer">
                        <div
                            class="w-[2rem] h-[2rem] rounded-full bg-[url(https://cdn.pixabay.com/photo/2023/05/16/13/14/ai-generated-7997537_1280.jpg)] bg-cover">
                        </div>
                        <p class="hover:underline">Clare Moreo</p>
                    </div> -->
                </div>
            </div>

            <Circle right="0" />
        </div>

    </div>
</template>

<script>
import Circle from './Circle.vue';

export default {
    components: { Circle }
}
</script>
