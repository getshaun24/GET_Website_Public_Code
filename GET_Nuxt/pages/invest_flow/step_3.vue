<template>

    <div>
        <CircleTransition ref="cicle_tansition"/>

        <div class="loader_container" v-if="start_loader">

     <InvestFlowLoadersApiLoader/>
        <!-- <div class="loader"></div> -->
        </div>



     <!-- -------------------------- modal popup --------------------------------- -->

                <div class="modal_container" :class="{modal_hide_anim: modal_exit_anim, modal_hide_disp: modal_exit_display}">
    <div class="modal_popup" :class="{modal_bix_hide_anim: modal_exit_anim}" ref="modal">
        <div @click="modal_leave" class="modal_exit">
            <div class="horizontal_line"></div>
            <div class="vertical_line"></div>
        </div>

        <div v-show="contact_modal">
        <h3 class="modal_info_step_3"><span class="no_return_text_contact">Some of the information entered is incorrect and/or does not match our payment processor's records. Please double check that everything was entered correctly, or, should you prefer to talk with us directly, use the Calendly link below to setup a time for a member of GET Resources Group to call you. You can also email support directly at support@thisisget.com</span></h3>
        <div class="modal_flex">
            <div class="modal_next_button" @click="transition_and_route('step_1')" >Back to first step</div>
        <a class="modal_next_button" target="_blank" href="https://calendly.com/get-resources/investment">Calandly</a>
    </div>
</div>

    <div v-show="verify_modal">
        <h3 class="modal_info_step_3"><span class="no_return_text">Make sure all the information in the previous pages are correct, you will not be able to return to this page</span></h3>
        <div class="modal_flex">
            <div class="modal_next_button" @click="transition_and_route('step_1')" >Back to first step</div>
        <div class="modal_next_button" @click="step_3_api_send()">Submit</div>
    </div>
    </div>

    <div v-show="accred_modal">
        <h3 class="modal_info_step_3"><span class="accred_modal_text">You must be accredited to continue. Please double check your finances to ensure accredation status. If you are experiencing issues or are uncertain about your status, please contact us at get-accredited@thisisget.com or set a Calendly appointment.</span></h3>
        <div class="modal_flex">
            <a class="modal_next_button" target="_blank" href="https://calendly.com/get-resources/investment">Calandly</a>
    </div>
    </div>

    </div>
</div>

        <!-- -------------------------- modal popup --------------------------------- -->





    <Header/>
    <div class="white_background">
    <GSAPScrollSmoother>


        <InvestFlowStepCircles v-bind="step_circles" />

<div class="progress_bar_container">
<div class="progress_bar"></div>
</div>

<div class="part_1_container" :class="{is_active:part_1, visibility_animation:part_1_vis}">
<div class="form_grid_1">








    <div class="input_wrap">
            <select v-model="investing_as"   class="select_white">
                    <option value="" disabled selected hidden></option>
                    <option value="individual">Individual</option>
                    <option value="corporation">Corporation</option>
                    <option value="llc">LLC</option>
                    <option value="partnership">Partnership</option>
                    <option value="soleProprietorship">Sole Proprietorship</option>
            </select>
                <label class="label_white">Investing As:</label>
        </div>


      

    <div class="input_wrap">
            <select v-model="exempt_from_withholding"  class="select_white withholding_input">
                    <option value="" disabled selected hidden></option>
                    <option value="yes">Yes</option>
                    <option value="no">No</option>
            </select>
                <label class="label_white withholding_label">Are you exempt from backup withholding?</label>
                <p class="extra_label_format">Typical answer is yes unless otherwise informed by the IRS that you/entity are not excempt</p>
        </div>

        

</div>
</div>






<div class="part_2_container" :class="{is_active:part_2, visibility_animation:part_2_vis}">







<div :class="{hide_it:hide_business_info}">
    <h5 class="form_title">Business Information</h5>
<div class="form_grid_2">

    <InvestFlowIndustryClassification v-model:industry_classification="industry_classification"/>

<InvestFlowBusinessClassification v-bind="entity_bis_class"  v-model:business_classification="business_classification"/>


<div class="input_wrap">
        <input v-model="business_name" class="input_white" placeholder=' ' />
        <label class="label_white">Business Name</label>
 </div>


 <div class="input_wrap">
        <input @keypress="onEINKeyPress_business_ein" @keyup="remove_chrs('business_ein')" v-model="business_ein" class="input_white" placeholder=' ' type="text" maxlength="10" />
        <label class="label_white">Business EIN</label>
</div>


<div class="input_wrap">
            <select @blur="check_accred" v-model="is_accredited"  class="select_white">
                <option value="" disabled selected hidden></option>
                <option value="yes_1">Yes 1 - My business owns assets in excess of $5,000,000</option>
                <option value="no">No - I am not accredited</option>
            </select>
                <label class="label_white">Are you an Accredited Investor:</label>
        </div>



<div>

    
<div class="input_wrap">
            <select v-model="entity_purpose_to_invest"   class="select_white">
                    <option value="" disabled selected hidden></option>
                    <option value="yes">Yes</option>
                    <option value="no">No</option>
            </select>
                <label class="label_white">Entity Purpose:</label>
                <p class="extra_label_format">Was your business entity primarily created to invest in this fund?</p>
        </div>

    </div>



</div>
</div>





<div :class="{hide_it:hide_sole_prop_info}">
    <h5 class="form_title">Sole Proprietorship Info</h5>
    <div class="form_grid_2">


        <div class="input_wrap">
            <input v-model="sole_prop_first_name" class="input_white" placeholder=' ' />
            <label class="label_white">First Name</label>
     </div>


     <div class="input_wrap">
            <input v-model="sole_prop_last_name" class="input_white" placeholder=' ' type="text" />
            <label class="label_white">Last Name</label>
    </div>


<InvestFlowIndustryClassification v-model:industry_classification="sole_prop_industry_classification"/> 

<InvestFlowBusinessClassification v-bind="sole_prop_bis_class" v-model:business_classification="sole_prop_business_classification"/>




<div class="input_wrap">
        <input v-model="sole_prop_business_name" class="input_white" placeholder=' ' />
        <label class="label_white">Business Name</label>
 </div>


 <div class="input_wrap">
        <input @keypress="onEINKeyPress_sole_prop" @keyup="remove_chrs('sole_prop_business_ein')" v-model="sole_prop_business_ein" class="input_white" placeholder=' ' type="text" maxlength="10" />
        <label class="label_white">Business EIN</label>
</div>

<div class="input_wrap">
        <input v-model="sole_prop_dob" class="input_white input_date" placeholder=' ' type="date" maxlength="10" min="1900-01-01" max="2020-12-31" />
        <label  class="label_white">Date of Birth</label>
</div>


<div class="input_wrap">
        <input @keypress="onSSNKeyPress_sole_prop" @keyup="remove_chrs('sole_prop_ssn')" v-model="sole_prop_ssn" maxlength="11"  class="input_white" placeholder=' ' type="text" />
        <label class="label_white">Social Security Number</label>
</div>

<div class="input_wrap">
            <input v-model="sole_prop_address" class="input_white" placeholder=' ' type="text" />
            <label  class="label_white">Address</label>
    </div>


    <div class="input_wrap">
            <input v-model="sole_prop_city" class="input_white" placeholder=' ' type="text" />
            <label  class="label_white">City</label>
    </div>


    <InvestFlowStateCodesSelect v-bind="sole_prop_state_codes" v-model:state_value="sole_prop_state"/>

    <div class="input_wrap">
            <input @keypress="onKeyPress_sole_prop_zip" v-model="sole_prop_zip" class="input_white" maxlength="5" placeholder=' ' type="text" @keyup="remove_chrs('sole_prop_zip')" />
            <label  class="label_white">Zip</label>
    </div>

<div class="input_wrap">
            <select @blur="check_accred" v-model="is_accredited"  class="select_white">
                <option value="" disabled selected hidden></option>
                <option value="yes_1">Yes 1 - My business ownes assets in excess of $5,000,000</option>
                <option value="no">No - I am not accredited</option>
            </select>
                <label class="label_white">Are you an Accredited Investor:</label>
        </div>

    

</div>

</div>



<div :class="{hide_it:hide_personal_info}">
    <h5 class="form_title">Individual Information</h5>
    <div class="form_grid_2">



        <div class="input_wrap">
            <select @blur="check_accred" v-model="is_accredited"  class="select_white">
                <option value="" disabled selected hidden></option>
                <option value="yes_1">Yes 1 - I have earned over $200,000 in the last 2 years</option>
                <option value="yes_2">Yes 2 - My spouse and I have jointly earned over $300,000 in the last 2 years</option>
                <option value="yes_3">Yes 3 - I have a networth over $1,000,000</option>
                <option value="no">No - I am not accredited</option>
            </select>
                <label class="label_white">Are you an Accredited Investor:</label>
        </div>




    <div class="input_wrap">
            <input v-model="individual_first_name" class="input_white" placeholder=' ' />
            <label class="label_white">First Name</label>
     </div>


     <div class="input_wrap">
            <input v-model="individual_last_name" class="input_white" placeholder=' ' type="text" />
            <label class="label_white">Last Name</label>
    </div>

    <div class="input_wrap">
                <input v-model="individual_dob" class="input_white input_date" placeholder=' ' type="date" maxlength="10" min="1900-01-01" max="2020-12-31" />
                <label  class="label_white">Date of Birth</label>
    </div>

    <div class="input_wrap">
            <input @keypress="onSSNKeyPress_individual_ssn" @keyup="remove_chrs('individual_ssn')" v-model="individual_ssn" class="input_white" placeholder=' ' type="text" maxlength="11" />
            <label  class="label_white">SSN</label>
    </div>


    <div class="input_wrap">
            <input v-model="individual_address" class="input_white" placeholder=' ' type="text" />
            <label  class="label_white">Address</label>
    </div>


    <div class="input_wrap">
            <input v-model="individual_city" class="input_white" placeholder=' ' type="text" />
            <label  class="label_white">City</label>
    </div>


    <InvestFlowStateCodesSelect v-bind="individual_state_codes" v-model:state_value="individual_state"/>

    <div class="input_wrap">
            <input @keypress="onKeyPress_individual_zip" v-model="individual_zip" class="input_white" placeholder=' ' type="text" @keyup="remove_chrs('individual_zip')" maxlength="5" />
            <label  class="label_white">Zip</label>
    </div>

    <div class="input_wrap">
            <select v-model="empolyment_status"  class="select_white">
                <option value="" disabled selected hidden></option>
                <option value="employed">Yes</option>
                <option value="not_employed">No</option>
            </select>
                <label class="label_white">Are you Employed?</label>
        </div>


</div>



</div>



</div>




<div class="part_3_container" :class="{is_active:part_3, visibility_animation:part_3_vis}">


<h5 class="form_title">Controller Information <span class="designation_hover" @mouseover="designation_show = true">?</span></h5>
<p class="designation_text" :class="{designation_show: designation_show}" @mouseleave="designation_show = false">A controller is a natural person who holds significant responsibilities to control, manage or direct a company or other corporate entity (i.e. CEO, CFO, General Partner, President, etc). A company may have more than one controller, but only one controller’s information must be collected.</p>


<div class="form_grid_3">




<div class="input_wrap">
            <input v-model="controller_first_name" class="input_white" placeholder=' ' />
            <label class="label_white">Controller First Name</label>
     </div>


     <div class="input_wrap">
            <input v-model="controller_last_name" class="input_white" placeholder=' ' type="text" />
            <label class="label_white">Controller Last Name</label>
    </div>

    <div class="input_wrap">
            <input v-model="controller_title" class="input_white" placeholder=' ' type="text" />
            <label  class="label_white">Controller Title</label>
    </div>

    <!-- <div class="input_wrap">
            <input v-model="controller_email" class="input_white" placeholder=' ' type="text" />
            <label  class="label_white">Controller Email</label>
    </div> -->

    <div class="input_wrap">
                <input v-model="controller_dob" class="input_white input_date" placeholder=' ' type="date" maxlength="10" min="1900-01-01" max="2020-12-31" />
                <label  class="label_white">Controller Date of Birth</label>
    </div>

    <div class="input_wrap">
            <input @keypress="onSSNKeyPress_controller" @keyup="remove_chrs('controller_ssn')" v-model="controller_ssn" class="input_white" placeholder=' ' type="text" maxlength="11" />
            <label  class="label_white">Controller SSN</label>
    </div>


    <div class="input_wrap">
            <input v-model="controller_address" class="input_white" placeholder=' ' type="text" />
            <label  class="label_white">Controller Address</label>
    </div>



    <div class="input_wrap">
            <input v-model="controller_city" class="input_white" placeholder=' ' type="text" />
            <label  class="label_white">Controller City</label>
    </div>

    <InvestFlowStateCodesSelect v-bind="controller_state_codes" v-model:state_value="controller_state"/>

    <div class="input_wrap">
            <input @keypress="onKeyPress_controller_zip" v-model="controller_zip" class="input_white" placeholder=' ' type="text"  @keyup="remove_chrs('controller_zip')" maxlength="5"  />
            <label  class="label_white">Controller Zip</label>
    </div>

    <InvestFlowCountryCodesSelect v-bind="controller_country_codes" v-model:country_value="controller_country"/>

    

</div>
</div>



<div class="part_4_container" :class="{is_active:part_4, visibility_animation:part_4_vis}">


<h5 class="form_title">Beneficial Owner Information <span class="designation_hover" @mouseover="designation_show = true">?</span></h5>
<p class="designation_text" :class="{designation_show: designation_show}" @mouseleave="designation_show = false">A beneficial owner is a natural person who, directly or indirectly, owns 25% or more of a company. If there are no natural persons who own 25% or more of a company, then no information needs to be collected. A beneficial owner cannot be another company (or other corporate entity), nor a nominee owner. <br><br>
<b>How is the 25% Ownership Determined for a Beneficial Owner?</b><br>
If a natural person owns 25% or more of a company, then he or she is a beneficial owner. For example, if three people each directly own 33% of a company, then each individual is a beneficial owner. However, where a company is owned by other companies (or other corporate entities), indirect ownership must be identified.
</p>


<div @click="same_as" class="same_as_button">Same as Controller</div>

<div class="form_grid_4">


<div class="input_wrap">
            <input v-model="owner_first_name" class="input_white" placeholder=' ' />
            <label class="label_white">Owner First Name</label>
     </div>


     <div class="input_wrap">
            <input v-model="owner_last_name" class="input_white" placeholder=' ' type="text" />
            <label class="label_white">Owner Last Name</label>
    </div>

    <div class="input_wrap">
            <input v-model="owner_title" class="input_white" placeholder=' ' type="text" />
            <label  class="label_white">Owner Title</label>
    </div>

    <!-- <div class="input_wrap">
       <input v-model="owner_email" class="input_white" placeholder=' ' type="text" /> 
            <label  class="label_white">Owner Email</label>
    </div> -->

    <div class="input_wrap">
                <input v-model="owner_dob" class="input_white input_date" placeholder=' ' type="date" maxlength="10" min="1900-01-01" max="2020-12-31" />
                <label  class="label_white">Controller Date of Birth</label>
    </div>

    <div class="input_wrap">
            <input @keypress="onSSNKeyPress_owner" @keyup="remove_chrs('owner_ssn')" v-model="owner_ssn" class="input_white" placeholder=' ' type="text" maxlength="11" />
            <label  class="label_white">Owner SSN</label>
    </div>


    <div class="input_wrap">
            <input v-model="owner_address" class="input_white" placeholder=' ' type="text" />
            <label  class="label_white">Owner Address</label>
    </div>

    <div class="input_wrap">
            <input v-model="owner_city" class="input_white" placeholder=' ' type="text" />
            <label  class="label_white">Owner City</label>
    </div>

    <InvestFlowStateCodesSelect v-bind="owner_state_codes" v-model:state_value="owner_state"/>


    <div class="input_wrap">
            <input @keypress="onKeyPress_owner_zip" v-model="owner_zip" class="input_white" placeholder=' ' @keyup="remove_chrs('owner_zip')"  type="text" maxlength="5" />
            <label  class="label_white">Owner Zip</label>
    </div>

    <InvestFlowCountryCodesSelect v-bind="owner_country_codes" v-model:country_value="owner_country"/>

</div>

</div>


<div class="part_5_container" :class="{is_active:part_5, visibility_animation:part_5_vis}">


<div class="form_grid_5">

<p class="select_account_text">Please select the account from which to send funds from.</p>
<InvestFlowAccountSelectButtons  v-model:account_selected_value="account_selected_value"/> 

    </div>

    <p class="on_demand_text" >I agree that all future payments to or facilitated by GET will be processed by the Dwolla payment system from the selected account above. In order to cancel this authorization, I will change my payment settings within my GET account.</p>


</div>


   <!-- ------------------------------------------------------------------------------------- -->

    <div class="form_pagenation">
        <div class="prev_button" :class="{hide_it:is_hidden}" @click="page_counter_prev">Prev</div>
        <div class="next_button" :class="{reduce_width:reduce_width}" @click="page_counter_next">{{ next_text }}</div>
    </div>













<div style="padding-bottom:25vh"></div>





    </GSAPScrollSmoother>
    
</div>

</div>
    
    </template>
    
    
    <script setup>
        import { gsap } from 'gsap'
        import { ScrollTrigger } from 'gsap/ScrollTrigger'
        import { ScrollToPlugin } from 'gsap/all'
        gsap.registerPlugin(ScrollToPlugin)

// sleep time expects milliseconds
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}





const config = useRuntimeConfig()

const cookie_options = {default:()=> '', watch:true, maxAge:1800}


const is_hidden = ref(true)
const next_text = ref("Next")
const part_1 = ref(true)
const part_2 = ref(false)
const part_3 = ref(false)
const part_4 = ref(false)
const part_5 = ref(false)
const page_count = ref(1)
const progress_width = ref("0%")
const reduce_width = ref(true)


const investing_as = useCookie('investing_as', {default:()=> '', watch:true, maxAge:2400})
const hide_business_info = ref(true)
const hide_sole_prop_info = ref(true)
const hide_personal_info = ref(true)

const part_1_vis = ref(true)
const part_2_vis = ref(false)
const part_3_vis = ref(false)
const part_4_vis = ref(false)
const part_5_vis = ref(false)

const flow_bar_start = ref(true)

const designation_show = ref(false)

const cicle_tansition = ref('');
const start_loader = ref(false);

const input_error = ref(false)
const contact_modal = ref(false)
const verify_modal = ref(false)
const accred_modal = ref(false)


const step_circles = {
    current_num: 3
}




onMounted(() => {
    progress_width.value = "20%"
    flow_bar_start.value = false
})





function page_counter_prev(){
    gsap.to(window, {duration: .45, scrollTo: {y: ".progress_bar", offsetY: 20} });
    if(page_count.value==5){
        if(investing_as.value == "individual" || investing_as.value == "soleProprietorship") {
        page_count.value = 2
    } else{
        page_count.value -= 1
    }
}
else if(page_count.value > 1){
        page_count.value -= 1
    }
    if(page_count.value == 1){
            reduce_width.value = true
        }
    part_to_show(page_count.value)
}





function part_to_show(count){
    if(count == 1){
        next_text.value = "Next"
        is_hidden.value = true
        part_1.value = true
        sleep(0).then(() => {part_1_vis.value = true})
        progress_width.value = "20%"
    }else{
        part_1.value = false
        sleep(0).then(() => {part_1_vis.value = false})
    }
    if(count == 2){
        show_hide_page_2_info()
        next_text.value = "Next"
        is_hidden.value = false
        part_2.value = true
        sleep(0).then(() => {part_2_vis.value = true})
        progress_width.value = "40%"
    }else{
        part_2.value = false
        sleep(0).then(() => {part_2_vis.value = false})
    }

    if(count == 3){
        next_text.value = "Next"
        part_3.value = true
        sleep(0).then(() => {part_3_vis.value = true})
        is_hidden.value = false
        progress_width.value = "60%"
    }else{
        part_3.value = false
        sleep(0).then(() => {part_3_vis.value = false})
    }

    if(count == 4){
        next_text.value = "Next"
        part_4.value = true
        sleep(0).then(() => {part_4_vis.value = true})
        is_hidden.value = false
        progress_width.value = "80%"
    }else{
        part_4.value = false
        sleep(0).then(() => {part_4_vis.value = false})
    }

    if(count == 5){
        next_text.value = "Submit"
        part_5.value = true
        sleep(0).then(() => {part_5_vis.value = true})
        is_hidden.value = false
        progress_width.value = "100%"
    }else{
        part_5.value = false
        sleep(0).then(() => {part_5_vis.value = false})
    }


}

function show_hide_page_2_info(){
// set to default incase value changes later
hide_personal_info.value = true
hide_sole_prop_info.value = true
hide_business_info.value = true

if(investing_as.value == "individual"){
hide_personal_info.value = false
}
else if(investing_as.value == "soleProprietorship"){
hide_sole_prop_info.value = false
}
else{
hide_business_info.value = false
}
}




// ----------------------------------   format inputs  ----------------------------------


function onSSNKeyPress_individual_ssn(e) {
    sleep(5).then(() => { individual_ssn.value = individual_ssn.value.toString().replace(/[^0-9-]/g, '') })
    const key = e.keyCode || e.charCode;
    const input_len = individual_ssn.value.length
    if (key !== 8 || key !==  46) {
    if(input_len == 3 || input_len == 6){
        individual_ssn.value = individual_ssn.value + '-'
        }}}


//not working ?????
        function onSSNKeyPress_sole_prop(e) {
            sleep(5).then(() => { sole_prop_ssn.value = sole_prop_ssn.value.toString().replace(/[^0-9-]/g, '') })
    const key = e.keyCode || e.charCode;
    const input_len = sole_prop_ssn.value.length
    if (key !== 8 || key !==  46) {
    if(input_len == 3 || input_len == 6){
        sole_prop_ssn.value = sole_prop_ssn.value + '-'
        }}}



function onSSNKeyPress_controller(e) {
    sleep(5).then(() => { controller_ssn.value = controller_ssn.value.toString().replace(/[^0-9-]/g, '') })
    const key = e.keyCode || e.charCode;
    const input_len = controller_ssn.value.length
    if (key !== 8 || key !==  46) {
    if(input_len == 3 || input_len == 6){
        controller_ssn.value = controller_ssn.value + '-'
        }}}



function onSSNKeyPress_owner(e) {
    sleep(5).then(() => { owner_ssn.value = owner_ssn.value.toString().replace(/[^0-9-]/g, '') })
    const key = e.keyCode || e.charCode;
    const input_len = owner_ssn.value.length
    if (key !== 8 || key !==  46) {
    if(input_len == 3 || input_len == 6){
        owner_ssn.value = owner_ssn.value + '-'
        }}}




        function onEINKeyPress_sole_prop(e) {
            sleep(5).then(() => { sole_prop_business_ein.value = sole_prop_business_ein.value.toString().replace(/[^0-9-]/g, '') })
    const key = e.keyCode || e.charCode;
    const input_len = sole_prop_business_ein.value.length
    if (key !== 8 || key !==  46) {
    if(input_len == 2){
        sole_prop_business_ein.value = sole_prop_business_ein.value + '-'
        }}}




        function onEINKeyPress_business_ein(e) {
            sleep(5).then(() => { business_ein.value = business_ein.value.toString().replace(/[^0-9-]/g, '') })
    const key = e.keyCode || e.charCode;
    const input_len = business_ein.value.length
    if (key !== 8 || key !==  46) {
        if(input_len == 2){
        business_ein.value = business_ein.value + '-'
        }}}


        function onKeyPress_individual_zip(e) {
            sleep(5).then(() => { individual_zip.value = individual_zip.value.toString().replace(/[^0-9-]/g, '') })
}

function onKeyPress_sole_prop_zip(e) {
            sleep(5).then(() => { sole_prop_zip.value = sole_prop_zip.value.toString().replace(/[^0-9-]/g, '') })
}
    
function onKeyPress_controller_zip(e) {
            sleep(5).then(() => { controller_zip.value = controller_zip.value.toString().replace(/[^0-9-]/g, '') })
}
    
function onKeyPress_owner_zip(e) {
            sleep(5).then(() => { owner_zip.value = owner_zip.value.toString().replace(/[^0-9-]/g, '') })
}



// -------------------------------------------------------------------------------------------------------
// -------------------------------------------------------------------------------------------------------
// -------------------------------------------------------------------------------------------------------
// -------------------------------------------------------------------------------------------------------
// -------------------------------------------------------------------------------------------------------



const investor_ID = useCookie('investor_ID', cookie_options)
const fund_ID = useCookie('fund_ID', cookie_options)
const institution_ID = useCookie('institution_ID', cookie_options)
const email = useCookie('email', cookie_options)
const phone = useCookie('phone', cookie_options)


const is_accredited =  useCookie('is_accredited', cookie_options)
const exempt_from_withholding =  useCookie('exempt_from_withholding', cookie_options)



const industry_classification =  useCookie('industry_classification', cookie_options)
const business_classification =  useCookie('business_classification', cookie_options)
const business_name =  useCookie('business_name', cookie_options)
const business_ein =  useCookie('business_ein', cookie_options)
const entity_purpose_to_invest =  useCookie('entity_purpose_to_invest', cookie_options)

const controller_first_name = useCookie('controller_first_name', cookie_options)
const controller_last_name = useCookie('controller_last_name', cookie_options)
const controller_title =  useCookie('controller_title', cookie_options)
const controller_dob =  useCookie('controller_dob', cookie_options)
const controller_ssn =  useCookie('controller_ssn', cookie_options)
const controller_address = useCookie('controller_address', cookie_options)
const controller_state =  useCookie('controller_state', cookie_options)
const controller_city =  useCookie('controller_city', cookie_options)
const controller_zip =  useCookie('controller_zip', cookie_options)
const controller_country =  useCookie('controller_country', cookie_options)
// const controller_email =  useCookie('controller_email', cookie_options)

const owner_first_name =  useCookie('owner_first_name', cookie_options)
const owner_last_name =  useCookie('owner_last_name', cookie_options)
const owner_title =  useCookie('owner_title', cookie_options)
const owner_dob =  useCookie('owner_dob', cookie_options)
const owner_ssn =  useCookie('owner_ssn', cookie_options)
const owner_address =  useCookie('owner_address', cookie_options)
const owner_state =  useCookie('owner_state', cookie_options)
const owner_city =  useCookie('owner_city', cookie_options)
const owner_zip =  useCookie('owner_zip', cookie_options)
const owner_country =  useCookie('owner_country', cookie_options)
// const owner_email =  useCookie('owner_email', cookie_options)



const sole_prop_first_name = useCookie('sole_prop_first_name', cookie_options)
const sole_prop_last_name = useCookie('sole_prop_last_name', cookie_options)
const sole_prop_business_name = useCookie('sole_prop_business_name', cookie_options)
const sole_prop_business_ein = useCookie('sole_prop_business_ein', cookie_options)
const sole_prop_dob = useCookie('sole_prop_dob', cookie_options)
const sole_prop_ssn = useCookie('sole_prop_ssn', cookie_options)
const sole_prop_business_classification = useCookie('sole_prop_business_classification', cookie_options)
const sole_prop_industry_classification = useCookie('sole_prop_industry_classification', cookie_options)
const sole_prop_address = useCookie('sole_prop_address', cookie_options)
const sole_prop_state = useCookie('sole_prop_state', cookie_options)
const sole_prop_city = useCookie('sole_prop_city', cookie_options)
const sole_prop_zip = useCookie('sole_prop_zip', cookie_options)


const individual_first_name = useCookie('individual_first_name', cookie_options)
const individual_last_name = useCookie('individual_last_name', cookie_options)
const individual_dob = useCookie('individual_dob', cookie_options)
const individual_ssn = useCookie('individual_ssn', cookie_options)
const individual_address = useCookie('individual_address', cookie_options)
const individual_state = useCookie('individual_state', cookie_options)
const individual_city = useCookie('individual_city', cookie_options)
const individual_zip = useCookie('individual_zip', cookie_options)
const empolyment_status = useCookie('empolyment_status', cookie_options)
const account_selected_value = useCookie('account_selected_value_step_2', cookie_options)




const controller_state_codes = {
        name: 'controller_state',
        label: 'Controller State',
    }

const controller_country_codes = {
    name: 'controller_country',
        label: 'Controller Country',
    }

const owner_state_codes = {
    name: 'owner_state',
        label: 'Owner State',
    }

    const owner_country_codes = {
    name: 'owner_country',
        label: 'Owner Country',
    }


const individual_state_codes ={
    name: 'individual_state',
        label: 'State',
}

const sole_prop_state_codes ={
    name: 'sole_prop_state',
        label: 'State',
}

const entity_bis_class = ref({
    industry_class: industry_classification.value
})


const sole_prop_bis_class = ref({
    industry_class: sole_prop_industry_classification.value
})


watch(industry_classification, (new_industry_classification) => {
        entity_bis_class.value = {industry_class: new_industry_classification}
    })


watch(sole_prop_industry_classification, (new_industry_classification) => {
        sole_prop_bis_class.value = {industry_class: new_industry_classification}
})




const same_as_controller = ref(false)


function same_as(){
    same_as_controller.value = !same_as_controller.value
    if(same_as_controller.value == true){
        sleep(200).then(() => {owner_first_name.value = controller_first_name.value })
        sleep(400).then(() => { owner_last_name.value = controller_last_name.value })
        sleep(600).then(() => {owner_title.value = controller_title.value })
        // sleep(800).then(() => {owner_email.value = controller_email.value })
        sleep(800).then(() => {owner_dob.value = controller_dob.value })
        sleep(1000).then(() => {owner_ssn.value = controller_ssn.value })
        sleep(1200).then(() => {owner_address.value = controller_address.value })
        sleep(1400).then(() => {owner_state.value = controller_state.value })
        sleep(1600).then(() => {owner_city.value = controller_city.value })
        sleep(1800).then(() => {owner_zip.value = controller_zip.value })
        sleep(2200).then(() => {owner_country.value = controller_country.value })
    }
} 












function page_counter_next(){
    gsap.to(window, {duration: .45, scrollTo: {y: ".progress_bar", offsetY: 20}});
    if(page_count.value == 5){
        verify_modal.value = true
        open_modal()
    }
    if(page_count.value < 5){
        if(page_count.value == 2 && ( investing_as.value == "individual" || investing_as.value == "soleProprietorship")) {
        page_count.value = 5
    }
    else{
        reduce_width.value = false
        page_count.value += 1
    }
    part_to_show(page_count.value)
}

}





function check_accred(){
    if(is_accredited.value == 'no'){
        verify_modal.value = false
        accred_modal.value = true
        open_modal()
    }
}




// -------------------------------- Send API Request --------------------------------









function step_3_api_send() {

  

    if(account_selected_value.value == null){
        alert('Please select an account')
    }else if (is_accredited.value == 'no'){
        accred_modal.value = true
        verify_modal.value = false
    } else{


    const data_to_send = {
    investor_ID: investor_ID.value,
    fund_ID: fund_ID.value,
    institution_ID: institution_ID.value,
    email: email.value,
    phone: phone.value,
    account_selected_value: account_selected_value.value,

    investing_as: investing_as.value,
   is_accredited: is_accredited.value ,
 exempt_from_withholding:  exempt_from_withholding.value,

 industry_classification: industry_classification.value ,
 business_classification:  business_classification.value,
 business_name:  business_name.value,
 business_ein:  business_ein.value,
 entity_purpose_to_invest:  entity_purpose_to_invest.value,

 controller_first_name:  controller_first_name.value,
 controller_last_name: controller_last_name.value,
 controller_title: controller_title.value ,
 controller_dob:  controller_dob.value,
 controller_ssn:  controller_ssn.value,
 controller_address: controller_address.value ,
 controller_state: controller_state.value ,
 controller_city: controller_city.value ,
 controller_zip: controller_zip.value ,
 controller_country: controller_country.value ,
//  controller_email: controller_email.value ,

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
//  owner_email: owner_email.value ,


 sole_prop_first_name: sole_prop_first_name.value ,
 sole_prop_last_name: sole_prop_last_name.value ,
 sole_prop_business_name: sole_prop_business_name.value ,
 sole_prop_business_ein: sole_prop_business_ein.value ,
 sole_prop_dob: sole_prop_dob.value,
 sole_prop_ssn: sole_prop_ssn.value ,
 sole_prop_business_classification: sole_prop_business_classification.value ,
 sole_prop_industry_classification: sole_prop_industry_classification.value ,
 sole_prop_address:  sole_prop_address.value,
 sole_prop_state: sole_prop_state.value ,
 sole_prop_city: sole_prop_city.value ,
 sole_prop_zip: sole_prop_zip.value ,


 individual_first_name: individual_first_name.value,
 individual_last_name:individual_last_name.value ,
 individual_dob: individual_dob.value ,
 individual_ssn: individual_ssn.value  ,
 individual_address:  individual_address.value,
 individual_state: individual_state.value ,
 individual_city: individual_city.value ,
 individual_zip: individual_zip.value ,
 empolyment_status: empolyment_status.value ,
}

const individual_dict = {
    individual_first_name: individual_first_name.value,
 individual_last_name:individual_last_name.value ,
 individual_dob: individual_dob.value ,
 individual_ssn: individual_ssn.value  ,
 individual_address:  individual_address.value,
 individual_state: individual_state.value ,
 individual_city: individual_city.value ,
 individual_zip: individual_zip.value ,
 empolyment_status: empolyment_status.value ,
}

const sole_prop_dict = {
 sole_prop_first_name: sole_prop_first_name.value ,
 sole_prop_last_name: sole_prop_last_name.value ,
 sole_prop_business_name: sole_prop_business_name.value ,
 sole_prop_business_ein: sole_prop_business_ein.value ,
 sole_prop_dob: sole_prop_dob.value,
 sole_prop_ssn: sole_prop_ssn.value ,
 sole_prop_business_classification: sole_prop_business_classification.value ,
 sole_prop_industry_classification: sole_prop_industry_classification.value ,
 sole_prop_address:  sole_prop_address.value,
 sole_prop_state: sole_prop_state.value ,
 sole_prop_city: sole_prop_city.value ,
 sole_prop_zip: sole_prop_zip.value ,
}


const entity_dict = {
    industry_classification: industry_classification.value ,
 business_classification:  business_classification.value,
 business_name:  business_name.value,
 business_ein:  business_ein.value,
 entity_purpose_to_invest:  entity_purpose_to_invest.value,
 controller_first_name:  controller_first_name.value,
 controller_last_name: controller_last_name.value,
 controller_title: controller_title.value ,
 controller_dob:  controller_dob.value,
 controller_ssn:  controller_ssn.value,
 controller_address: controller_address.value ,
 controller_state: controller_state.value ,
 controller_city: controller_city.value ,
 controller_zip: controller_zip.value ,
 controller_country: controller_country.value ,
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



//a for loop to check if any of the values are empty
// if so, alert the user to fill out the form
// else, send the data to the backend
if (investing_as.value == 'individual'){
for (const [key, value] of Object.entries(individual_dict)) { 
    console.log(key, value);  
    if (value == ''){
            alert('Please fill out the ___ ' + key + ' ___')
            input_error.value = true
    } else if (key == 'individual_zip' && value.length != 5){
        alert('Check Zip Code')
        input_error.value = true
        }
    else if (key == 'sole_prop_ssn' && value.length != 11){
        alert('Check SSN Number')
        input_error.value = true
        }     
        else if (key == 'individual_address'){
            if (!regex.test(value)) {
            alert('Address must contain at least one number and letter')
        input_error.value = true
        }}
    else if (key == 'individual_dob' && value.length != 10){
        alert('Check Date of Birth')
    }
    else if( key == 'individual_dob' ){
            if( new Date(Date.parse(value.replace(/-/g, " "))) <= new Date(Date.parse('1900-01-01'.replace(/-/g, " "))) || new Date(Date.parse(value.replace(/-/g, " "))) >= new Date(Date.parse('2005-01-01'.replace(/-/g, " "))) ){
                alert('Please input a valid date of birth that is after 1900 and before 2005')
                input_error.value = true
            }
        }
}
}
else if (investing_as.value == 'soleProprietorship'){
for (const [key, value] of Object.entries(sole_prop_dict)) {   
    console.log(key, value);
        if (value == ''){
        alert('Please fill out the ___ ' + key + ' ___')
        input_error.value = true
        }
       else if (key == 'sole_prop_business_ein' && value.length != 10){
        alert('Check EIN Number')
        input_error.value = true
        }
       else if (key == 'sole_prop_ssn' && value.length != 11){
        alert('Check SSN Number')
        input_error.value = true
        }
        else if (key == 'sole_prop_zip' && String(value).length != 5){
        alert('Check Zip Code')
        input_error.value = true
        }
        else if (key == 'sole_prop_address'){
            if (!regex.test(value)) {
        alert('Address must contain at least one number and letter')
        input_error.value = true
        }}
        else if (key == 'sole_prop_dob' && value.length != 10){
        alert('Check Date of Birth')
        }
        else if( key == 'sole_prop_dob' ){
            if( new Date(Date.parse(value.replace(/-/g, " "))) <= new Date(Date.parse('1900-01-01'.replace(/-/g, " "))) || new Date(Date.parse(value.replace(/-/g, " "))) >= new Date(Date.parse('2005-01-01'.replace(/-/g, " "))) ){
                alert('Please input a valid date of birth that is after 1900 and before 2005')
                input_error.value = true
            }
        }
        }
    }


else if (investing_as.value == 'corporation' || investing_as.value == 'llc' || investing_as.value == 'partnership'){
for (const [key, value] of Object.entries(entity_dict)) {   
    console.log(key, value);
    if (value == ''){
        alert('Please fill out the ___ ' + key + ' ___')
        input_error.value = true
        }
        else if (key == 'business_ein' && value.length != 10){
        alert('Check EIN Number')
        input_error.value = true
        }
        else if (key == 'controller_ssn' && value.length != 11){
        alert('Check Controller SSN Number')
        input_error.value = true
        }
        else if (key == 'owner_ssn' && value.length != 11){
        alert('Check Controller SSN Number')
        input_error.value = true
        }
        else if (key == 'controller_zip' && String(value).length != 5){
        alert('Check Controller Zip Code')
        input_error.value = true
        }
        else if (key == 'owner_zip' && String(value).length != 5){
        alert('Check Owner Zip Code')
        input_error.value = true
        }
        else if (key == 'controller_address'){
            if (!regex.test(value)) {
        alert('Controller address must contain at least one number and letter')
        input_error.value = true
        }}
        else if (key == 'owner_address'){
            if (!regex.test(value)) {
        alert('Owner address must contain at least one number and letter')
        input_error.value = true
        }}
        else if( key == 'controller_dob' ){
        if( new Date(Date.parse(value.replace(/-/g, " "))) <= new Date(Date.parse('1900-01-01'.replace(/-/g, " "))) || new Date(Date.parse(value.replace(/-/g, " "))) >= new Date(Date.parse('2005-01-01'.replace(/-/g, " "))) ){
                alert('Please input a Controller valid date of birth that is after 1900 and before 2005')
                input_error.value = true
            }
        }
        else if( key == 'owner_dob' ){
        if( new Date(Date.parse(value.replace(/-/g, " "))) <= new Date(Date.parse('1900-01-01'.replace(/-/g, " "))) || new Date(Date.parse(value.replace(/-/g, " "))) >= new Date(Date.parse('2005-01-01'.replace(/-/g, " "))) ){
            alert('Please input a Owner valid date of birth that is after 1900 and before 2005')
            input_error.value = true
            }
        }
    }
}
else{
    console.log('___ xxx ' + key + ' xxx ___')
    input_error.value = false
}



if (input_error.value == false){

    start_loader.value = true;

    fetch(`${config.flask_url}/api/invest_flow/step_3/`, {
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
        cicle_tansition.value.animation_and_route("step_4");

    })
    .catch(error => {
        verify_modal.value = false
        contact_modal.value = true
        open_modal()
        start_loader.value = false;
        console.error('There was an error!', error);
    });

} else{
    input_error.value = false
    start_loader.value = false;
    console.error('There was an error no send');
}
}
}



function transition_and_route(route_to) {
cicle_tansition.value.animation_and_route(route_to);
}










// <!-- -------------------------- modal popup --------------------------------- -->
// <!-- -------------------------- modal popup --------------------------------- -->

const modal_exit_anim = ref(true)
const modal_exit_display = ref(true)



function modal_leave(){
    verify_modal.value = false
    contact_modal.value = false
    accred_modal.value = false
    modal_exit_anim.value = true
    sleep(1100).then(() => {
    modal_exit_display.value = true
    });
}

const modal = ref(null)


function open_modal(){
   
    modal_exit_display.value = false
    sleep(100).then(() => {
    modal_exit_anim.value = false
    });
}






// <!-- -------------------------- modal popup --------------------------------- -->
// <!-- -------------------------- modal popup --------------------------------- -->







const dwolla_customer_created = useCookie('dwolla_customer_created', cookie_options)

const first_name = useCookie('first_name', cookie_options)
const last_name = useCookie('last_name', cookie_options)

onMounted(() => {
 if(dwolla_customer_created.value == true){
    sleep(3000).then(() => {
    alert('You already submitted this information. Continue forward.')
    cicle_tansition.value.animation_and_route("step_4");})}
 // autofill 

controller_first_name.value = first_name.value
controller_last_name.value = last_name.value
// controller_email.value = email.value
sole_prop_first_name.value = first_name.value
sole_prop_last_name.value = last_name.value
individual_first_name.value = first_name.value
individual_last_name.value = last_name.value


})













</script>


<style scoped>

.hide_it{
    display:none
}
.is_active{
    display:block !important;
}



.select_account_text{
color:#000;
margin-left:10%;
margin-bottom:5%;
margin-top:5%
}
.white_background{
    background-color: #fff;
    height:100vh;
    width:100vw;
    position:fixed;
    top:0;
    left:0;
    z-index:0
}


.form_title{
    color:#000;
    margin-left:14%;
    z-index:10;
    position: relative;
    display: block;
}



.form_grid_1{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: repeat(2, 1fr);
grid-column-gap: 0px;
grid-row-gap: 0px;
z-index: 10;
width:80%;
margin-left:10%;
}


.form_grid_2{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: repeat(2, 1fr);
grid-column-gap: 0px;
grid-row-gap: 0px;
z-index: 10;
width:80%;
margin-left:10%;
}


.form_grid_3{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: repeat(5, 1fr);
grid-column-gap: 0px;
grid-row-gap: 0px;
z-index: 10;
width:80%;
margin-left:10%;
opacity:1
}



.form_grid_4{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: repeat(4, 1fr);
grid-column-gap: 0px;
grid-row-gap: 0px;
z-index: 10;
width:80%;
margin-left:10%;
}

.form_grid_5{
z-index: 10;
width:60%;
margin-left:20%;
}


.confirm_text{
    color:#000;
    line-height: 1.5;
}

.wide_label{
    margin-left:40px;
    margin-top:-30px
}

.wide_select{
    margin-left:-95px;
    margin-top:70px
}


.form_pagenation{
    display: flex;
    justify-content: center;
width:80%;
margin-left:10%;
margin-top:5%
}

.prev_button{
    width:100%;
    padding:10px 20px;
    background-color:rgb(25, 120, 237);
    color:#fff;
    text-align: center;
    border-radius:100px;
    cursor: pointer;
    margin:50px;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}

.prev_button:hover{
  box-shadow: 0px 10px 15px rgb(25, 120, 237, .5);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
} 

.next_button{
    width:100%;
    padding:10px 20px;
    background-color:rgb(25, 120, 237);
    color:#fff;
    text-align: center;
    border-radius:100px;
    cursor: pointer;
    margin:50px;
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


.reduce_width{
    width:50%
}

.progress_bar_container{
 width:70%;
 height:20px;
margin-top:125px;
margin-left:0px;
margin-right:0px;
margin-bottom:50px;
z-index:0;
border:#0a00ca solid 1px;
margin-left:15%;
border-radius:20px;
}

.progress_bar{
    width:v-bind(progress_width);
    height:20px;
    z-index:0;
    border-radius:20px;
    background: rgb(25, 120, 237);
    transition:all 2s ease-in-out;

/* 
-webkit-animation: AnimationName 5s ease infinite;
    -moz-animation: AnimationName 5s ease infinite;
    -o-animation: AnimationName 5s ease infinite;
    animation: AnimationName 5s ease infinite;

    animation-fill-mode: forwards;
  animation-timing-function: linear;

  background-position: 0 100%; */
}




.progress_bar:before{
-webkit-mask:linear-gradient(#fff 0 0);
          mask:linear-gradient(#fff 0 0);

}

@-webkit-keyframes AnimationName {
    0%{background-position:0% 51%}
    50%{background-position:100% 50%}
    100%{background-position:0% 51%}
}
@-moz-keyframes AnimationName {
    0%{background-position:0% 51%}
    50%{background-position:100% 50%}
    100%{background-position:0% 51%}
}
@-o-keyframes AnimationName {
    0%{background-position:0% 51%}
    50%{background-position:100% 50%}
    100%{background-position:0% 51%}
}
@keyframes AnimationName {
    0%{background-position:0% 51%}
    50%{background-position:100% 50%}
    100%{background-position:0% 51%}
}


.part_1_container{
    display:none;
    opacity:0;
    margin-right:10%;
    margin-left:-10%;
    margin-bottom:-10%
}


.part_2_container{
    display:none;
    opacity:0;
    margin-right:10%;
    margin-left:-10%
}

.part_3_container{
    display:none;
    opacity:0;
    margin-right:10%;
    margin-left:-10%
}

.part_4_container{
    display:none;
    opacity:0;
    margin-right:10%;
    margin-left:-10%
}

.part_5_container{
    display:none;
    opacity:0;
    margin-right:10%;
    margin-left:-10%
}


.visibility_animation{
    margin-right:0% !important;
    margin-left:0% !important;
    opacity: 1 !important;
        transition: all .7s ease-in-out;
}



.same_as_button{
    width:200px;
    padding:5px 0px;
    font-size: 15px;
    background-color:#010101;
    color:#fff;
    text-align: center;
    border-radius:10px;
    cursor: pointer;
    margin-left:13.5%;
    margin-top:-8px;
    margin-bottom:15px;
    transition: all .35s ease-in-out;
    /* border: 2px solid rgba(25, 120, 237, 0.7); */
}

.same_as_button:hover{
    background-color:rgba(25, 120, 237, 0.7);
    transition: all .35s ease-in-out;
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
}

.designation_show{
    margin-top:-12%;
    opacity:1;
    visibility: visible;
    transition: all .35s ease-in-out;
}
.designation_hover{
    font-size:13px;
    padding:2px 7px;
    border: 1px solid rgba(0,0,0, 0.1);
    color: rgba(0,0,0, 0.7);
    border-radius:100%;
    cursor:pointer;
    transition: all .35s ease-in-out;
}

.designation_hover:hover{
    background-color:rgba(25, 120, 237, 0.3);
    color:#fff;
    transition: all .35s ease-in-out;
}


.extra_label_format{
    color:#000;
    width:80%;
    font-size:1.25vw;
    margin-left:10%;
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



    .no_return_text{
        color:#fff;
        width:50%;
        text-align:center;
        text-decoration: underline;
        text-decoration-color: rgba(255, 0, 0, 0.7);
        text-underline-offset: 4px;
        text-decoration-thickness: 1px;
    }

    .no_return_text_contact{
        color:#fff;
        text-align:center;
        text-decoration: underline;
        text-decoration-color: rgba(255, 0, 0, 0.7);
        text-underline-offset: 4px;
        text-decoration-thickness: 1px;
        font-size:15px
    }

    .accred_modal_text{
        color:#fff;
        text-align:center;
        font-size:15px;
    }


    .on_demand_text{
        color:#000;
        width:50%;
        margin-left:25%;
        text-align:center;
        margin-top:2%;
        font-size:12px;
    }



    @media only screen and (min-width: 0px) and (max-width: 380px) {

        .next_button{
    width:40%;
    height:40px;
    margin-top:12%;
    font-size:3.5vw;
}

.next_button{
    width:50%;
    height:30px;
    margin-top:15%;
    font-size:3.5vw;
    margin-left: 25%;
}

.withholding_input{
    width:125%;
}

.withholding_label{
    width:125%;
}

}




@media only screen and (min-width: 380px) and (max-width: 576px) {



.form_grid_1{
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(2, 1fr);
width:60%;
margin-left:5%;
grid-row-gap: 0px;
}


.form_grid_2{
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(4, 1fr);
width:90%;
margin-left:5%;
grid-row-gap: 20px;
}


.form_grid_3{
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(10, 1fr);
width:90%;
margin-left:5%;
grid-row-gap: 20px;
}



.form_grid_4{
    display: grid;
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(8, 1fr);
width:90%;
margin-left:5%;
grid-row-gap: 20px;
}

.form_grid_5{
z-index: 10;
width:100%;
margin-left:0%;
}

.form_pagenation{
margin-top:15%;
margin-bottom:35%
}



.prev_button{
    width:100%;
    padding:10px 50px;
    margin:10px;
    font-size:14px
}

.next_button{
    width:100%;
    padding:10px 50px;
    margin:10px;
    font-size:14px
}

.extra_label_format{
    font-size:2.5vw;
}


.withholding_input{
    width:125%;
}

.withholding_label{
    width:125%;
}

}



@media only screen and (min-width: 576px) and (max-width: 768px) {

    .withholding_input{
    width:125%;
}

.withholding_label{
    width:125%;
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
    width:50%;
    height:420px;
    background-color:#fff;
    z-index:10;
    border-radius:20px;
    margin-top:-50px;
    border: rgb(25, 120, 237) solid 3px;
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


.modal_info_step_3{
    font-size:22px;
    font-weight:600;
    color:#fff;
    margin-left:10%;
    width:80%;
    text-align:center;
    margin-top:6%;
    line-height: 1.75;
}


.no_return_text{
        color:#fff;
        text-align:center;
        text-decoration: underline;
        text-decoration-color:rgb(218, 43, 43);
        text-underline-offset: 4px;
        text-decoration-thickness: 2px;
    }


.no_return_text_contact{
        color:#fff;
        text-align:center;
        text-decoration: underline;
        text-decoration-color:rgb(218, 43, 43);
        text-underline-offset: 4px;
        text-decoration-thickness: 2px;
        font-size:15px;
        width:100%;
        margin-top:-10%
    }
    
    .accred_modal_text{
        color:#fff;
        text-align:center;
        font-size:15px;
        width:100%;
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



.modal_flex{
    display:flex;
    justify-content:center;
    align-items:center;
    margin-top:10%;
}

.modal_next_button{
    width:30%;
    height:20px;
    padding:5px 0px;
    background-color:rgb(25, 120, 237);
    color:#fff;
    margin-left:4%;
    margin-right:4%;
    text-align: center;
    border-radius:100px;
    cursor: pointer;
    margin-top:-2%;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}

.modal_next_button:nth-of-type(1){
font-size:80%;
line-height:1.5;
box-shadow: 0px 5px 10px rgba(128, 0, 0, 0.15);
}
.modal_next_button:nth-of-type(2){
    box-shadow: 0px 5px 10px rgba(0, 128, 0, 0.2);
}

.modal_next_button:hover{
  box-shadow: 0px 10px 15px rgb(25, 120, 237, .6);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
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
    


 /* ------------------- modal ------------------- */
 /* ------------------- modal ------------------- */
 /* ------------------- modal ------------------- */


</style>