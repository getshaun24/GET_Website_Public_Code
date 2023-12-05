<template>

    <div>
    <Header/>
    
    <GSAPScrollSmoother>
    
        <FundPagesSectionsLanding v-bind="landing_image"/>
        <p class="landing_subtext">Premium Leather Products</p>
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
        <FundPagesSectionsExtraSection v-bind="top_products"/>
    
    
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
    import { page_to } from "../../stores/page_to.js"
    
    import { gsap } from 'gsap'
    
    import image1 from "~/assets/content/fund_pages/boysterous/boy_22.png";
    import image2 from "~/assets/content/fund_pages/boysterous/clutch.png"
    import image3 from "~/assets/content/fund_pages/boysterous/boy_1_square.png"
    import image4 from "~/assets/content/fund_pages/boysterous/boy_7.jpg"
    import image5 from "~/assets/content/fund_pages/boysterous/boy_10.jpg"
    import image6 from "~/assets/content/fund_pages/boysterous/boy_2.jpg"
    import image8 from "~/assets/content/fund_pages/boysterous/boy_20.jpg"
    import image9 from "~/assets/content/fund_pages/social_wise/social_wise_x.png"

    import vid1 from "~/assets/content/fund_pages/boysterous/boy_2.mp4"
    import vid2 from "~/assets/content/fund_pages/helpful/sphere_3.mp4"
    import vid3 from "~/assets/content/fund_pages/helpful/chipset.mp4"
    
    
    import swiper1 from "~/assets/content/fund_pages/boysterous/boy_8.jpg"
    import swiper2 from "~/assets/content/fund_pages/boysterous/boy_14.jpg"
    import swiper3 from "~/assets/content/fund_pages/boysterous/boy_15.jpg"

    const most_recent_fund_page = useCookie('most_recent_fund_page', {default:()=> '', watch:true, maxAge:18000})
    const route_from = page_to()
    const page_from_url = ref(String(route_from.current_page_from).replace('/fund_pages/','').replace('/invest_flow/',''))
    console.log('page from is - ', page_from_url.value)
    most_recent_fund_page.value = page_from_url.value

    
    
    const landing_image = {
        title: "Boysterous Couture",
        title_color: "#fff",
        text_align: "left",
        line_width: "860px",
        line_margin: "50px",
        image: image1,
        font_calc: "1"
    }
    
    const big_text_1 = {text:'Made By Hand', font_size:'12.5vw', margin_top:'5%', padding_top:'0'}
    
    
    const intro_info ={
        video: '',
        image: image2,
        is_image: true,
        is_video: false,
        main_text:"<h3>Boysterous Southern Couture</h3> We are proud to pledge that each of our luxury leather accessories are patiently and expertly designed by hand in historic Charleston, South Carolina. <br><br> Throughout our website you will find a series of heirloom collections that feature one-of-one designs that, because the nature of bespoke leather crafting, will never be available again once inherited. <br><br> Be sure to take time to appreciate the intricacies and nuances of our designs as you are looking through our collections. If you are interested in purchasing custom couture, please fill out our contact form to begin the design process."
    }
    
    const slab1 = {
        margin_top:"25%",
        margin_bottom: "0%",
        image: image3,
    }
    
    const big_text_2 = {text:'Luxury Fashion', font_size:'13.55vw', margin_top:'5%', padding_top:'0'}
    
    
    const strategy = {
        video: '',
        image: image6,
        is_image: true,
        is_video: false,
        image_margin_calc: "1.2",
        image_margin_mobile_calc: "1",
        container_margin:"0%",
        container_margin_bottom:"-110%",
        title:"Key Investors",
        text:"Private - Contact For Access"}
    
    
    
    const revenue = {
        image: image4,
        image_margin: "40%",
        title:"Directors",
        text:"CEO<br>Nicholas Overstreet <br><br>COO<br>Naif Hajjar"
    }
    
    const swiper_images = {
        image_1: swiper1,
        image_2: swiper2,
        image_3: swiper3
    }
    
    const big_text_3 = {text:'Be Boysterous', font_size:'14.35vw', margin_top:'2%', padding_top:'2%'}
    
    
    const investment_highlights = {
        title_1: "Company Name:",
        info_1: "Boysterous Couture",
        title_2: "Offering Amount:",
        info_2: "$280,000",
        title_3: "Minimum Investment:",
        info_3: "$25,000",
        title_4: "Implied Valuation:",
        info_4: "$1.4 M",
        title_5: "Security Type:",
        info_5: "Units of Interest",
        title_6: "Discount:",
        info_6: "N/A",
        image: image5,
        image_margin: "20%"
    }
    
    const slab2 = {
        margin_top:"10%",
        margin_bottom: "5%",
        video: vid1,
    }
    

    
    const big_text_4 = {text:'Unique Leathers', font_size:'12.5vw', margin_top:'5%', padding_top:'2%'}
    
    

    const company_highlights = {
    left_side_text: "• Boysterous Couture Is An Arthouse Tailoring The Ambition Of Slow Fashion With Using Ethically Sourced Fine Leathers From Home And Abroad While Challenging The Face + The Pace Of Luxury Fashion. <br><br>• Recently partnered with Suited Ltd Co. to design and manufacture high end playing cards for and and a line of couture cases.",
    right_side_text_1: "• Partnered with WAX to launch a line of NFT backed products, tokens, and experiences with excellent uptake by the online community.",
    right_side_text_2: "• A successful Spring pop-up store in Downtown Charleston led to a permanent first storefront nearby.",
    image: '',
    has_image:false
}



const top_products = {
        image: image8,
        image_margin: "25%",
        title:"Top Products",
        text:"<p style='color:#000'> • The Original Oyster Shell Bowtie <br><br> • The Leather Choker <br><br> • The One-of-a-kind Clutch <br><br> • The Man’s Exotic Leather Wallet <br><br> • The Exotic Leather Purse <br><br> • The Exclusive Leather Apple Watch Wrist Band",
        text_2:''
    }
    




    const footer = {
        title:"Social Wise",
        image:image9,
        nuxt_link:"/fund_pages/social_wise",
    }
    
    
    
    const uncover = ref()
        
    
  
    
        
    
    
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


    
@media only screen and (min-width: 900px) and (max-width: 5200px) {
.comp_highlights_margin{
    margin-top:-20%
}

}
    
    
    
    
    
    
    
    
    </style>