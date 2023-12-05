<template>

    <div style="background-color: black; height 100%;">
    <Header/>
    
    <!-- <FundPagesCompsNDAmodal v-bind="nda_fund" /> -->
    
    <GSAPScrollSmoother>
    
        <FundPagesSectionsLanding v-bind="landing_image"/>
        <p class="landing_subtext">Oil & Gas Revitalization Fund</p>
        <FundPagesCompsBigText v-bind="big_text_1"/>
        <FundPagesSectionsIntroInfo v-bind="intro_info"/>
        <FundPagesSectionsVidAndImage v-bind="naif_vid"/>
        <FundPagesCompsSlabImg v-bind="slab1"/>
        <FundPagesCompsBigText v-bind="big_text_2"/>
        <FundPagesSectionsStrategy v-bind="strategy"/>

    
      
    <div class="white_section">
        <FundPagesCompsBigText v-bind="big_text_3"/>
        <FundPagesSectionsExtraSection v-bind="revenue"/>
        <FundPagesCompsSlabImg v-bind="slab2"/>
        <FundPagesSectionsInvestmentHighlights v-bind="investment_highlights"/>
        <FundPagesSectionsTextSection v-bind="text_section"/>
    
    
    <div class="bottom_line"></div>
    
    <FundPagesSectionsBottom2/>
    
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
    
    import image1 from "~/assets/content/fund_pages/eco/eco_2_1.jpg";
    import image2 from "~/assets/content/fund_pages/eco/eco_3.jpg"
    import image3 from "~/assets/content/fund_pages/eco/eco_4.jpg"
    import image4 from "~/assets/content/fund_pages/eco/eco_5.png"
    import image5 from "~/assets/content/fund_pages/eco/eco_6x.png"
    import image6 from "~/assets/content/fund_pages/eco/eco_1x.jpg"
    import image7 from "~/assets/content/fund_pages/eco/eco_8.jpg"
    import image8 from "~/assets/content/investments/invest_5_square.jpg"
    import image10 from "~/assets/content/fund_pages/eco/eco_10.jpg"


    
    

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
    
    const nda_fund = {investment: "eco"}
    
    const landing_image = {
        title: "Eco Energy Partners",
        title_color: "green",
        text_align: "center",
        line_width: "575px",
        line_margin: "157.5px",
        image: image1,
        image_width: "125%",
        font_calc: "1"
    }
    
    const big_text_1 = {text:'Green Energy', font_size:'15vw', margin_top:'5%', padding_top:'0'}

    
    const intro_info ={
        video: '',
        image: image2,
        is_image: true,
        is_video: false,
        main_text:"The Eco Energy Partners fund supports companies that specialize in Enhanced Oil Recovery (EOR). Specifically, we invest in companies that bring the latest technology to revitalize existing Oil & Gas wells and fields. By using environmentally  friendly best practices, these companies can quickly and efficiently start extracting valuable oil and gas from wells that were previously ‘tapped’.<br><br>The principal underlying company in the portfolio has been working in the space for over three decades and is now opening up to outside investment as they scale. They have over 3,000 acres in their portfolio, all of the necessary equipment, and a dedicated field team. A recent revitalization project yielded over 400% more oil than expected, and there are many more similar fields and wells ready to go.<br><br>Eco Energy Partners investors take advantage of substantial tax advantages the first year, then the fund aims to deliver annual growth of 20% for the life of the investment.</p>"
    }
    
    
    const slab1 = {
        margin_top:"0%",
        margin_bottom: "0%",
        image:image3
    }
    
    const big_text_2 = {text:'Green Oil & Gas Revitalization', font_size:'12vw', margin_top:'5%', padding_top:'0'}


    const strategy = {
        video: '',
        image: image4,
        is_image: true,
        is_video: false,
        image_margin_calc: "1.2",

        image_margin_mobile_calc: "1",
        text_margin_mobile: "-80%",
        container_margin_bottom:"-60%",


        title:"",
        text:"Currently, we cannot produce an electric car, solar panel, or wind turbine without petrochemicals/petrochemical derived fuels. This won’t change in the foreseeable future.<br><br>Being Green, really Green, requires acknowledging the above truth. With that, we invest in the smartest ways to minimize the impact of extracting the resources needed in service of creating the world and economy we want our children to grow up in.<br><br>Enhanced Oil Recovery (EOR) has been in practice for more than 40 years. It has not been widely pursued due to the economics of pulling “easy” oil out of new wells - despite the environmental harm. Now that much of the “easy” oil has been tapped and environmental regulation is tightening, new sites are more scarce and much more costly."
    }
    
    


    const big_text_3 = {text:'A Cleaner Process for a Cleaner Future', font_size:'12.75vw', margin_top:'2%', padding_top:'2%'}
    
        
    const revenue = {
        image: image7,
        image_margin: "0%",
        text_margin: "-15%",
        title:"",
        text:"Today’s EOR benefits from decades of ongoing technological improvements. N2/C02 injection and nanoparticle solution application - which have compounded to make revitalization of wells - is the smartest hydrocarbon extraction method both financially and environmentally.",
        text_2:"<b>Enhanced Oil Recovery is Green Because It:</b> <br><br>⚫ Avoids habitat loss due to well pad creation, lease roads & flowlines, pipelines & power lines<br><br>⚫ Avoids the use of a million or more gallons of fresh water per well<br><br>⚫ Avoids venting or flaring of methane gas (among the worst of the Greenhouse Gasses) while waiting on construction of the production infrastructure<br><br>⚫ Avoids carbon emissions associated with high pressure fracking<br><br>⚫ Avoids contamination of groundwater due to poor cement jobs and chemical processes.<br><br>⚫ Preserves potential farm and grazing land for commercial food operations"
    }

    const slab2 = {
        margin_top:"10%",
        margin_bottom: "10%",
        image:image6
    }


    const investment_highlights = {
        title_1: "Company Name:",
        info_1: "Eco Energy Partners",
        title_2: "Entity Type:",
        info_2: "SPV with tax pass-throughs",
        title_3: "Min Investment:",
        info_3: "TBA",
        title_4: "Expected Annual Growth*",
        info_4: "20%",
        title_5: "First year Tax Incentive:",
        info_5: "80-100% writeoff or 20-30% back on principal",
        title_6: "*after first year",
        info_6: "",
        image: image5,
        image_margin: "40%"
    }
    
    const text_section = {
        lower_text: "The principal underlying company is run by a management team which has been working and innovating in the EOR space for three decades and counting. They have worked for some of the biggest names in the Oil & Gas space and bring their expertise to this project.<br><br>Along with management experience, the company has a dedicated and experienced field team who have proven their knowledge and capabilities in the field for decades each. Perhaps most critically, the company recently made a major investment in dedicated equipment for the cleaning and preparing of sites, which means increased returns, and efficiency in revitalizing wells.",
        image: '',
        has_image:false
    }
    

    
    const footer = {
        title:"Impossible <br> Foods",
        image:image8,
        nuxt_link:"/fund_pages/impossible",
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