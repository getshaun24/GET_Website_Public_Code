<template>
    
    <h1 class="landing_big" :style="{ 'font-size': font_size }">{{ text }}</h1>
</template>


<script setup>




const props = defineProps(['text', 'font_size', 'margin_top', 'padding_top'])


</script>

<style scoped>

.landing_big{
    font-size:10vw;
    margin-left:5%;
    margin-top:v-bind(margin_top);
    width:90%;
    line-height: .9;
    border-bottom: #fff solid 1px;
    padding-bottom:12px;
    padding-top: v-bind(padding_top);
}


/* @media only screen and (min-width: 0px) and (max-width: 576px) {

    .landing_big{
    padding-top: calc(v-bind(padding_top) * 2);
}

} */

</style>