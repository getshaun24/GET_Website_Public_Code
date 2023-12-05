<template>
    
    <div>
        <CircleTransition ref="cicle_tansition"/>


        <div class="loader_container" v-if="start_loader">
            <InvestFlowLoadersApiLoader/>
        </div>

        
        <video class="landing_video" autoplay muted playsinline loop>
            <source src="~/assets/content/homepage/home_333.mp4" type="video/mp4">
        </video>
        
        
        <!-- <Header/> -->
        
        <GSAPScrollSmoother>

                            
            <h3 class="welcome_text">GET Invested</h3>
                <p class="welcome_subtext">Let's solidify your investment</p>
                
                
                
            
          
            
                
    
                    
           
                    
               
<!-- 
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
    </div> -->


    <InvestDial/>



                <div class="next_button" @click="submit_investment">Submit</div>






                    
                
                
       
            
            <div class="bottom_padding" ></div>
            
            
        </GSAPScrollSmoother>
        
        
        
    </div>
    
</template>


<script setup>

const config = useRuntimeConfig()

const investment_amount = ref('')
const message = ref('')
const start_loader = ref(false);
const plaid_blur = ref(false);


const cicle_tansition = ref(null);
function transition_and_route(route_to) {
    cicle_tansition.value.animation_and_route(route_to);
}

const route = useRoute().query
console.log(route.ivid)
const cookie_options = {default:()=> '', watch:true, maxAge:1800}
const ivid =  useCookie('ivid', cookie_options)
ivid.value = route.ivid










function submit_investment() {

    start_loader.value = true;
    plaid_blur.value = true;

    const investment_amount = useCookie('investment_amount', cookie_options)

    if(confirm("Intitate Transfer of " + '$' + investment_amount.value)){

    investment_amount.value = investment_amount.value.toString().replace(/\D/g, "")


    fetch(`${config.flask_url}/api/manager_dashboard/manager_upsell_received/`, {
   method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ivid: ivid.value, investment_amount: investment_amount.value})
}).then((response) => response.json())
    .then((data) => {

        if(data.status = 'success'){
            alert(data.msg)
            window.location.href = "https://thisisget.com/";
        } else{
            alert(data.msg)
        }


    })
    .catch(error => {
        start_loader.value = false;
        plaid_blur.value = false;
        console.error('Error');
    });
    } else{
        start_loader.value = false;
        plaid_blur.value = false;
    }
}




fetch(`${config.flask_url}/api/investor_dashboard/confirm_link_expire/`, {
   method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
    body: JSON.stringify({ivid: ivid.value})
}).then((response) => response.json())
    .then((data) => {
    if (data.status == 'token_invalid') {
            navigateTo('/investor_dashboard/investor_expire')
        }
    })
    .catch(error => {
        console.error('Token Error');
        navigateTo('/investor_dashboard/investor_expire')
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

:deep(.invest_input_mod){
    background-color:rgba(0, 0, 0, 0.25);
border-bottom: #fff solid 1px;
color:#fff;
width:110%;
margin-left:20%
}

:deep(.invest_place_mod){
margin-left:10%;
width:110%
}

.dial_wrap{
    width:50%;
    margin-left:25%;
    margin-top:10%
}
.dial_select{
    background-color:rgba(0, 0, 0, 0.25);
}


.main_content_container{
    width:90%;
    margin-left:5%;
    margin-top:0%;
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);
    background-color:rgba(0, 0, 0, 0.25);
    padding-top:10%;
    padding-bottom:10%;
    border-radius:30px;
}


.form_container {
    width:90%;
    margin-left:0%;
    margin-top:50px;
}



.landing_video{
    width: 80%;
    height: auto;
    object-fit: cover;
    z-index: -1;
    margin-left:10%;
    opacity:.075;
    position:fixed;
    top:-2%;
    left:0;
    margin-top:2%
}

.welcome_text{
    text-align:center;
    margin-top:15%;
    position: relative;
}
.welcome_subtext{
    text-align:center;
    position: relative;
    margin-top:-2%;
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
    margin-left:33%;
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


.bottom_padding{
    padding-bottom:10vh
}


@media screen and (min-width: 2300px) and (max-width: 5600px) {
    
    .bottom_padding{
    padding-bottom:40vh
}


}









@media screen and (min-width: 1900px) and (max-width: 2300px) {
    
    .bottom_padding{
    padding-bottom:35vh
}

}


@media screen and (min-width: 1600px) and (max-width: 1900px) {
    
    .bottom_padding{
    padding-bottom:30vh
}

}





@media screen and (min-width: 1400px) and (max-width: 1600px) {
    .bottom_padding{
    padding-bottom:25vh
}
}




@media screen and (min-width: 1200px) and (max-width: 1400px) {
    .bottom_padding{
    padding-bottom:20vh
}
    
}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
    
    
    
    
    
    
}


@media only screen and (min-width: 768px) and (max-width: 992px) {
    
    
    .next_button{
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
    
    .form_container {
        width:80%;
        margin-left:10%;
    }
    
    
}

@media only screen and (min-width: 0px) and (max-width: 576px) {
    
    
    .landing_video{
        margin-top:30%
    }
    
    .next_button{
        margin-left:15%;
        width:60%
    }
    
    
    .form_container {
        width:80%;
        margin-left:10%;
        margin-top:8%
    }
    
    
    
    .input_wrap_welcome .input_black {
        
        height:3.5vw;
        font-size: 6vw;
        padding-bottom:5px
    }
    
    .input_wrap_welcome .label_black {
        font-size: 4.25vw;
        left: 7.75vw;
        top: 0vw;
    }
    
    
    .input_wrap_welcome .input_black:focus~ .label_black,
    .input_wrap_welcome .input_black:valid ~ .label_black{
        top: -5vw;
        left: 8vw;  
        font-size: 3vw;
    }
    
    
    
    
}





</style>