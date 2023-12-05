<template>

<div>

<Header/>
    <GSAPScrollSmoother>

    
      <div v-if="!is_mobile" class="hero">
       <div class="hero__inner constrain">
        <div class="hero__image-cont">
         <img src="~/assets/content/about/about_1.jpg" />
         <div class="anim-swipe"></div>
        </div>
        <div class="hero__image-cont">
         <img src="~/assets/content/about/about_1.jpg" />
         <div class="anim-swipe"></div>
        </div>
        <div class="hero__image-cont">
         <img src="~/assets/content/about/about_1.jpg" />
         <div class="anim-swipe"></div>
        </div>
        <div class="hero__image-cont">
         <img src="~/assets/content/about/about_1.jpg" />
         <div class="anim-swipe"></div>
        </div>
        <div class="hero__image-cont">
         <img src="~/assets/content/about/about_1.jpg" />
         <div class="anim-swipe"></div>
        </div>
        <div class="hero__image-cont">
         <img src="~/assets/content/about/about_1.jpg" />
         <div class="anim-swipe"></div>
        </div>
       </div>
      </div>

      <div v-else><img class="mobile_landing_img" src="~/assets/content/about/about_1.jpg" /></div>

      <h1 class="about_title" data-speed=".6">About Us</h1>

    
    
    <h3 v-if="!is_mobile" class="about_subtitle" data-speed=".6">Why People Choose Us</h3>
    <h3 v-else class="about_subtitle" data-speed=".9">Why People Choose Us</h3>
    
    <div class="center_text_container" data-speed="1.1" data-lag=".2">
        <p class="about_center_text">
          GET Equity Partners is a finance company that focuses on unique, high-growth, high-return funds. From pre-IPO companies to slightly more conservative income funds, GET Equity Partners is a home for investors that want the feeling of being a multi-billion dollar titan while being qualified and or accredited per the SEC investor requirements. GET's white glove service and extraordinary investment types is what differentiates us from any other PE firm on the planet.
        </p>
      </div>
    
    <h1 class="partners_big" data-speed=".9">PARTNERS</h1>

      
        <div class="partners_container" id="get_height">
            <div class="partners_container_line"></div>
        <div class="partner_container_info">
        <h5 class="partners_title">Our Premium Partners</h5>
        <h6>Escrow Services</h6>
        <img class="partner_img" src="../assets/content/about/bank-of-america-logo.png" />
        <h6>Auditing</h6>
        <img class="partner_img" src="../assets/content/about/indigo_spire.png" />
        <h6>Legal Team</h6>
        <img class="partner_img" style="width:15%; margin-top:-50px" src="../assets/content/about/JP_logo.png" />
        <h6>Administration</h6>
        <img class="partner_img" src="../assets/content/about/notting.png" />
    </div>
</div>


<img v-if="!is_mobile" class="chs_img" data-speed="1.4" src="../assets/content/about/charleston.jpg" />
<img v-else class="chs_img" data-speed="1.05" src="../assets/content/about/charleston.jpg" />


<h1 class="office_big" data-speed=".9">CULTURE</h1>




<div class="swiper_container">
<swiper data-lag="1" :effect="'coverflow'" :modules="modules" :coverflowEffect="{rotate: -7, stretch: 0, depth: 100, modifier: 1, slideShadows: false, }" :freemode="true" :loop="true" :speed="3000" :freeModeMomentum="true" :centeredSlides="true"  :grabCursor="true" :breakpoints="swiperOptions.breakpoints" :autoplay="{delay: 1500, disableOnInteraction: false}" style="transition-timing-function:linear" @slideChange="swiper_index" class="about_swiper_wrapper">

<swiper-slide><img class="swiper_img" src="../assets/content/about/office_3_3.jpg" /></swiper-slide>
<swiper-slide><img class="swiper_img" src="../assets/content/about/office_2_2.jpg" /></swiper-slide>
<swiper-slide class="main_image"><img class="swiper_img" src="../assets/content/about/get_offices_3.jpg" />
  <div class="swiper_dropdown"><div class="swiper_line"></div><h6 class="swiper_title">Head Offices</h6><p class="swiper_subtitle">Chareston. SC</p></div>
</swiper-slide>
<swiper-slide><img class="swiper_img" src="../assets/content/about/office_4.jpg" /></swiper-slide>
<swiper-slide><img class="swiper_img" src="../assets/content/about/office_5.jpg" /></swiper-slide>

</swiper>
</div>


<div class="team_section">
<h1 class="team_big" data-speed="1.25">TEAM</h1>


<div v-if="!is_mobile">
<div class="team_member" style="margin-bottom:15%">
    <img data-lag=".1" class="naif_img" src="../assets/content/about/get_naif_1.jpg" />
    <div>
    <h6 class="naif_title">CEO</h6>
    <h5>Naif Hajjar</h5>
    </div>
</div>

<p class="naif_text">Led by Naif Hajjar, who has over 14 years experience in the financial industry. With over a decade on Wall Street, he has advised for a wide range of investment services at multi-billion dollar brokerage firms as well as disruptive clean energy companies.
        <br><br>
        During his tenure on Wall Street, his responsibilities have ranged from bringing public companies to their strategic bankers, providing trading and syndicate offerings to funds and institutions, as well as support and account services for corporations across all major exchanges. Success with multiple clients allowed him the privilege of ringing the closing bell at the Nasdaq Capital Markets in 2013 and the opening bell in 2014.
        <br><br>
        Naif is involved in design patents for ultra high efficiency green energy technologies, blueprinting a renewable oasis, and utility patents in antimicrobial consumer applications, as well as served as an advisor for governments in Africa, India, and intra-state USA.
        <br><br>
        GET Equity Partners is the evolution of these and other innovations to come.
    </p>



<div class="team_member" style="margin-top:10%">
    <div class="team_title">
        <h6 class="job_title">COO</h6>
    <h6 class="name">Jonathan Beirn</h6>
</div>
    <div class="team_img_container">
    <img data-speed=".9" class="team_img" src="../assets/content/about/get_jon_1.jpg" />
</div>
</div>

<div class="team_member" style="margin-top:10%">
    <div class="team_img_container">
    <img data-speed=".9" class="team_img" src="../assets/content/about/get_shaun_1.jpeg" />
</div>
    <div class="team_title">
    <h6 class="job_title">CTO</h6>
    <h6 class="name">Shaun Cohen</h6>
</div>
</div>

</div>




<div v-else>


  <img data-lag=".1" class="naif_img" src="../assets/content/about/get_naif_1.jpg" />
  <div style="margin-left:6%">
    <h6 class="mobile_job_title">CEO</h6>
    <h5 class="mobile_name">Naif Hajjar</h5>

    <p class="naif_text">Led by Naif Hajjar, who has over 14 years experience in the financial industry. With over a decade on Wall Street, he has advised for a wide range of investment services at multi-billion dollar brokerage firms as well as disruptive clean energy companies.
        <br><br>
        During his tenure on Wall Street, his responsibilities have ranged from bringing public companies to their strategic bankers, providing trading and syndicate offerings to funds and institutions, as well as support and account services for corporations across all major exchanges. Success with multiple clients allowed him the privilege of ringing the closing bell at the Nasdaq Capital Markets in 2013 and the opening bell in 2014.
        <br><br>
        Naif is involved in design patents for ultra high efficiency green energy technologies, blueprinting a renewable oasis, and utility patents in antimicrobial consumer applications, as well as served as an advisor for governments in Africa, India, and intra-state USA.
        <br><br>
        GET Equity Partners is the evolution of these and other innovations to come.
    </p>
  </div>
    <div class="team_img_container_mobile" style="float:left">
    <img data-speed=".9" class="team_img_mobile" src="../assets/content/about/get_jon_1.jpg" />
</div>
<div class="title_box_mobile">
<h6 class="mobile_job_title">COO</h6>
    <h6 class="mobile_name">Jonathan Beirn</h6>
  </div>


  <div class="team_img_container_mobile" style="float:right; margin-right:12%; margin-top:2%">
    <img data-speed=".9" class="team_img_mobile" src="../assets/content/about/get_shaun_1.jpeg" />
</div>
<div class="title_box_mobile">
<h6 class="mobile_job_title">CTO</h6>
    <h6 class="mobile_name">Shaun Cohen</h6>
  </div>



</div>



<div class="team_move_container">

  <div class="services_box">
    <div class="service" data-speed="1" data-lag="0.2"><img class="icon_img" src="../assets/content/about/jp.jpg"><p class="icon_text">Joshua Patterson</p></div>
    <div class="service" data-speed="1" data-lag="0.4"><img class="icon_img" src="../assets/content/about/reid.jpg"><p class="icon_text">Reid Kostenuck</p></div>
    <div class="service" data-speed="1" data-lag="0.6"><img class="icon_img" src="../assets/content/about/heidi_1.jpg"><p class="icon_text">Heidi Perez</p></div>
    <div class="service" data-speed="1" data-lag="0.8"><img class="icon_img" src="../assets/content/about/overstreet.png"><p class="icon_text">Nicholas Overstreet</p></div>

  </div>

<!-- <div class="services_box">
    <div class="service" data-speed="1" data-lag="0.2"><img class="icon_img" src="../assets/content/about/jp.jpg"><p class="icon_text">Joshua Patterson</p></div>
    <div class="service" data-speed="1" data-lag="0.4"><img class="icon_img" src="../assets/content/about/raina.png"><p class="icon_text">Rania Abboud</p></div>
    <div class="service" data-speed="1" data-lag="0.6"><img class="icon_img" src="../assets/content/about/caro.png"><p class="icon_text">Caro Chaves</p></div>
    <div class="service" data-speed="1" data-lag="0.8"><img class="icon_img" src="../assets/content/about/heidi_1.jpg"><p class="icon_text">Heidi Perez</p></div>

  </div>

  <div class="services_box" style="padding-bottom:200px">
    <div class="service" data-lag="1"><img class="icon_img" src="../assets/content/about/reid.jpg"><p class="icon_text">Reid Kostenuck</p></div>
    <div class="service" data-lag="0.8"><img class="icon_img" src="../assets/content/about/aiden.jpg"><p class="icon_text">Aiden Livingston</p></div>
    <div class="service" data-lag="0.6"><img class="icon_img" src="../assets/content/about/overstreet.png"><p class="icon_text">Nicholas Overstreet</p></div>
    <div class="service" data-lag="0.4"><img class="icon_img" src="../assets/content/about/person_4.jpg"><p class="icon_text">Ry</p></div>
  </div> -->

</div>


</div>




    
      <Footer/>
    </GSAPScrollSmoother>
    
  </div> 
    </template>
    
    
    
    
    <script setup>
    
    
    import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Autoplay, EffectCoverflow } from "swiper";
import 'swiper/css/bundle';
import "swiper/css/effect-coverflow";
import { useWindowSize } from '@vueuse/core'

const is_mobile = ref(false)
const { width, height } = useWindowSize()

onMounted(() => {
if(width.value < 768){
    is_mobile.value = true
}
})






      
const modules = [EffectCoverflow, Autoplay]



const swiperOptions = {
          breakpoints: {      
            0: {       
         slidesPerView: 1.5,
         spaceBetween: 40     
      }, 
      576: {       
         slidesPerView: 1.9,
         spaceBetween: 40     
      },          
      768: {       
         slidesPerView: 2.5,       
         spaceBetween: 40     
      },   
  
      992: {       
         slidesPerView: 2.9,       
         spaceBetween: 50     
      } 
   }   
}


const swiper_line_height = ref("0px")
const swiper_line_margin = ref("-90px")
const swiper_opacity = ref(0)
function swiper_index(swiper) {
    if(swiper.realIndex == 2){
        swiper_line_height.value = "105px"
        swiper_line_margin.value = "0px"
        swiper_opacity.value = 1
    }
    if(swiper.realIndex == 4){
        swiper_line_height.value = "0px"
        swiper_line_margin.value = "-90px"
        swiper_opacity.value = 0
    }
    
}




    
    </script>
    
    
    
    <style scoped>
    
    
    .about_title{
        display:flex;
        justify-content:center;
        top:-50px;
        position:absolute;
        z-index:10;
        left:25%;
        width:50%;
        font-size:10vw
    }
    
    .hero {
      height: 100vh;
    }
    .hero__inner {
      height: 100%;
      display: grid;
      grid-template-columns: repeat(6, 1fr);
    
    }
    .hero__image-cont {
      position: relative;
      overflow: hidden;
    }
    .hero__image-cont:not(:last-child):after {
      content: "";
      position: absolute;
      right: 0px;
      height: 100%;
      top: 0;
      width: 2.5px;
      z-index: 999;
    }

    .hero__image-cont img{
      border-bottom:rgba(255, 255, 255, 0.5) 1px solid;
    }

    .hero__image-cont .anim-swipe {
      border-bottom:rgba(255, 255, 255, 0.241) 1px solid;
    }


    .hero__image-cont img,
    .hero__image-cont .anim-swipe {
      position: absolute;
      width: 700%;
      height: 60vh;
      top: 0;
      left: 0;
      object-fit: cover;
      object-position: top;
      transition:all .35s ease 0s;
    }
    .hero .anim-swipe {
      width: 100%;
      background-color: #000;
    }
    .hero__image-cont:nth-child(1) img {
      left: -100%;
    }
    .hero__image-cont:nth-child(2) img {
      left: -200%;
    }
    .hero__image-cont:nth-child(3) img {
      left: -300%;
    }
    .hero__image-cont:nth-child(4) img {
      left: -400%;
    }
    .hero__image-cont:nth-child(5) img {
      left: -500%;
    }
    .hero__image-cont:nth-child(6) img {
      left: -600%;
    }
    
    .spacer {
      height: 2vh;
    }
    .spacer2 {
      height: 200vh;
    }
    
    .scroll {
      position: fixed;
      bottom: 1rem;
      left: 50%;
      transform: translateX(-50%);
      z-index: 999;
      width: 75px;
        height: 75px;
    }
    
    
    .center_text_container{
      margin-top:10%;
      margin-bottom:200px;
      width:70%;
      margin-left:15%;
      border-bottom: 1px solid #fff;
      padding:10px;
      padding-bottom: 20px;
      transition: all 2s ease;
      background-color: #000;
      border-top-left-radius: 5%;
      border-top-right-radius: 5%;
    }
    
    .about_center_text{
      text-align:justify;
      font-size:25px;
      font-weight: 200;
    }
    
    .about_subtitle{
        position:absolute;
        top:82.5vh;
        left:5%;
        font-size:25px;
        text-decoration: underline;
    text-underline-offset: 5px;
    text-decoration-thickness: 1px;
    text-decoration-color: #1978ed;
    }

    .partners_big{
        margin-top:35vh;
        left:5%;
        font-size:18vw;
        margin-left:5%
    }
    
    .partners_container{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        margin-left:15%;
    }


    .partners_container_line{
        width:1px;
        border-left:#fff solid 4px;
        margin-top:15%;
        height:0px;
        position:absolute;
        transition: all .5s ease;
    }

    .partner_container_info{
        margin-left:15%;
        width:150%;
    }


    .partners_title{
        font-weight: 500;
        line-height: 0;
    }

    .partner_img{
        width:50%;
        margin-top:-10%
    }

    .office_big{
        margin-left:5%;
        font-size:21vw;
        line-height: 0;
        margin-top:-50%;
        z-index:1;
        font-weight: 900;
    }

    .chs_img{
        width:80%;
        margin-left:10%;
        z-index:-1;
        margin-top:35%;
        filter: grayscale(50%);
    }
    

.swiper_img{
    width:100%
}

.about_swiper_wrapper{
    width:100%;
    overflow: visible;
}

.swiper_container{
    position: absolute;
    margin-top:20%;
    width:100%
}

.swiper_line{
    width:1px;
    border-left:#fff solid 2px;
    height:v-bind(swiper_line_height);
    margin-left:30px;
    margin-top:v-bind(swiper_line_margin);
    opacity: v-bind(swiper_opacity);
    transition:all 1.5s ease;
}

.swiper_dropdown{
  position:absolute;
}



/* .main_image:hover .swiper_line{
    height:110px;
    margin-top:0px;
} */

.swiper_title{
    margin-left:50px;
    margin-top:-85px;
    font-size:200%;
    opacity: v-bind(swiper_opacity);
}
.swiper_subtitle{
    margin-left:50px;
    margin-top:-63px;
    opacity: v-bind(swiper_opacity);
}

.swiper_img{
    filter: grayscale(1);
}

.swiper_img:hover{
    filter: grayscale(0);
}

.team_big{
    font-size:24vw;
    margin-left:15%;
    font-weight: 900;
    margin-top:85%;
    line-height: 0;
}

.naif_img{
    width:75%;
    border-radius:100%;
    margin-top: 24%;
    border: 5px solid #1978ed00;
    padding:12px;
    box-shadow: -5px 8px 10px rgba(255, 255, 255, 0);
    transition: all .5s ease;
}

.naif_img:hover{
    border: 5px solid #1978ed;
    box-shadow: -5px 8px 10px rgba(255, 255, 255, 0.2);
    transition: all .5s ease;
}


.naif_title{
    line-height:1;
    width:90px;
    padding-bottom:7px;
    margin-bottom:-11%;
    text-decoration: underline;
  text-decoration-color: #3a6df0;
  text-underline-offset: 8px;
  margin-top:45%
 }

 .job_title{
    line-height:1;
    margin-bottom:-18%;
    text-decoration: underline;
  text-decoration-color: #3a6df0;
  text-underline-offset: 8px;
 }

.name{
  white-space: nowrap;
  margin-top:25%
}


 .naif_text{
    line-height: 1.5;
    width:70%;
    margin-left:15%;
    margin-top:-10%
 }


.team_member{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 1fr;
grid-column-gap: 0px;
grid-row-gap: 0px;
width:80%;
margin-left:12.5%;
margin-top:20%
}

.team_img_container{
    width:75%;
    height:50vh;
    border-radius:5%;
    overflow:hidden;
    transition: transform .8s ease;
}

.team_img_container_mobile{
  width:35%;
  margin-left:15%;
    height:250px;
    border-radius:10%;
    overflow:hidden;
    transition: transform .8s ease;
    margin-top:20%
}

.team_img_container_mobile:hover{
    transition: transform .8s ease;
    transform: scale(1.05);
}

.team_img{
    height:115%;
    margin-left:-25%;
    transition: width .5s ease;
    margin-top:-5%
}

.team_img_mobile{
    height:120%;
    margin-left:-45%;
    transition: width .5s ease;
    margin-top:-5%
}

.team_img_container:hover{
    transition: transform .8s ease;
    transform: scale(1.05);
}


.team_title{
    margin-top:25%;
}

.team_title:first-of-type{
    text-align: right;
    margin-right:25%
}







.services_box{
  height:300px;
  width:100%;
  display: flex;
  justify-content: space-evenly;
  padding-top:50px;
  margin-left:-2.5%

}

.service{
  height: 200px;
  width: 200px;
  border-radius: 25px;
}


.icon_img{
  width: 100%;
  height:100%;
  margin-top: 15px;
  border-radius: 10%;
  transition: transform .8s ease;
}

.icon_img:hover{
    transition: transform .8s ease;
    transform: scale(1.05);
}


.icon_text{
  font-size: 19px;
  margin-top: 10px;
  border-top:3px solid rgb(14, 85, 166);
  padding-top:7px
}

.team_move_container{
    margin-top:17.5%;
    margin-bottom:10%;
    width:95%;
    margin-left:5%
 }


 .mobile_landing_img{
  height:50vh;
  border-bottom:1px solid #fff
 }


.mobile_job_title{
  text-decoration: underline;
  text-decoration-color: #3a6df0;
  text-underline-offset: 8px;
  margin-bottom:-4%;
  text-align: center;
  width:80%;
  margin-left:5%;
  padding-top:5%
}


.mobile_name{
  text-align: center;
  width:80%;
  margin-left:5%
}



.title_box_mobile{
  margin-top:30%; 
  margin-left:10%
}












 @media only screen and (min-width: 0px) and (max-width: 576px) {


.team_move_container{
    margin-top:15%;
    margin-bottom:10%;
    padding-top:1%
 }
  .services_box{
  height:50px;
  width:85%;
  margin-left:7.5%;
  margin-top:15%
}

.service{
  height: 100px;
  width: 100px;
  border-radius: 25px;
}

.icon_img{
  width: 80%;
  height:80%;
  margin-top: 15px;
  border-radius: 10%;
  transition: transform .8s ease;
}

.icon_text{
  font-size: 12px;
  width:85%
}

.center_text_container{
  margin-top:45%;
      width:80%;
      margin-left:7.5%
    }
    
.about_center_text{
  font-size:125%
}

.partners_container{
        margin-bottom:20%;
    } 
.partners_big{
        margin-top:10vh;
    }


    .partners_title{
        font-weight: 500;
        line-height: 1;
    }

    .office_big{
        margin-left:2.5%;
        font-size:21vw;
        line-height: 0;
        margin-top:-50%;
        z-index:1;
        font-weight: 900;
    }

    .swiper_container{
    position: absolute;
    margin-top:30%;
    width:85%;
    margin-left:7%;
    display:block
}

    .about_swiper_wrapper{
    margin-top:-5%;
    width:100%
}

.team_big{
    margin-top:140%;
}

.about_subtitle{
  margin-top:-28%;
}

.naif_img{
  margin-left:7.5%
}

}

@media only screen and (min-width: 576px) and (max-width: 768px) {


.team_move_container{
    margin-top:15%;
    margin-bottom:10%;
    padding-top:1%
 }
  .services_box{
  height:50px;
  width:85%;
  margin-left:7.5%;
  margin-top:15%
}

.service{
  height: 100px;
  width: 100px;
  border-radius: 25px;
}

.icon_img{
  width: 80%;
  height:80%;
  margin-top: 15px;
  border-radius: 10%;
  transition: transform .8s ease;
}

.icon_text{
  font-size: 12px;
  width:85%
}

.center_text_container{
  margin-top:45%;
      width:80%;
      margin-left:7.5%
    }
    
.about_center_text{
  font-size:125%
}

.partners_big{
        margin-top:10vh;
    }


    .partners_title{
        font-weight: 500;
        line-height: 1;
    }

    .office_big{
        margin-left:5%;
        font-size:21vw;
        line-height: 0;
        margin-top:-5%;
        z-index:1;
        font-weight: 900;
    }

    .about_swiper_wrapper{
    margin-top:-5%;
    width:100%
}

.team_big{
    margin-top:50%;
}

.about_subtitle{
  margin-top:-24%;
}

.naif_img{
  margin-left:7.5%
}

}

@media only screen and (min-width: 768px) and (max-width: 992px) {
  .team_img{
    margin-left:-40%;
}
}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
  .team_img{
    margin-left:-35%;
}

}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
}


    </style>
    