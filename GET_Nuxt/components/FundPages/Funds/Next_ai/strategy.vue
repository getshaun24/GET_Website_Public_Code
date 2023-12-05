<template>
    
    <CircleTransition ref="cicle_tansition"/>
    <FundPagesFundsNextAiReserveModal ref="open_it"/>

    <div class="strategy_container">
    
    <div class="strategy_image_container">
    <img data-speed=".9" class="strategy_image" src="~/assets/content/fund_pages/next_ai/next_8.jpg" />
    

    
    
    
    </div>
    <div class="text_container" data-lag=".1">
        <h5>A Proven Approach</h5>
        <p class="para">By investing across the stack, we limit exposure to technology and platform risk, as well as the risk of any given application getting swallowed by a larger company. We seek out companies innovating in materials, energy sources, hardware, storage, and AI technical processes, as well as start-ups that are applying these tools to unique applications and datasets. We are particularly interested in companies that leverage narrow and deep datasets for specific uses - be that medical, legal, technical, or other areas - we see value outside of the high visibility opportunities.</p>
        <button @click="open_popup_modal()" class="next_button">Get Involved</button>
    </div>
    
    </div>
    
    </template>
    
    
    <script setup>

const cicle_tansition = ref(null);

function transition_and_route(route_to) {
cicle_tansition.value.animation_and_route(route_to);
}


const open_it = ref(null);
function open_popup_modal() {
  open_it.value.open_modal();
}

    

    </script>
    
    <style scoped>
    
    .hide_it{
        display:none;
    }
    
    .strategy_container{
        display:grid;
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: 1fr;
        grid-column-gap: 20px;
        grid-row-gap: 0px;
        width:90%;
        margin-left:5%;
        margin-top:v-bind(container_margin_top);
        z-index:1
    }
    
    .strategy_image{
        width:100%;
        margin-left:-8%
    }
    
    .strategy_video{
        width:90%;
        margin-top:40%
    
    }
    .para{
        width:80%;
    }
    
    .invest_button{
        position:absolute
    }

    .next_button{
    width:60%;
    height:40px;
    background-color:rgb(25, 120, 237) ;
    margin-left: 10%;
    margin-top:7%;
    border-radius:100px;
    border:#fff solid 0px;
    cursor:pointer;
    font-size:2vw;
    color:#fff;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
    z-index:2
}


.next_button:hover{
  box-shadow: 0px 10px 15px rgb(25, 120, 237, .5);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
} 
    
@media only screen and (min-width: 0px) and (max-width: 576px) {
.next_button{
    margin-top:100%;
    font-size:3vw;
    margin-bottom:50%
}
}


    @media only screen and (min-width: 0px) and (max-width: 380px) {
        .strategy_container{
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr); 
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        width:80%;
        margin-left:10%;
        margin-top:-115%;
        margin-bottom:0%;
    }
    
    .strategy_image{
        margin-left:0%;
        margin-top:150%;
    }
    
    
    .strategy_video{
        margin-top:0%;
        margin-bottom:-225%;
        z-index:-1;
        position: relative;
    }
    .para{
        width:100%;
        margin-bottom:v-bind(text_margin_mobile);
    }
    
    .text_container{
        margin-top:0%;
        mix-blend-mode: difference;
    }
    
    .invest_button{
        margin-top:210%
    }
    
    }
    
    
    @media only screen and (min-width: 380px) and (max-width: 430px) {
        .strategy_container{
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr); 
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        width:80%;
        margin-left:10%;
        margin-top:-135%;
        margin-bottom:-20%;
    }
    
    .strategy_image{
        margin-left:0%;
        margin-top:180%;
    }
    
    
    .strategy_video{
        margin-top:0%;
        margin-bottom:-215%;
        z-index:-1;
        position: relative;
    }
    .para{
        width:100%;
        margin-bottom:v-bind(text_margin_mobile);
    }
    
    .text_container{
        margin-top:0%;
        mix-blend-mode: difference;
    }
    .invest_button{
        margin-top:210%
    }
    
    }
    
    
    
    @media only screen and (min-width: 430px) and (max-width: 576px) {
    
    .strategy_image{
        margin-left:0%;
        margin-top:110%;
    }
    
    
    .strategy_video{
        margin-top:0%;
        margin-bottom:-150%;
        z-index:-1;
        position: relative;
    }
    .para{
        width:100%;
        margin-bottom:-80%;
    }
    
    .text_container{
        margin-top:0%;
    }
    
    .invest_button{
        margin-top:210%
    }
    
    }

    @media only screen and (min-width: 430px) and (max-width: 500px) {
        .strategy_container{
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr); 
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        width:80%;
        margin-left:10%;
        margin-top:-80%;
        margin-bottom:-30%;
    }
    
    }

    @media only screen and (min-width: 500px) and (max-width: 576px) {
        .strategy_container{
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr); 
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        width:80%;
        margin-left:10%;
        margin-top:-80%;
        margin-bottom:-60%;
    }
    
}
    
    @media only screen and (min-width: 576px) and (max-width: 768px) {
    

    .strategy_image{
        margin-left:0%;
        margin-top:10%;
    }
    
    .para{
        width:100%;
    }
    

    
    }

    @media only screen and (min-width: 576px) and (max-width: 700px) {
        .strategy_container{
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr); 
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        width:80%;
        margin-left:10%;
        margin-bottom:-10%;
    }
    
    .text_container{
        margin-top:-15%;
    }
    }


    @media only screen and (min-width: 700px) and (max-width: 768px) {
        .strategy_container{
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(2, 1fr); 
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        width:80%;
        margin-left:10%;
        margin-bottom:-20%;
    }
    .text_container{
        margin-top:-10%;
    }

}
    
    @media only screen and (min-width: 768px) and (max-width: 992px) {
    
    
    .para{
        width:100%;
    }
    
    .text_container{
        margin-top:-8%
    }
    .strategy_container{
        margin-bottom:15%;
    }

    
    }

    @media only screen and (min-width: 768px) and (max-width: 900px) {
    .strategy_image{
        margin-left:-5%;
        margin-top:25%;
    }
    }


    @media only screen and (min-width: 900px) and (max-width: 992px) {
    .strategy_image{
        margin-left:-5%;
        margin-top:5%;
    }
    }
    
    @media only screen and (min-width: 992px) and (max-width: 1200px) {
        .strategy_image{
            margin-top:25%;
    }
    .strategy_container{
        margin-bottom:10%;
    }
    }
    
    @media only screen and (min-width: 1200px) and (max-width: 1400px) {
        .strategy_image{
            margin-top:25%;
    }
    .strategy_container{
        margin-bottom:15%;
    }
    }
    
    @media only screen and (min-width: 1400px) and (max-width: 1600px) {
        .strategy_container{
        margin-bottom:15%;
    }
    }
    
    @media only screen and (min-width: 1600px) and (max-width: 5600px) {
        .strategy_container{
        margin-bottom:20%;
    }
    }
    
    
    
    
    
    </style>