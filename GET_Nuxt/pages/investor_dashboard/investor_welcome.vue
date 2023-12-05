<template>
    
    <div>
        <CircleTransition ref="cicle_tansition"/>
        
        <video class="landing_video" autoplay muted playsinline loop>
            <source src="~/assets/content/homepage/home_333.mp4" type="video/mp4">
        </video>
        
        
        <!-- <Header/> -->
        
        <GSAPScrollSmoother>
            
            <div class="main_content_container">
                
                
                
                <h3 class="welcome_text">Welcome To GET</h3>
                <p class="welcome_subtext">Let's begin by initializing your account</p>
                
                
                
                
                <div class="form_container">
                    
                    <div class="input_wrap_welcome">
                        <input v-model="password" type="password" class="input_black" placeholder=' ' required/>
                        <label class="label_black">Password</label>
                    </div>
                    
                    
                    <div class="input_wrap_welcome">
                        <input v-model="password2" type="password" class="input_black" placeholder=' ' required/>
                        <label class="label_black">Re-Enter Password</label>
                        <br>
                        <p class="welcome_subtext">{{message}}</p>
                    </div>
                    
                </div>
                
                <div class="next_button" @click="welcome_submit">Submit</div>
                
            </div>
            
            <div class="bottom_padding" ></div>
            
            
        </GSAPScrollSmoother>
        
        
        
    </div>
    
</template>


<script setup>

const config = useRuntimeConfig()

const password = ref('')
const password2 = ref('')
const message = ref('')



const cicle_tansition = ref(null);
function transition_and_route(route_to) {
    cicle_tansition.value.animation_and_route(route_to);
}

const route = useRoute().query
console.log(route.ivid)
const cookie_options = {default:()=> '', watch:true, maxAge:1800}
const ivid =  useCookie('ivid', cookie_options)
ivid.value = route.ivid

const investor_ID = useCookie('investor_ID', cookie_options)






function welcome_submit() {
    if (password.value != password2.value || password.value == '' || password2.value == '') {
        message.value = "Passwords do not match. Please try again."
        password.value = ''
        password2.value = ''
    } else if (password.value.length < 8) {
        message.value = "Your password is too short. Minimum length is 8 characters"
    } else {
        submit_password()
    }
}

function submit_password() {



    fetch(`${config.flask_url}/api/login/create_user/`, {
   method: 'POST',
        mode: 'cors',
        credentials: 'include',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ivid: ivid.value, password: password.value})
}).then((response) => response.json())
    .then((data) => {


        if(data.status == 'token_error'){
            alert(data.msg)
            if (data.msg == 'User already exists'){
                navigateTo('../../login_pages/login')
            }
        } else {
            const cookie = useCookie('auth_cookie')
            cookie.value = new Date().getTime()+30*60*1000
            investor_ID.value = data.investor_ID
            if (data.accredation_status == 'Not Accredited') {
                navigateTo('/investor_dashboard/get_accred/')
            } else {
                navigateTo('/investor_dashboard/investor_home')
            }
        }
    })
    .catch(error => {
        console.error('Token Error');
        navigateTo('/investor_dashboard/investor_expire')
    });

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

.main_content_container{
    width:90%;
    margin-left:5%;
    margin-top:12%;
    height:110vh
}


.form_container {
    display: grid;
    grid-template-columns:  1fr; 
    grid-template-rows: repeat(2, 1fr);
    grid-column-gap: 0px;
    grid-row-gap: 20px;
    width:50%;
    margin-left:25%;
    margin-top:50px
}



.landing_video{
    width: 80%;
    height: auto;
    object-fit: cover;
    z-index: -1;
    margin-left:10%;
    opacity:.1;
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