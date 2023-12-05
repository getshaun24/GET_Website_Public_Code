<template>

<div>
<CircleTransition ref="cicle_tansition"/>

    
    <div class="modal_container" :class="{modal_hide_anim: modal_exit_anim, modal_hide_disp: modal_exit_display}">
    <div class="modal_popup" :class="{modal_bix_hide_anim: modal_exit_anim}" ref="modal">
        <div @click="modal_leave" class="modal_exit">
            <div class="horizontal_line"></div>
            <div class="vertical_line"></div>
        </div>
        <h3 class="modal_login_info">If you have invested with us already then please login and skip this process. </h3>
        <button @click="transition_and_route('/login_pages/login')" class="login_redirect">Login</button>
    </div>
</div>

</div>
</template>





<script setup>

import { ref } from 'vue'
import { onClickOutside, useElementVisibility } from '@vueuse/core'


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

sleep(6500).then(() => {
onClickOutside(modal, (event) => modal_leave()) 
})

// open modal on load
sleep(3999).then(() => {      // Do something after the sleep!
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
    background-color:rgba(0, 0, 0, 0.5);
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
    width:600px;
    height:375px;
    background-color:rgb(0, 0, 0);
    z-index:10;
    border-radius:20px;
    margin-top:-100px;
    border: #fff solid 2px;
    transition: all 1s ease-in-out
}

.modal_login_info{
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
    margin-top:0px;
    margin-left:540px;
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