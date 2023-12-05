<template>
    
    <Header/>
    
        <GSAPScrollSmoother>
    
<h5 class="page_title" data-speed="0.6" data-lag="0.2">Careers</h5>

<CareersFaqs style="z-index:-1"/>


<Footer/>
        </GSAPScrollSmoother>
    

</template>

<script setup>

const title_move = ref('100%');


onMounted(() => {
title_move.value = '35%';
})

</script>


<style scoped>

.page_title{
    background-color:#fff;
    background-image: url('~/assets/content/careers/careers_2.jpg');
    padding:25px;
    width:65%;
    margin-left:v-bind(title_move);
    text-align: center;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    z-index:10000;
    color: #fff;
    filter: drop-shadow(5px 3px 5px #ffffff21);
    transition: margin-left 1.75s ease 1.5s;
}



@media only screen and (min-width: 0px) and (max-width: 576px) {
    .page_title{
margin-top:5%;
margin-bottom:40%
}
}

@media only screen and (min-width: 576px) and (max-width: 768px) {
}

@media only screen and (min-width: 768px) and (max-width: 992px) {
}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
}
 




</style>