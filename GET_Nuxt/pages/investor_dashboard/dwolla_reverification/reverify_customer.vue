<template>
    


    <div class="dark_mode">
        <div class="background_blur"></div>
        <div class="z_scope">
        <InvestorDashDashboardHeader v-bind="active_page"/>
        <InvestorDashLeftSidebar/>
    </div>
            <GSAPScrollSmoother>
   
          <div class="navigation_header">
            <div class="nav_menu_title">Re-Verify KYC Info</div>
            <!-- <div class="header_menu">
              <div class="navigation_menu is-active" href="#">xxx</div>
              <div class="navigation_menu" href="#">xxx</div>
              <div class="navigation_menu" href="#">xxx</div>
            </div> -->
          </div>
          <div class="dashboard_inner_section">
              <div class="main_content_container">


               




                <div style="padding-bottom:10vh"></div>







<div class="form_container">




                <div class="progress_bar_container">
<div class="progress_bar"></div>
</div>

<div class="part_1_container" :class="{is_active:part_1, visibility_animation:part_1_vis}">
<div class="form_grid_1">








    <div class="input_wrap">
            <select v-model="investing_as"  required class="select_black">
                    <option value="" disabled selected hidden></option>
                    <option value="individual">Individual</option>
                    <option value="corporation">Corporation</option>
                    <option value="llc">LLC</option>
                    <option value="partnership">Partnership</option>
                    <option value="soleProprietorship">Sole Proprietorship</option>
            </select>
                <label class="label_black">Investing As:</label>
        </div>

        <div class="input_wrap">
        <input v-model="customer_email" class="input_black" placeholder=' ' required/>
        <label class="label_black">Email</label>
 </div>



      

</div>
</div>






<div class="part_2_container" :class="{is_active:part_2, visibility_animation:part_2_vis}">







<div :class="{hide_it:hide_business_info}">
    <h5 class="form_title">Business Information</h5>
<div class="form_grid_2">

    <InvestFlowIndustryClassificationBlack v-model:industry_classification="industry_classification"/>

<InvestFlowBusinessClassificationBlack v-bind="entity_bis_class"  v-model:business_classification="business_classification"/>


<div class="input_wrap">
        <input v-model="business_name" class="input_black" placeholder=' ' required/>
        <label class="label_black">Business Name</label>
 </div>


 <div class="input_wrap">
        <input @keypress="onEINKeyPress_business_ein" @keyup="remove_chrs('business_ein')" v-model="business_ein" class="input_black" placeholder=' ' type="text" maxlength="10" required/>
        <label class="label_black">Business EIN</label>
</div>








</div>
</div>





<div :class="{hide_it:hide_sole_prop_info}">
    <h5 class="form_title">Sole Proprietorship Info</h5>
    <div class="form_grid_2">


        <div class="input_wrap">
            <input v-model="sole_prop_first_name" class="input_black" placeholder=' ' required/>
            <label class="label_black">First Name</label>
     </div>


     <div class="input_wrap">
            <input v-model="sole_prop_last_name" class="input_black" placeholder=' ' type="text" required/>
            <label class="label_black">Last Name</label>
    </div>


<InvestFlowIndustryClassificationBlack v-model:industry_classification="sole_prop_industry_classification"/> 

<InvestFlowBusinessClassificationBlack v-bind="sole_prop_bis_class" v-model:business_classification="sole_prop_business_classification"/>




<div class="input_wrap">
        <input v-model="sole_prop_business_name" class="input_black" placeholder=' ' required/>
        <label class="label_black">Business Name</label>
 </div>


 <div class="input_wrap">
        <input @keypress="onEINKeyPress_sole_prop" @keyup="remove_chrs('sole_prop_business_ein')" v-model="sole_prop_business_ein" class="input_black" placeholder=' ' type="text" maxlength="10" required/>
        <label class="label_black">Business EIN</label>
</div>

<div class="input_wrap">
        <input v-model="sole_prop_dob" class="input_black input_date" placeholder=' ' type="date" required/>
        <label  class="label_black">Date of Birth</label>
</div>


<div class="input_wrap">
        <input @keypress="onSSNKeyPress_sole_prop" @keyup="remove_chrs('sole_prop_ssn')" maxlength="11" v-bind="sole_prop_ssn" class="input_black" placeholder=' ' type="text" required/>
        <label class="label_black">Social Security Number</label>
</div>

<div class="input_wrap">
            <input v-model="sole_prop_address" class="input_black" placeholder=' ' type="text" required/>
            <label  class="label_black">Address</label>
    </div>

    <InvestFlowStateCodesSelectBlack v-bind="sole_prop_state_codes" v-model:state_value="sole_prop_codes"/>


    <div class="input_wrap">
            <input v-model="sole_prop_city" class="input_black" placeholder=' ' type="text" required/>
            <label  class="label_black">City</label>
    </div>

    <div class="input_wrap">
            <input v-model="sole_prop_zip" class="input_black" placeholder=' ' type="text" @keyup="remove_chrs('sole_prop_zip')" required/>
            <label  class="label_black">Zip</label>
    </div>



    

</div>

</div>



<div :class="{hide_it:hide_personal_info}">
    <h5 class="form_title">Individual Information</h5>
    <div class="form_grid_2">




    <div class="input_wrap">
            <input v-model="individual_first_name" class="input_black" placeholder=' ' required/>
            <label class="label_black">First Name</label>
     </div>


     <div class="input_wrap">
            <input v-model="individual_last_name" class="input_black" placeholder=' ' type="text" required/>
            <label class="label_black">Last Name</label>
    </div>

    <div class="input_wrap">
                <input v-model="individual_dob" class="input_black input_date" placeholder=' ' type="date" required/>
                <label  class="label_black">Date of Birth</label>
    </div>

    <div class="input_wrap">
            <input @keypress="onSSNKeyPress_individual_ssn" @keyup="remove_chrs('individual_ssn')" v-model="individual_ssn" class="input_black" placeholder=' ' type="text" maxlength="11" required/>
            <label  class="label_black">SSN</label>
    </div>


    <div class="input_wrap">
            <input v-model="individual_address" class="input_black" placeholder=' ' type="text" required/>
            <label  class="label_black">Address</label>
    </div>

    <InvestFlowStateCodesSelectBlack v-bind="individual_state_codes" v-model:state_value="individual_state"/>


    <div class="input_wrap">
            <input v-model="individual_city" class="input_black" placeholder=' ' type="text" required/>
            <label  class="label_black">City</label>
    </div>

    <div class="input_wrap">
            <input v-model="individual_zip" class="input_black" placeholder=' ' type="text" @keyup="remove_chrs('individual_zip')" maxlength="5" required/>
            <label  class="label_black">Zip</label>
    </div>



</div>



</div>



</div>




<div class="part_3_container" :class="{is_active:part_3, visibility_animation:part_3_vis}">


<h5 class="form_title">Controller Information <span class="designation_hover" @mouseover="designation_show = true">?</span></h5>
<p class="designation_text" :class="{designation_show: designation_show}" @mouseleave="designation_show = false">A controller is a natural person who holds significant responsibilities to control, manage or direct a company or other corporate entity (i.e. CEO, CFO, General Partner, President, etc). A company may have more than one controller, but only one controller’s information must be collected.</p>


<div class="form_grid_3">




<div class="input_wrap">
            <input v-model="controller_first_name" class="input_black" placeholder=' ' required/>
            <label class="label_black">Controller First Name</label>
     </div>


     <div class="input_wrap">
            <input v-model="controller_last_name" class="input_black" placeholder=' ' type="text" required/>
            <label class="label_black">Controller Last Name</label>
    </div>

    <div class="input_wrap">
            <input v-model="controller_title" class="input_black" placeholder=' ' type="text" required/>
            <label  class="label_black">Controller Title</label>
    </div>

    <div class="input_wrap">
                <input v-model="controller_dob" class="input_black input_date" placeholder=' ' type="date" required/>
                <label  class="label_black">Controller Date of Birth</label>
    </div>

    <div class="input_wrap">
            <input @keypress="onSSNKeyPress_controller" @keyup="remove_chrs('controller_ssn')" v-model="controller_ssn" class="input_black" placeholder=' ' type="text" maxlength="11" required/>
            <label  class="label_black">Controller SSN</label>
    </div>


    <div class="input_wrap">
            <input v-model="controller_address" class="input_black" placeholder=' ' type="text" required/>
            <label  class="label_black">Controller Address</label>
    </div>

    <InvestFlowStateCodesSelectBlack v-bind="controller_state_codes" v-model:state_value="controller_state"/>


    <div class="input_wrap">
            <input v-model="controller_city" class="input_black" placeholder=' ' type="text" required/>
            <label  class="label_black">Controller City</label>
    </div>

    <div class="input_wrap">
            <input v-model="controller_zip" class="input_black" placeholder=' ' type="text"  @keyup="remove_chrs('controller_zip')" maxlength="5"  required/>
            <label  class="label_black">Controller Zip</label>
    </div>

    <InvestFlowCountryCodesSelectBlack v-bind="controller_country_codes" v-model:country_value="controller_country"/>

    

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

</div>



   <!-- ------------------------------------------------------------------------------------- -->

    <div class="form_pagenation">
        <div class="prev_button" :class="{hide_it:is_hidden}" @click="page_counter_prev">Prev</div>
        <div class="next_button" :class="{reduce_width:reduce_width}" @click="page_counter_next">{{ next_text }}</div>
    </div>






</div>






<div style="padding-bottom:15vh"></div>























                

              </div>
        </div>
         <!-- div for footer scroll over -->
        <div style="padding-bottom:1px"></div>
    </GSAPScrollSmoother>
    <InvestorDashDashboardFooter/>
</div>





</template>






<script setup>


import { form_store } from "~/stores/form_store.js"

const form_stuff = form_store()
const config = useRuntimeConfig()


const is_hidden = ref(true)
const next_text = ref("Next")
const part_1 = ref(true)
const part_2 = ref(false)
const part_3 = ref(false)
const part_4 = ref(false)
const page_count = ref(1)
const progress_width = ref("0%")
const reduce_width = ref(true)

const investing_as = ref("")
const hide_business_info = ref(true)
const hide_sole_prop_info = ref(true)
const hide_personal_info = ref(true)

const part_1_vis = ref(true)
const part_2_vis = ref(false)
const part_3_vis = ref(false)
const part_4_vis = ref(false)

const flow_bar_start = ref(true)

const designation_show = ref(false)

const cicle_tansition = ref(null);
const start_loader = ref(false);


const step_circles = {
    current_num: 3
}




onMounted(() => {

    progress_width.value = "20%"
    flow_bar_start.value = false
})





function page_counter_prev(){
    if(page_count.value==4){
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



// sleep time expects milliseconds
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}


function part_to_show(count){
    if(count == 1){
        next_text.value = "Next"
        is_hidden.value = true
        part_1.value = true
        sleep(0).then(() => {part_1_vis.value = true})
        progress_width.value = "25%"
    }else{
        part_1.value = false
        sleep(0).then(() => {part_1_vis.value = false})
    }
    if(count == 2){
        show_hide_page_2_info()
        is_hidden.value = false
        part_2.value = true
        sleep(0).then(() => {part_2_vis.value = true})
        if(investing_as.value == "individual" || investing_as.value == "soleProprietorship") {
        page_count.value = 2
        next_text.value = "Submit"
        progress_width.value = "80%"
    } else{
        next_text.value = "Next"
        progress_width.value = "50%"
    }
    }else{
        part_2.value = false
        sleep(0).then(() => {part_2_vis.value = false})
    }

    if(count == 3){
        next_text.value = "Next"
        part_3.value = true
        sleep(0).then(() => {part_3_vis.value = true})
        is_hidden.value = false
        progress_width.value = "75%"
    }else{
        part_3.value = false
        sleep(0).then(() => {part_3_vis.value = false})
    }

    if(count == 4){
        next_text.value = "Submit"
        part_4.value = true
        sleep(0).then(() => {part_4_vis.value = true})
        is_hidden.value = false
        progress_width.value = "100%"
    }else{
        part_4.value = false
        sleep(0).then(() => {part_4_vis.value = false})
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
// -------------------------------------------------------------------------------------------------------
// -------------------------------------------------------------------------------------------------------
// -------------------------------------------------------------------------------------------------------
// -------------------------------------------------------------------------------------------------------



const investor_ID = ref(form_stuff.investor_ID)
const fund_ID = ref(form_stuff.fund_ID)
const institution_ID = ref(form_stuff.institution_ID)




const customer_email = ref()



const industry_classification = ref("")
const business_classification = ref("")
const business_name = ref("")
const business_ein = ref("")

const controller_first_name = ref()
const controller_last_name = ref()
const controller_title = ref("")
const controller_dob = ref("")
const controller_ssn = ref("")
const controller_address = ref("")
const controller_state = ref("")
const controller_city = ref("")
const controller_zip = ref("")
const controller_country = ref("")

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


const sole_prop_first_name = ref()
const sole_prop_last_name = ref()
const sole_prop_business_name = ref("")
const sole_prop_business_ein = ref("")
const sole_prop_dob = ref("")
const sole_prop_ssn = ref("")
const sole_prop_business_classification = ref("")
const sole_prop_industry_classification = ref("")
const sole_prop_address = ref("")
const sole_prop_state = ref("")
const sole_prop_city = ref("")
const sole_prop_zip = ref("")

const individual_first_name = ref()
const individual_last_name = ref()
const individual_dob = ref("")
const individual_ssn = ref("")
const individual_address = ref("")
const individual_state = ref("")
const individual_city = ref("")
const individual_zip = ref("")



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
    owner_first_name.value = controller_first_name.value
 owner_last_name.value = controller_last_name.value
 owner_title.value = controller_title.value
 owner_dob.value = controller_dob.value
 owner_ssn.value = controller_ssn.value
 owner_address.value = controller_address.value
 owner_state.value = controller_state.value
 owner_city.value = controller_city.value
 owner_zip.value = controller_zip.value
 owner_country.value = controller_country.value
    }
} 












function page_counter_next(){
    if(page_count.value == 4){
        form_stuff.update_info_step_1(controller_first_name.value, controller_last_name.value)
        step_3_api_send()
    }
    if(page_count.value < 4){
        if(page_count.value == 2 && ( investing_as.value == "individual" || investing_as.value == "soleProprietorship")) {
        step_3_api_send()
    }
    else{
        reduce_width.value = false
        page_count.value += 1
    }
    part_to_show(page_count.value)
}

}








// -------------------------------- Send API Request --------------------------------









function step_3_api_send() {

    start_loader.value = true;



    const data_to_send = {
    investor_ID: investor_ID.value,
    fund_ID: fund_ID.value,
    institution_ID: institution_ID.value,
    email: customer_email.value,

    investing_as: investing_as.value,

 industry_classification: industry_classification.value ,
 business_classification:  business_classification.value,
 business_name:  business_name.value,
 business_ein:  business_ein.value,

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
}





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
        // transition_and_route('step_3')
        cicle_tansition.value.animation_and_route("/investor_dashboard/investor_home");

    })
    .catch(error => {
        start_loader.value = false;
        alert('Error')
        console.error('There was an error!', error);
    });
}







const active_page = {is_active: "documents_active"}


</script>













<style scoped>






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











.hide_it{
    display:none
}
.is_active{
    display:block !important;
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
    color:#fff;
    margin-left:14%;
    z-index:10;
    position: relative;
    display: block;
    mix-blend-mode: normal;
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
    margin-left:-10%
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
    font-size:12px
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





    .form_container{
        background-color: #000;
        border-radius:50px;
        padding-top:5%
    }




@media only screen and (min-width: 0px) and (max-width: 576px) {

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












































/* ------------------------ CSS For The Dashboard --------------------------------------- */
/* ------------------------ CSS For The Dashboard --------------------------------------- */
/* ------------------------ CSS For The Dashboard --------------------------------------- */
/* ------------------------ CSS For The Dashboard --------------------------------------- */
/* ------------------------ CSS For The Dashboard --------------------------------------- */




.dashboard_inner_section{
margin-bottom: 450px; 
width:calc(100vw - 250px); 
margin-left:250px;
border-bottom: rgba(75, 75, 75, 0.1) .5px solid;
background-color:var(--inner_background);
}

.main_content_container{
width:90%; 
margin-right:10%;
margin-left:5%
}


.navigation_header {
display: flex;
align-items: center;
border-bottom: 1px solid var(--border-color);
height: 58px;
flex-shrink: 0;
margin-top:80px;
width:calc(100vw - 250px); 
margin-left: 250px;
background-color: #000000cc;
}



.nav_menu_title {
text-decoration: none;
color: var(--theme-color);
padding: 0 30px;
margin-left:25px;
padding-right:50px
}



::-webkit-scrollbar {
width: 3px;
border-radius: 10px;
}

::-webkit-scrollbar-thumb {
background: rgba(0, 149, 255, 0.676);
border-radius: 10px;
}


@media only screen and (min-width: 0px) and (max-width: 576px) {
    .dashboard_inner_section{
width:calc(100vw - 20px); 
margin-left:20px;
}

.navigation_header {
    width:100vw; 
margin-left:20px;
}

}

@media only screen and (min-width: 576px) and (max-width: 768px) {
    .dashboard_inner_section{
width:calc(100vw - 20px); 
margin-left:20px;
}

.navigation_header {
    width:100vw; 
margin-left:20px;
}

}

@media only screen and (min-width: 768px) and (max-width: 992px) {

    .dashboard_inner_section{
width:calc(100vw - 180px); 
margin-left:180px;
}

.navigation_header {
    width:100vw; 
margin-left:150px;
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











