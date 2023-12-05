<template>
    


    <Teleport to="body">
        <MainTransition ref="main_tansition"/>
    <div class="modal_container" :class="{modal_hide_anim: modal_exit_anim, modal_hide_disp: modal_exit_display}">
            <div class="modal_popup" :class="{modal_bix_hide_anim: modal_exit_anim}" ref="modal_ref">
                <div @click="modal_leave" class="modal_exit">
                <div class="horizontal_line"></div>
                <div class="vertical_line"></div>
            </div>


            <div class="modal_grid">

                <div class="modal_img_container">
                <div class="modal_img"  :style="{ transform: `scale(${img_scale})` }">
               <!-- <img class="modal_img" :style="{ transform: `scale(${img_scale})` }" src="~/assets/content/wallstreet/modal_img.jpg"> -->
               <video class="video_style" poster="~/assets/content/homepage/homepage_poster.png" autoplay muted playsinline loop>
                    <source src="~/assets/content/homepage/home_333.mp4" type="video/mp4">
                </video>
                <p class="reserve_text">1 Step Reserve</p>
                <p class="reserve_text">Reserve For Free, No Payment Required.</p>
            </div>

        </div>

    
        <div>
            <div class="loader_container" v-if="start_loader">
            <InvestFlowLoadersApiLoader/>
        </div>
            <div class="modal_info" v-if="!start_loader">
                <h6 class="modal_text">Reserve a Seat</h6>
                <p class="modal_subtitle">Next AI Fund</p>
    
    
                <div class="input_wrap first_input">
                <input v-model="first_name" type="text" class="input_white input_edit" placeholder=' ' required/>
                <label class="label_white label_edit" >First Name</label>
              </div>

              <div class="input_wrap">
                <input v-model="last_name" type="text" class="input_white input_edit" placeholder=' ' required/>
                <label class="label_white label_edit" >Last Name</label>
              </div>

              <div class="input_wrap">
                <input v-model="email" type="text" class="input_white input_edit" placeholder=' ' required/>
                <label class="label_white label_edit" >Email</label>
              </div>

              <div class="input_wrap">
                <input ref="phone_focused" @keyup="remove_chrs" @keypress="onPhoneKeyPress" maxlength="17" v-model="phone" class="input_white input_edit" placeholder=' ' required/>
                <label class="label_white label_edit">Phone Number</label>
                <span v-if="show_international" class="international_toggle" @click="international_toggle"> {{ inter_text }}</span>
         </div>


         <div class="input_wrap">
            <input v-model="investment_amount" @keyup="format_val" class="input_white input_edit" placeholder=' ' required/>

                <label class="label_white label_edit">Desired Investment Amount</label>

        </div>


        <div class="input_wrap">
            <select v-model="is_accredited"  class="select_white">
                <option value="" disabled selected hidden></option>
                <option value="yes">Yes</option>
                <option value="no">No</option>
            </select>
                <label class="label_white label_edit">Are you an Accredited Investor:</label>
        </div>
    
              <div @click="submit_form" class="modal_submit_button">Submit</div>
    
            </div>
        </div>

        </div>


        <div class="modal_info_2" v-if="reserve_submitted">
            <h4 class="info_2_title">Congratulations!</h4>
            <p class="subtitle_2">Your seat is reserved for the Next AI Fund</p>
            <p class="reserve_text_2">You can now use the Calend.ly link below to set up a call to speak directly with a manager if you would like to learn more about early access opportunities (or for a little more info about the fund)</p>

            <div @click="link_to_calendly" class="modal_submit_button_2">Let's Talk</div>
            <p @click="modal_leave" class="no_thanks_text">No thanks, please let me know when the Next Fund is open.</p>
            </div>

        </div>

    
            </div>

    
        <div class="plaid_blur" v-if="plaid_blur"></div>
    
    </Teleport>
    
    </template>
    
    
    <script setup>
        import { gsap } from 'gsap'
    
    
    const config = useRuntimeConfig()
    const modal_exit_anim = ref(true)
    const modal_exit_display = ref(true)
    const start_loader = ref(false)

    const img_scale = ref(2)

    const reserve_submitted = ref(false)
    const cookie_options = {default:()=> '', watch:true, maxAge:1800}

    const investment_amount = useCookie('investment_amount', cookie_options)
    const is_accredited = useCookie('is_accredited', cookie_options)


    function format_val() {
        investment_amount.value  = '$' + investment_amount.value.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",")
}



    
        
        
        // sleep time expects milliseconds
        function sleep (time) {
          return new Promise((resolve) => setTimeout(resolve, time));
        }
        
    function open_modal(){
        modal_exit_display.value = false
            sleep(100).then(() => {
                img_scale.value = 1
            modal_exit_anim.value = false
            });
    }
    
    function modal_leave(){
            modal_exit_anim.value = true
            sleep(1100).then(() => {
                img_scale.value = 2
            modal_exit_display.value = true
            start_loader.value = false;
            plaid_blur.value = false;
            });
        }
    
    
        defineExpose({
            open_modal,
            modal_leave
    })
    
    
    


    
    function submit_form(){
        
        const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if(!re.test(String(email.value).toLowerCase())) {
        alert('Email is not valid!');
    } else {
        
    
    start_loader.value = true
    fetch(`${config.flask_url}/api/reserve_seat/`, {
        method: 'POST',
        mode: 'cors',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
          body: JSON.stringify({first_name:first_name.value, last_name: last_name.value, email:email.value, phone:phone.value, investment_amount:investment_amount.value, is_accredited:is_accredited.value, fund_reserved:"next_ai"})
      })
      .then((response) => response.json())
      .then((data) => {
           if (data.status == 'success_reserved'){
            move_form() 
           } else {
            alert(data.message)
           }
           sleep(2000).then(() => { start_loader.value = false})
    
      })
      .catch(error => {
          console.error('There was an error!', error);
      });
    
        }

    }
    
    
    const modal_ref = ref(null)
    function move_form(){
        reserve_submitted.value = true
        gsap.to('.modal_grid', 1, {
    xPercent: -100,
  });
  sleep(10).then(() => {
  gsap.to('.modal_info_2', .5, {
    autoAlpha:1,
    opacity: 1,
    yPercent: -2.5,
    delay: .5
  });
});


// scroll to top of the modal
modal_ref.value.scrollTop = 0;


    }










const most_recent_fund_page = useCookie('most_recent_fund_page', cookie_options)
most_recent_fund_page.value = 'next_ai'
const first_name = useCookie('first_name', cookie_options)
const last_name = useCookie('last_name', cookie_options)
const email = useCookie('email', cookie_options)
const phone = useCookie('phone', cookie_options)


    const is_international = ref(false)
const is_international_color = ref('#1b91ebb3')
const inter_text = ref('International ?')
const inter_margin = ref('10%')


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
        sleep(800).then(() => { inter_opacity.value = 1, inter_margin.value = '30%' })
} else{
        is_international_color.value = '#1b91ebb3'
        phone.value = '+1 ('
        inter_text.value = 'International ?'
        phone_focused.value.focus()
        sleep(1110).then(() => {show_international.value = true})
        sleep(800).then(() => { inter_opacity.value = 1, inter_margin.value = '10%' })
}
}

const show_international = ref(false)
const inter_opacity = ref(0)
const phone_focused = ref()
const { focused } = useFocus(phone_focused)

watch(focused, (focused) => {
  if (focused) {
    show_international.value = true
    sleep(10).then(() => { inter_opacity.value = 1, inter_margin.value = '20%' })
  }
  else{
    sleep(1100).then(() => {show_international.value = false})
    sleep(800).then(() => { inter_opacity.value = 0, inter_margin.value = '10%' })
  }
})

    


function link_to_calendly(){

    const newWindow = window.open("https://calendly.com/get-resources/investment?month=2023-07", '_blank');
    if (newWindow) {
        newWindow.focus();
    } else {
        window.location.href = "https://calendly.com/get-resources/investment?month=2023-07";
    }

}
    
    
    
    </script>
    
    
    
    <style scoped>

.info_2_title{
    color: #000;
    text-align: center;
}

.subtitle_2{
    color: #ff0aff;;
    text-align: center;
    margin-top:-8%;
    font-weight: 800;
    margin-left:0%;
    width:100%
}
.reserve_text_2{
    color:#000;
    text-align: center;
    margin-top:10%;
    width:70%;
    margin-left:15%
}

.no_thanks_text{
    color:#3770ff;
    text-align: center;
    margin-top:15%;
    width:50%;
    margin-left:25%;
    text-decoration: underline;
    cursor:pointer;
}

.international_toggle{
    font-size:60%;
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


.modal_info_2{
        opacity:0;
        position:relative;
        margin-top:-80%;
        width:60%;
        margin-left:20%;
        margin-bottom:10%
    }
    
    
    .reserve_text{
        color:#fff;
        text-align: center;
        width:80%;
    }


    .input_edit{
      color:#000;
      border-bottom: #000 1px solid;
    }
    
     .input_edit:focus~ .label_edit,
      .input_edit:valid ~ .label_edit{
        top: -1.75vw;
        left: 3.3vw;  
        font-size: 1vw; 
        color: #ff0aff;
      }

      .input_wrap .select_white:focus~ .label_white,
  .input_wrap .select_white:valid ~ .label_white{
    top: -1.75vw;
    left: 4vw;  
    font-size: 1vw;
    color: #ff0aff;
  }
    
    .label_edit{
      margin-left:-3%
    }
    /* 
    // ------------------------------- Modal  ---------------
    // ------------------------------- Modal  ---------------
    // ------------------------------- Modal  --------------- 
    */
    


    .modal_grid{
        display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 1fr;
grid-column-gap: 0px;
grid-row-gap: 0px;
margin-top:-60px;
    }

    .modal_img{
        width:100%;
        height:65vh;
        object-fit: cover;
        object-position: 50% 50%;
        transition: all 1s ease-in-out .25s;
        background-color:#000;
        display:flex;
        justify-content:center;
        align-items:center;
        flex-direction: column;
        z-index:5
    }


    .modal_img_container{
        background-color: #000;
        height:115%;
    }


    .video_style{
        width:85%; 
        margin-top:2.5%
    }
    
    
    
    .plaid_blur{
        position:fixed;
        top:0;
        left:0;
        height:100vh;
        width:100vw;
        background-color:rgba(193, 255, 237, 0.08);
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
            background-color:rgba(111, 151, 140, 0.2);
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
            width:65%;
            height:65vh;
            background-color:#fff;
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
    
        
        .modal_info{
            font-size:30px;
            font-weight:600;
            color:#fff;
            margin-left:10%;
            margin-top:3%;
            width:80%;
            text-align:center
        }
        
        .modual_buttons{
            width:40%;
            height:35px;
            background-color:green;
            margin-left: 30%;
            margin-top:3.5%;
            border-radius:100px;
            border:#fff solid 0px;
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
    
    
        .modal_submit_button{
        width:70%;
        height:40px;
        background-color:#ff0aff;
        margin-left: 15%;
        margin-top:25%;
        border-radius:100px;
        border:#fff solid 0px;
        font-size:16px;
        line-height:40px;
        color:#fff;
        box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
        outline: 0px solid rgba(19, 218, 218, 0.6);
        transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
        text-align: center;
        cursor:pointer

    }
    
    
    .modal_submit_button:hover{
      box-shadow: 0px 10px 15px rgb(255, 10, 255, .3);
      transform: translateY(-3px);
      outline: 3px solid rgba(19, 218, 218, 0.6);
      transition: outline 12s ease 1s;
    } 

    .modal_submit_button_2{
        width:50%;
        height:50px;
        background-color:#ff0aff;
        margin-left: 25%;
        margin-top:12%;
        border-radius:100px;
        border:#fff solid 0px;
        font-size:16px;
        line-height:40px;
        color:#fff;
        box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
        outline: 0px solid rgba(19, 218, 218, 0.6);
        transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
        text-align: center;
        cursor:pointer
    }
    
    
    .modal_submit_button_2:hover{
      box-shadow: 0px 10px 15px rgb(255, 10, 255, .3);
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
        }
        
        
        .modal_exit{
            margin-top:10px;
            margin-left:93%;
            z-index: 10;
            position: relative;
            width:50px;
            height:50px;
            cursor: pointer;
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
            background-color:#000;
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
            background-color:#000;
            transform: rotate(45deg);
            position: absolute;
        }
        
    
        .modal_text{
            font-size:120%;
            color:#fff;
            margin-left:5%;
            margin-top:25%;
            width:90%;
            text-align:center;
            line-height:1.3;
            margin-bottom:0
        }

        .modal_subtitle{
            color:#ff0aff;
            font-size:18px;
            margin-top:0px;
            filter: invert(1);
        }
        
        
        
        @media only screen and (min-width: 0px) and (max-width: 576px) {
        
            .modal_popup{
            width:90%;
            height:70%;
        }
        
        .modal_exit{
            margin-top:10px;

            margin-left:80%;
            width:40px;
            height:40px;
        }

        .info_2_title{
            color: #000;
            text-align: center;
            margin-left:15%
        }

        .subtitle_2{
            color: #ff0aff;;
            text-align: center;
            margin-top:-8%;
            font-weight: 800;
            margin-left:20%
        }
        .reserve_text_2{
            color:#000;
            text-align: center;
            margin-top:10%;
            width:100%;
            margin-left:20%
        }

        .no_thanks_text{
            color:#3770ff;
            text-align: center;
            margin-top:15%;
            width:90%;
            margin-left:25%;
            text-decoration: underline;
            cursor:pointer;
        }


        .modal_submit_button{
            width:80%;
        margin-left: 30%;
    }

    .modal_submit_button_2{
        width:80%;
        margin-left: 30%;
    }

    .modal_info_2{
        margin-top:-280%;
        width:70%;
        margin-left:0%;
        margin-bottom:10%
    }
    


    .modal_grid{
        display: grid;
grid-template-columns: 1fr;
grid-template-rows: repeat(2, 1fr); 
    }

    .video_style{
        width:60%; 
        margin-top:0%;
        margin-bottom:5%
    }

    .reserve_text{
        margin-top:-2%
    }

    .modal_img_container{
        background-color: #000;
        height:65%;
    }

    .modal_img{
        height:45vh;
    }

        .input_edit:focus~ .label_edit,
      .input_edit:valid ~ .label_edit{
        top: -4.25vw;
        left: 9.75vw;  
        font-size: 3vw; 
        color: #ff0aff;
      }

      .input_wrap .select_white:focus~ .label_white,
  .input_wrap .select_white:valid ~ .label_white{
    top: -4.25vw;
    left: 9.75vw;  
    font-size: 3vw; 
    color: #ff0aff;
  }

  .first_input{
    margin-top:0%
  }

  .modal_submit_button{
        margin-left: 10%;
        margin-top:17%;
        margin-bottom:20%
    }

    .info_2_title{
    font-size:10vw
}

.input_wrap{
            margin-top:15%

        }
        
        .international_toggle{
    font-size:40%;
    margin-top:1%;
    margin-left:calc(v-bind(inter_margin) + -10%);
}

        }
    

        @media only screen and (min-width: 0px) and (max-width: 385px) {
            .modal_text{
            margin-top:-50%;
        }

        .first_input{
    margin-top:30%
  }

        }

        @media only screen and (min-width: 385px) and (max-width: 576px) {

            .modal_text{
            margin-top:-45%;
        }

        .first_input{
    margin-top:30%
  }

}
    
    
    
    
        .loader_container{
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top:45%
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
    
    
    
    
    
        @media only screen and (min-width: 0px) and (max-width: 576px) {


}

@media only screen and (min-width: 576px) and (max-width: 768px) {

    .international_toggle{
    font-size:50%;
    margin-top:1%;
    margin-left:calc(v-bind(inter_margin) + -5%);
}
    .modal_info_2{
        margin-top:-125%;
        width:80%;
        margin-left:10%;
        margin-bottom:10%
    }

    .modal_exit{
            margin-left:80%;
        }

        .no_thanks_text{
            margin-top:15%;
            width:90%;
            margin-left:5%;
        }



    .modal_grid{
        display: grid;
grid-template-columns: 1fr;
grid-template-rows: repeat(2, 1fr); 
    }

    .video_style{
        width:60%; 
        margin-top:0%;
        margin-bottom:5%
    }

    .reserve_text{
        margin-top:-2%
    }

    .modal_img_container{
        background-color: #000;
        height:65%;
    }

    .modal_img{
        height:45vh;
    }

        .input_edit:focus~ .label_edit,
      .input_edit:valid ~ .label_edit{
        top: -4.25vw;
        left: 7vw;  
        font-size: 2.5vw; 
        color: #ff0aff;
      }

      .input_wrap .select_white:focus~ .label_white,
  .input_wrap .select_white:valid ~ .label_white{
    top: -4.25vw;
        left: 7vw;  
    font-size: 2.5vw; 
    color: #ff0aff;
  }

  .first_input{
    margin-top:0%
  }

  .modal_submit_button{
        margin-left: 15%;
        margin-top:17%;
        margin-bottom:20%
    }

    .info_2_title{
    font-size:7vw;
    margin-top:-315%
}

.input_wrap{
            margin-top:15%
        }

        .modal_text{
            margin-top:-45%;
        }

        .first_input{
    margin-top:30%
  }
}

@media only screen and (min-width: 768px) and (max-width: 992px) {
    .modal_info_2{
        margin-top:-125%;
        width:80%;
        margin-left:10%;
        margin-bottom:20%
    }

    .modal_exit{
            margin-left:87%;
        }

        .no_thanks_text{
            margin-top:15%;
            width:90%;
            margin-left:5%;
        }
}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
        .modal_info_2{
        margin-top:-120%;
        width:80%;
        margin-left:10%;
        margin-bottom:20%
    }

    .modal_exit{
            margin-left:87%;
        }

        .no_thanks_text{
            margin-top:15%;
            width:90%;
            margin-left:5%;
        }
}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
    .modal_info_2{
        margin-top:-110%;
        width:80%;
        margin-left:10%;
        margin-bottom:20%
    }

    .modal_exit{
            margin-left:87%;
        }

        .no_thanks_text{
            margin-top:15%;
            width:90%;
            margin-left:5%;
        }
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
    .modal_info_2{
        margin-top:-95%;
        width:80%;
        margin-left:10%;
        margin-bottom:20%
    }

    .modal_exit{
            margin-left:87%;
        }

        .no_thanks_text{
            margin-top:15%;
            width:90%;
            margin-left:5%;
        }
}

@media only screen and (min-width: 1600px) and (max-width: 2000px) {
    .modal_popup{
            height:75vh;
        }
        .modal_img{
            height:75vh;
    }

    .subtitle_2{
        margin-top:-4%
    }

    .no_thanks_text{
        margin-top:8%
    }

    .modal_info_2{
        margin-top:-85%;
        width:80%;
        margin-left:10%;
        margin-bottom:20%
    }
    
    
}

@media only screen and (min-width: 2000px) and (max-width: 5600px) {

    .modal_popup{
            height:75vh;
        }
        .modal_img{
            height:75vh;
    }


    .subtitle_2{
        margin-top:-4%
    }

    .no_thanks_text{
        margin-top:8%
    }
    
    
}
    
    
    </style>