<template>

<div style="overflow: hidden;">

    <CircleTransition ref="cicle_tansition"/>

<div :class="{hide_vid:hide_vid}" class="loading_vid_container">
<video :class="{hide_vid:hide_vid}" class="loading_video" autoplay muted playsinline loop>
    <source src="../assets/content/homepage/get_intro.mp4" type="video/mp4">
</video>
</div>


<!-- <span style="z-index:100000">
  <VuePreloader
    background-color="#0000"
    color="#ffffff"
    transition-type="fade-up"
    :loading-speed="60"
    :transition-speed="1000"
    @loading-is-over="loadingIsOver"
    @transition-is-over="transitionIsOver">

  <video style="z-index:100000" class="loading_video" autoplay muted playsinline loop>
    <source src="../assets/content/homepage/get_intro.mp4" type="video/mp4">
</video>

</VuePreloader>

</span> -->



<Header/>

    <GSAPScrollSmoother>

        <div class="transition_padding"></div>

            <h1 class="landing_title_home" ref="under_loader">GET</h1>
            <div class="landing_line"></div>
            <h4 class="landing_sub_title">Venture Studio</h4>
            <h6 class="landing_sub_title_2" ref="subtext_target">GET Equity Partners</h6>
            <p class="landing_text">Innovating Financial Relationships</p>
            <div class="landing_vid_container">
            <video poster="~/assets/content/homepage/homepage_poster.png" style="filter:contrast(1.05);"  class="landing_video" autoplay muted playsinline loop>
                <source src="~/assets/content/homepage/home_333.mp4" type="video/mp4">
            </video>
            <div class="landing_text_box" data-speed="1.5">
            <div class="landing_letter_1">G</div>
            <div class="landing_letter_2">E</div>
            <div class="landing_letter_3">T</div>
            </div>


            <p v-if="!is_mobile" class="video_text" data-speed=".75">We are a unique financial organization with the goal of offering top quality private opportunities while spreading the benefit to a wider audience of previously restricted offerings.  
            <br><br>GET gives you access to the <span class="big_emphasis">$500B+ </span><br>market for pre-IPO companies
            </p>

            <p v-else class="video_text" data-speed=".85">We are a unique financial organization with the goal of offering top quality private opportunities while spreading the benefit to a wider audience of previously restricted offerings.  
            <br><br>GET gives you access to the <span class="big_emphasis">$500B+ </span><br>market for pre-IPO companies
            </p>





        </div>

        <div class="home_about_section">
            <h5 class="about_text">GET Equity Partners focuses on early and mid-stage companies that are undervalued and/or yet to be discovered. Our tech forward approach allows us to offer innovative financing and partnering solutions across a wide array of sectors.
 </h5>

            <div class="scrub_line"></div>

        </div>


        <div class="invest_text" data-lag=".3">INVEST</div>


        <HomePageInvestCircle />


        <HomePageHoverSection />


            <div class="home_partner_section">
            <h6 class="partner_text">GET Equity Partners works with forward-thinking firms, enterprises, and startups to offer intelligent growth and financing solutions at all stages of growth. </h6>




        <swiper data-lag="1" :effect="'coverflow'" :modules="modules" :coverflowEffect="{rotate: -7.5, stretch: 0, depth: 100, modifier: 1, slideShadows: false, }" :freemode="true" :loop="true" :speed="1800" :freeModeMomentum="true" :centeredSlides="true"  :grabCursor="true" :breakpoints="swiperOptions.breakpoints" :autoplay="{delay: 1500, disableOnInteraction: true}" class="swiper_wrapper" style="transition-timing-function:linear">





            <swiper-slide><div><img class="partner_swiper_img" style="width:250px; margin-left:-45px" src="../assets/content/homepage/logos/jp_morgan.png"><p class="partner_swiper_text">Our Banking Agent</p></div></swiper-slide>


<swiper-slide><div><img class="partner_swiper_img" style="width:200px; margin-left:-25px" src="../assets/content/homepage/logos/plaid.png"><p class="partner_swiper_text">Our Accredidation Partners </p></div></swiper-slide>

<swiper-slide><div><img class="partner_swiper_img" style="width:250px; margin-left:-25px" src="../assets/content/homepage/logos/dwolla.png"><p class="partner_swiper_text">Our Transfer Custodians </p></div></swiper-slide>

<swiper-slide><div><img class="partner_swiper_img" style="width:300px; margin-left:-40px" src="../assets/content/homepage/logos/b_of_a.png"><p class="partner_swiper_text">Our Banking Agent </p></div></swiper-slide>

<swiper-slide><div><img class="partner_swiper_img" style="width:90px; margin-left:5px; margin-top:-20px" src="../assets/content/homepage/logos/JP_logo.png"><p class="partner_swiper_text">Our Legal Team</p></div></swiper-slide>


<!-- --------------------------------------------- DUPLICATE --------------------------------------------- -->
<!-- --------------------------------------------- DUPLICATE --------------------------------------------- -->

<swiper-slide><div><img class="partner_swiper_img" style="width:250px; margin-left:-45px" src="../assets/content/homepage/logos/jp_morgan.png"><p class="partner_swiper_text">Our Banking Agent</p></div></swiper-slide>


<swiper-slide><div><img class="partner_swiper_img" style="width:200px; margin-left:-25px" src="../assets/content/homepage/logos/plaid.png"><p class="partner_swiper_text">Our Accredidation Partners </p></div></swiper-slide>

<swiper-slide><div><img class="partner_swiper_img" style="width:250px; margin-left:-25px" src="../assets/content/homepage/logos/dwolla.png"><p class="partner_swiper_text">Our Transfer Custodians </p></div></swiper-slide>

<swiper-slide><div><img class="partner_swiper_img" style="width:300px; margin-left:-40px" src="../assets/content/homepage/logos/b_of_a.png"><p class="partner_swiper_text">Our Banking Agent </p></div></swiper-slide>

<swiper-slide><div><img class="partner_swiper_img" style="width:90px; margin-left:5px; margin-top:-20px" src="../assets/content/homepage/logos/JP_logo.png"><p class="partner_swiper_text">Our Legal Team</p></div></swiper-slide>
<!-- --------------------------------------------- DUPLICATE --------------------------------------------- -->


<!-- --------------------------------------------- DUPLICATE --------------------------------------------- -->
<!-- --------------------------------------------- DUPLICATE --------------------------------------------- -->


<swiper-slide><div><img class="partner_swiper_img" style="width:250px; margin-left:-45px" src="../assets/content/homepage/logos/jp_morgan.png"><p class="partner_swiper_text">Our Banking Agent</p></div></swiper-slide>


<swiper-slide><div><img class="partner_swiper_img" style="width:200px; margin-left:-25px" src="../assets/content/homepage/logos/plaid.png"><p class="partner_swiper_text">Our Accredidation Partners </p></div></swiper-slide>

<swiper-slide><div><img class="partner_swiper_img" style="width:250px; margin-left:-25px" src="../assets/content/homepage/logos/dwolla.png"><p class="partner_swiper_text">Our Transfer Custodians </p></div></swiper-slide>

<swiper-slide><div><img class="partner_swiper_img" style="width:300px; margin-left:-40px" src="../assets/content/homepage/logos/b_of_a.png"><p class="partner_swiper_text">Our Banking Agent </p></div></swiper-slide>

<swiper-slide><div><img class="partner_swiper_img" style="width:90px; margin-left:5px; margin-top:-20px" src="../assets/content/homepage/logos/JP_logo.png"><p class="partner_swiper_text">Our Legal Team</p></div></swiper-slide>

<!-- --------------------------------------------- DUPLICATE --------------------------------------------- -->



</swiper>

</div>





<div class="pin_scroll_section">

    <div class="video_overlay" data-speed="1.75" data-lag="2"></div>
    <video class="pin_scroll_video" autoplay muted playsinline loop data-speed="1.75" data-lag="2">
                <source src="../assets/content/homepage/home_333.mp4" type="video/mp4">
            </video>

   <h5 class="pinned_text" data-speed="2.5" >What We Offer</h5>

    <div class="scroll_text"><h5 class="scroll_title">Access Private Technology Companies</h5><div @click="HIW_anchor('HowItWorks', '#anchor_1')" class="learn_more">Learn More</div></div>
    <div class="scroll_text"><h5 class="scroll_title">Company-Friendly Transactions</h5><div @click="HIW_anchor('HowItWorks', '#anchor_2')" class="learn_more">Learn More</div></div>
    <div class="scroll_text"><h5 class="scroll_title">Curated Investments</h5><div @click="HIW_anchor('HowItWorks', '#anchor_3')" class="learn_more">Learn More</div></div>
    <div class="scroll_text"><h5 class="scroll_title">Guided Transactions</h5><div @click="HIW_anchor('HowItWorks', '#anchor_4')" class="learn_more">Learn More</div></div>

</div>



<Footer/>


    </GSAPScrollSmoother>



</div>

</template>


<script setup>
import { VuePreloader } from 'vue-preloader';
import '@/node_modules/vue-preloader/dist/style.css'

import { Swiper, SwiperSlide } from 'swiper/vue';
import { Autoplay, EffectCoverflow } from "swiper";
import { useElementVisibility } from '@vueuse/core'
import { useIntersectionObserver } from '@vueuse/core'


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


// const nuxtApp = useNuxtApp()
  
// nuxtApp.hook('page:start', () => {
//   console.log('page load start --- XXXXXXXXXXXXX')
// })
// nuxtApp.hook('page:finish', () => {
//   console.log('page load finish HOME')
// })




const modules = [EffectCoverflow, Autoplay]



const swiperOptions = {
          breakpoints: {      
            0: {       
         slidesPerView: 1.25,
         spaceBetween: 40     
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
         slidesPerView: 3.5,       
         spaceBetween: 120     
      } 
   }   
}




     


        // sleep time expects milliseconds
        function sleep (time) {
          return new Promise((resolve) => setTimeout(resolve, time));
        }


const transition_padding_height = ref("70vh")
const landing_line_width = ref("0%")
const landing_sub_title_margin = ref("300%")
const vid_scale = ref(1.25)


const hide_vid = ref(true)
const vid_margin = ref('0%')

const nuxtApp = useNuxtApp()
nuxtApp.hook("page:start", () => {
    hide_vid.value = false
    sleep(1001).then(() => { 
     transition_padding_height.value = "80vh"
    landing_line_width.value = "0%"
    landing_sub_title_margin.value = "300%"
    })
    sleep(2000).then(() => { 
        vid_scale.value = 0.8
})
    sleep(2700).then(() => { 
        vid_margin.value = '-100%'
})
    sleep(60000).then(() => { 
        hide_vid.value = true
})

sleep(3500).then(() => { 
    landing_line_width.value = "67%"
    landing_sub_title_margin.value = "75%"
})

sleep(3150).then(() => { 
    transition_padding_height.value = "103px"
})
sleep(4000).then(() => { 
    transition_padding_height.value = "103px"
})

sleep(7000).then(() => { 
    transition_padding_height.value = "0px"
})

});
// nuxtApp.hook("page:finish", () => {
// //   loading.value = false;
// });

// if(hide_vid.value == false){
//     land_trans_sleep.value = 8000
//     land_trans_sleep_2.value = 12000
// }
// else{
//     land_trans_sleep.value = 1000
//     land_trans_sleep_2.value = 4000
// }



// const under_loader = ref(null)
// const underIsVisible = useElementVisibility(under_loader)
// console.log(underIsVisible.value)

// const { stop } = useIntersectionObserver(
//     under_loader,
//       ([{ isIntersecting }], observerElement) => {
//         underIsVisible.value = isIntersecting
//       },
//     )

// onMounted(() => {
// if (underIsVisible.value) {
//     console.log("VISIBLE")
// } else {
//     console.log("HIDDEN")
// }

// })

sleep(1000).then(() => { 
    transition_padding_height.value = "103px"
    landing_line_width.value = "67%"
    landing_sub_title_margin.value = "75%"
})


sleep(4000).then(() => { 
    transition_padding_height.value = "0px"
})



const HIW_anchor_cookie = useCookie('HIW_anchor_cookie', {default:()=> '', watch:true, maxAge:30})
function HIW_anchor(route_to, anchor_to){
    HIW_anchor_cookie.value = anchor_to
    transition_and_route(route_to)
}


const cicle_tansition = ref('');
function transition_and_route(route_to) {
 cicle_tansition.value.animation_and_route(route_to);
}



</script>

<style scoped>

.invest_text{
    font-size:25vw;
    color:#fff;
    font-weight: 900;
    margin-left:5%;
    margin-bottom:-80px;
    margin-top:5%;
    mix-blend-mode: difference;
    z-index:10;
    position: relative;
}



.loading_vid_container{
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    margin-top:v-bind(vid_margin); 
    z-index:10000;
    background-color:#000;
    transition: margin-top 2.5s ease;
}
.loading_video{
    width:100%;
    height:100%;
    z-index:10000;
    background-color:#000;
    transform: scale(v-bind(vid_scale));
    transition: transform 1.5s ease;
}
.hide_vid{
    display:none;
}

.transition_padding{
    height:v-bind(transition_padding_height);
    background-color: #fff;
    transition: all .75s ease-in-out;
    margin-bottom:calc( -0.7 * v-bind(transition_padding_height));
}


.landing_sub_title{
    margin-left:v-bind(landing_sub_title_margin);
    margin-top:-8%;
    transition: all 1.7s ease;
}

.landing_sub_title_2{
    margin-left:5%;
    margin-top:-4%;
}

.landing_title_home{
    margin-left:5%;
    margin-top:10%;
}

.landing_line{
    width:v-bind(landing_line_width);
    height: 1px;
    border-top:solid 2px #fff;
    margin-top:-160px;
    margin-left:5%;
    transition: all 1.6s cubic-bezier(0.33, 1, 0.68, 1) .5s;

}


.big_emphasis{
    font-size:80px
}

.scrub_line{
    width:65%;
    height: 1px;
    border-top:solid 4px #fff;
    margin-top:-15px
}

.landing_text{
    margin-left:75%;
    width:20%;
    margin-top:-5%;
}

.landing_vid_container{
    height:100vh;
    margin-top:7.5vh;
    z-index:-1
}
.landing_video{
    width: 80%;
    height: auto;
    object-fit: cover;
    z-index: -1;
    margin-left:5%;
}



.landing_text_box{
    position: absolute;
    top:52vh;
    margin-left:5%;

}
.landing_letter_1{
    color:#fff;
    font-size: 580px;
    font-weight: 900;

}

.landing_letter_2{
    color:#fff;
    font-size: 580px;
    font-weight: 900; 
    margin-top:-50px;

}

.landing_letter_3{
    color:#fff;
    font-size: 580px;
    font-weight: 900;
    margin-top:-50px;

}

.video_text{
    margin-left: 76.5%;
    width: 21%;
    margin-top:-40%;
    font-weight: 500;
    line-height: 1.2;
}

.home_about_section{
    margin-top:40%;
    width:90%;
    margin-left:5%;
}

.about_text{
    width:70%;
}












.home_partner_section{
    margin-left:5%;
    width:90%;
    margin-top:20%;
    margin-bottom:-3%;
    z-index:-1;
    padding:5vh 0;
}

.partner_text{
    width:60%;
}

.partner_swiper_img{
    width:125px;
}
.partner_swiper_text{
    width:90%;
    line-height: 1.5;
    margin-top:10%

}

.swiper_wrapper{
    margin-top:7%;
    width:100%;
    border-bottom:#fff solid 1px;
    padding-bottom:75px;
    padding-top:30px
}

.pin_scroll_section{
    width:90%;
    margin-left:5%;
    margin-top:0%;
    margin-bottom:0%;
    position: relative;
    z-index:-1
}



.pinned_text{
    position: absolute;
    text-decoration: underline;
    text-decoration-color: #ffffff;
    text-underline-offset: 20px;
    text-decoration-thickness: 3px;
    background-color: aqua;
    line-height: 0;
}

.scroll_text{
    margin-left:50%;
    margin-bottom:50vh;
    padding-top:40vh;
    z-index: 1
}

.scroll_text:last-child{
    margin-bottom:75vh;
}
.scroll_text:first-child{
    padding-top:90vh;
}

.learn_more{
    color:#fff;
    margin-left:5px;
    margin-top:0px;
    cursor: pointer;
    text-decoration: underline;
  text-decoration-color: #3a6ef08d;
  text-underline-offset: 6px;
}

.scroll_title{
    margin-bottom:5%
}

.pin_scroll_video{
    width: 60%;
    height: auto;
    object-fit: cover;
    z-index: -2;
    margin-left:12.5%;
    position:absolute;
    margin-top:-15%;
    filter: blur(10px) contrast(1.05);
}

.video_overlay{
    width:100%;
    height:128vh;
    background-color: #000;
    opacity: 0.75;
    z-index: -1;
    position: absolute;
    margin-top:-22%;
    filter: blur(20px);
}





@media screen and (min-width: 2300px) and (max-width: 5600px) {


.landing_sub_title{
    margin-left:v-bind(landing_sub_title_margin);
margin-top:-2%;
}



.landing_sub_title_2{
margin-left:5%;
margin-top:-1%;
}



.landing_text{
margin-left:75.2%;
width:20%;
margin-top:-5%;
}







}









@media screen and (min-width: 1900px) and (max-width: 2300px) {


    .landing_sub_title{
margin-top:-5%;
}



.landing_sub_title_2{
margin-top:-4%;
}



.landing_text{
margin-left:75.2%;
margin-top:-2%;
}








}


@media screen and (min-width: 1600px) and (max-width: 1900px) {


.landing_sub_title{
    margin-left:v-bind(landing_sub_title_margin);
margin-top:-5%;
}



.landing_sub_title_2{
margin-left:5%;
margin-top:-4%;
}



.landing_text{
margin-left:75.2%;
width:20%;
margin-top:-2%;
}





}





@media screen and (min-width: 1400px) and (max-width: 1600px) {

    .landing_sub_title_2{
margin-left:5%;
margin-top:-7%;
}

.landing_text{
margin-left:75.2%;
width:20%;
margin-top:-6%;
}



}




@media screen and (min-width: 1200px) and (max-width: 1400px) {

    .landing_sub_title_2{
margin-left:5%;
margin-top:-9%;
}

.landing_text{
margin-left:75.2%;
width:20%;
margin-top:-5%;
}



}

@media only screen and (min-width: 992px) and (max-width: 1200px) {


    .landing_sub_title{
        margin-left:v-bind(landing_sub_title_margin);
    margin-top:-7.5%;
}

.landing_sub_title_2{
    margin-left:5%;
    margin-top:-10%;
    color:#fff
}

.landing_title_home{
    margin-left:5%;
    margin-top:13%;
}




.landing_text{
margin-left:75.2%;
width:20%;
margin-top:-1%;
}




.landing_line{
    width:v-bind(landing_line_width);
    margin-top:-10%;
    margin-left:5%

}

.landing_video{
    width: 70%;
    height: auto;
    object-fit: cover;
    z-index: -1;
    margin-left:9%;
}

.video_text{
    margin-left: 72%;
    width: 21%;
    margin-top:-40%;
}

.landing_text_box{
    top:42vh;
}
.landing_letter_1{
    font-size: 380px;
}

.landing_letter_2{
    font-size: 380px;
}

.landing_letter_3{
    font-size: 380px;
}

.home_about_section{
    margin-top:15%;
    width:90%;
    margin-left:5%;
}





.scroll_text{
    margin-left:55%;
    font-size: 95%;

}
}


@media only screen and (min-width: 768px) and (max-width: 992px) {



    .landing_sub_title{
        margin-left:v-bind(landing_sub_title_margin);
    margin-top:-7.5%;
}

.landing_sub_title_2{
    margin-left:5%;
    margin-top:-8%;
    color:#fff
}

.landing_title_home{
    margin-left:5%;
    margin-top:13%;
}

.big_emphasis{
    font-size:55px
}



.landing_text{
margin-left:75.2%;
width:20%;
margin-top:-1%;
}



.landing_line{
    width:v-bind(landing_line_width);
    height: 1px;
    border-top:solid 2px #fff;
    margin-top:-10%;
    margin-left:5%

}

.landing_video{
    width: 70%;
    height: auto;
    object-fit: cover;
    z-index: -1;
    margin-left:9%;
}

.video_text{
    margin-left: 72%;
    width: 23%;
    margin-top:-30%;
}

.landing_text_box{
    top:42vh;
}
.landing_letter_1{
    font-size: 300px;
}

.landing_letter_2{
    font-size: 300px;
}

.landing_letter_3{
    font-size: 300px;
}

.home_about_section{
    margin-top:15%;
    width:90%;
    margin-left:5%;
}







.scroll_text{
    margin-left:55%;
    font-size: 95%;

}



}



@media only screen and (min-width: 576px) and (max-width: 768px) {





    .landing_sub_title{
    margin-left:5%;
    margin-top:5%;
}

.landing_sub_title_2{
    margin-left:5%;
    margin-top:-30%;
    color:#fff
}

.landing_title_home{
    margin-left:5%;
    margin-top:22%;
}

.big_emphasis{
    font-size:55px
}



.landing_text{
margin-left:5.2%;
width:70%;
margin-top:22%;
}



.landing_line{
    width:v-bind(landing_line_width);
    height: 1px;
    border-top:solid 2px #fff;
    margin-top:-5%;
    margin-left:5%

}

.landing_video{
    width: 80%;
    height: auto;
    object-fit: cover;
    z-index: -1;
    margin-left:0%;
    margin-top:-15%
}

.video_text{
    margin-left: 55%;
    width: 40%;
    margin-top:-15%;
    text-align: right;
}

.landing_text_box{
    top:42vh;
}
.landing_letter_1{
    font-size: 250px;
}

.landing_letter_2{
    font-size: 250px;
}

.landing_letter_3{
    font-size: 250px;
}

.home_about_section{
    margin-top:-25%;
    width:120%;
    margin-left:5%;
}



.home_partner_section{
    margin-left:5%;
    width:90%;
    margin-top:5%;
}

.partner_text{
    width:90%;
}



.pinned_text{
    font-size:140%;
    white-space: nowrap;
}



.scroll_text{
    margin-left:55%;
    font-size: 95%;
    width:45%

}

.invest_text{
    margin-bottom:-7%;
}


}





@media only screen and (min-width: 430px) and (max-width: 576px) {
    .landing_sub_title{
    margin-left:5%;
    margin-top:8%;
}
.landing_sub_title_2{
    margin-left:5%;
    margin-top:-36%;
    color:#fff
}
.landing_title_home{
    margin-left:5%;
    margin-top:22%;
}
.big_emphasis{
    font-size:50px
}
.landing_text{
margin-left:5.2%;
width:70%;
margin-top:26%;
}
.landing_line{
    width:v-bind(landing_line_width);
    height: 1px;
    border-top:solid 2px #fff;
    margin-top:-8%;
    margin-left:5%
}
.landing_video{
    width: 70%;
    height: auto;
    object-fit: cover;
    z-index: -1;
    margin-left:0%;
    margin-top:-5%
}
.video_text{
    margin-left: 45%;
    width: 50%;
    margin-top:-20%;
    text-align: right;
}
.landing_text_box{
    top:52vh;
}
.landing_letter_1{
    font-size: 150px;
}
.landing_letter_2{
    font-size: 150px;
    padding:40px 0px
}
.landing_letter_3{
    font-size: 150px;
}
.home_about_section{
    margin-top:0%;
    width:120%;
    margin-left:5%;
}
.home_partner_section{
    margin-left:5%;
    width:90%;
    margin-top:5%;
}
.partner_text{
    width:90%;
}
.pinned_text{
    font-size:100%;
    margin-top:0%
}

.scroll_text{
    margin-left:55%;
    font-size: 70%;
    width:45%
}

.invest_text{
    margin-bottom:-7%;
}
}


@media only screen and (min-width: 0px) and (max-width: 430px) {





    .landing_sub_title{
    margin-left:5%;
    margin-top:5%;
}

.landing_sub_title_2{
    margin-left:5%;
    margin-top:-38%;
    color:#fff
}

.landing_title_home{
    margin-left:5%;
    margin-top:30%;
}

.big_emphasis{
    font-size:50px
}



.landing_text{
margin-left:5.2%;
width:70%;
margin-top:26%;
}



.landing_line{
    width:v-bind(landing_line_width);
    height: 1px;
    border-top:solid 2px #fff;
    margin-top:-12%;
    margin-left:5%

}

.landing_video{
    width: 95%;
    height: auto;
    object-fit: cover;
    z-index: -1;
    margin-left:0%;
    margin-top:-5%
}

.video_text{
    margin-left: 38%;
    width: 59%;
    margin-top:-20%;
    text-align: right;
}

.landing_text_box{
    top:62vh;
}
.landing_letter_1{
    font-size: 150px;
}

.landing_letter_2{
    font-size: 150px;
    padding:40px 0px
}

.landing_letter_3{
    font-size: 150px;
}

.home_about_section{
    margin-top:0%;
    width:120%;
    margin-left:5%;
}

.about_text{
  margin-top:-1%
}


.invest_text{
    margin-bottom:-7%;
    font-size:24.5vw;
}

.home_partner_section{
    margin-left:5%;
    width:90%;
    margin-top:0%;
    margin-bottom:5%
}

.swiper_wrapper{
    border-bottom:#fff solid 0px;
}

.partner_text{
    width:90%;
}



.pinned_text{
    font-size:50%
}


.scroll_text{
    margin-left:55%;
    font-size: 70%;
    width:45%

}

.pin_scroll_section{
display: none;
}

}





</style>