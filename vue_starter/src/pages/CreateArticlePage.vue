<script setup>
import Hero from '../components/Hero.vue';
import Article from '../components/Articles.vue';
import MainLayout from '../layouts/MainLayout.vue';
import Subscribe from '../components/Subscribe.vue';
import Topics from '../components/Topics.vue';
import CustomCursor from '../components/CustomCursor.vue'
import Form from '../components/Form.vue'

const childrenComponents = [Form]; 
</script>

<template>

    <div class="flex justify-center flex-col bg-[#292523] overflow-y-hidden">
        {{ $route.fullPath }}
        <RouterLink to="/article">Go to article</RouterLink>
        <MainLayout :childrens="childrenComponents"/>
        <div> <custom-cursor :targets="['img', 'a', 'button', 'your-hover-class']" :circleColor="'#3468C0'"
            :circleColorHover="'#2f2f2f'" :dotColor="'#3468C0'" :dotColorHover="'lightgray'"
            :hoverSize="1.8"></custom-cursor>
    </div>
    </div>

</template>
<style scoped></style>