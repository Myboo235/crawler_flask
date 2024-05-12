<script setup>
import Hero from '../components/Hero.vue';
import Article from '../components/Articles.vue';
import MainLayout from '../layouts/MainLayout.vue';
import Subscribe from '../components/Subscribe.vue';
import Topics from '../components/Topics.vue';
import CustomCursor from '../components/CustomCursor.vue'
import axios from 'axios';
const childrenComponents = [Hero, Article, Subscribe]; 
</script>

<template>

    <div class="flex justify-center flex-col bg-[#292523] overflow-y-hidden">
        <!-- {{ $route.fullPath }} -->
        <!-- <RouterLink to="/article/1">Go to article</RouterLink> -->

        <MainLayout :childrens="childrenComponents" />
    </div>

</template>
<style scoped></style>
