<template>

<div style="overflow:hidden">

<Header/>
<GSAPScrollSmoother>



<section class="landing_elments">

    <video poster="~/assets/content/how_it_works/how_it_works_7.jpg" class="landing_vid" playsinline autoplay muted loop onloadstart="this.playbackRate = 2.25;">
  <source src="~/assets/content/how_it_works/video_1.mp4" type="video/mp4">
</video>


<div class="how_it_works_landing_text">
    <h6 class="how_it_works_landing_title"> GET Equity Partners democratizes access to the $500B+ market for pre-IPO and other private companies.
    <br><br>
<span class="landing_subtext">Companies are staying private for longer.</span>
</h6>
<p class="how_it_works_landing_p">Value creation in technology-enabled companies is increasingly occurring in the private markets. In 2004, companies typically went public after 4 years, today the average company IPOs after 10+ years.
<br><br>
Until recently, access to pre-IPO companies has been limited. GET is here to change that.</p>

</div>


<div class="landing_circle">
    <video class="landing_circle_vid" autoplay muted playsinline loop>
                <source src="../assets/content/homepage/home_333.mp4" type="video/mp4">
            </video>
</div>


</section>


<div class="landing_big_text_container_1">
    <div class="landing_big_text_1" >How It Works</div>
    </div>
    
    
    <div class="landing_big_text_container_2">
    <div class="landing_big_text_2" >How It Works</div>
    </div>
    



    <p id="anchor_1" class="main_description_services" data-speed="0.7" data-lag="0">At GET Equity Partners, we are creating a revolutionary financial framework which leverages industry leading technologies to algorithmically enhance a portfolio and provide personalized and actionable feedback for individuals and institutions.
</p>




 <HIWTextWithSlab id="anchor_2"/>




<HIWScrollerCube/>









<h1 class="FAQs_big" id="anchor_3">FAQS</h1>

<HIWFaqs/>




<div class="services">

    <h1 class="services_big" id="anchor_4">Services</h1>


    <h5 class="services_sub">Additional Services We Can Help You With</h5>
    <div class="services_line"></div>




    <swiper data-lag=".2" :effect="'coverflow'" :modules="modules" :coverflowEffect="{rotate: -2, stretch: 0, depth: 0, modifier: 1, slideShadows: true, }" :freemode="true" :loop="true" :speed="1500" :freeModeMomentum="true" :centeredSlides="true"  :grabCursor="true" :breakpoints="swiperOptions.breakpoints" style="transition-timing-function:linear" class="services_swiper_wrapper">





<swiper-slide><h5>Connect</h5><p class="services_swiper_text"> We can connect you to the movers and shakers in our extensive and prestigious network. </p></swiper-slide>

<swiper-slide><h5>Take Public</h5><p class="services_swiper_text">We can take your company public. It is not our first time. </p></swiper-slide>

<swiper-slide><h5>Private Raise</h5><p class="services_swiper_text">We can raise money for your start up.</p></swiper-slide>

<swiper-slide><h5>GET Media</h5><p class="services_swiper_text">A prominant arm of our business is our media company. This let's us supercharge our oefferings.</p></swiper-slide>



</swiper>

</div>







<Footer/>


</GSAPScrollSmoother>



</div>

</template>


<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { EffectCoverflow } from "swiper";
import 'swiper/css/bundle';
import "swiper/css/effect-coverflow";



      
const modules = [EffectCoverflow]



const swiperOptions = {
          breakpoints: {      
            0: {       
         slidesPerView: 1.5,
         spaceBetween: 20     
      }, 
      576: {       
         slidesPerView: 1.9,
         spaceBetween: 20     
      },          
      768: {       
         slidesPerView: 2.5,       
         spaceBetween: 40     
      },   
  
      992: {       
         slidesPerView: 4,       
         spaceBetween: 120     
      } 
   }   
}







</script>


<style scoped>





.how_it_works_landing_title {
    color: #fff;
    margin-top: 15%;
    font-size: 165%;
}

.landing_subtext{
  font-size: 80%;
  text-decoration: underline;
  text-decoration-color: #3a6df0;
  text-underline-offset: 5px;
  text-decoration-thickness: 1px;
}
.how_it_works_landing_p {
    color: #fff;
    font-size: 95%;
    margin-top:-6%
}

.how_it_works_landing_text {
    width: 40%;
    margin-left: 56%;
    padding-top: 5%;
    position: relative;
    position: absolute;
    word-spacing: 1px;
    color: #fff;
    z-index:1
}
.landing_vid {
    width: 50%;
    height: 100vh;
    object-fit: cover;
    position: absolute;
}
.landing_circle {
    width: 2000px;
    height: 2000px;
    border-radius: 50%;
    background-color: #000;
    margin-left: 115%;
    margin-top: -10%;
    overflow: hidden;
}
.landing_circle_vid {
    width: 100%;
    margin-top: 0;
    margin-left: -15%;
    filter: contrast(1.05);
}
.landing_big_text_1 {
    font-size: 13vw;
    margin-left: 10%;
    color: #fff;
    white-space: nowrap;

}

.landing_big_text_2 {
  margin-left: 10%;
    color: #fff;
    white-space: nowrap;
    font-size: 13.01vw;
}
.landing_big_text_container_1 {
    position: absolute;
    top: 55vh;
    padding-top: 28vh;
    display: flex;
    justify-content: space-between;
    mix-blend-mode: difference;
    white-space: nowrap;
    line-height: 1;
    left:0
}
.landing_big_text_container_2 {
    position: absolute;
    top: 55vh;
    padding-top: 28vh;
    display: flex;
    justify-content: space-between;
    z-index: -10;
    mix-blend-mode: difference;
    white-space: nowrap;
    line-height: 1;
    left:0
}


.main_description_services{
width:60%;
margin-left:20%;
margin-top:-15%;
color:#fff;
margin-bottom:20%;
font-size:200%;
text-align: justify;
}














.cube_grid{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 1fr;
grid-column-gap: 0px;
grid-row-gap: 0px;
margin-top:-15%
}

.cube_info{
    width:60%;
    margin-left:15%
}
.cube_info_grid{
    display: grid;
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(3, 1fr);
grid-column-gap: 0px;
grid-row-gap: 0px;
}


.info_elm{
    margin-top:50vh
}

.header_logo{
    width: var(--full_cube);
    mix-blend-mode: difference;
}



  .cube_hiw {
    width: var(--full_cube);
    height: var(--full_cube);
    position: relative;
    transform-style: preserve-3d;
    transform: rotateY(45deg);
    margin-left:25%;
    margin-top:2px;
    transition: all .25s ease;
  }

  .cube_hiw {
    transform: translateY(180px);
  }

  .face_hiw {
    position: absolute;
    width: var(--full_cube);
    height: var(--full_cube);
    text-align: center;
    font-size: 400px;
    color: white;
    background-color: #000;
    border: #fff 1px solid;
    line-height: var(--full_cube);
  }

  .front_hiw {
    transform: translateZ(var(--half_cube));
  }
  

  .back_hiw {
    transform: rotateY(180deg) translateZ(var(--half_cube));
  }

  .top_hiw {
    transform: rotateX(90deg) translateZ(var(--half_cube));
  }

  .bottom_hiw {
    transform: rotateX(-90deg) translateZ(var(--half_cube));
  }

  .left_hiw {
    transform: rotateY(-90deg) translateZ(var(--half_cube));
  }

  .right_hiw {
    transform: rotateY(90deg) translateZ(var(--half_cube));
  }








  .services{
    margin-top:15%
  }

  .services_big{
    margin-left:5%;
    font-size:23vw;
    margin-top:-5%;
  }

  .FAQs_big{
    margin-left:5%;
    font-size:23vw;
    margin-bottom:-8%
  }

  .services_sub{
    margin-left:5%;
    margin-top:-5%;
  }

  .services_line{
    width:80%;
    height:3px;
    background-color:rgb(14, 85, 166);
    margin-top:-5%;
    margin-left:5%;
    margin-bottom:10%
  }

  .services_swiper_text{
    width:100%;
    margin-top:-20%
}

.services_swiper_wrapper{
    margin-bottom:20%;
    margin-top:-5%
}








@media only screen and (min-width: 0px) and (max-width: 380px) {


.landing_elments{
    margin-top:-20%
}

.landing_big_text_container_1 {
    position: absolute;
    top: 55vh;
    padding-top: 35vh;
    display: flex;
    justify-content: space-between;
    mix-blend-mode: difference;
    white-space: nowrap;
    line-height: 1;
    left:0
}
.landing_big_text_container_2 {
    position: absolute;
    top: 55vh;
    padding-top: 35vh;
    display: flex;
    justify-content: space-between;
    z-index: -10;
    mix-blend-mode: difference;
    white-space: nowrap;
    line-height: 1;
    left:0
}





  .how_it_works_landing_text {
    width: 82.5%;
    margin-left: 75%;
    padding-top: 13%;
    position: relative;
    position: absolute;
    word-spacing: 1px;
    color: #fff;

}


.landing_vid {
    width: 64%;
    height: 100vh;
    object-fit: cover;
    position: absolute;
        margin-top: 0%;
}


.landing_circle {
    width: 1200px;
    height: 1200px;
    border-radius: 100%;
    background-color: #000;
    margin-left: 115%;
    margin-top: 20%;
    overflow: hidden;
    padding-top:70%
}

.landing_circle_vid {
    width: 65%;
    margin-top: 0%;
    margin-left: -7%;
    padding-top:7%;
    border-radius: 50%;
}



.main_description_services{
width:60%;
margin-left:20%;
margin-top:-95%;
color:#fff;
margin-bottom:20%;
font-size:125%;
text-align: center;
}


.FAQs_big{
    margin-left:5%;
    font-size:23vw;
    margin-bottom:-8%;
    padding-top:25%
  }




.services_swiper_text{
    width:100%;
    margin-top:-10%
}



}







@media only screen and (min-width: 380px) and (max-width: 576px) {




.landing_elments{
    margin-top:-20%
}

.landing_big_text_container_1 {
    position: absolute;
    top: 55vh;
    padding-top: 35vh;
    display: flex;
    justify-content: space-between;
    mix-blend-mode: difference;
    white-space: nowrap;
    line-height: 1;
    left:0
}
.landing_big_text_container_2 {
    position: absolute;
    top: 55vh;
    padding-top: 35vh;
    display: flex;
    justify-content: space-between;
    z-index: -10;
    mix-blend-mode: difference;
    white-space: nowrap;
    line-height: 1;
    left:0
}





  .how_it_works_landing_text {
    width: 82.5%;
    margin-left: 75%;
    padding-top: 16%;
    position: relative;
    position: absolute;
    word-spacing: 1px;
    color: #fff;

}


.landing_vid {
    width: 64%;
    height: 100vh;
    object-fit: cover;
    position: absolute;
        margin-top: 0%;
}


.landing_circle {
    width: 1200px;
    height: 1200px;
    border-radius: 100%;
    background-color: #000;
    margin-left: 115%;
    margin-top: 20%;
    overflow: hidden;
    padding-top:70%
}

.landing_circle_vid {
    width: 65%;
    margin-top: 0%;
    margin-left: -7%;
    padding-top:7%;
    border-radius: 100%;
}



.main_description_services{
width:60%;
margin-left:20%;
margin-top:-95%;
color:#fff;
margin-bottom:20%;
font-size:125%;
text-align: center;
}


.FAQs_big{
    margin-left:5%;
    font-size:23vw;
    margin-bottom:-8%;
    padding-top:25%
  }



.services_swiper_text{
    width:100%;
    margin-top:-10%
}



}

@media only screen and (min-width: 576px) and (max-width: 768px) {


.services_swiper_text{
    margin-top:-10%
}

}



@media only screen and (min-width: 768px) and (max-width: 992px) {
  
.services_swiper_text{
    margin-top:-10%
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