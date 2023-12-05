<template>
    <Header/>
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
    
                <h4 class="success_text">Thank You</h4>
                <h5 class="success_message_blue">Your bank transfer is being reviewed and will be fully initiated within 1-2 days. You will recieve an email when the process is complete.
            </h5>
    
                <br>
    
                <h5 class="success_message">Please check your email now and make sure to select the link to initiate your account and track your investments.
            </h5>
    
    
            <h5 v-if="number_of_transfers > 1" class="success_message_note">
                <i><span class="emph_3">Note:</span> Dwolla limits the amount per transfer, as such, in order to fulfill your investment, <span class="emph_3">{{ number_of_transfers }}</span> transfers will initated.
                <br>
                This is standard for deals of this nature.</i>
            </h5>
    
    
    
            <h5 class="success_message" style="text-align: center; width:60%; margin-left:20%"><span class="emph_2">This link expires in 30 minutes and is necessary for you to continue</span>
                <span style="font-size:15px"><br>Just in case: check your <b>spam</b>, we end up there sometimes</span>  </h5>
               
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
    
    const cicle_margin = ref('-20px')
    const circle_scale = ref(3)
    const check_scale = ref(3)
    
    const is_mobile = ref(false)
    
    const { width, height } = useWindowSize()
    
    if(width.value < 576){
        is_mobile.value = true
    }
    
    
    
    
    onMounted(() => {
    
    
    sleep(50).then(() => { 
    circle_scale.value = 1
    check_scale.value = 1
    cicle_margin.value = '45px'
    })
    
    
    // ------------------------------- Plaid Extra ---------------
    // ------------------------------- Plaid Extra ---------------
    // ------------------------------- Plaid Extra ---------------
    
    
    fetch(`${config.flask_url}/api/invest_flow/accred_and_investments/`, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({'investor_ID': investor_ID.value, 'fund_ID': fund_ID.value})
        })
        .then((response) => response.json())
        .then((data) => {
            console.log('sucess, got extra plaid products');
            // investor_ID.value = null
        })
        .catch(error => {
            console.error('There was an error with extra accounts!', error);
        });
    
    
    // ------------------------------- Plaid Extra ---------------
    // ------------------------------- Plaid Extra ---------------
    // ------------------------------- Plaid Extra ---------------
    
    })
    
    
    
    
    
    
    
    const cookie_options = {default:()=> '', watch:true, maxAge:1800}
    const cookie_options_remove = {default:()=> '', watch:true, maxAge:-1}
    
    const investment_amount = useCookie('investment_amount', cookie_options)
    const number_of_transfers = useCookie('number_of_transfers', cookie_options)
    const selected_fund = useCookie('selected_fund', cookie_options)
    
    
    const timer_status =  useCookie('timer_status', cookie_options)
    timer_status.value = 'timed_out'
    

    const investor_ID = useCookie('investor_ID')
    const fund_ID = useCookie('fund_ID')
    const institution_ID = useCookie('institution_ID')
    institution_ID.value = null;
    
    
    
    sleep(2000).then(() => { investor_ID.value = null; fund_ID.value = null;})
    sleep(1800000).then(() => { investment_amount.value = null; timer_status.value = null; number_of_transfers.value = null; selected_fund.value = null; navigateTo('~/index') })
    
    
    onBeforeRouteLeave(() => {
        investment_amount.value = null; 
        timer_status.value = null
        number_of_transfers.value = null; 
        selected_fund.value = null;
    })
    
    
    
    const dwolla_customer_created = useCookie('dwolla_customer_created', cookie_options_remove)
    const signature_typed = useCookie('signature_typed', cookie_options_remove)
    const countdown_timer = useCookie('countdown_timer', cookie_options_remove)
    const minimum_investment_amount = useCookie('minimum_investment_amount', cookie_options_remove)
    
    const account_list = useCookie('account_list', cookie_options_remove)
    const account_selected_value_step_2 = useCookie('account_selected_value_step_2', cookie_options_remove)
    const first_name = useCookie('first_name', cookie_options_remove)
    const last_name = useCookie('last_name', cookie_options_remove)
    
    const email = useCookie('email', cookie_options_remove)
    const phone = useCookie('phone', cookie_options_remove)
    const is_accredited =  useCookie('is_accredited', cookie_options_remove)
    const exempt_from_withholding =  useCookie('exempt_from_withholding', cookie_options_remove)
    
    const investing_as = useCookie('investing_as', cookie_options_remove)
    const industry_classification =  useCookie('industry_classification', cookie_options_remove)
    const business_classification =  useCookie('business_classification', cookie_options_remove)
    const business_name =  useCookie('business_name', cookie_options_remove)
    const business_ein =  useCookie('business_ein', cookie_options_remove)
    const entity_purpose_to_invest =  useCookie('entity_purpose_to_invest', cookie_options_remove)
    
    const controller_first_name = useCookie('controller_first_name', cookie_options_remove)
    const controller_last_name = useCookie('controller_last_name', cookie_options_remove)
    const controller_title =  useCookie('controller_title', cookie_options_remove)
    const controller_dob =  useCookie('controller_dob', cookie_options_remove)
    const controller_ssn =  useCookie('controller_ssn', cookie_options_remove)
    const controller_address = useCookie('controller_address', cookie_options_remove)
    const controller_state =  useCookie('controller_state', cookie_options_remove)
    const controller_city =  useCookie('controller_city', cookie_options_remove)
    const controller_zip =  useCookie('controller_zip', cookie_options_remove)
    const controller_country =  useCookie('controller_country', cookie_options_remove)
    const controller_email =  useCookie('controller_email', cookie_options_remove)
    
    const owner_first_name =  useCookie('owner_first_name', cookie_options_remove)
    const owner_last_name =  useCookie('owner_last_name', cookie_options_remove)
    const owner_title =  useCookie('owner_title', cookie_options_remove)
    const owner_dob =  useCookie('owner_dob', cookie_options_remove)
    const owner_ssn =  useCookie('owner_ssn', cookie_options_remove)
    const owner_address =  useCookie('owner_address', cookie_options_remove)
    const owner_state =  useCookie('owner_state', cookie_options_remove)
    const owner_city =  useCookie('owner_city', cookie_options_remove)
    const owner_zip =  useCookie('owner_zip', cookie_options_remove)
    const owner_country =  useCookie('owner_country', cookie_options_remove)
    const owner_email =  useCookie('owner_email', cookie_options_remove)
    
    
    
    const sole_prop_first_name = useCookie('sole_prop_first_name', cookie_options_remove)
    const sole_prop_last_name = useCookie('sole_prop_last_name', cookie_options_remove)
    const sole_prop_business_name = useCookie('sole_prop_business_name', cookie_options_remove)
    const sole_prop_business_ein = useCookie('sole_prop_business_ein', cookie_options_remove)
    const sole_prop_dob = useCookie('sole_prop_dob', cookie_options_remove)
    const sole_prop_ssn = useCookie('sole_prop_ssn', cookie_options_remove)
    const sole_prop_business_classification = useCookie('sole_prop_business_classification', cookie_options_remove)
    const sole_prop_industry_classification = useCookie('sole_prop_industry_classification', cookie_options_remove)
    const sole_prop_address = useCookie('sole_prop_address', cookie_options_remove)
    const sole_prop_state = useCookie('sole_prop_state', cookie_options_remove)
    const sole_prop_city = useCookie('sole_prop_city', cookie_options_remove)
    const sole_prop_zip = useCookie('sole_prop_zip', cookie_options_remove)
    
    
    const individual_first_name = useCookie('individual_first_name', cookie_options_remove)
    const individual_last_name = useCookie('individual_last_name', cookie_options_remove)
    const individual_dob = useCookie('individual_dob', cookie_options_remove)
    const individual_ssn = useCookie('individual_ssn', cookie_options_remove)
    const individual_address = useCookie('individual_address', cookie_options_remove)
    const individual_state = useCookie('individual_state', cookie_options_remove)
    const individual_city = useCookie('individual_city', cookie_options_remove)
    const individual_zip = useCookie('individual_zip', cookie_options_remove)
    const empolyment_status = useCookie('empolyment_status', cookie_options_remove)
    
    const dwolla_customer_status = useCookie('dwolla_customer_status', cookie_options_remove)
    const dwolla_beneficial_owner_status = useCookie('dwolla_beneficial_owner_status', cookie_options_remove)
    const documents_uploaded_successful = useCookie('documents_uploaded_successful',cookie_options_remove)
    
    countdown_timer.value = null
    minimum_investment_amount.value = null
    dwolla_customer_created.value = null;
    dwolla_customer_status.value = null;
    dwolla_beneficial_owner_status.value = null;
    documents_uploaded_successful.value = null;
    investing_as.value = null;
    account_list.value = null;
    account_selected_value_step_2.value = null;
    first_name.value = null;
    last_name.value = null;
    email.value = null; 
     phone.value = null; 
     is_accredited.value = null; 
     exempt_from_withholding.value = null; 
    
     industry_classification.value = null; 
     business_classification.value = null; 
     business_ein.value = null; 
     entity_purpose_to_invest.value = null; 
    
     controller_first_name.value = null; 
     controller_last_name.value = null; 
     controller_title.value = null; 
     controller_dob.value = null; 
     controller_ssn.value = null; 
     controller_address.value = null; 
     controller_state.value = null; 
     controller_city.value = null; 
     controller_zip.value = null; 
     controller_country.value = null; 
     controller_email.value = null; 
    
     owner_first_name.value = null; 
     owner_last_name.value = null; 
     owner_title.value = null; 
     owner_dob.value = null; 
     owner_ssn.value = null; 
     owner_address.value = null; 
     owner_state.value = null; 
     owner_city.value = null; 
     owner_zip.value = null; 
     owner_country.value = null; 
     owner_email.value = null; 
    
    
    
     sole_prop_first_name.value = null; 
     sole_prop_last_name.value = null; 
     sole_prop_business_name.value = null; 
     sole_prop_business_ein.value = null; 
     sole_prop_dob.value = null; 
     sole_prop_ssn.value = null; 
     sole_prop_business_classification.value = null; 
     sole_prop_industry_classification.value = null; 
     sole_prop_address.value = null; 
     sole_prop_state.value = null; 
     sole_prop_city.value = null; 
     sole_prop_zip.value = null; 
    
     individual_first_name.value = null; 
     individual_last_name.value = null; 
     individual_dob.value = null; 
     individual_ssn.value = null; 
     individual_address.value = null; 
     individual_state.value = null; 
     individual_city.value = null; 
     individual_zip.value = null; 
     empolyment_status.value = null; 
    
     signature_typed.value = null
    
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
        z-index: -1;
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
        top: 105px;
        margin-left:-2%;
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
        padding-bottom:10vh;
    }
    .success_outer_card_padding{
        padding-top:1px;
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

    .success_message_blue{
        font-size:225%;
        margin-top:-1.5%;
        width:80%;
        margin-left:10%;
        color:rgb(25, 120, 237)
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