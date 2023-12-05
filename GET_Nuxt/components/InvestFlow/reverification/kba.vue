<template>

    <div>


        <div class="loader_container" v-if="start_loader">
<InvestFlowLoadersApiLoader/>
   </div>

    
        
        <div class="modal_container" :class="{modal_hide_anim: modal_exit_anim, modal_hide_disp: modal_exit_display}">
        <div class="modal_popup" :class="{modal_bix_hide_anim: modal_exit_anim}" ref="modal">
            <!-- <div @click="modal_leave" class="modal_exit">
                <div class="horizontal_line"></div>
                <div class="vertical_line"></div>
            </div> -->




<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->
<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->





<div class="form_container">

    <h5 class="timer">{{ kba_finalTime }}</h5>
<p class="reverify_text" v-if="!kba_started">Our KYC partner requires additional information to verify your identity. </p>
<p class="kba_instructions" v-if="!kba_started">Once you click start, you will have 1 attempt and 2 minutes to answer at least 3 out of the 4 security questions. <span class="designation_hover" @mouseover="designation_show = true">?</span></p>
<p class="kba_small">If you do not pass this KBA step then you will be required to upload identifying documents</p>

<p class="designation_text" :class="{designation_show: designation_show}" @mouseleave="designation_show = false">
    This verification process utilizes a technique called Knowledge-based authentication, commonly referred to as KBA. KBA is a method of authentication which seeks to prove the identity of an individual. KBA requires the knowledge of private information of the individual to prove that the person providing the identity information is the owner of the identity. Questions are compiled from public and private data such as marketing data, credit reports or transaction history. These questions are also known as “out of wallet” questions which are dynamically generated on the spot.
    <br><br>
    GET Equity Partners acts strictly as a pass through application for the data displayed in this process. We do not store any of the data provided by our KYC partner.
</p>

<div v-if="!kba_started" class="kba_start_button"  @click="start_kba">Start KBA</div>






<div v-if="kba_started" class="form_grid">





<div class="input_wrap">
    <!-- <p class="kba_question">{{ value.text }}</p> -->
            <select  v-model="question_1" required class="select_black">
                <option value="" disabled selected hidden></option>
                <option v-for="(v, k) in kba_questions[0].answers" :value="v.id" >{{ v.text }}</option>
            </select>
                <label class="label_black label_edit" >{{ kba_questions[0].text }}</label>
</div>

<div class="input_wrap">
    <!-- <p class="kba_question">{{ value.text }}</p> -->
            <select  v-model="question_2" required class="select_black">
                <option value="" disabled selected hidden></option>
                <option v-for="(v, k) in kba_questions[1].answers" :value="v.id" >{{ v.text }}</option>
            </select>
                <label class="label_black label_edit" >{{ kba_questions[1].text }}</label>
</div>

<div class="input_wrap">
    <!-- <p class="kba_question">{{ value.text }}</p> -->
            <select  v-model="question_3" required class="select_black">
                <option value="" disabled selected hidden></option>
                <option v-for="(v, k) in kba_questions[2].answers" :value="v.id" >{{ v.text }}</option>
            </select>
                <label class="label_black label_edit" >{{ kba_questions[2].text }}</label>
</div>

<div class="input_wrap">
    <!-- <p class="kba_question">{{ value.text }}</p> -->
            <select  v-model="question_4" required class="select_black">
                <option value="" disabled selected hidden></option>
                <option v-for="(v, k) in kba_questions[3].answers" :value="v.id" >{{ v.text }}</option>
            </select>
                <label class="label_black label_edit" >{{ kba_questions[3].text }}</label>
</div>





        <div class="next_button" @click="kba_submit">Submit</div>

</div>



</div>





<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->
<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->


        </div>
    </div>
    
    </div>
    </template>
    
    
    
    
    
    <script setup>

    const config = useRuntimeConfig()

   const designation_show = ref(false)


    const investing_as = useCookie('investing_as')
    const investor_ID = useCookie('investor_ID')
    const dwolla_customer_status = useCookie('dwolla_customer_status')
    const dwolla_beneficial_owner_status = useCookie('dwolla_beneficial_owner_status')
    const documents_uploaded = useCookie('documents_uploaded')
    const start_loader = ref(false);


const kba_started = ref(false)
const kba_questions = ref()
const kba_url = ref()
const question_1 = ref('')
const question_2 = ref('')
const question_3 = ref('')
const question_4 = ref('')


    // -------------------------------------------------- GET KBA -------------------------------------------------- //
        // -------------------------------------------------- GET KBA -------------------------------------------------- //
            // -------------------------------------------------- GET KBA -------------------------------------------------- //




            function start_kba() {
                start_timer()
                kba_started.value = true;
    fetch(`${config.flask_url}/api/dwolla_reverification/kba/`, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({investor_ID:investor_ID.value, kba_action:'start',})
})
.then((response) => response.json())
.then((data) => {

    if (data.status == 'kba_questions_error'){
        dwolla_customer_status.value = data.dwolla_customer_status,
        dwolla_beneficial_owner_status.value = data.dwolla_beneficial_owner_status,
        start_loader.value = false;
        alert('Error')
        modal_leave()
        sleep(700).then(() => { window.location.reload(); });
    } else {
    console.log('Success:', data.message);
    kba_questions.value = data.kba_questions,
    kba_url.value = data.kba_url
    }
})
.catch(error => {
    start_loader.value = false;
    modal_leave()
        alert('Error')
        console.error('There was an error!', error);
}); }



function kba_submit(){
    start_loader.value = true;
var count = 0
const answers = []
    for (const question of kba_questions.value) {
        var q_id = question.id
  if (count == 0) {
      answers.push({questionId:q_id, answerId:question_1.value})
  } else if (count == 1) {
    answers.push({questionId:q_id, answerId:question_2.value})
  } else if (count == 2) {
    answers.push({questionId:q_id, answerId:question_3.value})
  } else if (count == 3) {
    answers.push({questionId:q_id, answerId:question_4.value})
  }
  count += 1
}

    
    fetch(`${config.flask_url}/api/dwolla_reverification/kba/`, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({investor_ID:investor_ID.value, kba_action:'submit', kba_url_return:kba_url.value, kba_answers:answers})
})
.then((response) => response.json())
.then((data) => {
    console.log('Success:', data.message);
    dwolla_customer_status.value = data.dwolla_customer_status,
    dwolla_beneficial_owner_status.value = data.dwolla_beneficial_owner_status
    
    modal_leave()
    start_loader.value = false;
    sleep(700).then(() => { window.location.reload(); });
    

})
.catch(error => {
    start_loader.value = false;
    modal_leave()
    sleep(700).then(() => { window.location.reload(); });
        alert('Error')
        console.error('There was an error!', error);
}); }




            function str_pad_left(string, pad, length) {
  return (new Array(length + 1).join(pad) + string).slice(-length);
}



const kba_timer = ref(118)
const kba_finalTime = ref('')
const minutes = ref()
const seconds = ref()

function start_timer() {
    setInterval(() => {
  if (kba_timer.value === 0) {
    kba_submit()
    return     
  } else {
    kba_timer.value--
  }
    minutes.value = Math.floor(kba_timer.value / 60);
    seconds.value = kba_timer.value - minutes.value * 60;       
    // milli_seconds.value = kba_timer.value - minutes.value * 60;       
    kba_finalTime.value = str_pad_left(minutes.value, '0', 2) + ':' + str_pad_left(seconds.value, '0', 2);     
}, 970)

}




    // -------------------------------------------------- MODAL -------------------------------------------------- //
    
    const modal_exit_anim = ref(true)
    const modal_exit_display = ref(true)
    
    
    
    // sleep time expects milliseconds
    function sleep (time) {
      return new Promise((resolve) => setTimeout(resolve, time));
    }
    
    
    
    
    function modal_leave(){
        modal_exit_anim.value = true
        sleep(1100).then(() => {
        modal_exit_display.value = true
        });
    }
    
    const modal = ref(null)
    

    
    // open modal on load
    sleep(500).then(() => {      // Do something after the sleep!
        modal_exit_display.value = false
        sleep(100).then(() => {
        modal_exit_anim.value = false
        });
    });
    
    
    

    
    </script>
    
    
    
    
    <style scoped>
    


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
    .label_edit{
        margin-left:5%
    }
.kba_question{
    color:#fff;
    font-size:12px
}

    .timer{
        color:rgb(25, 120, 237);
        text-align:center;
        margin-top:-1%;
    }
    .kba_instructions{
        width:70%;
        margin-left:15%;
        text-align:center
    }

    .kba_small{
        width:70%;
        margin-left:15%;
        text-align:center;
        font-size:11px;
    }
    .reverify_text{
    color:#fff;
    text-decoration: underline;
    text-decoration-color: rgba(255, 0, 0, 0.5);
  text-underline-offset: 2px;
  text-decoration-thickness: 1px;
  text-decoration-skip-ink: none;
    width:60%;
    margin-left:20%;
    text-align: center;
    margin-bottom:8%
    }

    .background_blur{
    background-color: rgba(255, 255, 255, 0.005);
    position: fixed;
    width: 100vw;
    height: 100vh;
    z-index: 0;
    opacity: 1;
    backdrop-filter: blur(4px);
    left:0;
    top:0
}


.next_button{
    width:30%;
    padding:10px 20px;
    background-color:rgb(25, 120, 237);
    color:#fff;
    text-align: center;
    border-radius:100px;
    cursor: pointer;
    margin-top:10%;
    margin-left:34%;
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




.form_container{
        background-color: #000;
        border-radius:50px;
        padding-top:10px;
        padding-bottom:10%;
        z-index: 10000000000000;
        position:relative;
        display: block;
    }





    .form_grid{
    display: grid;
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(4, 1fr);
grid-column-gap: 0px;
grid-row-gap: 0px;
z-index: 10;
width:100%;
}



.form_title{
    color:#fff;
    margin-left:14%;
    z-index:10;
    position: relative;
    display: block;
    margin-top:50px;
    mix-blend-mode: normal;
}







.designation_text{
    color:#000;
    width:60%;
    margin-left:14.25%;
    margin-top:0%;
    opacity:0;
    position:absolute;
    background-color:#fff;
    z-index:5;
    padding:6%;
    border-radius:10px;
    border: 4px solid rgba(25, 120, 237, 0.7);
    mix-blend-mode: normal;
    display: inline-block;
    transition: all .35s ease-in-out;
    visibility: hidden;
    font-size:12px
}

.designation_show{
    margin-top:-17%;
    opacity:1;
    visibility: visible;
    transition: all .35s ease-in-out;
}
.designation_hover{
    font-size:13px;
    padding:2px 7px;
    border: 1px solid rgba(255,255,255, 0.4);
    color: rgba(255,255,255, 0.4);
    border-radius:100%;
    cursor:pointer;
    transition: all .35s ease-in-out;
}

.designation_hover:hover{
    background-color:rgba(25, 120, 237, 0.3);
    color:#fff;
    transition: all .35s ease-in-out;
}


.kba_start_button{
    width:30%;
    padding:10px 20px;
    background-color:rgb(25, 120, 237);
    color:#fff;
    text-align: center;
    border-radius:100px;
    cursor: pointer;
    margin-top:10%;
    margin-left:34%;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}






    /* ------------------------------------ Modal ------------------------------------ */
        /* ------------------------------------ Modal ------------------------------------ */
            /* ------------------------------------ Modal ------------------------------------ */



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
        background-color:rgba(255, 255, 255, 0.1);
        position:fixed;
        top:0;
        left:0;
        z-index:1;
        display:flex;
        justify-content:center;
        align-items:center;
        backdrop-filter: blur(10px);
        transition: all 1s ease-in-out;
        opacity: 1;
    
    }
    .modal_popup{
        width:85%;
        height:75vh;
        background-color:rgb(0, 0, 0);
        z-index:10;
        border-radius:20px;
        margin-top:20px;
        border: rgba(25, 120, 237, 0.499) solid 2px;
        transition: all 1s ease-in-out;
        overflow-x:scroll
    }

    .modal_popup::-webkit-scrollbar {
  width:8px !important;
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
        margin-top:10%;
        width:80%;
        text-align:center
    }
    
    .login_redirect{
        width:40%;
        height:50px;
        background-color:rgb(25, 120, 237) ;
        margin-left: 30%;
        margin-top:7%;
        border-radius:100px;
        border:#fff solid 0px;
        cursor:pointer;
        font-size:20px;
        color:#fff;
          box-shadow: 0px 7px 10px rgb(25, 120, 237, .3);
      transition: outline 12s ease 1s;
    }
    
    .login_redirect:hover{
      box-shadow: 0px 10px 15px rgb(25, 120, 237, .5);
      transform: translateY(-3px);
      outline: 3px solid rgba(19, 218, 218, 0.6);
      transition: outline 12s ease 1s;
    } 
    
    
    .modal_exit{
        margin-top:20px;
        margin-left:90%;
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
    
    @media only screen and (min-width: 576px) and (max-width: 768px) {
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