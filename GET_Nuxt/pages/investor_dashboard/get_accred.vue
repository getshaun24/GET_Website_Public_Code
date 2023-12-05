<template>

    <div>
        <CircleTransition ref="cicle_tansition"/>


        <!-- -------------------------- modal popup --------------------------------- -->

        <div class="modal_container" :class="{modal_hide_anim: modal_exit_anim, modal_hide_disp: modal_exit_display}">
    <div class="modal_popup" :class="{modal_bix_hide_anim: modal_exit_anim}" ref="modal">
        <div @click="modal_leave" class="modal_exit">
            <div class="horizontal_line"></div>
            <div class="vertical_line"></div>
        </div>
        <h3 v-if="bank_total_qualifies" class="modal_info">Based on your provided income, you still do not meet accreditation requirements based on a monthly basis but you do meet the overall value requirements. Please make an appointment with one of our team mebers here and we can help.<br><br>Or, please re-connect another bank with Plaid, one where your total assets exceeeds $1 Million.</h3>
        <h3 v-else class="modal_info">Based on your provided income, you still do not meet accreditation requirements.<br><br>Please re-connect another bank with Plaid, one where your total assets exceeeds $1 Million.</h3>
        <div class="modal_flex">
        <div class="modal_next_button" @click="get_link_token('get_AUTH_link_token', 'get_AUTH_public_token')">Connect With Plaid</div>
    </div>
    </div>
</div>

        <!-- -------------------------- modal popup --------------------------------- -->





        <div class="plaid_blur" v-if="plaid_blur"></div>
    <div class="loader_container" v-if="start_loader">
        <div class="loader"></div>
    </div>
    
        <video class="landing_video" autoplay muted playsinline loop>
                    <source src="~/assets/content/homepage/home_333.mp4" type="video/mp4">
                </video>
    
    
    <!-- <Header/> -->
    
        <GSAPScrollSmoother>
    
            <div class="main_content_container">
    
        
                <div class="form_container">
            <div>
            <h3 class="welcome_text">Last Step</h3>
            <p class="welcome_subtext">Based on available information we need to further verify your accreditation status per these SEC <a class="link_color" target="_blank" href="https://www.sec.gov/education/capitalraising/building-blocks/accredited-investor#:~:text=Financial%20Criteria,same%20for%20the%20current%20year">guidelines</a>.<br><br>In order to streamline this process for you, we ask that you utilize the secure Plaid link to your right, so that we can safely verify your <span class="emph_underline">income or assets</span>.
                 <span class="designation_hover" @click="designation_show = true" @mouseover="designation_show = true">?</span>  </p>
        </div>
        <div class="plaid_button_move">
            <div v-if="!completed_plaid_income" class="next_button" @click="get_link_token('get_INCOME_link_token', 'get_INCOME_public_token')">Start with Income</div>
                <div class="next_button_2" @click="get_link_token('get_AUTH_link_token', 'get_AUTH_public_token')">Start with Assets</div>
            </div>

            </div>


<div ref="designation_box" class="designation_box" :class="{designation_show: designation_show}" @mouseleave="designation_show = false">
    <p class="designation_text desig_underline">The most common way to confirm your accreditation status is by meeting the requirements for income or assets.</p> 
    <p class="designation_text"><span style="font-size:10px; color:#ff9933">○</span> In order to qualify based on income, you must select all the accounts that cumulatively exceed $200,000 each year for an individual and $300,000 each year for spousal accounts, for the past two years. You must also be on track meet this level of income for the current year.</p>
    <p class="designation_text">We must verify that you have made at minimum $16,667 for every month over the past two years.</p> 
    <br>
    <p class="designation_text"><span style="font-size:10px; color:#ff9933">○</span> For qualifying via assets, you must prove that you have a net worth exceeding $1 million for an individual (excluding your personal residence). If you are an entity, you must have over $5 million in investments. <br><br>When logging into Plaid, be sure to select your main account that displays this information. We will add this amount with the account(s) previously provided.
</p>
</div>



            <div class="form_container container_gap">
            <div>
            <h5 class="backup_text">Backup Option</h5>
            <p class="backup_subtext">Instead of Plaid, you have the option to submit accreditation documents based on this SEC <a class="link_color" target="_blank" href="https://www.sec.gov/education/capitalraising/building-blocks/accredited-investor#:~:text=Financial%20Criteria,same%20for%20the%20current%20year">criteria</a>.<br><br>We do not reccomend this option as it can be timely and inconvenient.  </p>
        </div>


        <div ref="dropZoneRef" class="upload_container">
                <img @click="open" class="upload_image" src="~assets/content/dashboard/file_upload.png">
                


                <div v-if="drop_success == false">
            <div class="files_open" @click="open">Choose file</div>
                    </div>
                    <div v-else>
                        <div class="files_submit" @click="submit_file">Submit</div>
                    </div>


                <p class="drop_success">{{ dropped_file_name }}</p>
                <p class="drop_success">{{ select_file }}</p>
                <p class="show_drop_error" :class="{hide_it:!show_drop_error}">Filetype Not Supported</p>
            </div>

            </div>



            <h4 class="return_text">Contact</h4>
            <p class="return_subtext">If you have any questions or would like assistance in confirming your accreditation status, please set up an appointment via this <a class="link_color" target="_blank" href="https://calendly.com/get-resources/investment">Calandly</a>.<br>If you would like a full <u>refund</u> then please use this same Calandly link as well.</p>





        </div>

            <div class="bottom_padding"></div>
    
    
        </GSAPScrollSmoother>
    
    
    
    </div>
    
    </template>
    
    
<script setup>
import { useFileDialog } from '@vueuse/core'
import { useDropZone } from '@vueuse/core'
import { onClickOutside, useElementVisibility } from '@vueuse/core'


useHead({
  script: [{ src: "https://cdn.plaid.com/link/v2/stable/link-initialize.js", body:true, async: true, preload:true, ssr: false}],
});


// sleep time expects milliseconds
function sleep (time) {
return new Promise((resolve) => setTimeout(resolve, time));
}




const config = useRuntimeConfig()


const show_drop_error = ref(false)
const drop_success_border = ref("rgb(255, 255, 255, .05)")
const drop_success = ref(false)


const select_file = ref()
const { files, open, reset } = useFileDialog()

// single ref
watch(files, (newfiles) => {
    select_file.value = files.value[0].name
    drop_success_border.value = "green"
    drop_success.value = true
})


const dropped_file_name = ref()
const dropZoneRef = ref()
const { isOverDropZone } = useDropZone(dropZoneRef, onDrop) 
function onDrop(drop_files) {
    dropped_file_name.value = drop_files[0].name
    drop_success_border.value = "green"
    drop_success.value = true
}






const cicle_tansition = ref(null);
function transition_and_route(route_to) {
 cicle_tansition.value.animation_and_route(route_to);
}



const designation_show = ref(false)
const designation_box = ref(null)

watch(designation_show, (new_desig) => {
        if (new_desig == true) {
            sleep(1000).then(() => {
            onClickOutside(designation_box, (event) => designation_show.value = false) 
    })
}
})



const start_loader = ref(false);
const plaid_blur = ref(false);
const blur_amount = ref('0px');
const plaid_opacity = ref(0);


const cookie_options = {default:()=> '', watch:true, maxAge:1800}
const investor_ID = useCookie('investor_ID', cookie_options)
const institution_ID = useCookie('institution_ID', cookie_options)
const institution_array = useCookie('institution_array', cookie_options)
const product_public_var = useCookie('product_public_var', {default:()=> 'get_INCOME_public_token', watch:true, maxAge:1800})
const completed_plaid_income = useCookie('completed_plaid_income', {default:()=> false, watch:true, maxAge:1800})

const bank_total_qualifies = ref(false)
const link_token = ref()
const csrf_cookie = useCookie('csrf_access_token')



    function get_link_token(initialize_link_var, pub_var_val){

        product_public_var.value = pub_var_val



// -------  get link token from flask server ---------------

fetch(`${config.flask_url}/api/get_accred/get_accred_linktoken/`, {
        method: 'POST',
        mode: 'cors',
        credentials: 'include',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRF-TOKEN': csrf_cookie.value
        },
        body: JSON.stringify({'investor_ID': investor_ID.value, 'initialize_link_var':initialize_link_var})
    })
    .then((response) => response.json())
    .then((data) => {
        console.log('Success: - ', data.link_token);
        console.log('Success status: - ', data.status);
        institution_ID.value = data.institution_ID;
        institution_array.value = data.institution_array;
        open_plaid(data.link_token)

        // if(product_public_var.value == 'get_INCOME_public_token'){
        // open_plaid(data.link_token)
        // }
        
    })
    .catch(error => {
        console.error('There was an error!', error);
    });
  }


// ------------------------------- Plaid Link Token ---------------
// ------------------------------- Plaid Link Token ---------------
// ------------------------------- Plaid Link Token ---------------


function open_plaid(link_token){ 



plaid_blur.value = true;
sleep(10).then(() => { blur_amount.value = '10px', plaid_opacity.value = 1 });

const handler = Plaid.create({
token: link_token,
onSuccess: (public_token, metadata) => {

    if (metadata['institution']['institution_id'] in institution_array.value && product_public_var.value == 'get_AUTH_public_token')
    {
    alert('You entered the same institution as before, Please try again with a different institution or choose another accreditation option');
    }else {
        send_plaid_public(public_token, metadata)
     plaid_blur.value=false;}
},
onLoad: () => {},
onExit: (err, metadata) => {
blur_amount.value = '0px';
plaid_opacity.value = 0;
plaid_blur.value = false;
completed_plaid_income.value = false;
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

fetch(`${config.flask_url}/api/get_accred/get_accred_publictoken/`, {
    method: 'POST',
    mode: 'cors',
    credentials: 'include',
    headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRF-TOKEN': csrf_cookie.value
        },
    body: JSON.stringify({'public_token': public_token, 'metadata': metadata, 'investor_ID': investor_ID.value, 'institution_ID':institution_ID.value, 'product_public_var':product_public_var.value})
})
.then((response) => response.json())
.then((data) => {
    console.log('public- status', data.status);

    if(product_public_var.value == 'get_INCOME_public_token'){
        completed_plaid_income.value = true
    }
    
    if(data.status == "income_not_accredited" || data.status == "auth_not_accredited"){
        start_loader.value = false;
        plaid_blur.value = false;
        bank_total_qualifies.value = data.bank_total_qualifies
        open_accred_modal()
    } else if (data.status == "income_is_accredited" || data.status == "auth_is_accredited"){
    transition_and_route("../investor_home");
    }else{
        console.log('public- status', data.status)
    }

})
.catch(error => {
    start_loader.value = false;
    plaid_blur.value = false;
    console.error('There was an error! -- Public Token Error', error);
});
}





// <!-- -------------------------- modal popup --------------------------------- -->
// <!-- -------------------------- modal popup --------------------------------- -->

const modal_exit_anim = ref(true)
const modal_exit_display = ref(true)



function modal_leave(){
    modal_exit_anim.value = true
    sleep(1100).then(() => {
    modal_exit_display.value = true
    });
}

const modal = ref(null)


function open_accred_modal(){
    product_public_var.value = 'get_AUTH_public_token'
    // get_link_token('get_AUTH_link_token')

    modal_exit_display.value = false
    sleep(100).then(() => {
    modal_exit_anim.value = false
    });
}






// <!-- -------------------------- modal popup --------------------------------- -->
// <!-- -------------------------- modal popup --------------------------------- -->
  
    </script>
    
    <style scoped>
    


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



.main_content_container{
    width:90%;
    margin-left:5%;
    margin-top:15%;
    height:110vh
}


.form_container {
display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 1fr; 
grid-column-gap: 0px;
grid-row-gap: 20px;
margin-top:50px
}



    .landing_video{
        width: 80%;
        height: auto;
        object-fit: cover;
        z-index: -1;
        margin-left:10%;
        opacity:.09;
        position:fixed;
        top:0;
        left:0;
        margin-top:-5%
    }

    .welcome_text{
        text-align:left;
        margin-top:5%;
        position: relative;
    }
    

    .backup_text{
        text-align:left;
        margin-top:5%;
        position: relative;
        font-size:30px
    }

    .return_text{
        text-align:center;
        margin-top:20%;
        position: relative;
    }

    .welcome_subtext{
        text-align:left;
        position: relative;
        margin-top:-2%;
        width:100%;
    }

    .backup_subtext{
        text-align:left;
        position: relative;
        margin-top:-2%;
        width:100%;
        font-size:15px
    }


    .return_subtext{
        text-align:center;
        position: relative;
        margin-top:-5%;
        width:80%;
        margin-left:10%;
    }

    .link_color{
        color:rgb(25, 120, 237)
    }

    .next_button{
    width:50%;
    height:20px;
    padding:10px 20px;
    background-color:rgb(25, 120, 237);
    color:#fff;
    text-align: center;
    border-radius:100px;
    cursor: pointer;
    margin-top:40%;
    margin-left:22.5%;
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
  


.next_button_2{
    width:50%;
    height:20px;
    padding:10px 20px;
    background-color:rgb(25, 120, 237);
    color:#fff;
    text-align: center;
    border-radius:100px;
    cursor: pointer;
    margin-top:15%;
    margin-left:22.5%;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}

.next_button_2:hover{
  box-shadow: 0px 10px 15px rgb(25, 120, 237, .5);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
} 
    
    
    
    .input_wrap_welcome {
    position: relative;
    margin-top:3.5vw;
    z-index:1;
  }
  
  .input_wrap_welcome .input_black {
    display: block;
    width:80%;
      margin-left:10%;
      height:2.5vw;
      border-bottom: 1px solid #fff;
      background-color: #00000000;
      color: #fff;
      padding-left: 1vw;
      font-size:1.5vw;
  }
  
  .input_wrap_welcome .label_black {
    position: absolute;
    color: rgb(140, 140, 140);
    font-size: 2.25vw;
    font-weight: normal;
    pointer-events: none;
    left: 4.75vw;
    top: .15vw;
    transition: 300ms ease all;
  }

  
  .input_wrap_welcome .input_black:focus~ .label_black,
  .input_wrap_welcome .input_black:valid ~ .label_black{
    top: -1.75vw;
    left: 4vw;  
    font-size: 1vw;
    color: #1b91eb;
  }

    









.emph_underline{
    text-decoration:underline;
    text-decoration: underline;
    text-decoration-color: rgb(25, 120, 237);
    
}



.hide_it{
    display:none;
}

.files_open{
    padding:10px 0px;
    color:#ffffffbc;
    background-color:#17171724;
    border:1px solid rgb(255, 255, 255, .15);
    width:30%;
    border-radius:50px;
    text-align:center;
    height:20px;
    cursor:pointer;
    margin-left:35%;
    transition: all 0.5s ease;
}

.files_open:hover{
    background-color:rgba(25, 120, 237, 0.359);
    transition: all 0.5s ease;
}

.files_submit{
    padding: 10px 0px;
    color:#ffffff58;
    background-color:#17171724;
    border:1px solid #ffffff58;
    width:30%;
    border-radius:50px;
    text-align:center;
    height:20px;
    cursor:pointer;
    margin-left:35%;
    transition: all 0.5s ease;
}

.files_submit:hover{
    background-color:#17171724;
    transition: all 0.5s ease;
}

.upload_image{
    width:20%;
    margin-left:calc(35% - 15px);
    margin-bottom:20px;
    background-color:#17171734;
    padding:50px;
    border-radius:50px;
    border: 1px solid v-bind(drop_success_border);
    transition: background-color 2s ease, border .5s ease;
}

.upload_image:hover{
    background-color:#3a6df0;
    transition: background-color 30s ease;
}




.upload_container{
    cursor: pointer;
}

.upload_title{
    text-decoration: underline;
  text-decoration-color: red;
  text-underline-offset: 12px;
}

.drop_success{
    text-decoration: underline;
  text-decoration-color: #3a6df0;
  text-underline-offset: 8px;
}

.show_drop_error{
    text-decoration: underline;
  text-decoration-color: red;
  text-underline-offset: 8px;
}


.container_gap{
    margin-top:20%;
}




.designation_box{
    width:60%;
    margin-left:10%;
    margin-top:-10%;
    opacity:0;
    position:absolute;
    background-color:#fff;
    z-index:5;
    padding:6%;
    border-radius:10px;
    border: 4px solid rgba(25, 120, 237, 0.7);
    display: inline-block;
    transition: all .35s ease-in-out;
    visibility: hidden;
}

.designation_text{
    color:#fff;
    font-size:110% 
}
.desig_underline{
    border-bottom: 2px solid #ff9933b2;
    padding-bottom:10px;
    text-align:center;
    margin-top:-3%;
    width:80%;
    margin-left:10%;
    margin-bottom:5%
}

.designation_show{
    margin-top:-30%;
    opacity:1;
    visibility: visible;
    transition: all .35s ease-in-out;
}
.designation_hover{
    font-size:12px;
    padding:2px 7px;
    border: 1px solid #3a6df0;
    color: #fff;
    border-radius:100%;
    cursor:pointer;
    transition: all .35s ease-in-out;
}

.designation_hover:hover{
    background-color:rgba(25, 120, 237, 0.3);
    color:#fff;
    transition: all .35s ease-in-out;
}

.bottom_padding{
    padding-bottom:125vh;
}


@media only screen and (min-width: 0px) and (max-width: 410px) {

.upload_image{
    margin-bottom:20px
}
.upload_container{
    margin-left:0%
}

.form_container {
display: grid;
grid-template-columns:1fr; 
grid-template-rows: repeat(2, 1fr); 
grid-column-gap: 0px;
grid-row-gap: 0px;
margin-top:50px
}

.next_button{
    width:70%;
    margin-top:0%;
    margin-left:8% !important;
}

.next_button_2{
    width:70%;
    margin-top:10%;
    margin-left:8% !important;
    margin-bottom:90%
}

.container_gap{
    margin-top:-45%;
}

.return_text{
        margin-top:30%;
        margin-bottom:12%
    }

    .landing_video{
        margin-top:30%;
        opacity:.1;
    }

    .desig_underline{
    width:100%;
}



.files_open{
    margin-left:35%;
}

.files_submit{
    margin-left:29%;
}

.upload_image{
    margin-left:calc(27% - 5px);
}
    

.designation_box{
    width:70%;
    margin-left:3%;
    margin-top:-100%;
}

.designation_text{
    font-size:90% 
}
.desig_underline{
    margin-top:-3%;
    width:80%;
    margin-left:10%;
    margin-bottom:5%
}

.designation_show{
    margin-top:-160%;
}
.designation_hover{
    font-size:12px;
}


.plaid_button_move{
        margin-top:5%
    }

    .bottom_padding{
    padding-bottom:150vh;
}

}




@media only screen and (min-width: 410px) and (max-width: 576px) {

    .plaid_button_move{
        margin-top:10%
    }
    
.upload_image{
    margin-bottom:20px
}
.upload_container{
    margin-left:0%
}

.form_container {
display: grid;
grid-template-columns:1fr; 
grid-template-rows: repeat(2, 1fr); 
grid-column-gap: 0px;
grid-row-gap: 0px;
margin-top:50px
}

.next_button{
    width:70%;
    margin-top:-20%;
    margin-left:8% !important;
}

.next_button_2{
    width:70%;
    margin-top:10%;
    margin-left:8% !important;
    margin-bottom:90%
}

.container_gap{
    margin-top:-45%;
}

.return_text{
        margin-top:30%;
        margin-bottom:12%
    }

    .landing_video{
        margin-top:20%;
        opacity:.09;
    }

    .desig_underline{
    width:100%;
}

.bottom_padding{
    padding-bottom:200vh;
}

    

}

@media only screen and (min-width: 576px) and (max-width: 768px) {

.upload_image{
    margin-bottom:20px
}
.upload_container{
    margin-left:10%
}


.return_subtext{
        margin-top:-18% !important;
    }

    .desig_underline{
    width:100%;
}

}


@media only screen and (min-width: 768px) and (max-width: 992px) {

.upload_image{
    margin-bottom:20px
}
.upload_container{
    margin-left:10%
}

.desig_underline{
    width:90%;
    margin-left:5%
}

}










    
    @media screen and (min-width: 2300px) and (max-width: 5600px) {

    }
    
    
    
    
    
    
    
    
    
    @media screen and (min-width: 1900px) and (max-width: 2300px) {
    
    
    }
    
    
    @media screen and (min-width: 1600px) and (max-width: 1900px) {
    
    
    }
    
    
    
    
    
    @media screen and (min-width: 1400px) and (max-width: 1600px) {
    
    }
    
    
    
    
    @media screen and (min-width: 1200px) and (max-width: 1400px) {
    
    }
    
    @media only screen and (min-width: 992px) and (max-width: 1200px) {
    

    


    
    }
    
    
    @media only screen and (min-width: 768px) and (max-width: 992px) {
    

        .next_button{
    margin-left:32%;
}
 

.next_button_2{
    margin-left:32%;
}
 

    
    }
    
    
    
    @media only screen and (min-width: 576px) and (max-width: 768px) {
    
        .landing_video{
        margin-top:15%
    }

    .next_button{
    margin-left:31%;
}
.next_button_2{
    margin-left:31%;
}
    
    
    }









 /* ------------------- modal ------------------- */
 /* ------------------- modal ------------------- */
 /* ------------------- modal ------------------- */

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
    z-index:1;
    display:flex;
    justify-content:center;
    align-items:center;
    backdrop-filter: blur(10px);
    transition: all 1s ease-in-out;
    opacity: 1;

}



.modal_popup{
    width:65%;
    height:400px;
    background-color:rgb(0, 0, 0);
    z-index:10;
    border-radius:20px;
    margin-top:50px;
    border: #fff solid 2px;
    transition: all 1s ease-in-out;
    /* overflow-y: scroll; */
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
    font-size:20px;
    font-weight:600;
    color:#fff;
    margin-left:10%;
    width:80%;
    text-align:center;
    margin-top:5%;
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
    margin-top:10px;
    margin-bottom: -10px;
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



.modal_flex{
    display:flex;
    justify-content:center;
    align-items:center;
    margin-top:7%;
}

.modal_next_button{
    width:30%;
    height:20px;
    padding:10px 20px;
    background-color:rgb(25, 120, 237);
    color:#fff;
    text-align: center;
    border-radius:100px;
    cursor: pointer;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}

.modal_next_button:hover{
  box-shadow: 0px 10px 15px rgb(25, 120, 237, .5);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
} 
    



@media only screen and (min-width: 0px) and (max-width: 576px) {

    .modal_popup{
    width:85%;
    height:400px;
}

.modal_exit{
    margin-top:10px;
    margin-left:85%;
    width:40px;
    height:40px;
}

.modal_next_button{
    width:40%;
}


}
    


    
    
    </style>