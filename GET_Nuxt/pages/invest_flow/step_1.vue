<template>

    <div>

        <CircleTransition ref="cicle_tansition"/>

        
        <div class="loader_container" v-if="start_loader">
        <InvestFlowLoadersApiLoader/>
        </div>

        <InvestFlowModalsTwoFactorModal v-if="show_2fa_modal" />

    <Header/>



    <InvestFlowLoginPopup/>



<div class="white_background">

    <GSAPScrollSmoother>

        <InvestFlowStepCircles v-bind="step_circles" />



<!--     
<img class="invest_knob" id="knob" src="~assets/content/invest_knob.png" width="410" height="410">
 -->

<div class="form_container">

    <div class="form_grid">

        <div class="input_wrap">
                <input v-model="first_name" class="input_white" placeholder=' ' />
                <label class="label_white">First Name</label>
         </div>

         <div class="input_wrap">
                <input v-model="last_name" class="input_white" placeholder=' ' />
                <label class="label_white">Last Name</label>
         </div>

         <div class="input_wrap">
                <input v-model="email" class="input_white" placeholder=' ' type="email" />
                <label class="label_white">Email</label>
        </div>

        <div class="input_wrap">
                <input ref="phone_focused" @keyup="remove_chrs" @keypress="onPhoneKeyPress" maxlength="17" v-model="phone" class="input_white" placeholder=' ' />
                <label class="label_white">Phone Number</label>
                <span v-if="show_international" class="international_toggle" @click="international_toggle"> {{ inter_text }}</span>
         </div>


    <div class="input_wrap">
            <select v-model="selected_fund"   class="select_white">
                    <option value="" disabled selected hidden></option>
                    <option value="NEXT_AI">NEXT AI</option>
                    <option value="Nanotechnology">US Nano Technology Fund A</option>
                    <option value="Eco_Energy">Eco Energy Fund</option>
                    <option disabled="disabled" value="impossible">Impossible Foods</option>
                    <option disabled="disabled" value="social_wise">Social Wise</option>
                    <option disabled="disabled" value="agile_elements">Agile Elements</option>
                    <option disabled="disabled" value="boysterous">Boysterous Couture</option>
                    <option disabled="disabled" value="helpful">Helpful+</option>
                    <option disabled="disabled" value="neuralink">Neuralink</option>
                    <option disabled="disabled" value="thermo_ai">Thermo AI</option>
                    <option disabled="disabled" value="boring Company">The Boring Company</option>
            </select>
                <label class="label_white">Invest In:</label>
        </div>


            </div>



       <InvestDial/>


        

<button @click="handle_submit" class="next_button">Next</button>


</div>


    </GSAPScrollSmoother>
    
</div>

</div>
    </template>
    
    


    <script setup>
import { page_to } from "../../stores/page_to.js"
import { useFocus } from '@vueuse/core'

// sleep time expects milliseconds
function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}


const config = useRuntimeConfig()


const enabled_fund_list = ['nano']


const step_circles = {
    current_num: 1
}

const cicle_tansition = ref('');


const cookie_options = {default:()=> '', watch:true, maxAge:1800}
const most_recent_fund_page = useCookie('most_recent_fund_page', cookie_options)
const first_name = useCookie('first_name', cookie_options)
const last_name = useCookie('last_name', cookie_options)
const email = useCookie('email', cookie_options)
const phone = useCookie('phone', cookie_options)
const selected_fund = useCookie('selected_fund', cookie_options)
const investor_ID = useCookie('investor_ID', {default:()=> '', watch:true, maxAge:2400})
const fund_ID = useCookie('fund_ID', cookie_options)

const is_international = ref(false)
const is_international_color = ref('#1b91ebb3')
const inter_text = ref('International ?')
const inter_margin = ref('65%')
const start_loader = ref(false);

const show_2fa_modal = ref(false)

onMounted(() => {

    if (enabled_fund_list.includes(most_recent_fund_page.value)){
    selected_fund.value = most_recent_fund_page.value
    }
})



function onPhoneKeyPress(e) {
    const key = e.keyCode || e.charCode;
    const len_phone = phone.value.length

    if (!is_international.value){
    if (key !== 8 || key !==  46) {
    if(len_phone == 12){
        phone.value = phone.value + '-'
        }
    else if (len_phone == 7){   
        phone.value = phone.value + ') '
        }
    else if (len_phone == 0){   
        phone.value = '+1 ('
        }}

    }else{
        if (len_phone == 0){   
        phone.value = '+'
        }
}



}

function remove_chrs() {
    phone.value = phone.value.toString().replace(/[^0-9-()-+ ]/g, '');
}



function international_toggle() {
    is_international.value = !is_international.value
    if (is_international.value) {
        is_international_color.value = '#06ae46'
        phone.value = '+' + phone.value.toString().replace(/[^0-9]/g, '').substring(1);
        inter_text.value = 'U.S. ?'
        phone_focused.value.focus()
        sleep(1110).then(() => {show_international.value = true})
        sleep(800).then(() => { inter_opacity.value = 1, inter_margin.value = '85%' })
} else{
        is_international_color.value = '#1b91ebb3'
        phone.value = '+1 ('
        inter_text.value = 'International ?'
        phone_focused.value.focus()
        sleep(1110).then(() => {show_international.value = true})
        sleep(800).then(() => { inter_opacity.value = 1, inter_margin.value = '75%' })
}
}

const show_international = ref(false)
const inter_opacity = ref(0)
const phone_focused = ref()
const { focused } = useFocus(phone_focused)

watch(focused, (focused) => {
  if (focused) {
    show_international.value = true
    sleep(10).then(() => { inter_opacity.value = 1, inter_margin.value = '75%' })
  }
  else{
    sleep(1100).then(() => {show_international.value = false})
    sleep(800).then(() => { inter_opacity.value = 0, inter_margin.value = '65%' })
  }
})




function transition_and_route(route_to) {
 cicle_tansition.value.animation_and_route(route_to);
}




function handle_submit() {

    const email_regex = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/


    const investment_amount = useCookie('investment_amount', cookie_options)
    investment_amount.value = investment_amount.value.toString().replace(/\D/g, "")
    const data_to_send = {first_name: first_name.value, last_name: last_name.value, email: email.value, phone: phone.value, investment_amount: investment_amount.value, selected_fund: selected_fund.value, investor_ID:investor_ID.value}

    for (const [key, value] of Object.entries(data_to_send)) {
        if(key != 'investor_ID' && value == ''){
            alert('Please fill in all fields')
            return
        } else if ( !is_international.value && key == 'phone' && value.length < 17 ){
                alert('Please enter a phone number of the proper length')
                return
            }
       else if (key == 'email' && !value.match(email_regex)) {
        alert("please enter a valid email")
        return
        } 
    }

    step_1_api_send(data_to_send)

    }




function step_1_api_send(data_to_send) {

    start_loader.value = true;


    fetch(`${config.flask_url}/api/invest_flow/step_1/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data_to_send)
    })
    .then((response) => response.json())
    .then((data) => {

        if(data.status == 'email_exists'){
            show_2fa_modal.value = true
            start_loader.value = false;
        } else if (data.status == 'already_invested') {
            alert(data.message)
            start_loader.value = false;
        } else{
        fund_ID.value = data.fund_ID
        investor_ID.value = data.investor_ID

        console.log('Success:', data.message)
        transition_and_route('step_2')
        }


    })
    .catch(error => {
        alert('Error')
        start_loader.value = false;
        console.error('There was an error!', error);
    });
}



</script>



<style scoped>


.white_background{
    background-color: #fff;
    height:100%;
    width:100%;
    position:fixed;
    top:0;
    left:0;
    z-index:0;
}



.form_container{
    position: relative;
z-index:10;
width:100%;
padding-bottom:50vh;
}
.form_grid{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: repeat(2, 1fr);
grid-column-gap: 50px;
grid-row-gap: 0px;
width:80%;
margin-left:10%;
margin-top:10%;
position: relative;
z-index:10;
}


.next_button{
    width:30%;
    height:40px;
    background-color:rgb(25, 120, 237) ;
    margin-left: 35%;
    margin-top:7%;
    border-radius:100px;
    border:#fff solid 0px;
    cursor:pointer;
    font-size:2vw;
    color:#fff;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}


.next_button:hover{
  box-shadow: 0px 10px 15px rgb(25, 120, 237, .5);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
} 



.international_toggle{
    font-size:10%;
    color: v-bind(is_international_color);
    margin-left:v-bind(inter_margin);
    padding:0px 5px 5px 5px;
    margin-top:.9%;
    word-spacing: .05rem;
    cursor:pointer;
    position:absolute;
    opacity:v-bind(inter_opacity);
    transition: all .5s ease-in-out;
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




@media only screen and (min-width: 0px) and (max-width: 380px) {
    .form_grid{
        margin-top:-40%;
}

.next_button{
    width:50%;
    height:30px;
    margin-top:-55%;
    font-size:3.5vw;
    margin-left: 25%;
}

.form_grid{
    display: grid;
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(5, 1fr);
grid-column-gap: 0px;
grid-row-gap: 20px;
width:80%;
margin-left:10%;
margin-top:10%;
position: relative;
z-index:10;
margin-bottom:10%
}

}




@media only screen and (min-width: 380px) and (max-width: 576px) {
    .form_grid{
        margin-top:-40%;
}

.next_button{
    width:40%;
    height:40px;
    margin-top:12%;
    font-size:3.5vw;
}

.form_grid{
        margin-top:-40%;
}

.next_button{
    width:50%;
    height:30px;
    margin-top:15%;
    font-size:3.5vw;
    margin-left: 25%;
}

.form_grid{
    display: grid;
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(5, 1fr);
grid-column-gap: 0px;
grid-row-gap: 10px;
width:80%;
margin-left:10%;
margin-top:10%;
position: relative;
z-index:10;
margin-bottom:10%
}

}

@media only screen and (min-width: 576px) and (max-width: 768px) {

    .form_grid{
        margin-top:25%;
}

.next_button{
    width:40%;
    height:40px;
    margin-top:12%;
    font-size:3.5vw;
}

}

@media only screen and (min-width: 768px) and (max-width: 992px) {

    .form_grid{
        margin-top:15%;
}


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