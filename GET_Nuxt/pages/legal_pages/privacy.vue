<template>
    
    <Header/>
    
        <GSAPScrollSmoother>
    
<h5 class="page_title" data-speed="0.6" data-lag="0.2">Privacy Policy</h5>


<div class="main_text">







    <embed :src="privacy_doc" class="privacy_agreement">




</div>








<Footer/>
        </GSAPScrollSmoother>
    

</template>

<script setup>
 import privacy_doc from "~/assets/legal/privacy_policy.pdf";
const title_move = ref('100%');


onMounted(() => {
title_move.value = '35%';
})

</script>


<style scoped>

.privacy_agreement{
    width:100%;
    height:100vh;
    margin-top:10%;
    margin-bottom:10%;
}
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

.main_text{
    width:80%;
    margin-left:10%;
    margin-bottom:10%;
    margin-top:30%
}

.section_title{
    font-size:35px
}

.section_subtitle{
    text-decoration: underline;
    text-underline-offset: 5px;
    text-decoration-thickness: 1px;
    text-decoration-color: #1978ed;
}

</style>