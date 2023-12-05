<template>
<div>
<CircleTransition ref="cicle_tansition"/>

    <Header/>
    <div class="white_background">
    <GSAPScrollSmoother>



        <InvestFlowStepCircles v-bind="step_circles" />
    

    <div class="sub_agreement_grid">


    <embed v-if="selected_fund == 'Nanotechnology'" :src="nano_doc_1" class="sub_agreement">
    <embed v-if="selected_fund == 'Eco_Energy'" :src="documentSourceSubAgreement" class="sub_agreement" />
    <embed v-if="selected_fund == 'NEXT_AI'" :src="next_ai_doc_1" class="sub_agreement" />







        <div class="sub_ag_container">
<p class="confirm_text">
    
    
    By typing my full name below, I agree to the terms and conditions outlined in the attatched subscription agreement.

          </p>

          <div class="input_wrap mobile_move">
                <input v-model="signature_typed" class="input_white" placeholder=' ' />
                <label class="label_white">Type Full Name To Sign</label>
         </div>



        <!-- <button @click="transition_and_route('step_5')" class="continue_button">Submit All and Continue</button> -->

    </div>
























    <div style="display:none">


    <h6 class="start_button" @click="hide_start" :class="{start_hidden:start_hidden}">Start Signing</h6>

    <div class="form_pagenation">
        <div class="prev_button" :class="{hide_prev:hide_prev}" @click="page_counter_prev">Prev</div>
        <div class="next_button" :class="{hide_next:hide_next}" @click="page_counter_next">Next</div>
    </div>




    <div class="form_elm" :class="[active_elm_count === 1 ? 'active_form_elm' : active_elm_count > 1 ? 'filled_form_elm' : '']">
        <div class="tab_tip" :class="{tab_tip_show:show_tab_tip}">Tip: Click tab to go to next form input</div>
        <p class="input_text">Please Type Full Name For Signature</p>
        <div class="flex_input">
        <div class="input_wrap">
            <input v-model="entered_signature" @focus="form_focused(1)" @blur="form_blurred" name="owner_zip" class="input_white input_modify" placeholder=' ' type="text" :disabled="active_elm_count != 1" />
            <label  class="label_white label_modify">Full Name</label>
    </div>

</div>
    </div>



    <div class="form_elm" :class="[active_elm_count === 2 ? 'active_form_elm' : active_elm_count > 2 ? 'filled_form_elm' : '']">
        <p class="input_text">Please Type Initials</p>
        <div class="flex_input">
        <div class="input_wrap">
            <input v-model="entered_initials" @focus="form_focused(2)" @blur="form_blurred" name="owner_zip" class="input_white input_modify" placeholder=' ' type="text" :disabled="active_elm_count != 2" />
            <label  class="label_white label_modify">Initials</label>
    </div>
</div>
    </div>






    <div class="form_elm" :class="[active_elm_count === 3 ? 'active_form_elm' : active_elm_count > 3 ? 'filled_form_elm' : '']">
        <p class="input_text">I certify that I have a net worth (excluding the value of my primary residence) in excess of $1 million either individually or through aggregating my individual holdings and those in which I have a joint, community property or other similar shared ownership interest with my spouse.</p>
        <div class="flex_input">
        <div class="input_wrap">
            <input v-model="auto_3" :disabled="active_elm_count != 3" @blur="form_blurred" name="owner_zip" class="input_white input_modify" placeholder=' ' type="text" />
            <label  class="label_white label_modify">Initials</label>
    </div>
    <div @click="auto_button_single(3)" class="auto_button_single">Auto Fill</div>
    <div @click="auto_all" class="auto_button">Auto Fill All</div>
    </div>
</div>



    <div class="form_elm" :class="[active_elm_count === 4 ? 'active_form_elm' : active_elm_count > 4 ? 'filled_form_elm' : '']">
        <p class="input_text">yyyyyyyyyyyyyt</p>
        <div class="flex_input">
        <div class="input_wrap">
            <input v-model="auto_4" :disabled="active_elm_count != 4" @blur="form_blurred" name="owner_zip" class="input_white input_modify" placeholder=' ' type="text" />
            <label  class="label_white label_modify">Initials</label>
    </div>
    <div @click="auto_button_single(4)" class="auto_button_single">Auto Fill</div>
    <div @click="auto_all" class="auto_button">Auto Fill All</div>
    </div>
</div>

    <div class="form_elm" :class="[active_elm_count === 5 ? 'active_form_elm' : active_elm_count > 5 ? 'filled_form_elm' : '']">
        <p class="input_text">Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
        <div class="flex_input">
        <div class="input_wrap">
            <input v-model="auto_5" :disabled="active_elm_count != 5" @blur="form_blurred" name="owner_zip" class="input_white input_modify" placeholder=' ' type="text" />
            <label  class="label_white label_modify">Initials</label>
    </div>
    <div @click="auto_button_single(5)" class="auto_button_single">Auto Fill</div>
    <div @click="auto_all" class="auto_button">Auto Fill All</div>
    </div>
</div>



<div class="form_elm" :class="[active_elm_count === 6 ? 'active_form_elm' : active_elm_count > 6 ? 'filled_form_elm' : '']">
        <p class="input_text">yyyyyyyyyyyyyt</p>
        <div class="flex_input">
        <div class="input_wrap">
            <input v-model="auto_6" :disabled="active_elm_count != 6" @blur="form_blurred" name="owner_zip" class="input_white input_modify" placeholder=' ' type="text" />
            <label  class="label_white label_modify">Initials</label>
    </div>
    <div @click="auto_button_single(6)" class="auto_button_single">Auto Fill</div>
    <div @click="auto_all" class="auto_button">Auto Fill All</div>
    </div>
</div>




<div class="form_elm" :class="[active_elm_count === 7 ? 'active_form_elm' : active_elm_count > 7 ? 'filled_form_elm' : '']">
        <p class="input_text">Mauris cursus mattis molestie a iaculis. Libero volutpat sed cras ornare arcu dui. </p>
        <div class="flex_input">
        <div class="input_wrap">
            <input v-model="auto_7" :disabled="active_elm_count != 7" @blur="form_blurred" name="owner_zip" class="input_white input_modify" placeholder=' ' type="text" />
            <label  class="label_white label_modify">Initials</label>
    </div>
    <div @click="auto_button_single(7)" class="auto_button_single">Auto Fill</div>
    <div @click="auto_all" class="auto_button">Auto Fill All</div>
    </div>
</div>




<div class="form_elm" :class="[active_elm_count === 8 ? 'active_form_elm' : active_elm_count > 8 ? 'filled_form_elm' : '']">
        <p class="input_text"> Mauris commodo quis imperdiet massa. Odio aenean sed adipiscing diam donec adipiscing tristique risus nec. Eu scelerisque </p>
        <div class="flex_input">
        <div class="input_wrap">
            <input v-model="auto_8" :disabled="active_elm_count != 8" @blur="form_blurred" name="owner_zip" class="input_white input_modify" placeholder=' ' type="text" />
            <label  class="label_white label_modify">Initials</label>
    </div>
    <div @click="auto_button_single(8)" class="auto_button_single">Auto Fill</div>
    <div @click="auto_all" class="auto_button">Auto Fill All</div>
    </div>
</div>



<div class="form_elm" :class="[active_elm_count === 9 ? 'active_form_elm' : active_elm_count > 9 ? 'filled_form_elm' : '']">
        <p class="input_text">Pharetra pharetra massa massa ultricies mi quis hendrerit. Velit egestas dui id ornare. A pellentesque sit amet porttitor eget dolor.</p>
        <div class="flex_input">
        <div class="input_wrap">
            <input v-model="auto_9" :disabled="active_elm_count != 9" @blur="form_blurred" name="owner_zip" class="input_white input_modify" placeholder=' ' type="text" />
            <label  class="label_white label_modify">Initials</label>
    </div>
    <div @click="auto_button_single(9)" class="auto_button_single">Auto Fill</div>
    <div @click="auto_all" class="auto_button">Auto Fill All</div>
    </div>
</div>




<div class="form_elm" :class="[active_elm_count === 10 ? 'active_form_elm' : active_elm_count > 10 ? 'filled_form_elm' : '']">
        <p class="input_text">PQuam lacus suspendisse faucibus interdum posuere lorem ipsum. Etiam sit amet nisl purus. Dui faucibus in ornare quam viverra orci sagittis.</p>
        <div class="flex_input">
        <div class="input_wrap">
            <input v-model="auto_10" :disabled="active_elm_count != 10" @blur="form_blurred" name="owner_zip" class="input_white input_modify" placeholder=' ' type="text" />
            <label  class="label_white label_modify">Initials</label>
    </div>
    <div @click="auto_button_single(10)" class="auto_button_single">Auto Fill</div>
    <div @click="auto_all" class="auto_button">Auto Fill All</div>
    </div>
</div>




<div class="form_elm" :class="[active_elm_count === 11 ? 'active_form_elm' : active_elm_count > 11 ? 'filled_form_elm' : '']">
        <p class="input_text">Egestas purus viverra accumsan in nisl nisi scelerisque eu. Vel pretium lectus quam id leo in vitae turpis</p>
        <div class="flex_input">
        <div class="input_wrap">
            <input v-model="auto_11" :disabled="active_elm_count != 11" @blur="form_blurred" name="owner_zip" class="input_white input_modify" placeholder=' ' type="text" />
            <label  class="label_white label_modify">Initials</label>
    </div>
    <div @click="auto_button_single(11)" class="auto_button_single">Auto Fill</div>
    <div @click="auto_all" class="auto_button">Auto Fill All</div>
    </div>
</div>




<div class="form_elm" :class="[active_elm_count === 12 ? 'active_form_elm' : active_elm_count > 12 ? 'filled_form_elm' : '']">

    <h5 style="color:black; margin-left:10%">Completed!</h5>
    <p style="color:black; margin-left:10%">Scroll Down</p>
    </div>






</div>




    </div>

    <div style="padding-bottom:25vh"></div>


    <embed v-if="selected_fund == 'Nanotechnology'" :src="nano_doc_2" class="ppm_agreement">
    <embed v-if="selected_fund == 'Eco_Energy'" :src="documentSourcePPM" class="ppm_agreement" />
    <embed v-if="selected_fund == 'NEXT_AI'" :src="next_ai_doc_2" class="ppm_agreement" />


    


        <div class="ppm_select_container">
            <h6 style="color:#000; line-height:1; margin-bottom:40px">Final Attestation</h6>
<p class="confirm_text">* I confirm that the information submitted is correct to my knowledge
           <br><br>
           * I confirm that I have read the above PPM
           <br><br>
           * I understand that I am responsible for my own due diligence
           <br><br>
           * I give permission to GET to verify my accredited status
           <br><br>
           * I give permission to GET to initiate a ACH transfer from your bank account using Dwolla.
           <br><br>
           * By selecting this dropdown I agree to our partner Dwolla's terms of <a target="_blank" href="https://www.dwolla.com/legal/tos/" class="partner_link">Service</a> and <a target="_blank" href='https://www.dwolla.com/legal/privacy/' class="partner_link">Privacy Policy</a></p>

    <div class="input_wrap wide_select">
            <select v-model="agree_to_all"  class="select_white">
                    <option value="" disabled selected hidden></option>
                    <option value="yes">Yes</option>
                    <option value="no">No</option>
            </select>
                <label class="label_white wide_label">I agree to all of the above:</label>
        </div>


        <button @click="step_4_api_send()" class="continue_button">Submit All and Continue</button>

    </div>



    <div style="padding-bottom:50vh"></div>


    </GSAPScrollSmoother>
</div> 

</div>
    
    </template>
    
    
<script setup>


 import nano_doc_1 from "~/assets/legal/nano/Subscription_Agreement_&_Accredited_Cert__US_Nano_Fund_A.pdf";
 import nano_doc_2 from "~/assets/legal/nano/PPM_for_US Nanotechnology_Fund_A.pdf";
 import eco_doc_1 from "~/assets/legal/eco/Subscription_Agreement_Only_Eco_Energy.pdf";
 import eco_doc_2 from "~/assets/legal/eco/PPM_for_Eco_Energy_Partners.pdf";
 import next_ai_doc_1 from "~/assets/legal/next_ai/Next_AI_Fund_PPM.pdf"
 import next_ai_doc_2 from "~/assets/legal/next_ai/Next_AI_Fund_Sub_Agreement.pdf"


//  import legal_doc_1 from "~/assets/legal/nano/Subscription_Agreement_&_Accredited_Cert__US_Nano_Fund_A.pdf";
//  import legal_doc_2 from "~/assets/legal/nano/Final_of_PPM_for_US_Nanotechnology_Fund_A.pdf";


const config = useRuntimeConfig()
const selected_fund = useCookie('selected_fund')
const investing_as = useCookie('investing_as')
const start_hidden = ref(false)
const hide_next = ref(true)
const hide_prev = ref(true)
const show_tab_tip = ref(false)
const entered_signature = ref(null)
const entered_initials = ref(null)


const auto_3 = ref(null)
const auto_4 = ref(null)
const auto_5 = ref(null)
const auto_6 = ref(null)
const auto_7 = ref(null)
const auto_8 = ref(null)
const auto_9 = ref(null)
const auto_10 = ref(null)
const auto_11 = ref(null)
const auto_12 = ref(null)

const active_elm_count = ref(0)
const signed_elm_count = ref(1)

const flow_bar_start = ref(true)

const step_circles = {
    current_num: 4
}



const documentSourceSubAgreement = computed(() => {
    if (selected_fund.value === 'Eco_Energy') {
        if (investing_as.value == 'corporation' || investing_as.value == 'llc' || investing_as.value == 'partnership') {
            return eco_doc_1;
        } else {
            return eco_doc_1;
        }
    }
});


const documentSourcePPM = computed(() => {
    if (selected_fund.value === 'Eco_Energy') {
        if (investing_as.value == 'corporation' || investing_as.value == 'llc' || investing_as.value == 'partnership') {
            return eco_doc_2;
        } else {
            return eco_doc_2;
        }
    }
});






onMounted(() => {

flow_bar_start.value = false
})



function hide_start(){
    start_hidden.value = true;
    active_elm_count.value += 1
}

function form_blurred(event){

    if(event.target.value.length >= 1){
    if(active_elm_count.value == signed_elm_count.value){
        signed_elm_count.value += 1
    }

    if (active_elm_count.value > 0){
        hide_prev.value = false
    }

    active_elm_count.value += 1
}
}

function form_focused(elm_count){
   // active_elm_count.value = elm_count
    if (active_elm_count.value == 1){
        show_tab_tip.value = true
    }

}

function page_counter_prev(){
    if(active_elm_count.value > 1){
    active_elm_count.value -= 1
    hide_next.value = false
    }
    if(active_elm_count.value == 1){
        hide_prev.value = true
    }
}


function page_counter_next(){
    active_elm_count.value += 1
    hide_prev.value = false
    if(active_elm_count.value == signed_elm_count.value){
        hide_next.value = true
}
}

// sleep time expects milliseconds
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}



function auto_button_single(auto_num){
    //eval("auto_" + String(auto_num)).value = entered_initials.value

    if (auto_num == 3){
        auto_3.value = entered_initials.value
    } else if (auto_num == 4){
        auto_4.value = entered_initials.value
    } else if (auto_num == 5){
        auto_5.value = entered_initials.value
    } else if (auto_num == 6){
        auto_6.value = entered_initials.value
    } else if (auto_num == 7){
        auto_7.value = entered_initials.value
    } else if (auto_num == 8){
        auto_8.value = entered_initials.value
    } else if (auto_num == 9){
        auto_9.value = entered_initials.value
    } else if (auto_num == 10){
        auto_10.value = entered_initials.value
    } else if (auto_num == 11){
        auto_11.value = entered_initials.value
    } else if (auto_num == 12){
        auto_12.value = entered_initials.value
    }



    sleep(300).then(() => {
        if(active_elm_count.value == signed_elm_count.value){
        signed_elm_count.value += 1
    }

    if (active_elm_count.value > 0){
        hide_prev.value = false
    }

    active_elm_count.value += 1
    });

}

function auto_all(){
    for (let i = 3; i <= 12; i++) {
        // eval("auto_" + String(i)).value = entered_initials.value

        if (i == 3){
            auto_3.value = entered_initials.value
        } else if (i == 4){
            auto_4.value = entered_initials.value
        } else if (i == 5){
            auto_5.value = entered_initials.value
        } else if (i == 6){
            auto_6.value = entered_initials.value
        } else if (i == 7){
            auto_7.value = entered_initials.value
        } else if (i == 8){
            auto_8.value = entered_initials.value
        } else if (i == 9){
            auto_9.value = entered_initials.value
        } else if (i == 10){
            auto_10.value = entered_initials.value
        } else if (i == 11){
            auto_11.value = entered_initials.value
        } else if (i == 12){
            auto_12.value = entered_initials.value
        }
        active_elm_count.value = 12
        signed_elm_count.value = 12
}
}




const agree_to_all = ref(null)

const cookie_options = {default:()=> '', watch:true, maxAge:1800}
const signature_typed = useCookie('signature_typed', cookie_options)
const investor_ID = useCookie('investor_ID', cookie_options)
const fund_ID = useCookie('fund_ID', cookie_options)
const dwolla_customer_status = useCookie('dwolla_customer_status', cookie_options)
const dwolla_beneficial_owner_status = useCookie('dwolla_beneficial_owner_status', cookie_options)
const dwolla_customer_created = useCookie('dwolla_customer_created', cookie_options)
const minimum_investment_amount = useCookie('minimum_investment_amount', cookie_options)
dwolla_customer_created.value = true



function step_4_api_send() {

    if(agree_to_all.value != "yes"){
        alert("Please agree to all of the above")
    } else if (signature_typed.value == ''){
        alert("Please Sign First Document")
    }
    else{

    fetch(`${config.flask_url}/api/invest_flow/step_4/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({fund_ID:fund_ID.value, agree_to_all:agree_to_all.value, signature_typed:signature_typed.value, investor_ID:investor_ID.value})
    })
    .then((response) => response.json())
    .then((data) => {

        if (data.status == 'error'){
            alert(data.message)
        } else {
        console.log('Success:', data.message);
        dwolla_customer_status.value = data.dwolla_customer_status
        dwolla_beneficial_owner_status.value = data.dwolla_beneficial_owner_status
        minimum_investment_amount.value = data.minimum_investment_amount
        transition_and_route('step_5')
    }
    })
    .catch(error => {
        alert('Error')
        console.error('There was an error!', error);
    });
}
}





const cicle_tansition = ref('')
function transition_and_route(route_to) {

cicle_tansition.value.animation_and_route(route_to);

}










</script>

<style scoped>

.hide_prev{
    display: none;
}

.hide_next{
    display: none;
}

.start_hidden{
    display:none
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


/* Add frameborder="0" to html embed to remove print option */
.sub_agreement{
    width:45vw;
    height:80vh;
}

.ppm_agreement{
    width:80vw;
    height:70vh;
    margin-left:10vw
}


.sub_agreement_grid{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 75px;
    grid-row-gap: 0px;
    margin-left:5%;
    position: relative;
    z-index:1;
    margin-top:20%;
    width:90%
}

.start_button{
    padding:10px 25px;
    font-size:2vw;
    background-color:rgb(11, 184, 126);
    text-align:center;
    width:50%;
    margin-left:0%;
    border-radius:100px;
    cursor:pointer;
    margin-top:15%;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
    
}

.start_button:hover{
  box-shadow: 0px 10px 15px rgb(11, 184, 126, .5);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
} 

.form_elm{
    transition: all 1s ease-in-out;
    width:800px;
    margin-top:5%;
    margin-left:100%;
    opacity:0;
    visibility:"hiddn";
    position:absolute;
}

.active_form_elm{
    margin-top:5%;
    margin-left:-7%;
    opacity:1;
    visibility: visible;
    position:absolute;
    transition: all 1s ease-in-out;
    width:52%
}

.filled_form_elm{
    margin-top:60%;
    margin-left:-10%;
    opacity:0;
    visibility: hidden;
    position:absolute;
    transition: all 1s ease-in-out;
}



.form_hidden{
    margin-left:50%;
    display:none;
    transition: all 1s ease-in-out
}




.input_text{
    color:#000;
    width:80%;
    font-size:15px;
    margin-left:10%;
    margin-bottom:-30px;
    visibility: v-bind(text_visiblity);
    opacity:v-bind(text_opacity);
    transition: all .5s ease-in-out;
    line-height:1;
    font-size:12px

}


.partner_link{
    color:#000;
    text-decoration: underline !important;
}

.flex_input{
    display: flex;
    justify-content: flex-start;
    width:90%;
    margin-left:8%;
    margin-top:5%
}



.form_pagenation{
    display: flex;
    justify-content: center;
width:90%;
margin-top:10%;
margin-left:-7%
}

.prev_button{
    width:100%;
    max-width:100px;
    padding:10px 45px;
    background-color:rgb(25, 120, 237);
    color:#fff;
    text-align: center;
    border-radius:100px;
    cursor: pointer;
    margin:50px;
    font-size:1.5vw;
    margin-left:0px;
    margin-bottom:0;
    box-shadow: 0px 2px 9px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}

.prev_button:hover{
    box-shadow: 0px 5px 10px rgb(25, 120, 237, .5);
  transform: translateY(-1.5px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 3s;
} 


.next_button{
    width:100%;
    max-width:100px;
    padding:10px 45px;
    background-color:rgb(25, 120, 237);
    color:#fff;
    text-align: center;
    border-radius:100px;
    cursor: pointer;
    margin:50px;
    font-size:1.5vw;
    margin-left:0px;
    margin-bottom:0;
    box-shadow: 0px 2px 9px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}

.next_button:hover{
  box-shadow: 0px 5px 10px rgb(25, 120, 237, .5);
  transform: translateY(-1.5px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 3s;
} 


.input_modify{
    width:100%
}

.label_modify{
    margin-left:-12%
}

.auto_button{
    width:110px;
    height:7px;
    padding:10px 10px;
    background-color:rgb(25, 173, 112);
    color:#fff;
    text-align: center;
    border-radius:100px;
    cursor: pointer;
    margin-left:5%;
    margin-top:8%;
    font-size:10px;
    box-shadow: 0px 2px 9px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}

.auto_button:hover{
  box-shadow: 0px 7px 12px rgb(25, 173, 112, .3);
  transform: translateY(-1.5px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 3s;
} 

.auto_button_single{
    width:110px;
    height:7px;
    padding:10px 10px;
    background-color:rgb(230, 203, 68);
    color:#fff;
    text-align: center;
    border-radius:100px;
    cursor: pointer;
    margin-left:25%;
    margin-top:8%;
    font-size:10px;
    box-shadow: 0px 2px 9px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgb(25, 173, 112);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}

.auto_button_single:hover{
  box-shadow: 0px 7px 12px rgb(230, 203, 68, .3);
  transform: translateY(-1.5px);
  outline: 3px solid rgb(25, 173, 112);
  transition: outline 12s ease 3s;
} 

.tab_tip{
    width:0px;
    padding:10px;
    background-color:rgb(25, 120, 237);
    color:#fff;
    text-align: center;
    border-radius:100px;
    cursor: pointer;
    margin:50px;
    z-index:0;
    visibility: hidden;
    opacity: 0;
    transition:all .5s ease-in-out;
    margin-left:5%;
    font-size:0px
}

.tab_tip_show{
    visibility: visible;
    opacity: 1;
    margin-left:8%;
    width:270px;
    font-size:12px;
    transition:all .5s ease-in-out
}








.ppm_select_container{
    width:80%;
    margin-left:10%;
    margin-top:10%;
}

.sub_ag_container{
    width:80%;
    margin-left:10%;
    margin-top:10%;
}
.confirm_text{
    color:#000;
    line-height: 1.5;
    font-size:15px
}

.wide_label{
    margin-left:10px;
    margin-top:0%
}

.wide_select{
    margin-left:-5%;
    margin-top:10%;
    width:50%
}

.continue_button{
    padding:10px 25px;
    font-size:2vw;
    background-color:rgb(11, 184, 126);
    text-align:center;
    width:50%;
    margin-left:25%;
    border-radius:100px;
    cursor:pointer;
    margin-top:15%;
    color:#fff;
    border: #fff solid 0px;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}



.continue_button:hover{
  box-shadow: 0px 10px 15px rgb(11, 184, 126, .5);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
} 











@media only screen and (min-width: 0px) and (max-width: 576px) {


.sub_agreement_grid{
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    margin-left:10%;
    position: relative;
    z-index:1;
    margin-top:20%;
    width:90%
}

.sub_agreement{
    width:90%;
    height:60vh;
}

.ppm_agreement{
    width:80vw;
    height:70vh;
    margin-left:10vw;
    margin-top:-70%
}


.sub_ag_container{
    width:90%;
    margin-left:0%;
    margin-top:10%;
}


.form_pagenation{
    display: flex;
    justify-content: center;
width:100%;
margin-top:5%;
margin-left:0%
}

.active_form_elm{
    margin-top:15%;
    margin-left:-10%;
    width:100%;

}

.flex_input{
    display: flex;
    justify-content: flex-start;
    width:90%;
    margin-left:8%;
}

.input_wrap{
    margin-top:8%;
}

.input_modify{
    width:140%
}

.label_modify{
    margin-left:-12%
}


.input_text{
    width:90%;
    margin-left:10%;
    margin-bottom:10%;
    font-size:13px;

}

.wide_select{
    margin-top:20%;
    width:90%
}

.wide_label{
    margin-left:-6px;
    margin-top:-4%;
}


.mobile_move{
    margin-left:-10%;
}


.continue_button{
    font-size:3vw;
    width:60%;
    margin-left:20%;
    margin-top:20%;
}


}


@media only screen and (min-width: 576px) and (max-width: 768px) {


    .sub_agreement_grid{
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    margin-left:10%;
    position: relative;
    z-index:1;
    margin-top:20%;
    width:90%
}

.sub_agreement{
    width:90%;
    height:60vh;
}

.form_pagenation{
    display: flex;
    justify-content: center;
width:100%;
margin-top:5%;
margin-left:0%
}

.active_form_elm{
    margin-top:15%;
    margin-left:-10%;
    width:100%;

}

.flex_input{
    display: flex;
    justify-content: flex-start;
    width:90%;
    margin-left:8%;
}

.input_wrap{
    margin-top:8%;
}

.input_modify{
    width:140%
}

.label_modify{
    margin-left:-12%
}


.input_text{
    width:90%;
    margin-left:10%;
    margin-bottom:10%;
    font-size:13px;

}

.wide_select{
    margin-top:20%;
    width:70%
}

.wide_label{
    margin-left:15px;
    margin-top:0%
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










</style>