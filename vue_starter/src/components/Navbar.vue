<script>
import { ref } from 'vue'

export default {
    setup() {
        const date = ref(new Date().toLocaleDateString());
        const count = ref(0)
        const showMenu = ref(false)

        const toggleMenu = () => {
            showMenu.value = !showMenu.value
        }
        return { date, count, showMenu, toggleMenu }
    }
}

</script>

<template>
    <div
        class="grid lg:grid-cols-3 grid-cols-2  justify-center items-center w-full bg-[#292523] h-[4rem] text-secondary">
        <div class="text-xl cursor-pointer mr-auto ml-5">
            <RouterLink to="/">
                <!-- LeNhut. -->
                AI.Blog
            </RouterLink>

        </div>
        <nav class="lg:flex justify-center items-center h-full hidden bg-tertiary rounded-b-[2rem]">
            <ul class="flex items-center text-primary gap-[2rem]">
                <li class="cursor-pointer rounded-xl hover:bg-secondary hover:text-primary p-[0.5rem] duration-300">
                    Work
                </li>
                <li class="cursor-pointer rounded-xl hover:bg-secondary hover:text-primary p-[0.5rem] duration-300">
                    Project</li>
                <li class="cursor-pointer rounded-xl hover:bg-secondary hover:text-primary p-[0.5rem] duration-300">
                    Contact</li>
                <li class="cursor-pointer rounded-xl hover:bg-secondary hover:text-primary p-[0.5rem] duration-300">
                    Source</li>
            </ul>
        </nav>
        <div class="ml-auto pr-5 flex flex-col items-end relative" @click="toggleMenu">
            {{ date }}
            <button @click="toggleMenu" class="cursor-pointer hover:scale-110 duration-200 lg:hidden">
                <v-icon name="fa-align-right" scale="1.5" v-on:click="toggleMenu" />
            </button>
            <nav :class="{ hidden: !showMenu }" class="absolute top-[4rem] z-50 lg:hidden">
                <ul
                    class="flex flex-col items-center bg-primary rounded-lg px-[2rem] py-[0.5rem] border-2 border-secondary">
                    <li class="cursor-pointer rounded-xl hover:underline p-[0.5rem] duration-300">
                        Work
                    </li>
                    <li class="cursor-pointer rounded-xl hover:underline p-[0.5rem] duration-300">
                        Project</li>
                    <li class="cursor-pointer rounded-xl hover:underline p-[0.5rem] duration-300">
                        Contact</li>
                    <li class="cursor-pointer rounded-xl hover:underline p-[0.5rem] duration-300">
                        Source</li>
                </ul>
            </nav>
        </div>
    </div>

</template>



<style lang="scss" scoped></style>