<script setup>

import Footer from '../components/Footer.vue';
import Navbar from '../components/Navbar.vue';
import Search from '../components/Search.vue';


defineProps(['childrens']);
</script>


<template>
    <div class="flex justify-center flex-col bg-[#292523]">
        <Navbar />
        <Search />
        <div v-for="(child, index) in childrens" :key="index">
            <component :is="child"/>
        </div>
        <Footer />

    </div>

</template>
<style scoped></style>