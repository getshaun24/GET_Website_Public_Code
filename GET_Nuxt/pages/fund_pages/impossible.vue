<template>

    <div>
<Header/>

<GSAPScrollSmoother>

    <FundPagesSectionsLanding v-bind="landing_image"/>
    <p class="landing_subtext">GET Impossible Holdings</p>
    <FundPagesCompsBigText v-bind="big_text_1"/>
    <FundPagesSectionsIntroInfo v-bind="intro_info"/>
    <FundPagesCompsSlabImg v-bind="slab1"/>
    <FundPagesCompsBigText v-bind="big_text_2"/>
    <FundPagesSectionsStrategy v-bind="strategy"/>
    <FundPagesSectionsRevenue v-bind="revenue"/>
    <FundPagesCompsSwiperCardsWithLinks v-bind="swiper_images"/>

  

    
 
<div class="white_section">

    <FundPagesCompsBigText v-bind="big_text_3"/>
    <FundPagesSectionsInvestmentHighlights v-bind="investment_highlights"/>
    <FundPagesCompsSlabImg v-bind="slab2"/>
    <FundPagesCompsBigText v-bind="big_text_4"/>


<div class="bottom_line"></div>

<FundPagesSectionsBottom/>

</div>





    
<FundPagesSectionsFeet v-bind="footer"/>
    



</GSAPScrollSmoother>


</div>


</template>






<script setup>


import { ref, onMounted } from 'vue'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { useWindowSize } from '@vueuse/core'
import { gsap } from 'gsap'
import { page_to } from "../../stores/page_to.js"

import image1 from "~/assets/content/fund_pages/impossible/impossible_13.jpg";
import image2 from "~/assets/content/fund_pages/impossible/impossible_burger.png"
import image3 from "~/assets/content/fund_pages/impossible/impossible_21.jpg"
import image4 from "~/assets/content/fund_pages/impossible/impossible_2.jpg"
import image5 from "~/assets/content/fund_pages/impossible/impossible_3.jpg"
import image6 from "~/assets/content/fund_pages/impossible/impossible_ingredients.jpg"
import image8 from "~/assets/content/investments/invest_7.png"

import video1 from "~/assets/content/fund_pages/impossible/GET_Impossible_1.mp4"

import swiper1 from "~/assets/content/fund_pages/impossible/impossible_slide_1.jpg"
import swiper2 from "~/assets/content/fund_pages/impossible/impossible_slide_2.jpg"
import swiper3 from "~/assets/content/fund_pages/impossible/impossible_slide_3.jpg"



const most_recent_fund_page = useCookie('most_recent_fund_page', {default:()=> '', watch:true, maxAge:18000})
    const route_from = page_to()
    const page_from_url = ref(String(route_from.current_page_from).replace('/fund_pages/','').replace('/invest_flow/',''))
    console.log('page from is - ', page_from_url.value)
    most_recent_fund_page.value = page_from_url.value



const landing_image = {
    title: "Impossible Foods",
    title_color: "#fff",
    text_align: "left",
    line_width: "800px",
    line_margin: "25px",
    image: image1,
    font_calc: "1"
}

const big_text_1 = {text:'GET Impossible', font_size:'12.5vw', margin_top:'5%', padding_top:'0'}


const intro_info ={
    video: '',
    image: image2,
    is_image: true,
    is_video: false,
    main_text:"The two largest players in the plant-based meat world are Beyond Meat and IMPOSSIBLE Foods. Only one of them has had an IPO (Beyond Meat). This leaves IMPOSSIBLE Foods as the privately held company (for now), and we have reason to believe it will not stay this way much longer. <br><br>A good product? Check. Strong allies in finance? Check. Retail distribution? Check. The only thing missing is hiring a banker and going public. This could be weeks or months - but it may not be very long. We could see interest really ramp up. “Early-in” investors can be positioned to see the greatest returns and that is why we are providing this opportunity for you to participate.<br><br><span style='font-weight:900'>About IMPOSSIBLE Foods, Inc:</span> Impossible Foods develops plant-based substitutes for meat and dairy products. According to the company, it observes animal products at the molecular level, and selects specific proteins and nutrients from greens, seeds, and grains to recreate meats and dairy products. The company's first product is the Impossible Burger, which is made from ingredients including plant-based protein, coconut oil, and heme, among other ingredients. In January 2019, the company unveiled the Impossible Burger 2.0, which swaps out whey protein for soy protein. Heme is a protein found in animal muscle and is, according to the company, responsible for the characteristic taste and aroma of meat. Impossible Foods makes heme from plants. Currently, the Impossible Burger is now available online but can be found in over 30,000 restaurants and over 11,000 grocery stores in the U.S., Hong Kong, Macau, and Singapore."
}

const slab1 = {
    margin_top:"25%",
    margin_bottom: "0%",
    image: image3,
}

const big_text_2 = {text:'Exclusive Access', font_size:'22vw', margin_top:'5%', padding_top:'0'}


const strategy = {
    video: video1,
    image: '',
    is_image: false,
    is_video: true,
    current_find_page: 'impossible',
    image_margin_calc: "1.2",
    image_margin_mobile_calc: "1",
    container_margin:"-10%",
    container_margin_bottom:"0%",
    title:"Key Investors",
    text:"Innovative Fund <br><br> G Squared<br><br>Temasek Holdings<br><br>Horizons Ventures<br><br>Sailing Capital<br><br>Viking Global Investors<br><br>Serena Ventures<br><br>Khosla Ventures<br><br>GV<br><br>UBS<br><br>Trinity Capital Investment"}



const revenue = {
    image: image4,
    image_margin: "40%",
    title:"Management",
    text:"<span style='text-decoration: underline'>Founder</span><br>Patrick Brown, M.D.<br><br><span style='text-decoration: underline'>Chief Executive Officer</span><br>Peter McGuinness<br><br><span style='text-decoration: underline'>President</span><br>Dennis Woodside<br><br><span style='text-decoration: underline'>Chief Financial Officer</span><br>David Borecky<br><br><span style='text-decoration: underline'>Chief Legal Officer</span><br>Jason Gao"
}

const swiper_images = {
    image_1: swiper1,
    image_2: swiper2,
    image_3: swiper3
}

const big_text_3 = {text:'Make An Impact', font_size:'21vw', margin_top:'2%', padding_top:'2%'}


const investment_highlights = {
    title_1: "Company Name:",
    info_1: "Impossible Foods Inc.",
    title_2: "Security Type:",
    info_2: "Preferred Stock",
    title_3: "Stock Access:",
    info_3: "Very Lmited",
    title_4: "Valuation at Bid:",
    info_4: "TBD",
    title_5: "Price at Bid:",
    info_5: "TBD",
    image: image5,
    image_margin: "35%"
}

const slab2 = {
    margin_top:"20%",
    margin_bottom: "5%",
    image: image6,
}


const big_text_4 = {text:'Now Possible', font_size:'15vw', margin_top:'6%', padding_top:'2%'}


const footer = {
    title:"Green<br>Worldwide",
    image:image8,
    nuxt_link:"/fund_pages/green_worldwide",
}



const uncover = ref()
const { width, height } = useWindowSize()

// sleep time expects milliseconds
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}





onMounted(() => {



  sleep(2500).then(() => { 


    if(width.value < 576){


    gsap.set(".next_footer", { yPercent: 200 });
    uncover.value = gsap.timeline({ paused: true });

uncover.value.to(".next_footer", { yPercent: 0, ease:"ease-in-out" });

    }

    else if(width.value < 768){




        gsap.set(".next_footer", { yPercent: 200 });
    uncover.value = gsap.timeline({ paused: true });

uncover.value.to(".next_footer", { yPercent: 0, ease:"ease-in-out" });

}

    else{

        gsap.set(".next_footer", { yPercent: 200 });
    uncover.value = gsap.timeline({ paused: true });

uncover.value.to(".next_footer", { yPercent: -20, ease:"ease-in-out" });

    }
    

ScrollTrigger.create({
  trigger: ".white_section",
  start: "bottom bottom",
  end: "+=100%",
  animation: uncover.value,
  scrub: true,
});

ScrollTrigger.refresh();

})

})



</script>



<style scoped>



.landing_subtext{
    font-size:25px;
    margin-left:5%;
    margin-top:5%;
    width:80%;
    line-height:1;
}


.nano_video{
    width:100vw;
    filter: invert(1);
    margin-top:10%;
    height: 40vh;
    object-fit: cover;
}


.bottom_line{
    width:100vw;
    height:10px;
    margin-top:10%;
    background-color: #000;
}


.white_section{
    background-color:#fff;
    width:100%;
    height:110%;
    margin-top:5%;
    position: relative;
}





.next_footer{
    height:100%;
    position: -webkit-sticky;
    position: sticky;
    width:100%;
    z-index:1;
    border-top: 1px solid rgba(255, 255, 255, 0.3);
    margin-top:0%
}










</style>