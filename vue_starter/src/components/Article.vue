<script>

export default {
    setup() {
        const title = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quae, ea.";
        const image = "https://cdn.pixabay.com/photo/2023/05/16/13/14/ai-generated-7997537_1280.jpg";
        const content = ["Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi quasi eligendi eos aliquam autem debitis exercitationem iure at culpa, voluptates vitae provident quod rerum unde vero explicabo deserunt, velit sequi.","Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi quasi eligendi eos aliquam autem debitis exercitationem iure at culpa, voluptates vitae provident quod rerum unde vero explicabo deserunt, velit sequi."];
        const time = "1/13/2024";
        const author = "Clare Moreo";
        const avatar = "https://cdn.pixabay.com/photo/2023/05/16/13/14/ai-generated-7997537_1280.jpg";
        return {
            title, image, content, time
        };
    },
}
</script>


<template>
    <div class="bg-tertiary relative py-[5rem]">
        <div class="mx-auto px-[5rem]">
            <h2 class="px-8 pb-8 text-6xl font-bold lg:my-[4rem] cursor-pointer">{{ title }}</h2>
            <img v-bind:src="image" alt="" class="rounded-[1rem] object-cover group-hover:scale-105 duration-500 ">
            <div class="mt-4" v-for="c in content">
                <p class="py-4">
                    {{ c }}
                </p>
            </div>
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