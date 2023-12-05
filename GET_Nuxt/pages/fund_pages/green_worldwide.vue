<template>

    <div>
    <Header/>
    
    <GSAPScrollSmoother>
    
        <FundPagesSectionsLanding v-bind="landing_image"/>
        <p class="landing_subtext">Innovating Waste to Energy Technology</p>
        <FundPagesCompsBigText v-bind="big_text_1"/>
        <FundPagesSectionsIntroInfo v-bind="intro_info"/>
        <FundPagesCompsSlabImg v-bind="slab1"/>
        <FundPagesCompsBigText v-bind="big_text_2"/>
        <FundPagesSectionsStrategy v-bind="strategy"/>
        <FundPagesSectionsRevenue v-bind="revenue"/>
        <FundPagesCompsSwiperCards v-bind="swiper_images"/>
    

          

<div style="background-color: #000; height:100%">

      
    <div class="white_section">
    
        <FundPagesCompsBigText v-bind="big_text_3"/>
        <FundPagesSectionsInvestmentHighlights v-bind="investment_highlights"/>
        <FundPagesCompsSlabImg v-bind="slab2"/>
        <FundPagesCompsBigText v-bind="big_text_4"/>
    
    
    <div class="bottom_line"></div>
    
    <FundPagesSectionsBottom/>
    
    </div>
    
    
    
   
    
    <FundPagesSectionsFeet v-bind="footer"/>
    

    
  
</div>
    
    
    
    </GSAPScrollSmoother>
</div>
    
    </template>
    
    
    
    
    
    
    <script setup>
    
    
    import { ref, onMounted } from 'vue'
    import { ScrollTrigger } from 'gsap/ScrollTrigger'
    import { useWindowSize } from '@vueuse/core'
    import { gsap } from 'gsap'
    import { page_to } from "../../stores/page_to.js"
    
    import image1 from "~/assets/content/fund_pages/gww/green_4.jpg";
    import image2 from "~/assets/content/fund_pages/gww/green_13.png"
    import image3 from "~/assets/content/fund_pages/gww/green_8.jpg"
    import image4 from "~/assets/content/fund_pages/gww/green_11.jpg"
    import image5 from "~/assets/content/fund_pages/gww/green_7.jpg"
    import image6 from "~/assets/content/fund_pages/gww/green_16.jpg"
    import image8 from "~/assets/content/investments/invest_6.jpg"
    
    import image7 from "~/assets/content/fund_pages/gww/green_12.jpg"
    
    import swiper1 from "~/assets/content/fund_pages/nano/nano_8.jpg"
    import swiper2 from "~/assets/content/fund_pages/nano/nano_9.jpg"
    import swiper3 from "~/assets/content/fund_pages/nano/nano_10.jpg"

    const most_recent_fund_page = useCookie('most_recent_fund_page', {default:()=> '', watch:true, maxAge:18000})
    const route_from = page_to()
    const page_from_url = ref(String(route_from.current_page_from).replace('/fund_pages/','').replace('/invest_flow/',''))
    console.log('page from is - ', page_from_url.value)
    most_recent_fund_page.value = page_from_url.value

    
    
    const landing_image = {
        title: "Green Worldwide",
        title_color: "#fff",
        text_align: "left",
        line_width: "790px",
        line_margin: "35px",
        image: image1,
        image_width: "100%",
        font_calc: "1"
    }
    
    const big_text_1 = {text:'Re-Think Energy', font_size:'12.5vw', margin_top:'5%', padding_top:'0'}
    
    
    const intro_info ={
        video: '',
        image: image2,
        is_image: true,
        is_video: false,
        main_text:"<h6>Envinromentally & Economically Viable</h6>Green Worldwide is a Waste to Energy development company which implements scalable waste-to-energy solutions using the latest innovation in Thermalytic Oxidation technology. Our clean, reliable, and non-intermittent process creates thermal and electrical energy from virtually any type of waste. <br><br> Green Worldwide partners with industrial manufacturers, recyclers, municipalities, hospitals and others to create tailor-made energy solutions for the unique needs of each client. <br><h6>Monetize Your Waste Stream</h6>"
    }
    
    const slab1 = {
        margin_top:"25%",
        margin_bottom: "0%",
        image: image3,
    }
    
    const big_text_2 = {text:'Fiscally Responsibile', font_size:'17vw', margin_top:'5%', padding_top:'0'}
    
    
    const strategy = {
        video: '',
        image: image7,
        is_image: true,
        is_video: false,
        image_margin_calc: "1.2",
        image_margin_mobile_calc: "1",
        container_margin:"0%",
        container_margin_bottom:"-90%",

    text_margin_mobile: "-100%",

        title:"Key Investors",
        text:"Private - Contact For Access"}
    
    
    
    const revenue = {
        image: image4,
        image_margin: "40%",
        title:"Management",
        text:"<span style='text-decoration: underline'>CEO & Co-Founder</span><br>Naif Hajjar.<br><br><span style='text-decoration: underline'>COO</span><br>Jonathan Beirn<br><br><span style='text-decoration: underline'>CTO</span><br>Victor De Avila<br><br><span style='text-decoration: underline'>CMO</span><br>Shaun Cohen"
    }
    
    const swiper_images = {
        image_1: swiper1,
        image_2: swiper2,
        image_3: swiper3
    }
    
    const big_text_3 = {text:'Environmentally Conscientious', font_size:'12.5vw', margin_top:'2%', padding_top:'2%'}
    
    
    const investment_highlights = {
        title_1: "Company Name:",
        info_1: "Green Worldwide",
        title_2: "Security Type:",
        info_2: "Common Stock",
        title_3: "Implied Company Valuation:",
        info_3: "20 Million",
        title_4: "Latest Post Money Valuation:",
        info_4: "25 Million",
        title_5: "Discount:",
        info_5: "est. $18-$22 per share",
        title_6: "",
        info_6: "",
        image: image5,
        image_margin: "20%"
    }
    
    const slab2 = {
        margin_top:"20%",
        margin_bottom: "5%",
        image: image6,
    }
    

    
    const big_text_4 = {text:'Non-Intermittent Renewable', font_size:'12vw', margin_top:'5%', padding_top:'2%'}
    
    
    const footer = {
        title:"The Boring Company",
        image:image8,
        nuxt_link:"/fund_pages/boring_company",
    }
    
    
    
        
    
    
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