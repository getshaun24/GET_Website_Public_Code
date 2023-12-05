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
    import { page_to } from "../../stores/page_to.js"
    
    import { gsap } from 'gsap'
    
    import image1 from "~/assets/content/fund_pages/boring_company/boring_12_1.jpg";
    import image2 from "~/assets/content/fund_pages/boring_company/boring_9.png"
    import image3 from "~/assets/content/fund_pages/boring_company/boring_5.jpg"
    import image4 from "~/assets/content/fund_pages/boring_company/boring_13.jpg"
    import image5 from "~/assets/content/fund_pages/boring_company/boring_2.jpg"
    import image6 from "~/assets/content/fund_pages/boring_company/boring_10_1.jpg"
    import image7 from "~/assets/content/fund_pages/boring_company/boring_3.jpg"
    import image8 from "~/assets/content/fund_pages/helpful/helpful_8.jpg"
    

    
    const most_recent_fund_page = useCookie('most_recent_fund_page', {default:()=> '', watch:true, maxAge:18000})
    const route_from = page_to()
    const page_from_url = ref(String(route_from.current_page_from).replace('/fund_pages/','').replace('/invest_flow/',''))
    console.log('page from is - ', page_from_url.value)
    most_recent_fund_page.value = page_from_url.value



    const landing_image = {
        title: "The Boring Company",
        title_color: "#fff",
        text_align: "left",
        line_width: "790px",
        line_margin: "35px",
        image: image1,
        image_width: "120%",
        font_calc: "1"
    }
    
    const big_text_1 = {text:'Beyond Tunnels', font_size:'12.75vw', margin_top:'5%', padding_top:'0'}
    
    
    const intro_info ={
        video: '',
        image: image2,
        is_image: true,
        is_video: false,
        main_text:"The Boring Company's mission is to solve the problem of soul-destroying traffic, roads must go 3D, which means either flying cars or tunnels. Unlike flying cars, tunnels are weatherproof, out of sight and won't fall on your head. A large network of tunnels many levels deep would help alleviate congestion in any city, no matter how large it grew (just keep adding levels).<br><br>The key to making this work is increasing tunneling speed and dropping costs by a factor of 10 or more – this is the goal of The Boring Company. Fast to dig, low cost tunnels would also make Hyperloop adoption viable and enable rapid transit across densely populated regions, enabling travel from New York to Washington DC in less than 30 minutes."
    }
    
    const slab1 = {
        margin_top:"25%",
        margin_bottom: "0%",
        image: image3,
    }
    
    const big_text_2 = {text:'First Principals', font_size:'14vw', margin_top:'5%', padding_top:'0'}
    
    
    const strategy = {
        video: '',
        image: image4,
        is_image: true,
        is_video: false,
        image_margin_calc: "1.2",
        image_margin_mobile_calc: "1",
        container_margin:"0%",
        container_margin_bottom:"-100%",
        title:"Key Investors",
        text:"Vy Capital <br><br> Craft Ventures<br><br>8VC<br><br>Future Ventures<br><br>Threshold<br><br>Gigafund"}
    
    
    
    const revenue = {
        image: image5,
        image_margin: "40%",
        title:"Management",
        text:"<span style='text-decoration: underline'>Founder</span><br>Elon Musk<br><br><span style='text-decoration: underline'>Director, Office of the CEO</span><br>Sam Teller<br><br><span style='text-decoration: underline'>Finance & Operations</span><br>Greg Smithies<br><br><span style='text-decoration: underline'>Electrical Engineer</span><br>Eric Amikam"
    }
    

    
    const big_text_3 = {text:'Zero-Emmissions', font_size:'12.5vw', margin_top:'2%', padding_top:'2%'}
    
    
    const investment_highlights = {
        title_1: "Company Name:",
        info_1: "The Boring Company",
        title_2: "Security Type:",
        info_2: "Common Stock",
        title_3: "Implied Company Valuation:",
        info_3: "N/A",
        title_4: "Latest Post Money Valuation:",
        info_4: "950 Million",
        title_5: "Discount:",
        info_5: "N/A",
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
    

    
    const big_text_4 = {text:'Non-Intermittent Renewable', font_size:'12vw', margin_top:'5%', padding_top:'2%'}
    
    
    const footer = {
        title:"Helpful+",
        image:image8,
        nuxt_link:"/fund_pages/helpful",
    }
    
    
    
    const uncover = ref()
        
    
    onMounted(() => {
    
        gsap.set(".next_footer", { yPercent: 200 });
        uncover.value = gsap.timeline({ paused: true });
    
    uncover.value.to(".next_footer", { yPercent: -20, ease:"ease-in-out" });
    
    ScrollTrigger.create({
      trigger: ".white_section",
      start: "bottom bottom",
      end: "+=100%",
      animation: uncover.value,
      scrub: true,
    });
    
    ScrollTrigger.refresh();
    
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
    z-index:-1;
    border-top: 1px solid rgba(255, 255, 255, 0.3);
    margin-top:0%;
}


    
    
    
    
    
    
    
    
    
    
    </style>