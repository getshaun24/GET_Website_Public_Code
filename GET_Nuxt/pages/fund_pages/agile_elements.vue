<template>

<div style="background-color: black; height 100%;">
    <Header/>
    
    <GSAPScrollSmoother>
    
        <FundPagesSectionsLanding v-bind="landing_image"/>
        <p class="landing_subtext">Like An Immune System For Your Fabrics</p>
        <FundPagesCompsBigText v-bind="big_text_1"/>
        <FundPagesSectionsIntroInfo v-bind="intro_info"/>
        <FundPagesCompsSlabImg v-bind="slab1"/>
        <FundPagesCompsBigText v-bind="big_text_2"/>
        <FundPagesSectionsStrategy v-bind="strategy"/>
        <FundPagesSectionsRevenue v-bind="revenue"/>
        <FundPagesCompsSwiperCards v-bind="swiper_images"/>
    
      
    <div class="white_section">
    
        <FundPagesCompsBigText v-bind="big_text_3"/>
        <FundPagesSectionsInvestmentHighlights v-bind="investment_highlights"/>
        <FundPagesCompsSlabVid v-bind="slab2"/>
        <FundPagesCompsBigText v-bind="big_text_4"/>
        <FundPagesSectionsCompanyHighlights v-bind="company_highlights" class="comp_highlights_margin"/>
    
    
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
    import { page_to } from "../../stores/page_to.js"
    
    import { gsap } from 'gsap'
    
    import image1 from "~/assets/content/fund_pages/agile/agile_1.jpg";
    import image2 from "~/assets/content/fund_pages/agile/laundry_karma_bottle.png"
    import image3 from "~/assets/content/fund_pages/agile/agile_3.jpg"
    import image4 from "~/assets/content/fund_pages/agile/agile_12.png"
    import image5 from "~/assets/content/fund_pages/agile/agile_4.jpg"
    import image8 from "~/assets/content/fund_pages/helpful/helpful_8.jpg"
    import image9 from "~/assets/content/fund_pages/nano/invest_1_square.png"

    import vid1 from "~/assets/content/fund_pages/helpful/spin.mp4"
    import vid2 from "~/assets/content/fund_pages/helpful/sphere_3.mp4"
    import vid3 from "~/assets/content/fund_pages/helpful/chipset.mp4"
    
    
    import swiper1 from "~/assets/content/fund_pages/helpful/helpful_slider_4.jpg"
    import swiper2 from "~/assets/content/fund_pages/helpful/helpful_slider_5.jpg"
    import swiper3 from "~/assets/content/fund_pages/helpful/helpful_slider_6.jpg"
    
    

    const most_recent_fund_page = useCookie('most_recent_fund_page', {default:()=> '', watch:true, maxAge:18000})
    const route_from = page_to()
    const page_from_url = ref(String(route_from.current_page_from).replace('/fund_pages/','').replace('/invest_flow/',''))
    console.log('page from is - ', page_from_url.value)
    most_recent_fund_page.value = page_from_url.value


    const landing_image = {
        title: "Agile Elements",
        title_color: "#129ce6",
        text_align: "center",
        line_width: "375px",
        line_margin: "250px",
        image: image1,
        image_width: "120%",
        font_calc: "1"
    }
    
    const big_text_1 = {text:'Longlasting Clean', font_size:'11.35vw', margin_top:'5%', padding_top:'0'}
    
    
    const intro_info ={
        video: '',
        image: image2,
        is_image: true,
        is_video: false,
        main_text:"The Agile Elements Company is an innovation in antimicrobial. What has been solely for industrial application for antimicrobial fabric, Agile has put in the hands of the everyday user. With the new threats jeopardizing our health, Agile is diligent on having everyday things like our clothing, cars, masks, and surfaces, safer and cleaner.<h6>An Innovative & Proprietary Fabric Solution</h6>"
    }
    
    const slab1 = {
        margin_top:"25%",
        margin_bottom: "0%",
        image: image3,
    }
    
    const big_text_2 = {text:'Re-imagine Antimicrobial', font_size:'15.55vw', margin_top:'5%', padding_top:'0'}
    
    
    const strategy = {
        video: '',
        image: image4,
        is_image: true,
        is_video: false,
        image_margin_calc: "1.2",
        image_margin_mobile_calc: "1",
        container_margin:"0%",
        container_margin_bottom:"-120%",

    text_margin_mobile: "-100%",

        title:"Investors",
        text:"Private - Contact For Access"}
    
    
    
    const revenue = {
        image: image5,
        image_margin: "40%",
        title:"Directors",
        text:"<span style='text-decoration: underline'>CEO & Founder</span><br>Naif Hajjar<br><br><span style='text-decoration: underline'>COO</span><br>Shaun Cohen<br><br><span style='text-decoration: underline'>Chemist</span><br>Jan Gregory"
    }
    
    const swiper_images = {
        image_1: swiper1,
        image_2: swiper2,
        image_3: swiper3
    }
    
    const big_text_3 = {text:'20% Returns', font_size:'15.5vw', margin_top:'2%', padding_top:'2%'}
    
    
    const investment_highlights = {
        title_1: "Company Name:",
        info_1: "The Agile Elements Company",
        title_2: "Fund Strategy:",
        info_2: "Customer Referral",
        title_3: "Unit Price:",
        info_3: "$1,000 per unit",
        title_4: "Minimum Investment:",
        info_4: "$10,000",
        title_5: "Maximum Offering:",
        info_5: "$5 Million",
        title_6: "Term:",
        info_6: "3 Years",
        image: image5,
        image_margin: "20%"
    }
    
    const slab2 = {
        margin_top:"10%",
        margin_bottom: "5%",
        video: vid3,
    }
    

    
    const big_text_4 = {text:'Hand Selected', font_size:'13.75vw', margin_top:'5%', padding_top:'2%'}
    
    

    const company_highlights = {
    left_side_text: "• Helpful+ has a diverse underlying portfolio companies acts as a hedge against fluctuations in any given sector",
    right_side_text_1: "• By carefully vetting financing syndicates Helpful+ leverages their years of experience in further analyzing opportunities, and in industry specific best practices.",
    right_side_text_2: "• Helpful+ is an end-to-end solution which helps companies get the growth capital they need, the moment they need it.",
    image: '',
    has_image:false
}








    const footer = {
        title:"NanoCarbon",
        image:image9,
        nuxt_link:"/fund_pages/nano",
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
    z-index:11;
    border-top: 1px solid rgba(255, 255, 255, 0.3);
    margin-top:0%
}


    
@media only screen and (min-width: 900px) and (max-width: 5200px) {
.comp_highlights_margin{
    margin-top:-20%
}

}
    
    
    
    
    
    
    
    </style>