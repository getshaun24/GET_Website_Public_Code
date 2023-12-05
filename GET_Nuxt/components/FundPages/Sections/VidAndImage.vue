<template>
    


    <div class="strategy_container">
    

    <!-- <img  data-speed=".9" class="strategy_image" :src="image" /> -->
    
    
    <!-- <video :class="{ hide_it: is_image }" data-lag=".5" class="strategy_video" autoplay muted playsinline loop>
                    <source :src="vid" type="video/mp4">
    </video> -->

    <iframe data-speed="1.1" src="https://player.vimeo.com/video/821432762?h=02bcfd1239" class="vimeo" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>



    
    </div>
    
    </template>
    
    
    <script setup>
    
    
    
    const props = defineProps(['vid', 'image', 'container_margin_top'])
    
    
    </script>
    
    <style scoped>


.vimeo{
    width:80% !important;
    margin-left:10% !important;
    height:60vh !important;
    z-index:3;
    margin-top:10%;
    border-radius: 20px !important;
    padding: 5px 20px !important;
    background-color: #121212 !important;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}
/* 
.vimeo:hover{
    box-shadow: 2px 10px 15px rgba(255, 255, 255, 0.1);
  transform: translateY(-3px);
  transition: outline 12s ease 1s;
}
 */


.strategy_image{
        width:40%;
    }

    .strategy_container{
        display:flex;
        flex-direction:row;
        justify-content: space-between;
        width:90%;
        margin-left:5%;
        margin-top:5%;
        margin-bottom:10%;
    }
    
    /* .strategy_container{
        display:grid;
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: 1fr;
        grid-column-gap: 20px;
        grid-row-gap: 0px;
        width:90%;
        margin-left:5%;
        margin-top:10%;
        margin-bottom:10%
    } */
    
    
/*     
    @media only screen and (min-width: 0px) and (max-width: 380px) {
        .strategy_container{
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr); 
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        width:80%;
        margin-left:10%;
        margin-top:-115%;
        margin-bottom:v-bind(container_margin_bottom);
    }
    
    .strategy_image{
        margin-left:0%;
        margin-top:calc(150% * v-bind(image_margin_mobile_calc));
    }
    
    
    .strategy_video{
        margin-top:0%;
        margin-bottom:-225%;
        z-index:-1;
        position: relative;
    }
    .para{
        width:100%;
        margin-bottom:v-bind(text_margin_mobile);
    }
    
    .text_container{
        margin-top:0%;
        mix-blend-mode: difference;
    }
    
    .invest_button{
        margin-top:210%
    }
    
    }
    
    
    @media only screen and (min-width: 380px) and (max-width: 430px) {
        .strategy_container{
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr); 
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        width:80%;
        margin-left:10%;
        margin-top:-135%;
        margin-bottom:calc(v-bind(container_margin_bottom) * 1.35);
    }
    
    .strategy_image{
        margin-left:0%;
        margin-top:calc(180% * v-bind(image_margin_mobile_calc));
    }
    
    
    .strategy_video{
        margin-top:0%;
        margin-bottom:-215%;
        z-index:-1;
        position: relative;
    }
    .para{
        width:100%;
        margin-bottom:v-bind(text_margin_mobile);
    }
    
    .text_container{
        margin-top:0%;
        mix-blend-mode: difference;
    }
    .invest_button{
        margin-top:210%
    }
    
    }
    
    
    
    @media only screen and (min-width: 430px) and (max-width: 576px) {
    
        .strategy_container{
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr); 
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        width:80%;
        margin-left:10%;
        margin-top:-80%;
        margin-bottom:v-bind(container_margin_bottom);
    }
    
    .strategy_image{
        margin-left:0%;
        margin-top:calc(110% * v-bind(image_margin_mobile_calc));
    }
    
    
    .strategy_video{
        margin-top:0%;
        margin-bottom:-150%;
        z-index:-1;
        position: relative;
    }
    .para{
        width:100%;
        margin-bottom:v-bind(text_margin_mobile);
    }
    
    .text_container{
        margin-top:0%;
    }
    
    .invest_button{
        margin-top:210%
    }
    
    }
    
    @media only screen and (min-width: 576px) and (max-width: 768px) {
    
        .strategy_container{
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr); 
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        width:80%;
        margin-left:10%;
    }
    
    .strategy_image{
        margin-left:0%;
        margin-top:calc(1% * v-bind(image_margin_mobile_calc));
    }
    
    .para{
        width:100%;
    }
    
    .text_container{
        margin-top:-15%
    }
    
    }
    
    @media only screen and (min-width: 768px) and (max-width: 992px) {
    
        .strategy_container{
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr); 
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        width:80%;
        margin-left:10%;
    }
    
    .strategy_image{
        margin-left:0%;
        margin-top:calc(1% * v-bind(image_margin_mobile_calc));
    }
    
    .para{
        width:100%;
    }
    
    .text_container{
        margin-top:-5%
    }
    
    }
    
    @media only screen and (min-width: 992px) and (max-width: 1200px) {
        .strategy_image{
        margin-top:calc(1% * v-bind(image_margin_calc));
    }
    }
    
    @media only screen and (min-width: 1200px) and (max-width: 1400px) {
        .strategy_image{
        margin-top:calc(1% * v-bind(image_margin_calc));
    }
    }
    
    @media only screen and (min-width: 1400px) and (max-width: 1600px) {
    }
    
    @media only screen and (min-width: 1600px) and (max-width: 5600px) {
    }
     */
    
    
    
    
    </style>