<template>

    <div>
    <CircleTransition ref="cicle_tansition"/>
    
        
        <div class="modal_container" :class="{modal_hide_anim: modal_exit_anim, modal_hide_disp: modal_exit_display}">
        <div class="modal_popup" :class="{modal_bix_hide_anim: modal_exit_anim}" ref="modal">
            <!-- <div @click="modal_leave" class="modal_exit">
                <div class="horizontal_line"></div>
                <div class="vertical_line"></div>
            </div> -->



            <div class="loader_container" v-if="start_loader">
<InvestFlowLoadersApiLoader/>
   </div>

<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->
<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->





<div class="form_container">


<p class="reverify_text">Based on your previously inputted values our KYC identity vendor requires that you reverify your beneficial owner. Please double-check all entered information. </p>
<p class="form_title">Beneficial Owner Information <span class="designation_hover" @mouseover="designation_show = true">?</span></p>
<p class="designation_text" :class="{designation_show: designation_show}" @mouseleave="designation_show = false">A beneficial owner is a natural person who, directly or indirectly, owns 25% or more of a company. If there are no natural persons who own 25% or more of a company, then no information needs to be collected. A beneficial owner cannot be another company (or other corporate entity), nor a nominee owner. <br><br>
<b>How is the 25% Ownership Determined for a Beneficial Owner?</b><br>
If a natural person owns 25% or more of a company, then he or she is a beneficial owner. For example, if three people each directly own 33% of a company, then each individual is a beneficial owner. However, where a company is owned by other companies (or other corporate entities), indirect ownership must be identified.
</p>



<div class="form_grid">


<div class="input_wrap">
<input v-model="owner_first_name" class="input_black" placeholder=' ' required/>
<label class="label_black">Owner First Name</label>
</div>


<div class="input_wrap">
<input v-model="owner_last_name" class="input_black" placeholder=' ' type="text" required/>
<label class="label_black">Owner Last Name</label>
</div>

<div class="input_wrap">
<input v-model="owner_title" class="input_black" placeholder=' ' type="text" required/>
<label  class="label_black">Owner Title</label>
</div>

<div class="input_wrap">
<input v-model="owner_dob" class="input_black input_date" placeholder=' ' type="date" required/>
<label  class="label_black">Controller Date of Birth</label>
</div>

<div class="input_wrap">
<input @keypress="onSSNKeyPress_owner" @keyup="remove_chrs('owner_ssn')" v-model="owner_ssn" class="input_black" placeholder=' ' type="text" maxlength="11" required/>
<label  class="label_black">Owner SSN</label>
</div>


<div class="input_wrap">
<input v-model="owner_address" class="input_black" placeholder=' ' type="text" required/>
<label  class="label_black">Owner Address</label>
</div>

<InvestFlowStateCodesSelectBlack v-bind="owner_state_codes" v-model:state_value="owner_state"/>


<div class="input_wrap">
<input v-model="owner_city" class="input_black" placeholder=' ' type="text" required/>
<label  class="label_black">Owner City</label>
</div>

<div class="input_wrap">
<input v-model="owner_zip" class="input_black" placeholder=' ' @keyup="remove_chrs('owner_zip')"  type="text" maxlength="5" required/>
<label  class="label_black">Owner Zip</label>
</div>

<InvestFlowCountryCodesSelectBlack v-bind="owner_country_codes" v-model:country_value="owner_country"/>

</div>

<div class="next_button" @click="owner_submit">Submit</div>

</div>












<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->
<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->


        </div>
    </div>
    
    </div>
    </template>
    
    
    
    
    
    <script setup>
   const designation_show = ref(false)

   const dwolla_customer_status = useCookie('dwolla_customer_status')
    const dwolla_beneficial_owner_status = useCookie('dwolla_beneficial_owner_status')
    const investing_as = useCookie('investing_as')
    const investor_ID = useCookie('investor_ID')
    const owner_first_name = ref("")
    const owner_last_name = ref("")
    const owner_title = ref("")
    const owner_dob = ref("")
    const owner_ssn = ref("")
    const owner_address = ref("")
    const owner_state = ref("")
    const owner_city = ref("")
    const owner_zip = ref("")
    const owner_country = ref("")

    



    const owner_state_codes = {
    name: 'owner_state',
        label: 'Owner State',
    }

    const owner_country_codes = {
    name: 'owner_country',
        label: 'Owner Country',
    }









// ----------------------------------   format inputs  ----------------------------------


function onSSNKeyPress_individual_ssn(e) {
    const key = e.keyCode || e.charCode;
    const input_len = individual_ssn.value.length
    if (key !== 8 || key !==  46) {
    if(input_len == 3 || input_len == 6){
        individual_ssn.value = individual_ssn.value + '-'
        }}}


//not working ?????
        function onSSNKeyPress_sole_prop(e) {
    const key = e.keyCode || e.charCode;
    const input_len = sole_prop_ssn.value.length
    alert("sole prop")
    if (key !== 8 || key !==  46) {
    if(input_len == 3 || input_len == 6){
        sole_prop_ssn.value = sole_prop_ssn.value + '-'
        }}}



function onSSNKeyPress_controller(e) {
    const key = e.keyCode || e.charCode;
    const input_len = controller_ssn.value.length
    if (key !== 8 || key !==  46) {
    if(input_len == 3 || input_len == 6){
        controller_ssn.value = controller_ssn.value + '-'
        }}}



function onSSNKeyPress_owner(e) {
    const key = e.keyCode || e.charCode;
    const input_len = owner_ssn.value.length
    if (key !== 8 || key !==  46) {
    if(input_len == 3 || input_len == 6){
        owner_ssn.value = owner_ssn.value + '-'
        }}}




        function onEINKeyPress_sole_prop(e) {
    const key = e.keyCode || e.charCode;
    const input_len = sole_prop_business_ein.value.length
    if (key !== 8 || key !==  46) {
    if(input_len == 2){
        sole_prop_business_ein.value = sole_prop_business_ein.value + '-'
        }}}




        function onEINKeyPress_business_ein(e) {
    const key = e.keyCode || e.charCode;
    const input_len = business_ein.value.length
    if (key !== 8 || key !==  46) {
        if(input_len == 2){
        business_ein.value = business_ein.value + '-'
        }}}


        

        function remove_chrs(input_var) {
    this[input_var] = this[input_var].toString().replace(/[^0-9-]/g, '');
}



// -------------------------------------------------------------------------------------------------------







// -------------------------------- Send API Request --------------------------------




const input_error = ref(false)



function step_3_reverify_send() {

  


const data_to_send = {
    investor_ID: investor_ID.value,
    dwolla_customer_status: dwolla_customer_status.value,
    dwolla_beneficial_owner_status: dwolla_beneficial_owner_status.value,
    investing_as: investing_as.value,
 owner_first_name: owner_first_name.value ,
 owner_last_name:  owner_last_name.value,
 owner_title: owner_title.value ,
 owner_dob: owner_dob.value ,
 owner_ssn: owner_ssn.value ,
 owner_address: owner_address.value ,
 owner_state: owner_state.value ,
 owner_city: owner_city.value ,
 owner_zip: owner_zip.value ,
 owner_country: owner_country.value ,

}




// regex to check if password has at least one number and one letter
const regex = /^(?=.*[0-9])(?=.*[a-zA-Z])(?!.*[^ a-zA-Z0-9]).*$/



for (const [key, value] of Object.entries(data_to_send)) {   
console.log(key, value);
if (value == ''){
    alert('Please fill out the ___ ' + key + ' ___')
    input_error.value = true
    }
    else if (key == 'owner_ssn' && value.length != 11){
    alert('Check Controller SSN Number')
    input_error.value = true
    }
    else if (key == 'owner_zip' && String(value).length != 5){
    alert('Check Owner Zip Code')
    input_error.value = true
    }
    else if (key == 'owner_address'){
        if (!regex.test(value)) {
    alert('Owner address must contain at least one number and letter')
    input_error.value = true
    }}
    else if( key == 'owner_dob' ){
    if( new Date(Date.parse(value.replace(/-/g, " "))) <= new Date(Date.parse('1900-01-01'.replace(/-/g, " "))) || new Date(Date.parse(value.replace(/-/g, " "))) >= new Date(Date.parse('2005-01-01'.replace(/-/g, " "))) ){
        alert('Please input a Owner valid date of birth that is after 1900 and before 2005')
        input_error.value = true
        }
    }
}




if (input_error.value == false){

start_loader.value = true;

fetch(`${config.flask_url}/api/dwolla_reverification/reverify_customer/`, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data_to_send)
})
.then((response) => response.json())
.then((data) => {
    console.log('Success:', data.message);
    dwolla_beneficial_owner_status.value = data.dwolla_beneficial_owner_status
    dwolla_customer_status.value = data.dwolla_customer_status
    modal_leave()
    sleep(700).then(() => { window.location.reload(); });

})
.catch(error => {
    start_loader.value = false;
    modal_leave()
    sleep(700).then(() => { window.location.reload(); });
        alert('Error')
        console.error('There was an error!', error);
});

} else{
input_error.value = false
start_loader.value = false;
console.error('There was an error no send');
}
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
    
    
    
    
    const cicle_tansition = ref(null);
    function transition_and_route(route_to) {
     cicle_tansition.value.animation_and_route(route_to);
    }
    
    
    </script>
    
    
    
    
    <style scoped>
    
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


.z_scope :deep(.left_side){
z-index:-1
}

.z_scope :deep(.header){
z-index:-1
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
grid-template-columns: repeat(2, 1fr);
grid-template-rows: repeat(4, 1fr);
grid-column-gap: 0px;
grid-row-gap: 0px;
z-index: 10;
width:80%;
margin-left:10%;
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
  width: 8px !important;
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