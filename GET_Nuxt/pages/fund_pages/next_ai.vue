<template>


    <div style="background-color: black; height 100%;">
    <Header/>
    
    <!-- <FundPagesCompsNDAmodal v-bind="nda_fund" /> -->
    
    <GSAPScrollSmoother>
    
        <FundPagesFundsNextAiReserveLanding v-bind="landing_image"/>
        <p class="landing_subtext">NEXT AI Fund</p>
        <FundPagesCompsBigText v-bind="big_text_1"/>
        <FundPagesFundsNextAiIntroInfo v-bind="intro_info"/>
        <FundPagesFundsNextAiCompanyVideoScroller/>

        <FundPagesCompsSlabImg v-bind="slab1"/>
        <FundPagesCompsBigText v-bind="big_text_2"/>
        <FundPagesFundsNextAiStrategy/>
    
      
    <div class="white_section">
        <FundPagesCompsBigText v-bind="big_text_3"/>
        <FundPagesFundsNextAiBulletSection/>
        <FundPagesCompsSlabImg v-bind="slab2"/>
        <FundPagesSectionsInvestmentHighlights v-bind="investment_highlights"/>
        <FundPagesFundsNextAiManagersNote/>
        
    
    
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
    
    import image1 from "~/assets/content/fund_pages/next_ai/next_2.jpg";
    import image2 from "~/assets/content/fund_pages/next_ai/next_ai.png"
    import image3 from "~/assets/content/fund_pages/next_ai/next_11.jpg"
    import image4 from "~/assets/content/fund_pages/next_ai/next_8.jpg"
    import image5 from "~/assets/content/fund_pages/next_ai/next_10.jpg"
    import image6 from "~/assets/content/fund_pages/next_ai/next_5.jpg"
    import image7 from "~/assets/content/fund_pages/next_ai/next_9.jpg"
    import image8 from "~/assets/content/fund_pages/eco/eco_9.jpg"
    import image10 from "~/assets/content/fund_pages/eco/eco_10.jpg"


    await preloadComponents(['FundPagesSectionsLanding', 'FundPagesFundsNextAiCompanyVideoScroller'])
    

    const most_recent_fund_page = useCookie('most_recent_fund_page', {default:()=> '', watch:true, maxAge:18000})
    const route_from = page_to()
    const page_from_url = ref(String(route_from.current_page_from).replace('/fund_pages/','').replace('/invest_flow/',''))
    console.log('page from is - ', page_from_url.value)
    most_recent_fund_page.value = page_from_url.value



    const nda_completed = ref(false)
    
    function nda_submit(){
        nda_completed.value = true
    }

    const naif_vid = {
        vid:'',
        image:'',
    }
    
    const nda_fund = {investment: "next"}
    
    const landing_image = {
        title: "NEXT AI Fund",
        title_color: "#ff0aff",
        text_align: "center",
        line_width: "575px",
        line_margin: "157.5px",
        image: image1,
        image_width: "125%",
        font_calc: "1"
    }
    
    const big_text_1 = {text:'The NEXT Wave', font_size:'12vw', margin_top:'5%', padding_top:'0'}

    
    const intro_info ={
        video: '',
        image: image2,
        is_image: true,
        is_video: false,
        main_text:"The first fund of its kind. GET Equity Partners has once again created a unique investment opportunity and this time it’s in Artificial Intelligence, the most coveted industry in the world.<br><br>Investment strategy in the new, dynamic, and disruptive AI sector is critical. GET Equity Partners brings a seasoned team with deep practical and investment AI expertise. This is leveraged to identify and “and evaluate smart, high-value opportunities.<br><br>The critical component to a successful fund of this nature is to offer access to all parts of the AI stack, including: hardware, platform, and application. Investing in silicon is as important as investing in the best LLMs, both of which support a robust ecosystem at the application layer. Our team knows the players across the industry, not just the obvious names everyone else is chasing.</p>"
    }
    
    
    const slab1 = {
        margin_top:"0%",
        margin_bottom: "0%",
        image:image3
    }
    
    const big_text_2 = {text:'Take The Next Step', font_size:'10vw', margin_top:'5%', padding_top:'0'}



    
    


    const big_text_3 = {text:'A New Investment for a Better Future', font_size:'10.75vw', margin_top:'2%', padding_top:'2%'}
    
        
    const revenue = {
        image: image7,
        image_margin: "15%",
        text_margin: "-15%",
        title:"Building a Balanced Portfolio - Not all AI is Equal",
        text:"As we move towards building our portfolio, we do not solely focus on what's trending but strive to invest across a balanced spectrum of the AI stack. This involves an understanding that not all AI is equal; there are different forms, applications, and technologies that require varied expertise and resources. Our approach is to strike the right balance in investing in the game-changing technologies and also the foundational layers that enable those technologies.",
        text_2:"We are constantly scanning and analyzing a diverse range of AI companies, from the breakthrough innovators shaping the landscape to the infrastructural giants enabling the AI revolution. This includes machine learning, neural networks, robotics, natural language processing, and more. Our portfolio is purposefully diverse, reflecting our belief in the transformative power of AI across sectors - from healthcare and education to finance, energy, and beyond.<b>Enhanced Oil Recovery is Green Because It:</b> <br><br>⚫ Avoids habitat loss due to well pad creation, lease roads & flowlines, pipelines & power lines<br><br>⚫ Avoids the use of a million or more gallons of fresh water per well<br><br>⚫ Avoids venting or flaring of methane gas (among the worst of the Greenhouse Gasses) while waiting on construction of the production infrastructure<br><br>⚫ Avoids carbon emissions associated with high pressure fracking<br><br>⚫ Avoids contamination of groundwater due to poor cement jobs and chemical processes.<br><br>⚫ Preserves potential farm and grazing land for commercial food operations"
    }

    const slab2 = {
        margin_top:"10%",
        margin_bottom: "10%",
        image:image6
    }


    const investment_highlights = {
        title_1: "Company Name:",
        info_1: "Next AI Fund",
        title_2: "Entity Type:",
        info_2: "Speacialty Purpose Vehicle / LLC",
        title_3: "Min Investment:",
        info_3: "$10,000",
        title_4: "Fund Goal:",
        info_4: "$10,000,000",
        title_5: "Investment Duration:",
        info_5: "3-5 Years",
        title_6: "Investment Goal:",
        info_6: "4-7X Returns",
        image: image5,
        image_margin: "70%"
    }
    
    const text_section = {
        lower_text: "The principal underlying company is run by a management team which has been working and innovating in the EOR space for 3 decades and counting. They have worked for some of the biggest names in the Oil and Gas space and bring their expertise to this project.<br><br>Along with management experience, the company has a dedicated and experienced field team who have proven their knowledge and capabilities in the field for decades each. Perhaps most critically, the company recently made a major investment in dedicated equipment for the cleaning and preparing of sites, which means increased returns, and efficiency in revitalizing wells.",
        image: '',
        has_image:false
    }
    

    
    const footer = {
        title:"Eco <br> Energy",
        image:image8,
        nuxt_link:"/fund_pages/eco",
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