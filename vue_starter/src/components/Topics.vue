<script>
import Circle from './Circle.vue';

export default {
    setup() {
        const title = "Lorem.";
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
    <div class="bg-tertiary relative py-[4rem]">
        <div class="">
            <h2 class="px-8 pb-8 text-6xl font-bold lg:my-[4rem] cursor-pointer">Top Topics.</h2>
            <div class="px-4 lg:px-8 grid md:grid-cols-2 xl:grid-cols-6 justify-center items-center gap-[1rem]">
                <div v-for="i in 6">
                    <div class="flex flex-col justify-center items-center duration-300 group "
                        v-motion-fade-visible-once>

                        <div class=" relative p-4 rounded-[1rem] h-full flex justify-center duration-300">
                            <img v-bind:src="thumb" alt=""
                                class="rounded-[1rem] object-cover group-hover:scale-105 duration-500 group-hover:brightness-50">
                            <p
                                class="text-transparent group-hover:text-white absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 sm:text-sm">
                                {{ content }}</p>
                        </div>
                        <div>{{ title }}</div>
                    </div>
                </div>

            </div>
        </div>
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