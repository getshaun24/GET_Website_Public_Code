<template>


<div>
    <Header/>
    
    <GSAPScrollSmoother>
    
        <FundPagesSectionsLanding v-bind="landing_image"/>
        <p class="landing_subtext">GET-Helpful+ Holdings</p>
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
        <FundPagesSectionsCompanyHighlights v-bind="company_highlights"/>
    
    
    <div class="bottom_line"></div>
    
    <FundPagesSectionsBottom/>
    
    </div>



    
    <div class="next_footer">
    
    
    <FundPagesSectionsFeet v-bind="footer"/>
    
    
    </div>

    
    


    
</GSAPScrollSmoother> 

</div>
    
    
    </template>
    
    
    
    
    
    
    <script setup>
    
    
    import { ref, onMounted } from 'vue'
    import { ScrollTrigger } from 'gsap/ScrollTrigger'
    import { useWindowSize } from '@vueuse/core'
    import { page_to } from "../../stores/page_to.js"
    import { gsap } from 'gsap'
    
    import image1 from "~/assets/content/fund_pages/helpful/helpful_1.jpg";
    import image3 from "~/assets/content/fund_pages/helpful/helpul_offices_X.png"
    import image4 from "~/assets/content/fund_pages/helpful/helpful_4.png"
    import image5 from "~/assets/content/fund_pages/helpful/Helpful_search.jpg"
    import image8 from "~/assets/content/fund_pages/helpful/helpful_8.jpg"
    import image9 from "~/assets/content/fund_pages/boysterous/boy_square.png"

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
        title: "Helpful+",
        title_color: "#fff",
        text_align: "center",
        line_width: "375px",
        line_margin: "250px",
        image: image1,
        font_calc: "1"
    }
    
    const big_text_1 = {text:'Disrupting Diversification', font_size:'12.5vw', margin_top:'5%', padding_top:'0'}
    
    
    const intro_info ={
        video: vid1,
        image: '',
        is_image: false,
        is_video: true,
        main_text:"Record liquidity from the Fed does not mean easy access to funding for the people. <br><br> Banks are as selective, if not more selective, in their lending than they were after the crash of 2008. As a result of this, companies - even those with long track records and good credit - are finding themselves seeking alternative sources for capital to help and sometimes save their business from decimation. <br><br> This is where Helpful+ Steps in. <br><br> • Helpful+ helps capitalize the top funders in the industry (providing liquidity to funders with the best ratings and track records)"
    }
    
    const slab1 = {
        margin_top:"25%",
        margin_bottom: "0%",
        image: image3,
    }
    
    const big_text_2 = {text:'Re-Think Funding', font_size:'11.65vw', margin_top:'5%', padding_top:'0'}
    
    
    const strategy = {
        video: vid2,
        image: '',
        is_image: false,
        is_video: true,
        image_margin_calc: "1.2",
        image_margin_mobile_calc: "50",

        text_margin_mobile: "-80%",
        
        container_margin:"0%",
        title:"Strategy",
        text:"The GET Helpful+ fund generates returns through two primary channels: first, by participating with seasoned funding companies; Helpful+ generates income from the underlying performance of the clientele that our funding companies help. Second, as a customer portal and introduction agent, Helpful+ is entitled to industry standard referral compensation. <br><br> Helpful+ uses its reach and assets to bolster boths sides of the market by: 1. cultivating a top-tier network of industry focused funding experts, and 2. hand-picking the most appropriate source to complete the deal with total security and transparency. <br><br> Basically we help bring the clients into the best possible portfolios for them, generating revenue for the fund - at the point of a successful and mutually beneficial transaction."}
    
    
    
    const revenue = {
        image: image4,
        image_margin: "40%",
        title:"Revenue Sources",
        text:"Funding Portfolio Investments. <br> Helpful has the relationships to put our funds in the right hands with proven track records. Exclusive relationships, just for Helpful+. Just for you."
    }
    
    const swiper_images = {
        image_1: swiper1,
        image_2: swiper2,
        image_3: swiper3
    }
    
    const big_text_3 = {text:'20% Returns', font_size:'15.5vw', margin_top:'2%', padding_top:'2%'}
    
    
    const investment_highlights = {
        title_1: "Fund Name:",
        info_1: "Get Helpful Plus, and Helpful Custom Fund I & II",
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
        title:"Boysterous Couture",
        image:image9,
        nuxt_link:"/fund_pages/boysterous",
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
    z-index:2;
    border-top: 1px solid rgba(255, 255, 255, 0.3);
    margin-top:0%
}


    
    
    
    
    
    
    
    
    
    </style>