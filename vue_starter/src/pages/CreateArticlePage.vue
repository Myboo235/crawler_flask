<script setup>
import Hero from '../components/Hero.vue';
import Article from '../components/Articles.vue';
import MainLayout from '../layouts/MainLayout.vue';
import Subscribe from '../components/Subscribe.vue';
import Topics from '../components/Topics.vue';
import Form from '../components/Form.vue'

const childrenComponents = [Form]; 
</script>

<template>

    <div class="flex justify-center flex-col  overflow-y-hidden ">
        <MainLayout :childrens="childrenComponents"/>
    </div>

</template>
<style scoped></style>