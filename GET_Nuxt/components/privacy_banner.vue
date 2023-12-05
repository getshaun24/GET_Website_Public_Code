<template>
    
<div v-if="!privacy_agree" class="banner_container">
<p class="privacy_text">You must agree to be bound by the terms of our Privacy Policy to use our site. We also use cookies to ensure our site runs smoothly. Our Privacy Policy can be found <a href="https://thisisget.com/legal_pages/privacy" target="_blank" style="color:#ff9933">here.</a> Last updated May 11, 2023.</p>

<div class="privacy_button" @click="privacy_button_click">Accept</div>
</div>
</template>


<script setup>



const privacy_agree = useCookie('privacy_agree', {default:()=> false, watch:true})

function privacy_button_click(){
    privacy_agree.value = true
}


</script>



<style scoped>

.banner_container {
    position: fixed;
    bottom: 10px;
    left: 0;
    width: 80%;
    margin-left:10%;
    height: 60px;
    background-color: #fff;
    color: #fff;
    z-index: 999;
    border-radius:100px;
    display:flex;
    align-items:center;
    justify-content: space-around;
    border:2px solid rgb(25, 120, 237);
}

.privacy_text{
    width:60%;
    margin-left:5%;
    font-size:12px;
}

.privacy_button{
    background-color: #000;
    margin-left:10%;
    padding:10px 20px;
    border-radius:100px;
    margin-right:5%;
    cursor:pointer;
    transition: all 0.5s ease;
}

.privacy_button:hover{
    background-color: rgb(25, 120, 237);
}





@media only screen and (min-width: 0px) and (max-width: 576px) {
    .banner_container {
width: 98%;
margin-left:.5%;
    }

    .privacy_text{
    width:60%;
    margin-left:5%;
    font-size:10px;
    line-height: 1;
}
}

@media only screen and (min-width: 576px) and (max-width: 768px) {
    .banner_container {
width: 98%;
margin-left:.5%;
    }

    .privacy_text{
    width:60%;
    margin-left:5%;
    font-size:10px;
    line-height: 1;
}
}

@media only screen and (min-width: 768px) and (max-width: 992px) {
    .privacy_text{
    line-height: 1;
}
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
