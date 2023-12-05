<template>
    
    <CircleTransition ref="cicle_tansition"/>
    <FundPagesFundsNextAiReserveModal ref="open_it"/>

    <div class="first_container">
    
    
    <div class="left_info">
    
    <p class="info_text" v-html="main_text"></p>
    <button @click="open_popup_modal()" class="next_button">Get Shares</button>
    </div>
    
    <div class="right_content">
    
        <video :class="{ hide_it: is_image }" data-lag=".5" data-speed=".7" class="intro_video" autoplay muted playsinline loop>
                    <source :src="video" type="video/mp4">
                </video>
    
        <img :class="{ hide_it: is_video }" data-lag=".8" class="intro_image" data-speed=".7" :src="image" />
    
    
    </div>
    
    
    </div>
    
    
    </template>
    
    
    <script setup>
    
    
    
    
    const props = defineProps(['video', 'image', 'is_image', 'is_video', 'main_text'])
    
    
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
    
    .first_container{
        width:100%;
        display:grid;
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: 1fr;
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        margin-top:-50px;
        margin-bottom:15%
    }
    
    .intro_video{
        width:50%;
        margin-top:50%;
        margin-left:15%;
        background-color: #000;
        border-radius:20%;
        filter:contrast(1.1);
    }
    
    .intro_image{
        width:70%;
        margin-top:35%;
        margin-left:15%;
    }
    
    
    .info_text{
        margin-left:10%;
        margin-top:5%;
        width:80%;
        line-height: 1.5;
        color: #fff;
        display: block;
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
}


.next_button:hover{
  box-shadow: 0px 10px 15px rgb(25, 120, 237, .5);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
} 
    
    
    
    
    
    
    @media only screen and (min-width: 0px) and (max-width: 576px) {
    
        .right_content{
            display:none;
        }
    
        .first_container{
        width:100%;
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(1, 1fr); 
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        margin-top:20px;
        margin-bottom:0%
    }
    
    .info_text{
        margin-bottom:20%;
    }

    .next_button{
    margin-top:0%;
    font-size:3vw;
    margin-bottom:50%
}
    
    }
    
    @media only screen and (min-width: 576px) and (max-width: 768px) {
    
        .right_content{
            display:none;
        }
    
        .first_container{
        width:100%;
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(1, 1fr); 
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        margin-top:20px;
        margin-bottom:0%
    }
    
    }
    
    
    
    
    
    
    </style>