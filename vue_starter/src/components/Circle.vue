


<template>
    <div class="hidden lg:block">
        <!-- <div v-bind:class="`
        absolute
        bottom-0
        left-0
        right-0
        duration-100
        h-[5rem]
        

        before:content-['']
        before:translate-x-[-50%]
        before:h-[${size}rem] 
        before:w-[${size}rem] 
        before:rounded-[44%] 
        before:bg-[rgb(51, 51, 51)] 
        before:animate-waves

        after:content-none
        after:translate-[-50% -75%]
        after:h-[${size}rem] 
        after:w-[${size}rem] 
        after:rounded-[44%] 
        after:bg-[rgba(51, 51, 51, 1)] 
        after:animate-waves

        `"></div> -->

        <div :class="`waves `"></div>
    </div>
</template>

<script>
export default {
    props: {
        size: {
            default:"16rem"
        },
        right : {
            default:null
        }
    },
}

</script>

<style scoped>
.waves {
  position: absolute;
  bottom: 0;
  height: 10rem;
  transition: 500ms;
}

.waves::before,
.waves::after {
  content: '';
  position: absolute;
  width: v-bind(size); 
  height:  v-bind(size);
  top: 10rem;
  right: v-bind(right);
  transform: translate(-50%, -75%);
  z-index: 1;
}

.waves::before {
  border-radius: 44%;
  background: rgba(51, 51, 51, 1);
  animation: waves 8s linear infinite;
}

.waves::after {
  border-radius: 44%;
  background: rgba(51, 51, 51, 0.5);
  animation: waves 15s linear infinite;
}

@keyframes waves {
  0% {
    transform: translate(-50%, -75%) rotate(0deg);
  }
  
  100% {
    transform: translate(-50%, -75%) rotate(360deg);
  }
}

</style>