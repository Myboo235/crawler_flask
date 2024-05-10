<template>
    <div>
        <div class="absolute top-20 right-0 hidden lg:block ">
            <img src="../assets/astronaut.png" alt="" class="bounce z-[2]">
        </div>
    </div>
</template>

<script>
export default {
    setup () {
        

        return {}
    }
}
</script>

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