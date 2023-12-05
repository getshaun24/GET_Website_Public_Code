<template>


<div>
    <Header/>
    
    <GSAPScrollSmoother>
    
        <FundPagesSectionsLanding v-bind="landing_image"/>
        <p class="landing_subtext">Insurance For Your Talent</p>
        <FundPagesCompsBigText v-bind="big_text_1"/>
        <FundPagesSectionsIntroInfo v-bind="intro_info"/>
        <FundPagesCompsSlabImg v-bind="slab1"/>
        <FundPagesCompsBigText v-bind="big_text_2"/>
        <FundPagesSectionsStrategy v-bind="strategy"/>
        <FundPagesSectionsRevenue v-bind="revenue"/>
    
      
    <div class="white_section">
    
        <FundPagesCompsBigText v-bind="big_text_3"/>
        <FundPagesSectionsInvestmentHighlights v-bind="investment_highlights"/>
        <FundPagesCompsSlabImg v-bind="slab2"/>
        <FundPagesCompsBigText v-bind="big_text_4"/>
    
        <FundPagesSectionsRevenue v-bind="extra_text"/>
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
    
    import image1 from "~/assets/content/fund_pages/social_wise/social_11.jpg";
    import image2 from "~/assets/content/fund_pages/social_wise/Social_Wise_logo_1.png"
    import image3 from "~/assets/content/fund_pages/social_wise/social_8.jpg"
    import image4 from "~/assets/content/fund_pages/social_wise/social_3.jpg"
    import image5 from "~/assets/content/fund_pages/social_wise/social_11.jpg"
    import image6 from "~/assets/content/fund_pages/social_wise/social_12.png"
    import image7 from "~/assets/content/fund_pages/social_wise/social_13.jpg"
    import image8 from "~/assets/content/fund_pages/social_wise/social_15.png"
    import image9 from "~/assets/content/fund_pages/neuralink/neuro_12.png"
    
    
    import swiper1 from "~/assets/content/fund_pages/nano/nano_8.jpg"
    import swiper2 from "~/assets/content/fund_pages/nano/nano_9.jpg"
    import swiper3 from "~/assets/content/fund_pages/nano/nano_10.jpg"





    const most_recent_fund_page = useCookie('most_recent_fund_page', {default:()=> '', watch:true, maxAge:18000})
    const route_from = page_to()
    const page_from_url = ref(String(route_from.current_page_from).replace('/fund_pages/','').replace('/invest_flow/',''))
    console.log('page from is - ', page_from_url.value)
    most_recent_fund_page.value = page_from_url.value

    
    
    const landing_image = {
        title: "Social Wise",
        title_color: "#fff",
        text_align: "center",
        line_width: "520px",
        line_margin: "190px",
        image: image1,
        image_width: "120%",
        font_calc: "1"
    }
    
    const big_text_1 = {text:'Social Media Background Check', font_size:'10.5vw', margin_top:'5%', padding_top:'0'}
    
    
    const intro_info ={
        video: '',
        image: image2,
        is_image: true,
        is_video: false,
        main_text:"<h6>About Social Wise</h6>Social Wise is the first Artificial Intelligence social media background check. Using an advanced proprietary neural network technology, Social Wise scans Twitter, Facebook, and Instagram to make sure the person you hire represents your brand values at every level.<h6 style='font-size:150%'>PR has changed, each member of your organization is now a representitive</h6>"
    }
    
    const slab1 = {
        margin_top:"25%",
        margin_bottom: "0%",
        image: image3,
    }
    
    const big_text_2 = {text:'Proprietary A.I.', font_size:'13.5vw', margin_top:'5%', padding_top:'0'}
    
    
    const strategy = {
        video: '',
        image: image4,
        is_image: true,
        is_video: false,
        // image_margin_calc: "1.2",
        // image_margin_mobile_calc: "1",
        // container_margin:"0%",
        // container_margin_bottom:"-125%",

        image_margin_calc: "70",
        image_margin_mobile_calc: "1",
        text_margin_mobile: "-100%",
        container_margin_bottom:"-125%",


        title:"Key Investors",
        text:"Private - Contact For Access"}
    
    
    
    const revenue = {
        image: image5,
        image_margin: "40%",
        title:"Management",
        text:"<p><span style='text-decoration: underline'>CEO</span><br>Jonathan Beirn<br><br><span style='text-decoration: underline'>CTO</span><br>Shaun Cohen</p>"
    }

    
    const big_text_3 = {text:'Reputation is Everything', font_size:'15.75vw', margin_top:'2%', padding_top:'2%'}
    
    
    const investment_highlights = {
        title_1: "Company Name:",
        info_1: "Social Wise",
        title_2: "Security Type:",
        info_2: "Common Stock",
        title_3: "Implied Company Valuation:",
        info_3: "$20 Million",
        title_4: "Latest Post Money Valuation:",
        info_4: "$25 Million",
        title_5: "Discount:",
        info_5: "est. $18-$22 per share",
        title_6: "",
        info_6: "",
        image: image6,
        image_margin: "20%"
    }
    
    const slab2 = {
        margin_top:"20%",
        margin_bottom: "5%",
        image: image7,
    }
    

    
    const big_text_4 = {text:'Socially Insured', font_size:'13vw', margin_top:'5%', padding_top:'2%'}


        
    const extra_text = {
        image: image8,
        image_margin: "25%",
        title:"",
        text:"<p style='color:#000'>PR has changed, each member of your organization is now a representitive. Use Social Wise's state-of-the-art Artificial Intelligence to analyze the post and pictures of each constituent.</p>"
    }

    
    
    const footer = {
        title:"Neuralink",
        image:image9,
        nuxt_link:"/fund_pages/neuralink",
    }
    
    
    
   

const uncover = ref()
const { width, height } = useWindowSize()

// sleep time expects milliseconds
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
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
    z-index:-1;
    border-top: 1px solid rgba(255, 255, 255, 0.3);
    margin-top:0%
}


    
    
    
    
    
    
    
    
    </style>