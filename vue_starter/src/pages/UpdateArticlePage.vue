<script setup>
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';
import Form from '../components/Form.vue'

</script>

<template>

    <div class="flex justify-center flex-col bg-[#292523] overflow-y-hidden">
        <Navbar />
        <Form type="update"/>
        <Footer />
        <div> 
        <!-- <custom-cursor 
            :targets="['img', 'a', 'button', 'your-hover-class']" 
            :circleColor="'#3468C0'"
            :circleColorHover="'#2f2f2f'" 
            :dotColor="'#3468C0'" 
            :dotColorHover="'lightgray'"
            :hoverSize="1.8"
            :clientWith="2"
            ></custom-cursor> -->
    </div>
    </div>

</template>
<style scoped></style>