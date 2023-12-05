<template>

    <div>
    <CircleTransition ref="cicle_tansition"/>
    
        
        <div class="modal_container" :class="{modal_hide_anim: modal_exit_anim, modal_hide_disp: modal_exit_display}">
        <div class="modal_popup" :class="{modal_bix_hide_anim: modal_exit_anim}" ref="modal">
            <div @click="modal_leave" class="modal_exit">
                <div class="horizontal_line"></div>
                <div class="vertical_line"></div>
            </div>



            <div class="loader_container" v-if="start_loader">
<InvestFlowLoadersApiLoader/>
   </div>

<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->
<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->





<div class="form_container">


<p class="two_fact_text">An account with this email already exists.<br><br>Please enter the time sensitive two factor code sent to <span style="color:rgb(25, 120, 237)">{{ email }}</span> so that you can jump ahead to where you previously left off or sigup with a new unique email. </p>



<div class="input_wrap wrap_edit">
<input v-model="two_factor_code" @keyup="remove_chrs('two_factor_code')" class="input_black" placeholder=' ' required/>
<label class="label_black">Two Factor Code</label>
</div>


<div class="next_button" @click="two_factor_submit">Submit</div>

</div>












<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->
<!-- ------------------------------------------------------------ Modal Info ------------------------------------------------------------ -->


        </div>
    </div>
    
    </div>
    </template>
    
    
    
    
    
    <script setup>
    const config = useRuntimeConfig()
    const two_factor_code = ref("")
    const email = useCookie('email')
    const selected_fund = useCookie('selected_fund')
    


// ----------------------------------   format inputs  ----------------------------------

        function remove_chrs(input_var) {
    this[input_var] = this[input_var].toString().replace(/[^0-9-]/g, '');
}


// -------------------------------------------------------------------------------------------------------



// -------------------------------- Send API Request --------------------------------







function two_factor_submit() {


fetch(`${config.flask_url}/api/invest_flow/step_1/`, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({'email': email.value, 'submitted_two_factor_code': two_factor_code.value, 'selected_fund': selected_fund.value })
})
.then((response) => response.json())
.then((data) => {

    if(data.status == 'code_correct'){
            const fund_ID = useCookie('account_selected_value', {default:()=> data.fund_ID, watch:true, maxAge:1800});
            const investor_ID = useCookie('account_selected_value', {default:()=> data.investor_ID, watch:true, maxAge:1800});
            const account_selected_value = useCookie('account_selected_value', {default:()=> data.account_selected_value, watch:true, maxAge:1800});
            const dwolla_customer_created = useCookie('dwolla_customer_created', {default:()=> true, watch:true, maxAge:1800});
            transition_and_route('step_4')
        } else {
            alert('Two Factor Code Incorrect')
            modal_leave()
            sleep(700).then(() => { window.location.reload(); });
        }
})
.catch(error => {
    start_loader.value = false;
        alert('Two Factor Error')
        console.error('There was a two factor error!', error);
});

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
    
    .wrap_edit{
        width:35%;
        margin-left:32.5%;
    }
.two_fact_text{
    width:60%;
    margin-left:20%;
    color:#fff;
    text-align: center;
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
        width:65%;
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