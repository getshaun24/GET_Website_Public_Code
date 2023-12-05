<template>
    

<div class="swiper_box">
<swiper :freemode="true"  :speed="3000" :freeModeMomentum="true" :centeredSlides="true"  :grabCursor="true" :breakpoints="swiperOptions.breakpoints" style="transition-timing-function:linear" class="about_swiper_wrapper">

<swiper-slide><img class="swiper_img" :src="image_1" /></swiper-slide>
<swiper-slide><img class="swiper_img" :src="image_2" /></swiper-slide>
<swiper-slide><img class="swiper_img" :src="image_3" /></swiper-slide>

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