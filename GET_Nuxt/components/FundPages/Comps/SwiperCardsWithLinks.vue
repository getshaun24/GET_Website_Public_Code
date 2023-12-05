<template>
    

    <div class="swiper_box">
    <swiper :freemode="true"  :speed="3000" :freeModeMomentum="true" :centeredSlides="true"  :grabCursor="true" :breakpoints="swiperOptions.breakpoints" style="transition-timing-function:linear" class="about_swiper_wrapper">
    
    <swiper-slide><a data-lag=".25" href="https://www.fooddive.com/news/impossible-beef-lite-healthier-plant-based-meat/644476/" target="_blank" class="link_button btn_1">Read Now</a><img class="swiper_img" :src="image_1" /></swiper-slide>
    <swiper-slide><a data-lag=".35" href="https://impossiblefoods.com/sustainable-food" target="_blank" class="link_button btn_2">Read Now</a><img class="swiper_img" :src="image_2" /></swiper-slide>
    <swiper-slide><a data-lag=".45" href="https://research.contrary.com/reports/impossible-foods" target="_blank" class="link_button btn_3">Read Now</a><img class="swiper_img" :src="image_3" /></swiper-slide>
    
    </swiper>
    </div>
    
    
    
    </template>
    
    
    <script setup>
    
    import { Swiper, SwiperSlide } from 'swiper/vue';
    import { Autoplay, EffectCoverflow } from "swiper";
    import 'swiper/css/bundle';
    import "swiper/css/effect-coverflow";
    
    
    const props = defineProps(['image_1', 'image_2', 'image_3'])
    
    
    
    const swiperOptions = {
              breakpoints: {      
                0: {       
             slidesPerView: 2.05,
             spaceBetween: 20     
          }, 
          576: {       
            slidesPerView: 2.05,
             spaceBetween: 20     
          },          
          768: {       
            slidesPerView: 2.05,
             spaceBetween: 20     
          },   
      
          992: {       
             slidesPerView: 2,       
             spaceBetween: 80     
          } 
       }   
    }
    
    
    
    
    </script>
    
    <style scoped>
    
    
    .swiper_img{
        width:100%
    }
    
    
    .swiper_box{
        margin-top:12%
    }
    
    
    .link_button{
        background-color:rgb(25, 120, 237);
        cursor:pointer;
        padding:10px 30px;
        text-align:center;
        border-radius:20px;
        position:absolute;
    }
    
    .btn_1{
        margin-left:65%;
        margin-top:35%;
    }

    .btn_2{
        margin-left:3%;
        margin-top:24%;
    }

    .btn_3{
        margin-left:12.5%;
        margin-top:40%;
    }
    
    
    
    @media only screen and (min-width: 0px) and (max-width: 576px) {
    
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