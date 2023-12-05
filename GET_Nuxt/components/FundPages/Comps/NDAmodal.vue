<template>
    
    
    <!-- <div class="nda_modal" :class="{ nda_completed: nda_completed }"> -->
        <div class="nda_modal">
        <div class="nda_modal_container">
            <h5 class="nda_title">Non-Disclosure Agreement</h5>
            <p class="nda_text">By entering the information below, you agree to be bound by the terms of Non-Disclosure Agreement found <a style="color:rgb(25, 120, 237)" target="_blank" href="../../NDAs/GET_NDA.pdf">here</a>.</p>


            <p v-if="verification_sent" class="nda_message">Verification code sent to: <span style="color:#fff; text-decoration:underline; text-decoration-color: rgb(25, 120, 237); margin-left:10px">  {{ message }}</span></p>

                <p v-else class="nda_message"><span style="color:#fff; text-decoration:underline; text-decoration-color: rgb(25, 120, 237)">  {{ message }}</span></p>


            <div :class="{ nda_enterInfo: nda_enterInfo }">
                <div class="input_grid">
                    
                    <div class="input_wrap">
                        <input v-model="name" type="text" class="input_black" placeholder=' ' required/>
                        <label class="label_black">Full Name</label>
                    </div>
                    
                    <div class="input_wrap">
                        <input v-model="email" type="email" class="input_black" placeholder=' ' required/>
                        <label class="label_black">Email</label>
                    </div>
                    <div class="input_wrap">
                        <input ref="phone_focused" @keyup="remove_chrs" @keypress="onPhoneKeyPress" maxlength="17"   v-model="phone" type="text" class="input_black" placeholder=' ' required/>
                        <label class="label_black">Phone Number</label>
                        <span v-if="show_international" class="international_toggle" @click="international_toggle"> {{ inter_text }}</span>
                    </div>
                </div>
                <button class="nda_submit" @click="nda_enterInfo_submit">Submit</button>
            </div>
            <div class="nda_phone_style" :class="{nda_checkPhone: nda_checkPhone}">
                <div class="input_wrap">
                    <input v-model="mfaPhone" type="text" class="input_black" placeholder=' ' maxlength="6" required/>
                    <label class="label_black nda_label">Verification Code Sent To Phone.</label>
                </div>
                <button class="nda_submit" @click="nda_checkPhone_submit">Submit</button>
            </div> 
        </div>
    </div>
</template>

<script setup>
import { ref } from "vue"
import { useFocus } from '@vueuse/core'

// sleep time expects milliseconds
function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}




const props = defineProps(['investment'])
const nda_completed = useCookie('nda_completed', {default:()=> false, watch:true, maxAge:93600})
const nda_enterInfo = ref(false)
const nda_checkPhone = ref(true)
const name = ref('')
const email = ref('')
const phone = ref('')
const mfaPhone = ref('')
const message = ref('')
const config = useRuntimeConfig()




const nda_scale = ref(0)
const nda_opacity = ref(0)
const nda_display = ref('block')
sleep(2000).then(() => { nda_scale.value = 1; nda_opacity.value = 1;})
watch(nda_completed, (newX) => {
  if(newX == true){
    nda_scale.value = 0
    nda_opacity.value = 1
    nda_display.value = 'none'
  }
})

onMounted(() => {
    if (nda_completed.value == true){
        nda_scale.value = 0
        nda_opacity.value = 1
        nda_display.value = 'none'
    }
})




const is_international = ref(false)
const is_international_color = ref('#1b91ebb3')
const inter_text = ref('International ?')
const inter_margin = ref('55%')
        

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
}}

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
        sleep(800).then(() => { inter_opacity.value = 1, inter_margin.value = '78%' })
} else{
        is_international_color.value = '#1b91ebb3'
        phone.value = '+1 ('
        inter_text.value = 'International ?'
        phone_focused.value.focus()
        sleep(1110).then(() => {show_international.value = true})
        sleep(800).then(() => { inter_opacity.value = 1, inter_margin.value = '65%' })
}
}

const show_international = ref(false)
const inter_opacity = ref(0)
const phone_focused = ref()
const verification_sent = ref(false)
const { focused } = useFocus(phone_focused)

watch(focused, (focused) => {
  if (focused) {
    show_international.value = true
    sleep(10).then(() => { inter_opacity.value = 1, inter_margin.value = '65%' })
  }
  else{
    sleep(1100).then(() => {show_international.value = false})
    sleep(800).then(() => { inter_opacity.value = 0, inter_margin.value = '55%' })
  }
})






// ---------------------------- API Calls ------------------------------ >
// ---------------------------- API Calls ------------------------------ >
// ---------------------------- API Calls ------------------------------ >

function nda_enterInfo_submit() {
    message.value = ''
    fetch(`${config.flask_url}/api/nda/enterInfo/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        // credentials: 'include',
        body: JSON.stringify({name: name.value, email: email.value, phone_number: phone.value, investment: props.investment})
    })
    .then((response) => response.json())
    .then((data) => {
        message.value = data.message;
        if (data.status == "contactVerified") {
            nda_enterInfo.value = true
            nda_checkPhone.value = true
            nda_completed.value = true
            verification_sent.value = false
        } else if (data.status == "contactAdded") {
            nda_enterInfo.value = true
            nda_checkPhone.value = false
            verification_sent.value = true
        }
    })
    .catch(error => {
        message.value = error;
        alert("Error")
        console.error('There was an error!', error);
    });
}

function nda_checkPhone_submit() {
    message.value = ''
    fetch(`${config.flask_url}/api/nda/enterPhoneMFA/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({phone_number: phone.value, investment: props.investment, mfa_code: mfaPhone.value})
    })
    .then((response) => response.json())
    .then((data) => {
        message.value = data.message;
        verification_sent.value = false
        if (data.status == "success")  {
            nda_checkPhone.value = true
            nda_completed.value = true
        }
    })
    .catch(error => {
        message.value = error;
        console.error('There was an error!', error);
    });
}
</script>


<style scoped>

.nda_message{
    margin-left:5%;
    display: flex;
    justify-content: center;
    align-items: center;
    color:rgb(25, 120, 237);
    margin-top:5%
}
.nda_label{
    margin-left:0% !important;
    font-size:15px

}

.label_black{
    margin-left:-7%
}

.nda_completed{
    display:none !important
}

.nda_enterInfo{
    display:none !important
}

.nda_checkPhone{
    display:none !important
}




.nda_modal{
    background-color: rgba(0, 0, 0, 0.2);
    position: fixed;
    z-index:200;
    height:100vh;
    width:100vw;
    top:0;
    left:0;
    backdrop-filter: blur(20px);
    display:v-bind(nda_display);
    opacity:v-bind(nda_opacity);
    transition: all .7s ease;
}

.nda_modal_container{
    background-color: #000;
    width:60%;
    height:500px;
    margin-left:20%;
    margin-top:10%;
    border-radius: 20px;
    padding: 20px;
    border:1px solid #fff;
    overflow-y: scroll;
    display:v-bind(nda_display);
    opacity:v-bind(nda_opacity);
    transform: scale(v-bind(nda_scale));
    transition: transform .7s ease, opacity .2s ease;
}

.nda_modal_container::-webkit-scrollbar {
  width: 5px !important;
  border-radius: 10px !important;
}

.nda_modal_container::-webkit-scrollbar-thumb {
  background: rgba(0, 149, 255, 1) !important;
  border-radius: 10px !important;
}

.nda_title{
    color: #fff;
    margin-top: 3%;
    width:100%;
    text-align:center;
    margin-bottom:85px
}

.nda_phone_style{
    margin-top:10%;
    width:50%;
    margin-left:25%;
}

.nda_text{
    width:60%;
    margin-left:20%;
    text-align:center;
    margin-top:-7%;
    line-height:1.25;
    font-size:15px
}

.nda_input{
    width:80%;
    margin-left:10%;
    height:40px;
    border-bottom: 1px solid #fff;
    background-color: #181818;
    color: #fff;
    padding-left: 10px;
    font-size:20px;
    margin-top:5%
}

.input_grid{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-gap: 10px;
    margin-top: 2.5%;
}

.nda_submit{
    width:65%;
    margin-left:17.5%;
    margin-top:9%;
    height:35px;
    background-color:rgb(25, 120, 237) ;
    color: #fff;
    padding-left: 10px;
    cursor: pointer;
    font-size:16px;
    border-radius:50px;
    border:#fff solid 0px;
    box-shadow: 0px 5px 12px rgba(25, 120, 237, .3);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
    display: flex;
    justify-content: center;
    align-items: center;
}

.nda_submit:hover{
    box-shadow: 0px 10px 15px rgb(25, 120, 237, .5);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
}



.international_toggle{
    font-size:10%;
    color: v-bind(is_international_color);
    margin-left:v-bind(inter_margin);
    margin-top:.9%;
    word-spacing: .05rem;
    cursor:pointer;
    position:absolute;
    opacity:v-bind(inter_opacity);
    transition: all .5s ease-in-out;
}



@media only screen and (min-width: 0px) and (max-width: 380px) {
    .label_black{
        margin-left:0%;
        margin-top:-5%
    }

}

@media only screen and (min-width: 380px) and (max-width: 410px) {
    .label_black{
        margin-left:0%;
        margin-top:-.5%
    }

}


@media only screen and (min-width: 410px) and (max-width: 576px) {

    .label_black{
        margin-left:0%;
        margin-top:0%
    }
}



@media only screen and (min-width: 0px) and (max-width: 576px) {
    
    .nda_modal_container{
        width:80%;
        height:65vh;
        margin-left:5%;
        margin-top:22%;
    }
    
    .nda_text{
        width:60%;
        margin-left:20%;
        text-align:center;
        margin-top:-13%;
        line-height:1.25;
        font-size:15px
    }
    
    .nda_phone_style{
    margin-top:20%;
    width:100%;
    margin-left:0%
}


    
    .input_grid{
        margin-top: 10%;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(3, 1fr);
        grid-row-gap: 18px;
    }
    

    .nda_submit{
        width:60%;
        margin-left:20%;
        margin-top:13%;
        height:30px;
        cursor: pointer;
        font-size:15px;
        border-radius:50px;
    }
    
    
}

@media only screen and (min-width: 576px) and (max-width: 768px) {
    
    .nda_modal_container{
        width:80%;
        height:530px;
        margin-left:6%;
        margin-top:18%;
    }
    
    .nda_text{
        width:60%;
        margin-left:20%;
        text-align:center;
        margin-top:-7%;
        line-height:1.25;
        font-size:15px
    }

    .label_black{
        margin-left:5%;
        margin-top:0%
    }
    

    
    .input_grid{
        margin-top: 3%;
        width:90%;
        margin-left:5%;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(3, 1fr);
        grid-row-gap: 18px;
    }
    
    .nda_submit{
        width:60%;
        margin-left:20%;
        margin-top:7.5%;
        height:30px;
        cursor: pointer;
        font-size:15px;
        border-radius:50px;
    }
    
    
}

@media only screen and (min-width: 768px) and (max-width: 992px) {
    
    .nda_modal_container{
        width:70%;
        height:400px;
        margin-left:12%;
        margin-top:15%;
    }
    
    .nda_text{
        width:60%;
        margin-left:20%;
        text-align:center;
        margin-top:-7%;
        line-height:1.25;
        font-size:15px
    }
    

    
    
    .input_grid{
        margin-top: 3%;
        width:90%;
        margin-left:5%
    }
    
    .nda_submit{
        width:60%;
        margin-left:20%;
        margin-top:7.5%;
        height:30px;
        cursor: pointer;
        font-size:15px;
        border-radius:50px;
    }
    
    
    
}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
    .nda_modal_container{
        width:70%;
        height:450px;
        margin-left:13%;
        margin-top:15%;
    }
    
}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
    
    
    .nda_title{
        font-size: 300%;
    }
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
    
    .nda_submit{
        margin-top:5%;
    }
    
}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
    .nda_submit{
        margin-top:5%;
    }
}






</style>