<script setup>
import Article from '../components/Article.vue'
import MainLayout from '../layouts/MainLayout.vue';
const childrenComponents = [Article]; 
</script>

<template lang="">
    <div>
        <MainLayout :childrens="childrenComponents" />
    </div>
</template>
<style lang="">

</style>