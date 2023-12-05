<template>
    
<footer>

    <CircleTransition ref="cicle_tansition"/>


<div class="footer_section">

    <div class="footer_info">
        <h5 class="header_title">Impacting Finance</h5>
        <p class="header_subtitle">GET the best and most impactful financial insights & opportunities</p>
        <img data-lag="1" class="footer_logo" src="../assets/content/homepage/get_logo.png">


        <div class="footer_form">
            <input v-model="subscribe_email"  placeholder="Email" class="footer_input">
            <button @click="email_list_click" class="footer_form_button">Subscribe</button>
        </div>
    </div>

    <div class="footer_menu">
        <div @click="transition_and_route('/')" class="footer_menu_item">Home</div>
        <div @click="transition_and_route('/investments')" class="footer_menu_item">Investments</div>
        <div @click="transition_and_route('/HowItWorks')" class="footer_menu_item">How It Works</div>
        <div @click="transition_and_route('/about')" class="footer_menu_item">About</div>
        <div @click="transition_and_route('/blogs')" class="footer_menu_item">Blog</div>
        <div @click="transition_and_route('/careers')" class="footer_menu_item">Careers</div>
        <div @click="transition_and_route('/contact')"  class="footer_menu_item">Contact</div>
        <div class="footer_menu_item">
            <div class="social_links">
            <!-- <img class="social_img" src="~/assets/content/social_links/facebook.png">
            <img class="social_img" src="~/assets/content/social_links/instagram.png">
            <img class="social_img" src="~/assets/content/social_links/twitter.png">
            <img class="social_img" src="~/assets/content/social_links/linkedin.png"> -->
        </div>
        </div>
        <div class="footer_menu_item">
            <div class="policy_menu">
            <div class="policies_menu_item" @click="transition_and_route('/legal_pages/privacy')">Privacy Policy</div>
            <div class="policies_menu_item" @click="transition_and_route('/legal_pages/allocation')" >Allocation Policy</div>
            <div class="policies_menu_item" @click="transition_and_route('/legal_pages/continuity')">Business Continuity</div>
            <div class="policies_menu_item" @click="transition_and_route('/legal_pages/disclosures')" >Disclosures</div>
        </div>
        </div>

        <div class="footer_menu_item_legal">Some opportunities posted on this website are "private placements" of GET Holdings and are not publicly traded, yet are subject to holding period requirements which are intended for investors who do not need a liquid investment. Investing in private companies may be considered highly speculative and involves a high degree of risk, including the risk of substantial loss of investment. Investors must be able to afford the loss of their entire investment. See our Risk Factors for a more detailed explanation of the risks involved in investing in GET Resources Holdings. GET Resource Holdings LLC (“GET Holdings”) is a subsidiary of GET Resources LLC, a private company. ThisisGET.com is a website operated by GET Resources LLC ("GET"). By accessing this site and any pages thereof, you agree to be bound by our Terms of Use. GET and logo are owned by GET Resources LLC. Other trademarks are property of their respective owners. © 2020 GET Resources LLC. All rights reserved.</div>

</div>








<div class="footer_menu_mobile">
    <div class="footer_menu_links">
        <div @click="transition_and_route('/')"  class="footer_menu_item">Home</div>
        <div @click="transition_and_route('/investments')"  class="footer_menu_item">Investments</div>
        <div @click="transition_and_route('/HowItWorks')"  class="footer_menu_item">How It Works</div>
        <div @click="transition_and_route('/about')"  class="footer_menu_item">About</div>
        <div @click="transition_and_route('/blogs')"  class="footer_menu_item">Blog</div>
        <div @click="transition_and_route('/careers')"  class="footer_menu_item">Careers</div>
        <div @click="transition_and_route('/contact')"  class="footer_menu_item">Contact</div>
        <div class="footer_menu_item">
            <div class="social_links">
            <!-- <img class="social_img" src="~/assets/content/social_links/facebook.png">
            <img class="social_img" src="~/assets/content/social_links/instagram.png">
            <img class="social_img" src="~/assets/content/social_links/twitter.png">
            <img class="social_img" src="~/assets/content/social_links/linkedin.png"> -->
        </div>
    </div>

        </div>

        <div class="footer_menu_legal">
        <div class="footer_menu_item">
            <div class="policy_menu">
                <div class="policies_menu_item" @click="transition_and_route('/legal_pages/privacy')">Privacy Policy</div>
            <div class="policies_menu_item" @click="transition_and_route('/legal_pages/allocation')" >Allocation Policy</div>
            <div class="policies_menu_item" @click="transition_and_route('/legal_pages/continuity')">Business Continuity</div>
            <div class="policies_menu_item" @click="transition_and_route('/legal_pages/disclosures')" >Disclosures</div>
        </div>
        </div>

        <div class="footer_menu_item_legal">Some opportunities posted on this website are "private placements" of GET Holdings and are not publicly traded, yet are subject to holding period requirements which are intended for investors who do not need a liquid investment. Investing in private companies may be considered highly speculative and involves a high degree of risk, including the risk of substantial loss of investment. Investors must be able to afford the loss of their entire investment. See our Risk Factors for a more detailed explanation of the risks involved in investing in GET Resources Holdings. GET Resource Holdings LLC (“GET Holdings”) is a subsidiary of GET Resources LLC, a private company. ThisisGET.com is a website operated by GET Resources LLC ("GET"). By accessing this site and any pages thereof, you agree to be bound by our Terms of Use. GET and logo are owned by GET Resources LLC. Other trademarks are property of their respective owners. © 2020 GET Resources LLC. All rights reserved.</div>

    </div>

</div>




</div>
</footer>
</template>



<script setup>
const config = useRuntimeConfig()



const cicle_tansition = ref(null);

function transition_and_route(route_to) {
cicle_tansition.value.animation_and_route(route_to);
}

const subscribe_email = ref('');

function email_list_click() {

    

    fetch(`${config.flask_url}/api/contact_and_subscribe/`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({subscribe_email:subscribe_email.value})
    })
    .then((response) => response.json())
    .then((data) => {


        if (data.status == 'success_email_added') {
            alert('Success')
        } else {
            alert('message')
        }

    })
    .catch(error => {
        alert('Error')
        start_loader.value = false;
        console.error('There was an error!', error);
    });


}




</script>

<style scoped>




footer{
    z-index:10;
    background-color: #000;
}

.footer_section{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 1fr;
grid-column-gap: 0px;
grid-row-gap: 0px;
z-index:1;
}

.footer_menu_mobile{
    display: none
}

.footer_menu{
    display: grid;
grid-template-columns: 1fr;
grid-template-rows: repeat(10, 1fr);
grid-column-gap: 0px;
grid-row-gap: 0px;
}


.footer_menu_item{
    border:.5px solid #fff;
    color:#fff;
    text-align: center;
    display: flex;
    align-items: center;
    transition:all ease .4s;
    padding-left:40px;
    mix-blend-mode: difference;
    font-size:25px;
    cursor:pointer
}


.footer_menu_item_legal{
    border:.5px solid #fff;
    color:#fff;
    font-size:8px;
    padding:10px;
    text-align: left;
}

.footer_menu_item:hover{
    background-color: #fff;
    color:#000;
    mix-blend-mode: difference;
}

.footer_info{
    border: #fff solid .5px;
    border-right:0px;
    height:100%;
    mix-blend-mode: difference;
}

.header_title{
    text-align: center;
    margin-top:10%;
}

.header_subtitle{
    text-align: center;
    margin-top:5%;
    width:50%;
    line-height: 1.5;
    margin-left:25%
}


.footer_logo{
    margin-top:5%;
    width:35%;
    margin-left:32.5%;
}


.footer_input{
    width:50%;
    margin-left:25%;
    font-size:20px;
    padding:10px;
    border-bottom:1px solid rgba(255, 255, 255, 0.5);
    background-color: #000;
    margin-top:10%;
    color:#fff
    }

    .footer_input:hover{
        border-bottom:1px solid rgba(255, 255, 255, 1);
    }

    .footer_input:focus{
        border-bottom:1px solid rgb(0, 122, 204);
    }

    .footer_form{
        padding-bottom:20px;
    }
    .footer_form_button{
        width:40%;
        margin-left:30%;
        font-size:20px;
        border:rgba(255, 255, 255, 0.5) solid 1px;
        background-color:#000;
        color:#fff;
        border-radius: 100px;
        padding:20px;
        margin-top:60px;
        font-weight: 700;
        cursor: pointer;
    }

    .policy_menu{
        display: flex;
        justify-content: space-evenly;
        width:90%
    }

    .social_links{
        display: flex;
        justify-content: space-evenly;
        width:90%
    }

    .policies_menu_item{
        font-size: 14px;
        text-align: center;
        padding:5px;
        border-bottom:2px solid rgba(0, 122, 204, 0);
    }

    .policies_menu_item:hover{
        border-bottom:2px solid rgb(0, 122, 204);
        transition:all ease .3s;
    }


    .footer_form_button:hover{
        border:1px solid rgba(255, 255, 255, 1);
    }



.social_img{
    width:30px;
    height:30px;
    cursor:pointer;
    mix-blend-mode: difference;
    border:2px solid rgba(0, 122, 204, 0);
    border-radius: 100%;
    padding:5px;
}

.social_img:hover{
    border:2px solid #ff9933;
    transition:all ease .3s;
}












    @media only screen and (min-width: 576px) and (max-width: 768px) {
/* 
        footer{
    padding-bottom:4%
} */

        .footer_info{
    display:none
}

.footer_menu{
    display: none;
}

.footer_menu_mobile{
    display: grid;
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(1, 1fr);
}

.footer_menu_links{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: repeat(4, 1fr);
}

.footer_section{
    display: grid;
grid-template-columns: 1fr;
grid-template-rows: 1fr;
}


.footer_menu_item{
    padding-left:40px;
    font-size:20px
}

.policies_menu_item{
        font-size: 10px;
        text-align: center;
        padding:10px
    }


.footer_menu_item_legal{
    border:.5px solid #fff;
    color:#fff;
    font-size:7px;
    padding:5px;
    text-align: left;
}

.footer_menu_item_legal{
    font-size:7px;
    padding:5px;
    padding-right:2px;
}


}















@media only screen and (min-width: 0px) and (max-width: 576px) {

    /* footer{
    padding-bottom:4%
} */


.footer_info{
    display:none
}

.footer_menu{
    display: none;
}

.footer_menu_mobile{
    display: grid;
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(1, 1fr);
}

.footer_menu_links{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: repeat(4, 1fr);
}

.footer_section{
    display: grid;
grid-template-columns: 1fr;
grid-template-rows: 1fr;
}


.footer_menu_item{
    padding-left:40px;
    font-size:20px;
    padding:20px
}

.policies_menu_item{
        font-size: 10px;
        text-align: center;
        padding:10px
    }


.footer_menu_item_legal{
    font-size:7px;
    padding:5px;
    padding-right:1px;
}

.social_img{
    width:25px;
    height:25px;
    padding:3px;
}


}


@media only screen and (min-width: 576px) and (max-width: 768px) {


    .footer_info{
    display:none
}

.footer_menu{
    display: none;
}

.footer_menu_mobile{
    display: grid;
grid-template-columns: repeat(1, 1fr);
grid-template-rows: repeat(2, 1fr);
}

.footer_menu_links{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: repeat(4, 1fr);
}

.footer_section{
    display: grid;
grid-template-columns: 1fr;
grid-template-rows: 1fr;
}


.footer_menu_item{
    padding-left:40px;
    font-size:20px;
    padding:20px
}

.policies_menu_item{
        font-size: 10px;
        text-align: center;
        padding:10px
    }


.footer_menu_item_legal{
    font-size:7px;
    padding:5px;
    padding-right:1px;
}


}



</style>