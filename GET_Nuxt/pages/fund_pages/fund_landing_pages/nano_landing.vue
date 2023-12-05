<template>


    <div>
    
    
    
    <Header/>
    
    <FundPagesCompsNDAmodal v-bind="nda_fund" />
    
    <GSAPScrollSmoother>
    
        <FundPagesSectionsLanding v-bind="landing_image"/>
        <p class="landing_subtext">Nano Stuff abc</p>
        <FundPagesCompsBigText v-bind="big_text_1"/>
        <FundPagesSectionsIntroInfo v-bind="intro_info"/>
        <FundPagesCompsSlabImg v-bind="slab1"/>
        <FundPagesCompsBigText v-bind="big_text_2"/>
        <FundPagesSectionsStrategy v-bind="strategy"/>
        <!-- <FundPagesSectionsRevenue v-bind="revenue"/> -->
        <FundPagesCompsVerticalArrows/>
        <FundPagesCompsSwiperCards v-bind="swiper_images"/>
    
      
    
    
    
    <div class="white_section">
    
        <FundPagesCompsBigText v-bind="big_text_3"/>
        <FundPagesSectionsInvestmentHighlights v-bind="investment_highlights"/>
        <!-- <FundPagesSectionsCompanyHighlights v-bind="company_highlights"/> -->
        <img data-lag=".2" class="company_hightlights_image" src="~/assets/content/fund_pages/nano/nano_20.png"/>
        <FundPagesCompsBigText v-bind="big_text_4"/>
        <FundPagesSectionsUserbase/>
        <p class="user_extra_text">The industries Nano-C’s products address are among the largest and most valuable ones on the planet.<br><br>In each of the main business areas Nano-C has piloted and had their applied nanocarbon solution “Qualified” with top suppliers and/or manufacturers.<br><br>The results have been consistent across applications and solutions, Nano-C is delivering the highest quality nanocarbon products available, and doing so at competitive prices.<br><br>The adjacent list is a partial list of companies in late-stage talks with Nano-C to take their partnership to the commercialization phase. Each one represents a multimillion dollar revenue stream.
    </p>
    
    
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
    import { page_to } from "~/stores/page_to.js"
    
    import image1 from "~/assets/content/fund_pages/nano/nano_1.jpg";
    import vid1 from "~/assets/content/fund_pages/nano/nano_3.mp4"
    import image2 from "~/assets/content/fund_pages/nano/nano_chip_2.png"
    import image3 from "~/assets/content/fund_pages/nano/nano_14.png"
    import image4 from "~/assets/content/fund_pages/nano/nano_19.jpg"
    import image5 from "~/assets/content/fund_pages/nano/nano_20.png"
    import image6 from "~/assets/content/fund_pages/landing_pages/nano_landing/nano_landing_1.jpg"
    import image7 from "~/assets/content/fund_pages/nano/nano_6.jpg"
    
    import swiper1 from "~/assets/content/fund_pages/nano/1.jpg"
    import swiper2 from "~/assets/content/fund_pages/nano/2.jpg"
    import swiper3 from "~/assets/content/fund_pages/nano/3.jpg"
    
    
    
    
    const most_recent_fund_page = useCookie('most_recent_fund_page', {default:()=> '', watch:true, maxAge:18000})
        const route_from = page_to()
        const page_from_url = ref(String(route_from.current_page_from).replace('/fund_pages/','').replace('/invest_flow/',''))
        console.log('page from is - ', page_from_url.value)
        most_recent_fund_page.value = page_from_url.value
    
    
    
    
    
    const landing_image = {
        title: "NanoTechnology Fund",
        title_color: "rgb(69, 159, 239)",
        text_align: "center",
        line_width: "575px",
        line_margin: "157.5px",
        image: image1,
        image_width: "135%",
        font_calc: ".93"
    }
    
    const big_text_1 = {text:'NanoCarbon Mastered.', font_size:'14vw', margin_top:'5%', padding_top:'0'}
    const big_text_2 = {text:'Competative Advantage', font_size:'15vw', margin_top:'5%', padding_top:'0'}
    
    const intro_info ={
        video: vid1,
        image: '',
        is_image: false,
        is_video: true,
        main_text:"<span style='font-size:200%; font-weight:900; line-height:1.1'>$294 million dollars in upcoming contracts WILL change the game for our project.</span> <br><br>GET Equity Partners is proud to offer access to Nano-C Inc., a nanocarbon applications company which is working with the biggest names in solar, semiconductors, touch sensors, and more (names below) on the verge of unlocking massive revenue.<br><br>Based on extensive research, engagement with subject matter experts, and in-depth interviews with senior management, GET Equity Partners has determined that now is the time to get involved in helping to arrange pre-ipo financing. Nano-C has patent protected process and portfolio, a highly experienced team, and a best in class product as determined by current and future clients. All of this supports a substantial exit - either via IPO or acquisition.<br><br>In other words by the time Main Street knows about our project we plan to be selling our shares to them and we would do so ideally for the aforementioned premium. "
    }
    
    
    const slab1 = {
        margin_top:"0%",
        margin_bottom: "0%",
        image:image7
    }
    
    
    const strategy = {
        video: '',
        image: image2,
        is_image: true,
        is_video: false,
        has_invest_button:true,
        // container_margin:"50%",
        image_margin_calc: "70",
        image_margin_mobile_calc: "1",
        text_margin_mobile: "-200%",
        title:"Strategy",
        text:"Nano-C has been perfecting nanocarbon materials - fullerenes and nanotubes - for two decades; the technology and process is now tested, piloted, approved, and ready for commercialization.<br><br>GET Equity Partners is partnering with a top VC firm to fund the growth stage of Nano-C in advance of a series of commercialization contracts with top companies in semiconductors, solar, batteries, and more.<br><br>Nano-C, whose team and technology are out of Massachusetts Institute of Technology (MIT) and boast over 20 years of experience and now-how in the space, is a company at the inflection point for massive growth. They have proven their product lines across several BILLION dollar industries and are locking in hugely valuable contracts with Fortune 100/500 companies.<br><br>The result is a multi-pronged strategy with a number of applications potentially worth hundreds of millions in revenue to company.<br><br><span style='font-size:200%; font-weight:900; line-height:1.1'>This your opportunity</span>",
    }
    
    
    
    const revenue = {
        image: image3,
        image_margin: "5%",
        title:"Revenue Sources",
        text:"Nanocarbon has applications across some of the largest sectors globally including Electronic, Energy, and Healthcare. The total addressable markets to Nano-C is over $11.1 Billion. With major commercial contracts imminent, now is the time to get involved."
    }
    
    const swiper_images = {
        image_1: swiper1,
        image_2: swiper2,
        image_3: swiper3
    }
    
    const big_text_3 = {text:'220 Patents', font_size:'16.75vw', margin_top:'2%', padding_top:'2%'}
    
    const nda_fund = {investment: "nano"}
    
    
    const investment_highlights = {
        title_1: "Fund Name:",
        info_1: "US Nanotechnology Fund A",
        title_2: "Strategy:",
        info_2: "Growth",
        title_3: "Unit Price:",
        info_3: "$1,000",
        title_4: "Max Investment:",
        info_4: "$5,000,000",
        title_5: "Term:",
        info_5: "3 Years",
        image: image4,
        image_margin: "40%"
    }
    
    // const company_highlights = {
    //     left_side_text: "Decades of research at MIT have lead to major breakthroughs in nanotechnology manufacturing and applications across three distinct billion dollar sectors of the economy: Energy, Electronics, and Healthcare. <br><br> Deep relationships with customers who have vetted the technology for their specific applications.",
    //     right_side_text_1: "Electronics sector applications as such:  <br><br> Security / Biometrics <br> Race to Extend Moore’s Law <br> Connectivity through IoT <br> Mobility <br> Roll-out of 5G <br><br> Healthcare: <br><br> Chronic Disease <br> Treatment Pandemics <br> Remote Patient Monitoring",
    //     right_side_text_2: "Energy sector applications such as: <br><br> Renewable Energy <br> Climate Change <br> Green Hydrogen <br> Environmental <br> Monitoring",
    //     image: image5
    // }
    
    
    const big_text_4 = {text:'Advancing Semiconductors', font_size:'12.5vw', margin_top:'5%', padding_top:'2%'}
    
    
    const footer = {
        title:"Invest Now",
        image:image6,
        nuxt_link:"../../invest_flow/step_1/",
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
        margin-top:0%;
        background-color:#000;
    }
    
    
    
    .user_extra_text{
        width:70%;
        margin-left:15%;
        text-align:center;
        font-size:150%;
        line-height:1.2
    }
    
    
    
    
    .company_hightlights_image{
        width:60%;
        margin-left:20%;
        margin-bottom:0%;
        margin-top:15%
    }
    
    
    
    
    @media only screen and (min-width: 0px) and (max-width: 376px) {
    
    .company_hightlights_image{
        margin-top:10%
    }
    
    }
    
    
    @media only screen and (min-width: 376px) and (max-width: 430px) {
    
    
    .company_hightlights_image{
        margin-top:10%
    }
    
    }
    
    
    
    
    
    @media only screen and (min-width: 430px) and (max-width: 500px) {
    
    .company_hightlights_image{
        margin-top:0%
    }
    
    }
    
    
    @media only screen and (min-width: 500px) and (max-width: 530px) {
    
    
    
    .company_hightlights_image{
        margin-top:0%;
    }
    
    
    }
    
    
    @media only screen and (min-width: 530px) and (max-width: 576px) {
    
    .company_hightlights_image{
        margin-top:0%
    }
    
    }
    
    
    
    
    
    
    
    
    
    </style>