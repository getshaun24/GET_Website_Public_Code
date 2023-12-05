
<template>
    

    <CircleTransition ref="cicle_tansition"/>

    <div class="dark_mode" style="overflow-x:hidden">
        <InvestorDashDashboardHeader v-bind="active_page" />
        <InvestorDashLeftSidebar v-bind="active_page"/>
        <GSAPScrollSmoother>
            
            <div class="navigation_header">
                <div class="nav_menu_title">Welcome, {{ full_name }} </div>
                <!-- <div class="header_menu">
                    <div class="navigation_menu is-active" href="#">xxx</div>
                    <div class="navigation_menu" href="#">xxx</div>
                    <div class="navigation_menu" href="#">xxx</div>
                </div> -->
            </div>
            <div class="dashboard_inner_section">
                <div class="main_content_container">

<div class="invest_container">

    <div class="input_wrap dial_wrap">
            <select v-model="instant_selected_fund"   class="select_black dial_select">
                    <option value="" disabled selected hidden></option>
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
                <label class="label_black dial_label">Fund To Invest In:</label>
        </div>



                    <InvestDial/>


                    <button @click="new_instant_invest" class="next_button">Next</button>
                </div>



                </div>
            </div>
            
            <!-- div for footer scroll over -->
            <div style="padding-bottom:1px"></div>
            
        </GSAPScrollSmoother>
        <InvestorDashDashboardFooter/>
        
    </div>
    
    
    
    
    
</template>






<script setup>
import image1 from '~/assets/content/investments/invest_1.png'
import image2 from '~/assets/content/investments/invest_4.jpg'
import image3 from '~/assets/content/investments/invest_3.png'
import image4 from '~/assets/content/investments/invest_6.jpg'


onBeforeMount(() => { authCookieRefresh() })

const config = useRuntimeConfig()


        
const cookie_options = {default:()=> '', watch:true, maxAge:1800}
const investor_ID = useCookie('investor_ID', cookie_options)
const fund_ID = useCookie('fund_ID', cookie_options)
const notification_count = useCookie('notification_count', cookie_options)
const dashboard_config = useCookie('dashboard_config')


    console.log(dashboard_config.value)

    // console.log(dashboard_config.value['dwolla_reverification']['documents_needed'])

const full_name =ref('')

const active_page = {is_active: "overview_active"}

const instant_selected_fund = useCookie('instant_selected_fund', cookie_options)

const csrf_cookie = useCookie('csrf_access_token')

function new_instant_invest() {

    const investment_amount = useCookie('investment_amount', cookie_options)
    investment_amount.value = investment_amount.value.toString().replace(/\D/g, "")
    
    fetch(`${config.flask_url}/api/investor_dashboard/instant_invest/instant_invest_step_1/`, {
        method: 'post',
        mode: 'cors',
        credentials: 'include',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRF-TOKEN': csrf_cookie.value
        },
        body: JSON.stringify({investor_ID: investor_ID.value, instant_selected_fund: instant_selected_fund.value, investment_amount: investment_amount.value})
    })
    .then((response) => response.json())
    .then((data) => {

        if(data.status == 'investor_already_invested'){
            alert('You have already invested in this fund')
        } else {
        fund_ID.value = data.fund_ID
        transition_and_route('instant_invest_step_2')
        }
    })
    .catch(error => {
        //  alert("Error")
        console.error('There was an error!', error);
    });
}


function transition_and_route(route_to) {
    navigateTo(route_to)
 cicle_tansition.value.animation_and_route(route_to);
}
</script>
    
    
    
    
    
    
    
    
    <style scoped>
    
:deep(.container){
width:30vw
}

:deep(.invest_input_mod){
background-color: #121212;
border-bottom: #fff solid 1px;
color:#fff;
width:110%
}

:deep(.invest_place_mod){
margin-left:-8%;
width:110%
}

.dial_wrap{
    width:50%;
    margin-left:25%
}
.dial_select{
    background-color: #121212;
}

.invest_container{
    padding-top:10%;
    padding-bottom:15%
}

    .header_menu {
        display: flex;
        align-items: center;
    }
    
    .is-active {
        color: var(--header_menu_hover) !important;
        border-bottom: 3.5px solid var(--header_menu_hover) !important;
    }
    
    
    
    
    .navigation_menu {
        padding: 20px 30px;
        padding-bottom: 18px;
        text-decoration: none;
        color: var(--inactive-color);
        border-bottom: 2px solid transparent;
        transition: 0;
        cursor: pointer;
    }
    
    .navigation_menu:hover {
        color: var(--header_menu_hover);
        font-weight: bold;
    }
    
    
    
    
    .dashboard_inner_section{
        margin-bottom: 450px; 
        width:calc(100vw - 250px); 
        margin-left:250px;
        border-bottom: rgba(75, 75, 75, 0.1) .5px solid;
        background-color:var(--inner_background);
    }
    
    .main_content_container{
        width:95%; 
        margin-right:0%;
        margin-left:2.5%
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
        background-color:#000
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
            width:100vw;
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
    
    
    







    /* ------------------------------------------------------------------- */



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




@media only screen and (min-width: 0px) and (max-width: 380px) {

.next_button{
    width:50%;
    height:30px;
    margin-top:-55%;
    font-size:3.5vw;
    margin-left: 25%;
}


}




@media only screen and (min-width: 380px) and (max-width: 576px) {


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


}

@media only screen and (min-width: 576px) and (max-width: 768px) {


.next_button{
    width:40%;
    height:40px;
    margin-top:12%;
    font-size:3.5vw;
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











