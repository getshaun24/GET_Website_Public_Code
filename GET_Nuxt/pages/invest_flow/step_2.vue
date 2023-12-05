<template>

    <div>
        <CircleTransition ref="cicle_tansition"/>

    <Header/>

    <div class="plaid_blur" v-if="plaid_blur"></div>
    <div class="loader_container" v-if="start_loader">

     <InvestFlowLoadersApiLoader/>

<!--  <div class="loader"></div> -->
    </div>


    <div class="white_background">
    <GSAPScrollSmoother>


        <InvestFlowStepCircles v-bind="step_circles" />




        <div v-if="institution_ID" class="plaid_box">
            <p class="plaid_text">Welcome, {{ first_name }} {{ last_name }}, we use Plaid to help verify your accredation status and connect your account with our payment processor partner.</p>
   <button @click="transition_and_route('step_3')" class="continue_button">Continue With Same Bank</button>
<button @click="get_link_token" class="next_button">Connect A New Bank</button>
<p class="plaid_text_1">By continuing to the next page and inputting your information into Plaid, you permit GET Equity Partners to use your information to verify<br> you are accredited investor status</p>
</div>


      
        <div v-else class="plaid_box">
   <p class="plaid_text">Welcome, {{ first_name }} {{ last_name }}, we use Plaid to help verify your accredation status and connect your account with our payment processor partner.</p>
<button @click="get_link_token" class="next_button">Start Plaid Connect</button>
<p class="plaid_text_1">By continuing to the next page and inputting your information into Plaid, you permit GET Equity Partners to use your information to verify<br> you are accredited investor status</p>
</div>






    </GSAPScrollSmoother>
</div>
    </div>
    </template>
    
    
    <script setup>



useHead({
  script: [{ src: "https://cdn.plaid.com/link/v2/stable/link-initialize.js", body:true, async: true, preload:true, ssr: false}],
});

const cookie_options = {default:()=> '', watch:true, maxAge:1800}
const start_loader = ref(false);
const plaid_blur = ref(false);
const blur_amount = ref('0px');
const plaid_opacity = ref(0);
const investor_ID = useCookie('investor_ID', cookie_options)
const email = useCookie('email', cookie_options)
const phone = useCookie('phone', cookie_options)
const institution_ID = useCookie('institution_ID', cookie_options)
const account_list = useCookie('account_list', cookie_options)
const config = useRuntimeConfig()
const step_circles = {current_num: 2}
const cicle_tansition = ref('');

const first_name = useCookie('first_name', cookie_options)
const last_name = useCookie('last_name', cookie_options)


// sleep time expects milliseconds
function sleep (time) {
return new Promise((resolve) => setTimeout(resolve, time));
}



function transition_and_route(route_to) {
console.log('routing')
cicle_tansition.value.animation_and_route(route_to);
}



// ------------------------------- Plaid Fetches ---------------
// ------------------------------- Plaid Fetches ---------------
// ------------------------------- Plaid Fetches ---------------







  function get_link_token(){

    // ------- get link token from flask server ---------------

fetch(`${config.flask_url}/api/invest_flow/step_2_linktoken/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'investor_ID': investor_ID.value, 'email': email.value, 'phone': phone.value})
    })
    .then((response) => response.json())
    .then((data) => {
        console.log('Success:', data.link_token);
        open_plaid(data.link_token)
    })
    .catch(error => {
        alert('Error')
        console.error('There was an error!', error);
    });
  }





    function open_plaid(link_token){ 


    plaid_blur.value = true;
    sleep(10).then(() => { blur_amount.value = '10px', plaid_opacity.value = 1 });

const handler = Plaid.create({
token: link_token,
onSuccess: (public_token, metadata) => {


    if (metadata['institution']['institution_id'] != institution_ID.value){
        send_plaid_public(public_token, metadata)
    } else {
        alert('You entered the same institution, Please try again with a different institution')
        plaid_blur.value = false;
    }

},
onLoad: () => {},
onExit: (err, metadata) => {
    blur_amount.value = '0px',
    plaid_opacity.value = 0
    plaid_blur.value = false;
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



    fetch(`${config.flask_url}/api/invest_flow/step_2_publictoken/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'public_token': public_token, 'metadata': metadata, 'investor_ID': investor_ID.value})
    })
    .then((response) => response.json())
    .then((data) => {
        console.log('Success:', data.message);
        

        account_list.value = data.data
        institution_ID.value = data.institution_ID
        transition_and_route("step_3");

    })
    .catch(error => {
        start_loader.value = false;
        plaid_blur.value = false;
        console.error('There was an error! -- Public Token Error', error);
    });
}










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



    .plaid_box{
        padding-bottom: 35%;
    }

.next_button{
    width:30%;
    height:40px;
    background-color:rgb(25, 120, 237) ;
    margin-left: 35%;
    margin-top:5%;
    border-radius:100px;
    border:#fff solid 0px;
    cursor:pointer;
    font-size:2vw;
    color:#fff;
    position: relative;
    margin-bottom:7%;
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

.continue_button{
    width:30%;
    height:40px;
    background-color:rgb(11, 184, 126);
    margin-left: 35%;
    margin-top:5%;
    border-radius:100px;
    border:#fff solid 0px;
    cursor:pointer;
    font-size:2vw;
    color:#fff;
    position: relative;
    margin-bottom:1%;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}

.continue_button:hover{
    box-shadow: 0px 10px 15px rgb(11, 184, 126, .5);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
} 


.plaid_text{
    color:#000;
    width:40%;
    margin-left:30%;
    margin-top:10%;
    text-align: center;
    font-size:20px
}

.plaid_text_1{
    color:#000;
    width:40%;
    margin-left:30%;
    margin-top:0%;
    text-align: center;
    font-size:15px
}



.white_background{
    background-color: #fff;
    height:100vh;
    width:100vw;
    position:fixed;
    top:0;
    left:0;
    z-index:0;
}



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






@media only screen and (min-width: 0px) and (max-width: 380px) {

.next_button{
    width:50%;
    height:30px;
    margin-top:-55%;
    font-size:3.5vw;
    margin-left: 25%;
}

.plaid_text{
    width:80%;
    margin-left:10%;
    margin-top:15%;
}

.plaid_text_1{
    width:80%;
    margin-left:10%;
    margin-top:8%;
}

}




@media only screen and (min-width: 380px) and (max-width: 576px) {



.next_button{
    width:50%;
    height:30px;
    margin-top:15%;
    font-size:3.5vw;
    margin-left: 25%;
}

.plaid_text{
    width:80%;
    margin-left:10%;
    margin-top:15%;
}

.plaid_text_1{
    width:80%;
    margin-left:10%;
    margin-top:8%;
}


}





</style>