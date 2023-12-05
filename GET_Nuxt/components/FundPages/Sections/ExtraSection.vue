<template>
    
<div class="main_container">
    <div class="revenue_container">
    
    <div class="revenue_text" data-lag=".1">
        <div class="revenue_text_container">
        <h4 class="revenue_title">{{ title }}</h4>
        <p class="para" v-html="text">
           
        </p>
        </div>
    </div>
    
    <img data-lag=".5" class="revenue_image" :src="image" />
    
    
    </div>

    <p class="full_text" v-html="text_2"></p>
    
</div> 
    
<div class="main_container_mobile">
    <div class="revenue_container_mobile">
    
        <img data-lag=".5" class="revenue_image" :src="image" />
    
    <div class="revenue_text" data-lag=".1">
        <div class="revenue_text_container">
        <h2 class="title_mobile">{{ title }}</h2>
        <p class="para para_mobile" v-html="text">
           
        </p>
        </div>
    </div>
    
    </div>

    <p class="full_text" v-html="text_2"></p>
    </div>
    
    
    
    
    </template>
    
    
    <script setup>
    
    
    const props = defineProps(['image', 'image_margin', 'title', 'text', 'text_margin', 'text_2'])
    
    </script>
    
    
    
    <style scoped>


    .full_text{
        font-size:18px;
        color:#fff;
        width:70%;
        margin-left:15%;
    }
    
    
    .revenue_container{
        display:grid;
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: 1fr;
        grid-column-gap: 20px;
        grid-row-gap: 0px;
        width:90%;
        margin-left:5%;
        margin-top:10%;
        margin-bottom:10%
    }
    
    .main_container_mobile{
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr); 
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        width:90%;
        margin-left:5%;
        margin-top:-20%;
        margin-bottom:10%
    }
    
    .revenue_title{
        color:#000;
        margin-top:v-bind(text_margin);
    }
    
    .revenue_image{
        width:80%;
        margin-top:v-bind(image_margin);
        margin-left:-5%;
    }
    
    .revenue_text{
        margin-left:10%
    }
    
    .revenue_text_container{
        margin-top:30%
    }
    
    .para{
        width:80%;
        color:#000;
    }

    .para_mobile{
        margin-top:0%;
    }

    .title_mobile{
            color:#000;
            margin-top:-10%;
        }
    

        @media only screen and (min-width: 0px) and (max-width: 380px) {
    
    .title_mobile{
        font-size:310%;
        color:#000;
        margin-top:-15%;
    }
}

    
    
    @media only screen and (min-width: 380px) and (max-width: 500px) {
    
        .title_mobile{
            font-size:310%;
            color:#000;
            margin-top:-8%;
        }
        .revenue_image{
        width:80%;
        margin-top:calc(v-bind(image_margin) * .5);
        margin-left:-10%;
    }
    
    }
    
    @media only screen and (min-width: 0px) and (max-width: 576px) {
    
    
    .revenue_container{
        display:none;
    }
    
    .revenue_text_container{
        margin-top:0%
    }
    
    .revenue_image{
        width:90%;
        margin-left:5%;
        margin-bottom:20%
    }
    
    
    .para{
        width:90%
    }
    
    .revenue_title{
        color:#000;

    }
    
    
    }
    
    @media only screen and (min-width: 576px) and (max-width: 768px) {
    
    
        .revenue_container{
        display:none;
    }
    
    .revenue_text_container{
        margin-top:0%
    }
    
    .revenue_image{
        width:90%;
        margin-left:5%;
        margin-bottom:20%
    }
    
    
    .para{
        width:90%
    }
    

    .revenue_title{
        color:#000;
    }
    
    }
    
    @media only screen and (min-width: 768px) and (max-width: 992px) {
    .revenue_container{
        display:none;
    }
    
    .revenue_text_container{
        margin-top:0%
    }
    
    .revenue_image{
        width:90%;
        margin-left:5%;
        margin-bottom:20%
    }
    
    
    .para{
        width:90%
    }
    .revenue_title{
        color:#000;
    }
    
    
    }
    
    @media only screen and (min-width: 992px) and (max-width: 1200px) {
        .main_container_mobile{
            display:none;
        }
    }
    
    @media only screen and (min-width: 1200px) and (max-width: 1400px) {
        .main_container_mobile{
            display:none;
        }
    }
    
    @media only screen and (min-width: 1400px) and (max-width: 1600px) {
        .main_container_mobile{
            display:none;
        }
    }
    
    @media only screen and (min-width: 1600px) and (max-width: 5600px) {
        .main_container_mobile{
            display:none;
        }
    }
    
    
    
    
    
    </style>