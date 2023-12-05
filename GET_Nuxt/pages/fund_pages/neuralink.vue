<template>

    <div style="background-color: black; height 100%;">
    <Header/>
    
    
    
    <GSAPScrollSmoother>
    
        <FundPagesSectionsLanding v-bind="landing_image"/>
        <p class="landing_subtext">Breakthrough Brain Technology</p>
        <FundPagesCompsBigText v-bind="big_text_1"/>
        <FundPagesSectionsIntroInfo v-bind="intro_info"/>
        <FundPagesCompsSlabImg v-bind="slab1"/>
        <FundPagesCompsBigText v-bind="big_text_2"/>
        <FundPagesSectionsStrategy v-bind="strategy"/>

    
      
    <div class="white_section">
        <FundPagesCompsBigText v-bind="big_text_3"/>
        <FundPagesSectionsExtraSection v-bind="revenue"/>
        <FundPagesCompsSlabImg v-bind="slab2"/>
        <FundPagesSectionsInvestmentHighlights v-bind="investment_highlights"/>
        <FundPagesSectionsCompanyHighlights v-bind="company_highlights"/>
    
    
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
    import { page_to } from "../../stores/page_to.js"
    import { gsap } from 'gsap'
    
    import image1 from "~/assets/content/fund_pages/neuralink/neuro_5.jpg";
    import image2 from "~/assets/content/fund_pages/neuralink/neuro_14.png"
    import image3 from "~/assets/content/fund_pages/neuralink/neuro_8.jpg"
    import image4 from "~/assets/content/fund_pages/neuralink/neuro_13.png"
    import image5 from "~/assets/content/fund_pages/neuralink/neuro_6_square.jpg"
    import image6 from "~/assets/content/fund_pages/neuralink/neuro_4.png"
    import image7 from "~/assets/content/fund_pages/neuralink/neuro_15.png"
    import image8 from "~/assets/content/fund_pages/thermo_ai/thermo_11.jpg"
    
    
    

    const most_recent_fund_page = useCookie('most_recent_fund_page', {default:()=> '', watch:true, maxAge:18000})
    const route_from = page_to()
    const page_from_url = ref(String(route_from.current_page_from).replace('/fund_pages/','').replace('/invest_flow/',''))
    console.log('page from is - ', page_from_url.value)
    most_recent_fund_page.value = page_from_url.value



    const nda_completed = ref(false)
    
    function nda_submit(){
        nda_completed.value = true
    }
    
    
    const landing_image = {
        title: "Neuralink",
        title_color: "rgb(69, 159, 239)",
        text_align: "center",
        line_width: "575px",
        line_margin: "157.5px",
        image: image1,
        image_width: "125%",
        font_calc: "1"
    }
    
    const big_text_1 = {text:'Brain-Computer Interface', font_size:'12.5vw', margin_top:'5%', padding_top:'0'}

    
    const intro_info ={
        video: '',
        image: image2,
        is_image: true,
        is_video: false,
        main_text:'<p>Neuralink is developing the capabilities of the brain through technological augmentation. A "neural lace” would be surgically connected to a human brain and allow a user to interact with a computer without the bandwidth challenges that come with current input methods, including keyboards, mice and trackpads. Neuralink will explore how brain interfaces might alleviate the symptoms of dangerous and chronic medical conditions.<br><br> Neuralink, a secretive company developing brain-machine interfaces and founded by Elon Musk, finally showed off some of its technology in a July 2019 presentation to the public. The goal is to eventually begin implanting devices in paralyzed humans, allowing them to control things like computers and smartphones. This will be done via “threads” that are thinner than a piece of hair and capable of transferring electrodes to the brain. These threads are less likely to damage the brain than materials that are currently used for brain-machine interfaces, making them a safer technology.</p>'
    }
    
    
    const slab1 = {
        margin_top:"0%",
        margin_bottom: "0%",
        image:image3
    }
    
    const big_text_2 = {text:'Supercharge Cognition', font_size:'15vw', margin_top:'5%', padding_top:'0'}


    const strategy = {
        video: '',
        image: image7,
        is_image: true,
        is_video: false,
        image_margin_calc: "1.2",

        image_margin_mobile_calc: "1",
        text_margin_mobile: "-80%",
        container_margin_bottom:"-60%",


        title:"Key Investors",
        text:"Elon Musk <br><br> Dreamers Fund <br><br> Undisclosed"
    }
    
    


    const big_text_3 = {text:'Neural Lace', font_size:'16.75vw', margin_top:'2%', padding_top:'2%'}
    
        
    const revenue = {
        image: image5,
        image_margin: "40%",
        title:"Revenue Sources",
        text:" World-Class IP Portfolio Supports Multi-Billion Dollar Addressable Markets. <br><br> 220+ Patents, Extensive Trade Secrets, and substantial Process know-how based on decades of research at MIT. <br><br> Elegantly simple platform which is inherently safe and uses less energy than competition due to the exothermic natures of the process.",
        text_2:''
    }

    const slab2 = {
        margin_top:"10%",
        margin_bottom: "10%",
        image:image6
    }


    const investment_highlights = {
        title_1: "Company Name:",
        info_1: "Neuralink Corporation",
        title_2: "Security Type:",
        info_2: "Preferred Stock",
        title_3: "Stock Access:",
        info_3: "Very Lmited",
        title_4: "Valuation at Bid:",
        info_4: "TBD",
        title_5: "Price at Bid:",
        info_5: "TBD",
        title_6: "",
        info_6: "",
        image: image4,
        image_margin: "40%"
    }
    
    const company_highlights = {
        left_side_text: "• Musk admitted during the presentation that a monkey was able to control a computer with its brain. Neuralink hopes to have their device planted in a human patient by the end of 2020 pending FDA approval.<br><br><br>",
        right_side_text_1: "• Musk has poured $100 million (of $158 million raised) of his own funds into the company.",
        right_side_text_2: "Note: Information publicly reported. When not reported by the company or any of its repvntatives, information may not have been verified by the company or by GET.",
        image: '',
        has_image:false
    }
    

    
    const footer = {
        title:"Thermo A.I.",
        image:image8,
        nuxt_link:"/fund_pages/thermo_ai",
    }
    
    
    
    
    
    </script>
    
    
    
    <style scoped>
    
    .nda_completed{
        display:none !important
    }
    
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