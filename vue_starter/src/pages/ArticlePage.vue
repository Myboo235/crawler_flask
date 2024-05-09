<script setup>
import Hero from '../components/Hero.vue';
import Article from '../components/Articles.vue';
import MainLayout from '../layouts/MainLayout.vue';
import Subscribe from '../components/Subscribe.vue';
import Topics from '../components/Topics.vue';
import CustomCursor from '../components/CustomCursor.vue'

const childrenComponents = [Hero]; 
</script>

<template lang="">
    <div>
        <MainLayout :childrens="childrenComponents" />
    </div>
</template>
<style lang="">

</style>