<template>
    



    <div class="dark_mode">

        <div class="background_blur"></div>
        <div class="z_scope">
        <InvestorDashDashboardHeader v-bind="active_page"/>
        <InvestorDashLeftSidebar/>
    </div>
            <GSAPScrollSmoother>

   
          <div class="navigation_header">
            <div class="nav_menu_title">Re-Verify KYC Benificial Owner Info</div>
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



                <h5 class="form_title">Beneficial Owner Information <span class="designation_hover" @mouseover="designation_show = true">?</span></h5>
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


const owner_country_codes = {
    name: 'owner_country',
        label: 'Owner Country',
    }


    const owner_state_codes = {
    name: 'owner_state',
        label: 'Owner State',
    }

const designation_show = ref(false)


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






function owner_submit() {

const data_to_send = {
// investor_ID: investor_ID.value,
// fund_ID: fund_ID.value,
// institution_ID: institution_ID.value,

token: useRoute().query.token,
owner_first_name: owner_first_name.value,
owner_last_name:  owner_last_name.value,
owner_title: owner_title.value ,
owner_dob: owner_dob.value ,
owner_ssn: owner_ssn.value ,
owner_address: owner_address.value ,
owner_state: owner_state.value ,
owner_city: owner_city.value ,
owner_zip: owner_zip.value ,
owner_country: owner_country.value 
}





fetch(`${config.flask_url}/api/dwolla_reverification/reverify_owner/`, {
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
z-index: 1000;
position: relative;
}

.main_content_container{
width:90%; 
margin-right:10%;
margin-left:5%;
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
padding-right:50px;
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











