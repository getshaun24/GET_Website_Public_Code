<template>

    <div>

        <CircleTransition ref="cicle_tansition"/>


        <InvestFlowReverificationReverifyCustomer v-if="dwolla_reverify_customer"/>
        <InvestFlowReverificationReverifyOwner v-if="dwolla_reverify_owner"/>
        <InvestFlowReverificationKba v-if="dwolla_kba_needed"/>
        <InvestFlowReverificationUploadDocuments v-if="dwolla_documents_needed" />



        <div class="loader_container" v-if="start_loader">
            <InvestFlowLoadersApiLoader/>
        </div>


        <div class="modal_container" :class="{modal_hide_anim: modal_exit_anim, modal_hide_disp: modal_exit_display}">
        <div class="modal_popup" :class="{modal_bix_hide_anim: modal_exit_anim}" ref="modal">



            <div v-if="account_sel" class="account_select">
                <div @click="account_select_toggle()" class="back_arrow">￩</div>
            <InvestFlowAccountSelectButtons  v-model:account_selected_value="account_selected_value"/> 
            <button @click="modal_leave()" class="select_button">Select Account</button>
            </div>

            <!-- ---------------- action select ------------------- -->
            <!-- ---------------- action select ------------------- -->
            <div v-else >
            <h5 class="modal_info_step_5">Insufficient Funds In Selected Account. </h5>
            <button @click="account_select_toggle()" class="modual_buttons">Select Alternative Account</button>
            <button @click="start_plaid()" class="modual_buttons">Select Account From A New Bank</button>
            <button @click="modal_leave()" class="modual_buttons">Enter A New Investment Amount</button>

            <!-- ---------------- action select ------------------- -->
            <!-- ---------------- action select ------------------- -->

        </div>



        </div>
    </div>


    <div class="plaid_blur" v-if="plaid_blur"></div>
    <div class="loader_container" v-if="start_loader">
        <InvestFlowLoadersProgressLoader :start_loader="start_loader" :number_of_transfers="number_of_transfers"/>
    </div>

    


    <Header/>
    
    <div class="white_background">
    <GSAPScrollSmoother>


        <InvestFlowStepCircles v-bind="step_circles" />


        <div :class="[ investment_amount >= 0 ? '' : 'is_hidden']">
        <div class="investment_grid">
        <div class="invest_confirm_container">
            <p class="intended_amount">Intended Investment Amount</p>
            <div class="investment_line"></div>
            <p class="intended_amount">{{ '$' + investment_amount.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",") }}</p>
            <br>
            <p class="intended_amount">Number of Shares</p>
            <div class="investment_line"></div>
            <p class="intended_amount">{{  investment_amount.toString().replace(/\D/g, "") / 1000  }}</p>
        </div>
        <div class="invest_confirm_container">
            <div class="ppm_select_container">
<div class="input_wrap">
                <input v-model="investment_amount_updated" @keyup="format_val" class="input_white" placeholder=' ' />
                <label class="label_white mobile_label">Edit Investment Amount</label>
        </div>

        <button class="update_button" @click="updated_amount" >Update</button>
    </div>
            </div>
    </div>
        <button @click="step_5_api_send()"  class="transact_button">Transact & Invest</button>
</div>



        <div :class="[ investment_amount < 0 ? '' : 'is_hidden']">

            <div class="investment_grid">

<div class="invest_confirm_container">

    <h3 class="intended_amount">Our Minimum Investment Amount Is:</h3>
    <div class="investment_line_2"></div>
    <h3 class="intended_amount">$2,000</h3>


</div>

<div class="invest_confirm_container">


    <div class="ppm_select_container">
<p class="confirm_text">Please Update Your Investment</p>

<div class="input_wrap">
    <input v-model="investment_amount_updated" @keyup="format_val" class="input_white" placeholder=' ' />
        <label class="label_white mobile_label">New Investment Amount</label>
</div>


<button class="update_button_minimum" @click="updated_amount">Update</button>
</div>
    </div>
</div>
        </div>











    <div style="padding-bottom:50vh"></div>


    </GSAPScrollSmoother>
</div> 
   </div>  
    </template>
    
    
<script setup>

useHead({
  script: [{ src: "https://cdn.plaid.com/link/v2/stable/link-initialize.js", body:true, async: true, preload:true, ssr: false}],
});


const config = useRuntimeConfig()



const step_circles = {
    current_num: 5
}

const flow_bar_start = ref(true)


function transition_and_route(route_to) {
cicle_tansition.value.animation_and_route(route_to);
}


const dwolla_customer_status = useCookie('dwolla_customer_status')
const dwolla_beneficial_owner_status = useCookie('dwolla_beneficial_owner_status')
const dwolla_reverify_customer = ref(false)
const dwolla_reverify_owner = ref(false)
const dwolla_kba_needed = ref(false)
const dwolla_documents_needed = ref(false)
const dwolla_need_verification = ref(false)


onMounted(() => {
flow_bar_start.value = false
check_customer_status()
})



const cicle_tansition = ref('');


const cookie_options = {default:()=> '', watch:true, maxAge:1800}
const fund_ID = useCookie('fund_ID', cookie_options)
const investor_ID = useCookie('investor_ID', cookie_options)
const institution_ID = useCookie('institution_ID', cookie_options)
const email = useCookie('email', cookie_options)
const phone = useCookie('phone', cookie_options)
const account_list = useCookie('account_list', cookie_options)
const investment_amount = useCookie('investment_amount', cookie_options)
const number_of_transfers = useCookie('number_of_transfers', cookie_options)
const documents_uploaded_successful = useCookie('documents_uploaded_successful', {default:()=> false, watch:true, maxAge:1800})
const investment_amount_updated = ref()
const minimum_investment_amount = useCookie('minimum_investment_amount')

const start_loader = ref(false);
const plaid_blur = ref(false);
const blur_amount = ref('0px');
const plaid_opacity = ref(0);
const account_sel = ref(false)
const account_selected_value = ref(null)
const account_selected_value_step_2 = useCookie('account_selected_value_step_2', cookie_options)

const update_button_color = ref('grey')

const link_token = ref('')

function format_val() {
    investment_amount_updated.value  = '$' + investment_amount_updated.value.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",")
}



const underline_width = ref('85%')
const underline_width_2 = ref('70%')

function updated_amount() {


    underline_width.value = '0%'
    underline_width_2.value = '0%'



    if (parseInt(investment_amount_updated.value.toString().replace(/\D/g, "")) % 1000 !== 0){
        update_button_color.value = 'grey'
        alert("Please an amount that is a multiple of 1000")
    } else if (parseInt(investment_amount_updated.value.toString().replace(/\D/g, "")) < minimum_investment_amount.value){
        update_button_color.value = 'grey'
        alert("Our Minimum Investment Amount Is $" + minimum_investment_amount.value.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ","))
    } else {
        investment_amount.value = investment_amount_updated.value.toString().replace(/\D/g, "")
        update_button_color.value = 'rgb(25, 120, 237)'
    }

    // ------------  for testing  --------------------------
    // ------------  for testing  --------------------------
//     investment_amount.value = investment_amount_updated.value.toString().replace(/\D/g, "")
//     update_button_color.value = 'rgb(25, 120, 237)'

//     sleep(1000).then(() => {
//     underline_width.value = '85%'
//     underline_width_2.value = '85%'
// })
    
    // ------------  for testing  --------------------------
    // ------------  for testing  --------------------------
}

function step_5_api_send() {

    check_customer_status()
    if (dwolla_need_verification.value == true) {
        window.location.reload()
        return 
    }

    if(confirm("Intitate Transfer of " + '$' + investment_amount.value.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ","))){

        start_loader.value = true;
        plaid_blur.value = true;

        if (Math.ceil(investment_amount.value.toString().replace(/\D/g, "")) < config.dwolla_transaction_limit){
        number_of_transfers.value = 1
        } else {
            number_of_transfers.value = Math.ceil(investment_amount.value.toString().replace(/\D/g, "") / config.dwolla_transaction_limit)
        }

if (documents_uploaded_successful.value == true){
    transition_and_route('step_6_docs')
} else {
fetch(`${config.flask_url}/api/invest_flow/step_5/`, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({investor_ID:investor_ID.value, fund_ID: fund_ID.value, institution_ID:institution_ID.value, investment_amount:investment_amount.value, account_selected_value:account_selected_value.value, account_selected_value_step_2:account_selected_value_step_2.value, email:email.value, phone:phone.value})
})
.then((response) => response.json())
.then((data) => {

    if(data.status == 'Insufficient_Funds'){
        link_token.value = String(data.link_token)
        plaid_blur.value = false;
        open_modal()
    } else if (data.status == "transaction_already_initiated"){
        link_token.value = String(data.link_token)
        plaid_blur.value = false;
        alert("You Have Already Initiated A Transfer, It Will Be Completed Shortly. Your Confirmation Email Will Be Sent As Soon As The Transfer Is Completed. Thank You For Your Patience.")
        transition_and_route('step_6')
    }
    else{
    console.log('Success:', data.message);
    transition_and_route('step_6')
}
})
.catch(error => {
    alert('Error')
    start_loader.value = false;
    plaid_blur.value = false;
    console.error('There was an error!', error);
});
}
}
}


function account_select_toggle(){
    account_sel.value = !account_sel.value
}



function check_customer_status() {
if (dwolla_customer_status.value == 'retry'){
    dwolla_reverify_customer.value = true
    dwolla_need_verification.value = true
} else if (dwolla_customer_status.value != 'retry' && dwolla_beneficial_owner_status.value == 'incomplete'){
    dwolla_reverify_owner.value = true
    dwolla_need_verification.value = true
}
 else if (dwolla_customer_status.value == 'kba'){
    dwolla_kba_needed.value = true
    dwolla_need_verification.value = true
} else if (dwolla_customer_status.value == 'document' || dwolla_beneficial_owner_status.value == 'document'){
    if (documents_uploaded_successful.value != true){
    dwolla_documents_needed.value = true
    dwolla_need_verification.value = true
}
} else {
    dwolla_reverify_customer.value = false
    dwolla_reverify_owner.value = false
    dwolla_documents_needed.value = false
    dwolla_kba_needed.value = false
    dwolla_need_verification.value = false
}
}

// ------------------------------- Plaid Start ---------------
// ------------------------------- Plaid Start ---------------
// ------------------------------- Plaid Start ---------------



  function start_plaid(){

plaid_blur.value = true;
sleep(10).then(() => { blur_amount.value = '10px', plaid_opacity.value = 1 });

const handler = Plaid.create({
token: link_token.value,
onSuccess: (public_token, metadata) => {


    if (metadata['institution']['institution_id'] != institution_ID.value){
        send_plaid_public(public_token, metadata)
    } else {
        alert('You entered the same institution, Please try again with a different institution')
        plaid_blur.value = false;
    }
},
onLoad: () => {},
onExit: (err, metadata) => {
blur_amount.value = '0px',
plaid_opacity.value = 0
plaid_blur.value = false;
},
onEvent: (eventName, metadata) => {},
//required for OAuth; if not using OAuth, set to null or omit:
//   receivedRedirectUri: window.location.href,
});

handler.open();
}





function get_link_token(){

// ------- get link token from flask server ---------------

fetch(`${config.flask_url}/api/invest_flow/step_2_linktoken/`, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({'investor_ID': investor_ID.value, 'email': email.value, 'phone': phone.value})
})
.then((response) => response.json())
.then((data) => {
    console.log('Success:', data.link_token);
    open_plaid(data.link_token)
})
.catch(error => {
    alert('Error')
    console.error('There was an error!', error);
});
}





function open_plaid(link_token){ 


plaid_blur.value = true;
sleep(10).then(() => { blur_amount.value = '10px', plaid_opacity.value = 1 });

const handler = Plaid.create({
token: link_token,
onSuccess: (public_token, metadata) => {


if (metadata['institution']['institution_id'] != institution_ID.value){
    send_plaid_public(public_token, metadata)
} else {
    alert('You entered the same institution, Please try again with a different institution')
    plaid_blur.value = false;
}

},
onLoad: () => {},
onExit: (err, metadata) => {
blur_amount.value = '0px',
plaid_opacity.value = 0
plaid_blur.value = false;
},
onEvent: (eventName, metadata) => {},
//required for OAuth; if not using OAuth, set to null or omit:
//   receivedRedirectUri: window.location.href,
});

handler.open();
}





// ------------------------------- Plaid Public Token ---------------
// ------------------------------- Plaid Public Token ---------------
// ------------------------------- Plaid Public Token ---------------


function send_plaid_public(public_token, metadata){

start_loader.value = true;



fetch(`${config.flask_url}/api/invest_flow/step_5_publictoken/`, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({'public_token': public_token, 'metadata': metadata, 'investor_ID': investor_ID.value})
})
.then((response) => response.json())
.then((data) => {
    console.log('Success:', data.message);
    
    // plaid_extra(data.data, data.institution_ID);
    institution_ID.value = data.institution_ID
    account_list.value = data.data
    start_loader.value = false;
    plaid_blur.value = false;
    account_sel.value = true
    


})
.catch(error => {
    start_loader.value = false;
    plaid_blur.value = false;
    alert('Public Token Error')
    console.error('There was an error!', error);
});
}







// ------------------------------- Plaid Extra ---------------
// ------------------------------- Plaid Extra ---------------
// ------------------------------- Plaid Extra ---------------

function plaid_extra(account_list, institution_ID){


fetch(`${config.flask_url}/api/invest_flow/extra_plaid_products/`, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({'investor_ID': investor_ID.value, 'institution_ID':institution_ID, 'account_list': account_list})
})
.then((response) => response.json())
.then((data) => {
    console.log('sucess, got extra plaid products');
})
.catch(error => {
    // alert('Error')
    console.error('There was an error!', error);
});

}



// ------------------------------- Modal  ---------------
// ------------------------------- Modal  ---------------
// ------------------------------- Modal  ---------------


const modal_exit_anim = ref(true)
const modal_exit_display = ref(true)

    
    
    // sleep time expects milliseconds
    function sleep (time) {
      return new Promise((resolve) => setTimeout(resolve, time));
    }
    
function open_modal(){
    modal_exit_display.value = false
        sleep(100).then(() => {
        modal_exit_anim.value = false
        });
}

function modal_leave(){
        account_sel.value = false
        modal_exit_anim.value = true
        sleep(1100).then(() => {
        modal_exit_display.value = true
        start_loader.value = false;
        plaid_blur.value = false;
        });
    }
    

</script>

<style scoped>

.is_hidden{
 display: none;
}



.white_background{
    background-color:#fff;
    height:200vh;
    width:100vw;
    z-index:0;
    position:fixed;
    top:0;
    left:0
}



.investment_grid{
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr;
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    margin-left:5%;
    margin-top:150px;
    width:90%
}

.invest_confirm_container{
    margin-left:5%;
    margin-top:5%;
}

.intended_amount{
    font-weight:600;
    color:#000;
    font-size:120%
}

.investment_line{
    width:v-bind(underline_width_2);
    height:3px;
    background-color:rgb(25, 120, 237);
    margin-top:-1%;
    margin-bottom:-1%;
    transition: all 1s ease;
}

.investment_line_2{
    height:3px;
    background-color:rgb(25, 120, 237);
    width:v-bind(underline_width);
    margin-top:0px;
    margin-bottom:10px;
    transition: all 1s ease;
}



.ppm_select_container{
    width:80%;
    margin-left:10%;
}
.confirm_text{
    color:#000;
    line-height: 1.5;
    margin-bottom:30px;
    font-size:90%
}


.update_button{
    padding:10px 20px;
    font-size:12px;
    background-color:v-bind(update_button_color);
    text-align:center;
    width:50%;
    margin-left:20%;
    border-radius:100px;
    cursor:pointer;
    margin-top:10%;
    color:#fff;
    border: #fff solid 0px;
    box-shadow: 0px 2px 9px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out, background-color 0.5s ease-in-out;
}

.update_button:hover{
  box-shadow: 0px 5px 10px rgb(25, 120, 237, .5);
  transform: translateY(-1.5px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 3s;
} 

.update_button_minimum{
    padding:10px 20px;
    font-size:12px;
    background-color:v-bind(update_button_color);
    text-align:center;
    width:50%;
    margin-left:25%;
    border-radius:100px;
    cursor:pointer;
    margin-top:10%;
    color:#fff;
    border: #fff solid 0px;
    box-shadow: 0px 2px 9px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out, background-color 0.5s ease-in-out;
}


.update_button_minimum:hover{
  box-shadow: 0px 5px 10px rgb(25, 120, 237, .5);
  transform: translateY(-1.5px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 3s;
} 


.input_invest{
    width:100%;
    margin-left:0%
}

.label_invest{
    margin-left:-60px;
    margin-top:-30px
}


.transact_button{
    padding:10px 20px;
    font-size:20px;
    background-color:rgb(11, 184, 126);
    text-align:center;
    width:40%;
    margin-left:30%;
    border-radius:100px;
    cursor:pointer;
    margin-top:10%;
    color:#fff;
    border: #fff solid 0px;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}


.transact_button:hover{
  box-shadow: 0px 10px 15px rgb(11, 184, 126, .5);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
} 




.input_wrap{
    margin-left:-10%
}



@media only screen and (min-width: 0px) and (max-width: 576px) {

    
    .investment_grid{
    margin-left:5%;
    margin-top:75px;
    width:90%
}

    .intended_amount{
    font-size:80%;
}

.investment_line{
    width:80%;
    height:2px;
}

.ppm_select_container{
    width:80%;
    margin-left:15%;
    margin-top:0%;
}

.transact_button{
    padding:10px 20px;
    font-size:80%;
    width:40%;
    margin-left:30%;
}


.update_button{
    padding:6px 20px;
    font-size:8px;
}

.update_button_minimum{
    padding:6px 20px;
    font-size:8px;
    margin-left:0%
}

.transact_button{
    padding:10px 20px;
    font-size:80%;
    width:50%;
    margin-left:25%;
    margin-top:10%;
}



.investment_line_2{
    width:80%;
    margin-top:0px;
    margin-bottom:10px
}


.confirm_text{
    color:#000;
    line-height: 1.5;
    margin-bottom:30px;
    font-size:70%
}

.mobile_label{
    margin-left:-15%;
    font-size:60%
}

}

@media only screen and (min-width: 576px) and (max-width: 768px) {

    .investment_grid{
    margin-left:5%;
    margin-top:75px;
    width:90%
}

    .intended_amount{
    font-size:80%;
}

.investment_line{
    width:80%;
    height:2px;
}

.ppm_select_container{
    width:80%;
    margin-left:15%;
    margin-top:0%;
}

.transact_button{
    padding:10px 20px;
    font-size:80%;
    width:40%;
    margin-left:30%;
}


.update_button{
    padding:6px 20px;
    font-size:8px;
}

.update_button_minimum{
    padding:6px 20px;
    font-size:8px;
    margin-left:0%
}

.transact_button{
    padding:10px 20px;
    font-size:80%;
    width:50%;
    margin-left:25%;
    margin-top:10%;
}



.investment_line_2{
    width:80%;
    margin-top:0px;
    margin-bottom:10px
}


.confirm_text{
    color:#000;
    line-height: 1.5;
    margin-bottom:30px;
    font-size:70%
}



}

@media only screen and (min-width: 768px) and (max-width: 992px) {
}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
}





/* 
// ------------------------------- Modal  ---------------
// ------------------------------- Modal  ---------------
// ------------------------------- Modal  --------------- 
*/



.plaid_blur{
    position:fixed;
    top:0;
    left:0;
    height:100vh;
    width:100vw;
    background-color:rgba(25, 120, 237 , 0.08);
    z-index:100;
    backdrop-filter: blur(v-bind(blur_amount));
    transition:all 2s ease-in-out;
    display: flex;
    justify-content: center;
    align-items: center;
    opacity: v-bind(plaid_opacity);
}




.modal_hide_anim{
        transition: all 1s ease-in-out !important;
        opacity: 0 !important;
    }
    
    .modal_bix_hide_anim{
        transition: all .6s ease-in-out !important;
        transform: scale(0) !important;
    }
    
    .modal_hide_disp{
        display:none !important;
    }
    
    
    
    
    
    
    
    .modal_container{
        width:100vw;
        height:100vh;
        background-color:rgba(0, 0, 0, 0.5);
        position:fixed;
        top:0;
        left:0;
        z-index:200;
        display:flex;
        justify-content:center;
        align-items:center;
        backdrop-filter: blur(10px);
        transition: all 1s ease-in-out;
        opacity: 1;
    
    }
    .modal_popup{
        width:600px;
        height:425px;
        background-color:rgb(0, 0, 0);
        z-index:210;
        border-radius:20px;
        margin-top:0px;
        border: #fff solid 2px;
        transition: all 1s ease-in-out;
        overflow-y: scroll;
        overflow-x:hidden
    }

    .modal_popup::-webkit-scrollbar {
  width: 5px !important;
  border-radius: 10px !important;
}

.modal_popup::-webkit-scrollbar-thumb {
  background: rgba(0, 149, 255, 1) !important;
  border-radius: 10px !important;
}

    
    .modal_info_step_5{
        font-size:30px;
        font-weight:600;
        color:#fff;
        margin-left:10%;
        margin-top:10%;
        width:80%;
        text-align:center
    }
    
    .modual_buttons{
        width:40%;
        height:35px;
        background-color:rgb(25, 120, 237) ;
        margin-left: 30%;
        margin-top:3.5%;
        border-radius:100px;
        border:#fff solid 0px;
        cursor:pointer;
        font-size:12px;
        color:#fff;
          box-shadow: 0px 7px 10px rgb(25, 120, 237, .3);
      transition: outline 12s ease 1s;
    }
    
    .modual_buttons:hover{
      box-shadow: 0px 10px 15px rgb(25, 120, 237, .5);
      transform: translateY(-3px);
      outline: 3px solid rgba(19, 218, 218, 0.6);
      transition: outline 12s ease 1s;
    } 

    .select_button{
        width:40%;
        height:35px;
        background-color:rgb(25, 120, 237) ;
        margin-left: 30%;
        margin-top:5%;
        margin-bottom:20%;
        border-radius:100px;
        border:#fff solid 0px;
        cursor:pointer;
        font-size:12px;
        color:#fff;
          box-shadow: 0px 7px 10px rgb(25, 120, 237, .3);
      transition: outline 12s ease 1s;
    }

    .select_button:hover{
      box-shadow: 0px 10px 15px rgb(25, 120, 237, .5);
      transform: translateY(-3px);
      outline: 3px solid rgba(19, 218, 218, 0.6);
      transition: outline 12s ease 1s;
    } 

    .back_arrow{
        font-size:50px;
        color:#fff;
        position:relative;
        top:-60px;
        left:20px;
        margin-bottom:-7%;
        cursor: pointer;
    }
    
    
    .modal_exit{
        margin-top:0px;
        margin-left:540px;
        cursor:pointer;
        z-index: 10;
        position: relative;
        width:50px;
        height:50px;
    }
    
    .modal_exit:hover .horizontal_line{
        transform: rotate(180deg);
        transition: all 0.2s ease-in-out;
    }
    
    .modal_exit:hover .vertical_line{
        transform: rotate(-90deg);
        transition: all 0.5s ease-in-out;
    }
    .horizontal_line{
        height:1px;
        width:30px;
        background-color:rgb(255, 255, 255);
        top:25px;
        left:10px;
        transform: rotate(45deg);
        z-index:1000;
        position: absolute;
    }
    
    .vertical_line{
        width:1px;
        height:30px;
        top:11px;
        left:25px;
        background-color:#fff;
        transform: rotate(45deg);
        position: absolute;
    }
    
    
    
    
    @media only screen and (min-width: 0px) and (max-width: 576px) {
    
        .modal_popup{
        width:350px;
        height:400px;
    }
    
    .modal_exit{
        margin-top:10px;
        margin-left:290px;
        width:40px;
        height:40px;
    }
    
    }






    .account_select{
        margin-top:10%
    }







    .loader_container{
    position:fixed;
    top:0;
    left:0;
    height:100vh;
    width:100vw;
    background-color:rgba(25, 120, 237 , 0.125);
    z-index:100;
    backdrop-filter: blur(20px);
    transition:all 1s ease-in-out;
    display: flex;
    justify-content: center;
    align-items: center;
}

.loader {
      border: 50px solid #ffffff;
      border-top: 50px solid #3498db;
      border-radius: 50%;
      width: 240px;
      height: 240px;
      animation: spin 2s linear infinite;
    }

    @keyframes spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

</style>