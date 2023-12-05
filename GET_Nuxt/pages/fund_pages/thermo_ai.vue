<template>

    <div>
    <Header/>
    
    <GSAPScrollSmoother>
    
        <FundPagesSectionsLanding v-bind="landing_image"/>
        <p class="landing_subtext">Tuning Combustion Parameters</p>
        <FundPagesCompsBigText v-bind="big_text_1"/>
        <FundPagesSectionsIntroInfo v-bind="intro_info"/>
        <FundPagesCompsSlabImg v-bind="slab1"/>
        <FundPagesCompsBigText v-bind="big_text_2"/>
        <FundPagesSectionsStrategy v-bind="strategy"/>
        <FundPagesSectionsRevenue v-bind="revenue"/>
    
      
    <div class="white_section">
    
        <FundPagesCompsBigText v-bind="big_text_3"/>
        <FundPagesSectionsStrategy v-bind="inv_highlights"/>

        <div class="slab_move">
        <FundPagesCompsSlabImg v-bind="slab2"/>
         </div>
        <FundPagesCompsBigText v-bind="big_text_4"/>
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
    import { useWindowSize } from '@vueuse/core'
    import { gsap } from 'gsap'
    import { page_to } from "../../stores/page_to.js"
    
    import image1 from "~/assets/content/fund_pages/thermo_ai/thermo_5.jpg";
    import image2 from "~/assets/content/fund_pages/thermo_ai/thermo_8.png"
    import image3 from "~/assets/content/fund_pages/thermo_ai/thermo_12.jpeg"
    import image4 from "~/assets/content/fund_pages/thermo_ai/thermo_16.jpg"
    import image5 from "~/assets/content/fund_pages/thermo_ai/thermo_13.jpg"
    import image6 from "~/assets/content/fund_pages/thermo_ai/thermo_14.jpg"
    import image7 from "~/assets/content/fund_pages/thermo_ai/thermo_15.jpg"
    import image8 from "~/assets/content/fund_pages/agile/agile_7.jpg"
    



    const most_recent_fund_page = useCookie('most_recent_fund_page', {default:()=> '', watch:true, maxAge:18000})
    const route_from = page_to()
    const page_from_url = ref(String(route_from.current_page_from).replace('/fund_pages/','').replace('/invest_flow/',''))
    console.log('page from is - ', page_from_url.value)
    most_recent_fund_page.value = page_from_url.value

    
    
    const landing_image = {
        title: "Thermo A.I.",
        title_color: "#fff",
        text_align: "center",
        line_width: "790px",
        line_margin: "35px",
        image: image1,
        image_width: "100%",
        font_calc: "1"
    }
    
    const big_text_1 = {text:'Optimizing Combustion', font_size:'12.5vw', margin_top:'5%', padding_top:'0'}
    
    
    const intro_info ={
        video: '',
        image: image2,
        is_image: true,
        is_video: false,
        main_text:"<p>ThermoAI is using Artificial Intelligence (AI) and IoT (the Internet of Things) to optimize combustion, with the goal of saving millions in fuel and reducing emissions. ThermoAI’s product is currently seeing an increase of combustion efficiency of up to 20% with their early pilots. <br><br> ThermoAI relies on Artificial Intelligence techniques such as flexible regression hierarchy, to simulate plant operations in order to achieve optimal levels of combustion efficiency. This ensemble implements a nonparametric causal graph whose structure mirrors that of the target facility. They train an adaptive optimization algorithm to predict ideal airflow settings using the structural knowledge learned by our simulator. dynamic trajectories are regularized with smoothing splines.</p>"
    }
    
    const slab1 = {
        margin_top:"25%",
        margin_bottom: "0%",
        image: image3,
    }
    
    const big_text_2 = {text:'Maximizing Efficiency', font_size:'9.25vw', margin_top:'5%', padding_top:'0'}
    
    
    const strategy = {
        video: '',
        image: image5,
        is_image: true,
        is_video: false,
        image_margin_calc: "1.2",
        image_margin_mobile_calc: "1",
        container_margin:"5%",
        container_margin_bottom:"-90%",

        image_margin_calc: "70",
    text_margin_mobile: "-80%",



        title:"Key Investors",
        text:"<p>National Science Foundation<br><br>Techstars AI<br><br>NYSERDA<br>Creative Destruction Labs AI</p>"}
    
    
    
    const revenue = {
        image: image7,
        image_margin: "75%",
        title:"Management",
        text:"<span style='text-decoration: underline'>CEO & Co-Founder</span><br>Aiden Livingston<br><br><span style='text-decoration: underline'>CTO & Co-Founder</span><br>David Watson<br><br><span style='text-decoration: underline'>COO & Co-Founder</span><br>Carolina Chaves<br><br><span style='text-decoration: underline'>Advisor</span><br>Kebir Ratnani<br><br><span style='text-decoration: underline'>Advisor</span><br>Allan Benchetrit<br><br><span style='text-decoration: underline'>Research Partner</span><br>Benjamin Kumfer"
    }
    

    const big_text_3 = {text:'Environmentally Conscientious', font_size:'12.5vw', margin_top:'2%', padding_top:'2%'}
    
    
    const inv_highlights = {
        video: '',
        image: image4,
        is_image: true,
        is_video: false,
        container_margin:"0%",
        container_margin_bottom:"10%",
        title:"Investment Highlights",
        text:"<p>Private - Contact For Access</p>"}
    



    
    const slab2 = {
        margin_top:"20%",
        margin_bottom: "5%",
        image: image6,
    }
    

    
    const big_text_4 = {text:'Non-Intermittent Renewable', font_size:'12vw', margin_top:'5%', padding_top:'2%'}


    const company_highlights = {
    left_side_text: "• The Thermo A.I. team has over 100 years of experience building innovative new industrial solutions <br><br>• In 2021, ThermoAI won the grand prize of a $1M grant from NYSERDA. As a result the company moved its headquarters to NY state to pursue public and private partnerships in developing and implementing their technology.<br><br><br>",
    right_side_text_1: "• Their partnership with the state of New York has led to a close partnership with Binghamton University’s AI department who are helping to develop the next generation of combustion modeling with the team.",
    right_side_text_2: "• Initial tests show the AI systems improving the combustion efficiency of up to 20% and removing nearly all of the output variability in the system.",
    image: '',
    has_image:false
}



    
    
    const footer = {
        title:"Agile Elements",
        image:image8,
        nuxt_link:"/fund_pages/agile_elements",
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


@media only screen and (min-width: 0px) and (max-width: 430px) {
    
    .slab_move{
        margin-top:-120%;
        margin-bottom:30%
    }
    
}

@media only screen and (min-width: 430px) and (max-width: 576px) {
    
    .slab_move{
        margin-top:-110%;
        margin-bottom:20%
    }
    
}
    
    
    
    
    </style>