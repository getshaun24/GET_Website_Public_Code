<template>

    <div class="remove_mix_mode">
        <div class="backgorund_image"></div>
        <div class="backgorund_blur"></div>
    
        <div class="circle_box">
        <div class="check_outer_circle"></div>
        <div class="check_inner_circle"></div>
        <img class="check_mark" src="~/assets/content/investments/check_mark.png">
    </div>
    
        <div class="success_card">
            
    
            <div class="success_inner_container">

    
                <div v-if="is_mobile" class="amount_card">
                    <h5 class="amount_text">Investment Amount: <br><br> {{ '$' + investment_amount.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",") }}</h5>
                </div>
                <div v-else class="amount_card">
                    <h5 class="amount_text">Investment Amount: {{ '$' + investment_amount.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",") }}</h5>
                </div>
    
                <h4 class="success_text">Congratulations</h4>
    
                <br>
    
                <h5 class="success_message">You are now invested in another GET fund</h5>

                <h5 v-if="number_of_transfers > 1" class="success_message_note">
            <i><span class="emph_3">Note:</span> Dwolla limits the amount per transfer, as such, in order to fulfill your investment, <span class="emph_3">{{ number_of_transfers }}</span> transfers were initated.
            <br>
            This is standard for deals of this nature.</i>
        </h5>

     
    

    
               
                <div class="success_card_padding"></div>
    
        </div>
    
    
    
    </div>
    
    <div class="success_outer_card_padding"></div>
    </div>
    
    </template>
    
    
    
    
    <script setup>
    
    import { useWindowSize } from '@vueuse/core'
    
    
    // sleep time expects milliseconds
    function sleep (time) {
        return new Promise((resolve) => setTimeout(resolve, time));
    }
    
    
    const config = useRuntimeConfig()
    
    const cicle_margin = ref('40px')
    const circle_scale = ref(3)
    const check_scale = ref(3)
    
    const is_mobile = ref(false)
    
    const { width, height } = useWindowSize()
    
    if(width.value < 576){
        is_mobile.value = true
    }
    
    
    
    
    onMounted(() => {
    
    
    sleep(850).then(() => { 
    circle_scale.value = 1
    check_scale.value = 1
    cicle_margin.value = '160px'
    })
    
    })
    
    
    
    
    
    
    

    const investment_amount = useCookie('investment_amount')
    const number_of_transfers = useCookie('number_of_transfers')
    const selected_fund = useCookie('selected_fund')
    


    const fund_ID = useCookie('fund_ID')
    const institution_ID = useCookie('institution_ID')
    institution_ID.value = null;
    fund_ID.value = null;

    sleep(1800000).then(() => { investment_amount.value = null;  number_of_transfers.value = null; selected_fund.value = null;})
    
    
    onBeforeRouteLeave(() => {
        investment_amount.value = null; 
        number_of_transfers.value = null; 
        selected_fund.value = null;
    })
    
    
    
    </script>
    
    
    <style scoped>
    
    
    
    
    .remove_mix_mode :deep(.header_container){
    mix-blend-mode: normal !important;
    }
    
    
    
    .backgorund_image{
    background-image: url('~/assets/content/investments/success_background_3.jpg');
    opacity:.4;
    object-fit: cover;
    width:100vw;
    height:100vh;
    position:fixed;
    top:0;
    left:0;
    z-index:-1;
    filter: saturate(1.25);
    transform: rotate(180deg);
    }
    
    .backgorund_blur{
        backdrop-filter: blur(30px);
    opacity:.8;
    object-fit: cover;
    width:100vw;
    height:100vh;
    position:fixed;
    top:0;
    left:0;
    z-index:-1;
    }
    
    .circle_box{
        display: flex;
        justify-content: center;
    }
    .check_outer_circle{
        backdrop-filter: blur(180px);
        background: radial-gradient(green, #1dff4615);
        opacity:.2;
        width: 225px;
        height: 225px;
        border-radius: 50%;
        top:v-bind(cicle_margin);
        position: absolute;
        z-index: 1;
        border-color:#fff 2px solid;
        transition: top .25s ease-in-out .7s;
    }
    
    .check_inner_circle{
        backdrop-filter: blur(200px);
        opacity:.9;
        width: 150px;
        height: 150px;
        top:80px;
        border-radius: 50%;
        top: 200px;
        position: absolute;
        z-index: 5;
        border-color:#fff 2px solid;
        background: radial-gradient(green, green, rgba(0, 128, 0, 0.43), #1dff4608);
        transform: scale(v-bind(circle_scale));
        transition:transform 1s ease-in-out;
    }
    
    .check_mark{
        width: 115px;
        height: 115px;
        position: absolute;
        z-index: 10;
        top: 225px;
        margin-left:-.75%;
        transform:scale(v-bind(check_scale));
        transition:transform 1.25s ease-in-out;
    }
    
    .success_card{
        background-color: #000;
        width:92.5%;
        min-height:100vh;
        margin-left:3.25%;
        margin-top:150px;
        border-radius: 50px;
    }
    
    .success_card_padding{
        /* padding-bottom:10vh; */
    }
    .success_outer_card_padding{
        padding-top:15%;
    }
    .success_inner_container{
        width:90%;
        margin-left:5%;
        padding-top:15%;
        margin-bottom:10%;
    }
    
    
    .success_text{
        color:#fff;
        z-index:1;
        text-decoration: underline;
        text-decoration-color:rgb(25, 120, 237);
        /* text-decoration-color:green; */
        text-underline-offset: 10px;
        text-decoration-thickness: 1px;
    }
    
    .emph{
        text-decoration: underline;
        text-decoration-color:rgb(25, 120, 237);
        text-underline-offset: 3px;
        text-decoration-thickness: 4px;
    }
    
    .emph_2{
        text-decoration: underline;
        text-decoration-color:rgb(255, 0, 0);
        text-underline-offset: 3px;
        text-decoration-thickness: 1px;
        text-align:center
    }
    
    .emph_3{
        text-decoration: underline;
        text-decoration-color:rgb(25, 120, 237);
        text-underline-offset: 4px;
        text-decoration-thickness: 2px;
    }
    
    
    .amount_card{
        background-color: #121212;
        height:200px;
        border-radius:25px;
    }
    
    .amount_text{
        padding-top:0px;
        position:absolute;
        margin-left:20px
    }
    
    
    .success_message{
        font-size:225%;
        margin-top:-1.5%;
        width:80%;
        margin-left:10%
    }
    
    .success_message_note{
        font-size:180%;
        margin-top:0%;
        width:80%;
        margin-left:10%;
        margin-bottom:8%;
        line-height:1.1
    }
    
    
    @media only screen and (min-width: 0px) and (max-width: 430px) {
        .amount_card{
        height:120px;
        margin-top:70px;
    }
    .amount_text{
        margin-top:20px;
        font-size:170%
    }
    
    .success_text{
        font-size:250%;
        margin-top:15%;
        text-underline-offset: 10px;
        text-decoration-thickness: 2px;
    }
    
    .success_message{
        font-size:150%;
        margin-top:-1.5%
    }
    
    .success_message_note{
        font-size:120%;
        margin-top:0%;   
    }
    
    .success_card_padding{
        padding-bottom:10vh;
    }
    
    .success_card{
        min-height:100%;
    }
    
    }
    
    
    @media only screen and (min-width: 430px) and (max-width: 576px) {
        .amount_card{
        height:120px;
        margin-top:70px;
    }
    .amount_text{
        margin-top:20px;
        font-size:170%
    }
    .success_text{
        font-size:250%;
        margin-top:15%;
        text-underline-offset: 10px;
        text-decoration-thickness: 2px;
    }
    .success_message{
        font-size:150%;
        margin-top:-1%
    }
    
    .success_message_note{
        font-size:95%;
        margin-top:0%;   
    }
    
    .success_card_padding{
        padding-bottom:10vh;
    }
    
    .success_card{
        min-height:100%;
    }
    }
    
    @media only screen and (min-width: 576px) and (max-width: 768px) {
    
        .amount_card{
        height:120px;
        margin-top:70px;
    }
    .amount_text{
        margin-top:40px
    }
    
    }
    
    @media only screen and (min-width: 768px) and (max-width: 992px) {
        .amount_card{
        height:120px;
        margin-top:30px;
    }
    .amount_text{
        margin-top:45px
    }
    }
    
    @media only screen and (min-width: 992px) and (max-width: 1200px) {
    }
    
    @media only screen and (min-width: 1200px) and (max-width: 1400px) {
        .amount_text{
        margin-top:70px
    }
    }
    
    @media only screen and (min-width: 1400px) and (max-width: 1600px) {
        .amount_text{
        margin-top:70px
    }
    }
    
    @media only screen and (min-width: 1600px) and (max-width: 5600px) {
        .amount_text{
        margin-top:70px
    }
    }
    
    
    
    </style>