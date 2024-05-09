<template>
    <div>
         <kinesis-container
                event="scroll">
                    <kinesis-element 
                          tag="img"
                          :transformOrigin="sunOrigin"
                          :strength="100"
                          type="rotate"/>
                    <kinesis-element
                          :transformOrigin="earthmoonOrigin"
                          :strength="800"
                          type="rotate">
                          <img :src="earth" />
                          <kinesis-element
                          tag="img"
                          :src="moon"
                          :transformOrigin="moonOrigin"
                          :strength="1200"
                          type="rotate"/>
                    </kinesis-element>
                    <kinesis-element
                          tag="img"
                          :src="mars"
                          :transformOrigin="marsOrigin"
                          :strength="500"
                          type="rotate"/>
              </kinesis-container> <kinesis-container
                event="scroll">
                    <kinesis-element 
                          tag="img"
                          :transformOrigin="sunOrigin"
                          :strength="100"
                          type="rotate"/>
                    <kinesis-element
                          :transformOrigin="earthmoonOrigin"
                          :strength="800"
                          type="rotate">
                          <img :src="earth" />
                          <kinesis-element
                          tag="img"
                          :src="moon"
                          :transformOrigin="moonOrigin"
                          :strength="1200"
                          type="rotate"/>
                    </kinesis-element>
                    <kinesis-element
                          tag="img"
                          :src="mars"
                          :transformOrigin="marsOrigin"
                          :strength="500"
                          type="rotate"/>
              </kinesis-container>
    </div>
</template>

<script>
    export default {
        
    }
</script>

<style lang="scss" scoped>

</style>