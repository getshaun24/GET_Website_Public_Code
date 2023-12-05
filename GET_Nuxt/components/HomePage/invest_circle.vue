<template>

<div class="home_investment_section">
            <div class="white_container_home_circle">

                <div class="invest_grid">

                <div>

                <div class="invest_circle" data-lag=".1">

                        <div :class="{update_circle_1:update_circle_1}" class="circle_color_background_1"></div>
                        <div :class="{update_circle_2:update_circle_2}" class="circle_color_background_2"></div>
                        <div :class="{update_circle_3:update_circle_3}" class="circle_color_background_3"></div>
                        <div :class="{update_circle_4:update_circle_4}" class="circle_color_background_4"></div>
                        <div :class="{update_circle_5:update_circle_5}" class="circle_color_background_5"></div>
                        <div :class="{update_circle_6:update_circle_6}" class="circle_color_background_6"></div>

                </div>

                    <video :class="{update_vid:update_circle_1}" class="circle_vid" autoplay muted playsinline loop data-lag="5">
                        <source src="~/assets/content/homepage/circle_vids/new/next_vid_square_reduced.mp4" type="video/mp4">
                    </video>
                    <video :class="{update_vid:update_circle_2}" class="circle_vid" autoplay muted playsinline loop data-lag="5">
                        <source src="~/assets/content/homepage/circle_vids/new/nano_1.mp4" type="video/mp4">
                    </video>
                    <video :class="{update_vid:update_circle_3}" class="circle_vid" autoplay muted playsinline loop data-lag="5">
                        <source src="~/assets/content/homepage/circle_vids/new/oil_and_gas.mp4" type="video/mp4">
                    </video>
                    <video :class="{update_vid:update_circle_4}" class="circle_vid" autoplay muted playsinline loop data-lag="5">
                        <source src="~/assets/content/homepage/circle_vids/new/gww.mp4" type="video/mp4">
                    </video>
                    <video :class="{update_vid:update_circle_5}" class="circle_vid" autoplay muted playsinline loop data-lag="5">
                        <source src="~/assets/content/homepage/circle_vids/new/impossible.mp4" type="video/mp4">
                    </video>
                    <video :class="{update_vid:update_circle_6}" class="circle_vid" autoplay muted playsinline loop data-lag="5">
                        <source src="~/assets/content/homepage/home_333.mp4" type="video/mp4">
                    </video>


            </div>


                <div class="funds">
                    <h5 class="active_funds">Selected Funds</h5>


                    <h5 @click="route_to_circles('fund_pages/next_ai')" @mouseover="update_circle_1=true" @mouseleave="update_circle_1=false" class="fund"><img class="invest_arrow" src="~/assets/content/homepage/arrow_medium_light.svg">Next AI</h5>

            
                    <h5 @click="route_to_circles('fund_pages/nano')" @mouseover="update_circle_2=true" @mouseleave="update_circle_2=false" class="fund">
                        <img class="invest_arrow" src="~/assets/content/homepage/arrow_medium_light.svg">NanoCarbon</h5>


                    <h5 @click="route_to_circles('fund_pages/eco')" @mouseover="update_circle_3=true" @mouseleave="update_circle_3=false" class="fund"><img class="invest_arrow" src="~/assets/content/homepage/arrow_medium_light.svg">Eco Energy</h5>

           
                    <h5 @click="route_to_circles('fund_pages/green_worldwide')" @mouseover="update_circle_4=true" @mouseleave="update_circle_4=false" class="fund"><img class="invest_arrow" src="~/assets/content/homepage/arrow_medium_light.svg">Green Worldwide</h5>
  

                    <h5 @click="route_to_circles('fund_pages/impossible')" @mouseover="update_circle_5=true" @mouseleave="update_circle_5=false" class="fund"><img class="invest_arrow" src="~/assets/content/homepage/arrow_medium_light.svg">Impossible Foods</h5>


                    <h5 @click="route_to_circles('investments')" @mouseover="update_circle_6=true" @mouseleave="update_circle_6=false" class="fund"><img class="invest_arrow" src="~/assets/content/homepage/arrow_medium_light.svg">All Funds</h5>
                </div>







                <div class="funds_mobile">


    <swiper :effect="'coverflow'" :modules="modules" :coverflowEffect="{rotate: -90, stretch: 0, depth: 100, modifier: 1, slideShadows: false, }" :freemode="true" :loop="true" :speed="4000" :freeModeMomentum="true" :centeredSlides="true"  :grabCursor="true" :slides-per-view="1" :space-between="50" :autoplay="{delay: 1500, disableOnInteraction: false}" style="transition-timing-function:linear" @slideChange="swiper_index" @beforeSlideChangeStart="swiper_hide">



<swiper-slide><h3 @click="route_to_circles('fund_pages/next_ai')"  class="circle_swiper">Next AI<br><br><span class="swiper_span">View ➜</span></h3></swiper-slide>

<swiper-slide><h3 @click="route_to_circles('fund_pages/nano')" class="circle_swiper">NanoCarbon<br><br><span class="swiper_span">View ➜</span></h3></swiper-slide>

<swiper-slide><h3 @click="route_to_circles('fund_pages/eco')" class="circle_swiper">Eco Energy</h3></swiper-slide>

<swiper-slide><h3 @click="route_to_circles('fund_pages/green_worldwide')" class="circle_swiper">Green Worldwide<br><br><span class="swiper_span">View ➜</span></h3></swiper-slide>

<swiper-slide><h3 @click="route_to_circles('fund_pages/impossible')" class="circle_swiper">Impossible Foods<br><br><span class="swiper_span">View ➜</span></h3></swiper-slide>

<swiper-slide><h3 @click="route_to_circles('fund_pages/neuralink')"  class="circle_swiper">Neuralink<br><br><span class="swiper_span">View ➜</span></h3></swiper-slide>

<swiper-slide><h3 @click="route_to_circles('investments')" class="circle_swiper">All Funds<br><br><span class="swiper_span">View ➜</span></h3></swiper-slide>


</swiper>

                </div>







                </div>
            </div>
        </div>


</template>


<script setup>



import { Swiper, SwiperSlide } from 'swiper/vue';
import { Autoplay, EffectCoverflow } from "swiper";
import { gsap } from 'gsap'
import { SplitText } from 'gsap/SplitText'
import { ScrollTrigger } from 'gsap/ScrollTrigger'



import 'swiper/css/bundle';
import "swiper/css/effect-coverflow";

const update_circle_1 = ref(false)
const update_circle_2 = ref(false)
const update_circle_3 = ref(false)
const update_circle_4 = ref(false)
const update_circle_5 = ref(false)
const update_circle_6 = ref(false)


      
const modules = [EffectCoverflow, Autoplay]



function swiper_index(swiper) {
    // eval("update_circle_" + String(swiper.realIndex + 1)).value = true
    if (swiper.realIndex == 0){
        update_circle_1.value = true
    } else if (swiper.realIndex == 1){
        update_circle_2.value = true
    } else if (swiper.realIndex == 2){
        update_circle_3.value = true
    } else if (swiper.realIndex == 3){
        update_circle_4.value = true
    } else if (swiper.realIndex == 4){
        update_circle_5.value = true
    } else if (swiper.realIndex == 5){
        update_circle_6.value = true
    }
}

function swiper_hide(){
    update_circle_1.value = false
    update_circle_2.value = false
    update_circle_3.value = false
    update_circle_4.value = false
    update_circle_5.value = false
    update_circle_6.value = false
}







function route_to_circles(route_to){
    preloadRouteComponents(route_to)
    navigateTo(route_to)
}

</script>

<style>






.home_investment_section{
    margin-top:5%;
    z-index:5;
    overflow: hidden;
}

.white_container_home_circle{
    width:100%;
    height: 100% !important;
    background-color: #fff;
    z-index:1;
        mix-blend-mode: difference;
    padding: 10% 0%;
} 

.invest_grid{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 1fr;
grid-column-gap: 50px;
grid-row-gap: 0px;
align-items: center;
}


.active_funds{
    color:rgb(255, 255, 255);
    margin-top:10vh;
    padding-left:0px;
    margin-bottom:155px;
    text-decoration: underline;
  text-decoration-color: #e68712;
  text-underline-offset: 8px;
}

.funds_mobile{
    display:none;
}

.funds{
    overflow:hidden;
}

.fund{
    color:rgb(255, 255, 255);
    margin-top:-15%;
    padding:30px 0px;
    overflow:hidden;
    white-space: nowrap;
    cursor: pointer;
}

.fund:hover{
    padding-left:200px;
    transition: all ease 1s;
}


.fund:last-child{
    color:rgb(255, 255, 255);
    margin-top:120px;
    width:0px;
    padding:10px 0px;
    padding-bottom:3px;
    border-bottom: 3px solid rgb(255, 255, 255);
    cursor: pointer;
    overflow: visible;
    text-decoration: underline;
    text-decoration-thickness: 2px;
    text-underline-offset: 11px;
    text-decoration-color: #fff;
}

.fund:last-child:hover{
    width:40%;
    padding:10px 20%;
    padding-bottom:3px;
    border-bottom: 3px solid #e68712;
    text-decoration-color: #00000000;
    overflow: visible;
    transition: width ease 1s, padding ease 1s, border-bottom ease 1s, text-decoration-color ease .35s ;
}

.fund:last-child:hover .invest_arrow{
    transition: all ease 1s;
    margin-left:-120px;
    margin-right:20px;
    cursor: pointer;
}



.invest_arrow{
    width:200px;
    margin-left:-320px;
    margin-right:120px;
    margin-top:10px;
    filter: invert(1);
}

.fund:hover .invest_arrow{
    transition: all ease 1s;
    margin-left:-220px;
    margin-right:20px;
    cursor: pointer;
}


.invest_circle{
    width:50vh;
    margin-left:15%;
    border:#000 3px solid;
    height:50vh;
    border-radius: 100%;
    overflow: hidden;
}

.circle_color_background_1{
    width:50vh;
    margin-left:25%;
    height:50vh;
    margin-top:47.5vh;
    border-radius: 100%;
    background-color:rgb(17, 101, 210);
    position:absolute;
    top:20%;
    left:50%;
    z-index:-10;
    transition: all 2.5s;
}

.circle_color_background_2{
    width:50vh;
    margin-left:25%;
    height:50vh;
    margin-top:47.5vh;
    border-radius: 100%;
    background-color:rgb(254, 200, 35);
    position:absolute;
    top:20%;
    left:-90%;
    z-index:-10;
    transition: all 2.5s;
}


.circle_color_background_3{
    width:50vh;
    margin-left:25%;
    height:50vh;
    margin-top:47.5vh;
    border-radius: 100%;
    background-color:rgb(254, 35, 35);
    position:absolute;
    top:-200%;
    left:-100%;
    z-index:-10;
    transition: all 2.5s;
}

.circle_color_background_4{
    width:50vh;
    margin-left:25%;
    height:50vh;
    border-radius: 100%;
    background-color:rgb(171, 27, 207);
    position:absolute;
    top:-200%;
    left:100%;
    z-index:-10;
    transition: all 2.5s;
}

.circle_color_background_5{
    width:50vh;
    margin-left:25%;
    height:50vh;
    margin-top:100%;
    border-radius: 100%;
    background-color:rgb(12, 229, 233);
    position:absolute;
    top:50px;
    left:250px;
    z-index:-10;
    transition: all 2.5s;
}

.circle_color_background_6{
    width:50vh;
    margin-left:25%;
    height:50vh;
    margin-top:100%;
    border-radius: 100%;
    background-color:rgb(239, 254, 35);
    position:absolute;
    top:20%;
    left:-100%;
    z-index:-10;
    transition: all 2.5s .75s;
}

.update_circle_1{
    top:-200%;
    left:-80%;
    transition: all 4s .1s;
    background-color: green !important;
}

.update_circle_2{
    top:-200%;
    left:30%;
    transition: all 4s .1s;
    background-color: rgb(148, 227, 31) !important;
}

.update_circle_3{
    top:50%;
    left:70%;
    transition: all 4s .1s;
    background-color: rgb(190, 4, 69) !important;
}

.update_circle_4{
    top:90%;
    left:-90%;
    transition: all 4s .1s;
    background-color: rgb(123, 76, 234) !important;
}

.update_circle_5{
    top:-200%;
    left:-80%;
    transition: all 4s .1s;
    background-color: rgb(69, 224, 152) !important;
}

.update_circle_6{
    top:-200%;
    left:45%;
    transition: all 4s .1s;
    background-color: rgb(232, 177, 25) !important;
}

.circle_vid{
    position:absolute;
    object-fit: cover;
    border-radius:100%;
    overflow:hidden;
    width:20vh;
    height: 20vh;
    -webkit-transform: translateZ(0);
    height:auto;
    top:30%;
    left:15%;
    opacity:0;
    filter: drop-shadow(3px 3px 4px #0000006d);
    transition: all .2s;
}

.update_vid{
    top:30%;
    left:9.75%;
    object-fit: cover;
    display: inline;
    border-radius:100%;
    -webkit-transform: translateZ(0);
    transition: all 1s;
    width:43vh;
    height: 43vh;
    -webkit-animation: moveit 2s ease forwards;
          animation: moveit 2s ease forwards;
  will-change: transform;
}


.swiper_span{
    font-size:18px;
    color:rgb(25, 120, 237)
}

@-webkit-keyframes moveit {
  0% {
    transform: translateY(190px); opacity:.9;
  }
  20% {
    transform: translateY(-50px); opacity:.9;
  }
  40% {
    transform: translateY(50px); opacity:1;
  }
  60% {
    transform: translateY(62px); opacity:1;
  }
  80% {
    transform: translateY(60px); opacity:1;
  }
  100% {
    transform: translateY(60px); opacity:1;
  }
}

@keyframes moveit {
  0% {
    transform: translateY(80px); opacity:.9;
  }
  20% {
    transform: translateY(-50px); opacity:1;
  }
  40% {
    transform: translateY(50px); opacity:1;
  }
  60% {
    transform: translateY(20px); opacity:1;
  }
  80% {
    transform: translateY(40px); opacity:1;
  }
  100% {
    transform: translateY(30px); opacity:1;
  }
}


@media only screen and (min-width: 800px) and (max-width: 992px) {

.white_container_home_circle{
    width:100%;
    height: 180% !important;
} 

}




@media only screen and (min-width: 992px) and (max-width: 1200px) {

    

    .funds_mobile{
    display:none;
}


.invest_arrow{
    width:150px;
    margin-left:-250px;
    margin-right:140px;
}


    .circle_vid{
    width:10vh;
    height:10vh;
    top:32%;
    left:15%;
}

.update_vid{
    width:33vh;
    height:33vh;
    top:36%;
    left:10%;

}


.invest_circle{
width:40vh;
height:40vh;
}

.circle_color_background_1{
    width:40vh;
height:40vh;
}

.circle_color_background_2{
    width:40vh;
height:40vh;
}


.circle_color_background_3{
    width:40vh;
height:40vh;
}

.circle_color_background_4{
    width:40vh;
height:40vh;
}

.circle_color_background_5{
    width:40vh;
height:40vh;
}

.circle_color_background_6{
    width:40vh;
height:40vh;
}

}



@media only screen and (min-width: 768px) and (max-width: 992px) {



    .invest_arrow{
    width:90px;
    margin-left:-180px;
    margin-right:110px;
}

.funds_mobile{
    display:none;
}

.fund{
    padding:25px 0px;
}

.fund:last-child{
    margin-top:75px;
    width:0px;
}

    .circle_vid{
    width:10vh;
    height:10vh;
    top:32%;
    left:15%;
}

.update_vid{
    width:33vh;
    height:33vh;
    top:34.5%;
    left:10%;
}


.invest_circle{
width:40vh;
height:40vh;
}

.circle_color_background_1{
    width:40vh;
height:40vh;
}

.circle_color_background_2{
    width:40vh;
height:40vh;
}


.circle_color_background_3{
    width:40vh;
height:40vh;
}

.circle_color_background_4{
    width:40vh;
height:40vh;
}

.circle_color_background_5{
    width:40vh;
height:40vh;
}

.circle_color_background_6{
    width:40vh;
height:40vh;
}

}


@media only screen and (min-width: 576px) and (max-width: 768px) {

    .invest_grid{
    display: grid;
grid-template-columns: 1fr;
grid-template-rows: repeat(2, 1fr);
grid-column-gap: 0px;
grid-row-gap: 0px;
align-items: center;
}


.funds{
display:none
}

.funds_mobile{
    width:90%;
    margin-left:5%;
    z-index:10;
    display: block;
    position: absolute;
    margin-top:90%;

}


.circle_swiper{
    color:#000;
    text-align: center;
    cursor: pointer;
    line-height: .7;
}


.invest_circle{
    margin-top:15%;
    width:50vh;
    margin-left:25%;
    height:50vh;
}



.circle_vid{
    width:10vh;
    height:10vh;
    top:25%;
    left:45%;
}

.update_vid{
    width:45vh;
    height:45vh;
    top:12%;
    left:28%;
}

}

@media only screen and (min-width: 0px) and (max-width: 576px) {


    .invest_grid{
    display: grid;
grid-template-columns: 1fr;
grid-template-rows: repeat(2, 1fr);
grid-column-gap: 0px;
grid-row-gap: 0px;
align-items: center;
}


.funds{
display:none
}

.funds_mobile{
    width:90%;
    margin-left:5%;
    z-index:10;
    display: block;
    position: absolute;
    margin-top:135%;

}


.circle_swiper{
    color:#000;
    text-align: center;
    font-size:35px;
    line-height: .7;
}


.invest_circle{
    margin-top:65%;
    width:40vh;
    margin-left:12%;
    height:40vh;
}

.circle_vid{
    top:30%;
    left:32%;
    width:28vh;
height:28vh;
transition: all .2s;
}

.update_vid{
    top:18.5%;
    left:17%;
    width:28vh;
height:28vh;
}

.invest_circle{
width:30vh;
height:30vh;
}

.circle_color_background_1{
    width:30vh;
height:30vh;
top:-250%;
    left:-100%;
}

.circle_color_background_2{
    width:30vh;
height:30vh;
}


.circle_color_background_3{
    width:30vh;
height:30vh;
margin-left:20%;
    margin-top:35vh;
}

.circle_color_background_4{
    width:30vh;
height:30vh;
}

.circle_color_background_5{
    width:30vh;
height:30vh;
}

.circle_color_background_6{
    width:30vh;
height:30vh;
}

.invest_grid{
margin-bottom:-30% !important;
margin-top:-20% !important
}



}

@media only screen and (min-width: 0px) and (max-width: 376px) {
    .invest_circle{
    margin-left:22%;
    top:50%;
}

.circle_vid{
    left:25%;
    top:10%
}

.update_vid{
    left:25%;
    top:21%;
}

.invest_grid{
margin-bottom:-50%
}

}

@media only screen and (min-width: 376px) and (max-width: 576px) {
    .invest_circle{
    margin-left:20%;
    top:20%;
}

.circle_vid{
    left:25%;
    top:10%
}

.update_vid{
    left:22.5%;
    top:22%;
}

.invest_grid{
margin-bottom:10%;
margin-top:0%;
}

}


@media only screen and (min-width: 1200px) and (max-width: 1400px) {

    .circle_vid{
    width:20vh;
    height: 20vh;
    top:34%;
    left:15%;
}

.update_vid{
    width:43vh;
    height:43vh;
    top:34%;
    left:10%;
}
}

@media only screen and (min-width: 1400px) and (max-width: 1800px) {

.circle_vid{
width:20vh;
height: 20vh;
top:34%;
left:15%;
}

.update_vid{
width:43vh;
height:43vh;
top:34.5%;
left:9.75%;
}
}

</style>