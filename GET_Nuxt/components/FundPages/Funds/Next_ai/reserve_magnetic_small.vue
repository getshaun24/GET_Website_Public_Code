<template>
   

    <FundPagesFundsNextAiReserveModal ref="open_it"/>
    
 <div>
     <div @click="open_popup_modal()" class="magnetic_wrap" ref="mwrap_small">
       <div class="js_magnetic_area magnetic_size" @mouseover="mouseEnter" @mousemove="mouseMove" @mouseleave="mouseLeave" ref="marea_small"></div>
       <div class="js_magnetic_content" ref="mcontent_small">
         <div class="invest_button">Reserve Your <span style="color:#ff0aff">Next</span> Seat</div>
       </div></div>
 
     </div>
 </template>
 
 
 <script setup>
 import { ref, onMounted } from 'vue'
 import { ScrollTrigger } from 'gsap/ScrollTrigger'
 //import { TweenMax } from 'gsap/TweenMax'
 import { gsap } from 'gsap'
 
 const mwrap_small = ref(null)
 const mcontent_small = ref(null)
 const marea_small = ref(null)
 
 
 



 const open_it = ref(null);
function open_popup_modal() {
  open_it.value.open_modal();
}

 
 
 
 function parallaxIt_small(e, mcontent_small, marea_small, movement = 1) {
   var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
   var boundingRect = marea_small.value.getBoundingClientRect();
   var halfDiff = Math.abs(boundingRect.width - boundingRect.height) / 10;
   var relX = e.pageX - boundingRect.left - halfDiff;
   var relY = e.pageY - boundingRect.top;
   gsap.to(mcontent_small.value, {
     x: (relX - boundingRect.width / 2) * movement,
     y: (relY - boundingRect.height / 2 - scrollTop) * movement,
     ease: "power1",
     duration: 0.6
   });
 }
 
 
 // function mouseEnter(e) {
 //   this.$el.addEventListener('mousemove', this.mouseMove, false);
 // }
 
 function mouseMove(e) {
 
   parallaxIt_small(e, mcontent_small, marea_small);
 }
 
 function mouseLeave(e) {
   gsap.to(mcontent_small.value, {
     scale: 1,
     x: 0,
     y: 0,
     ease: "power3",
     duration: 0.6
   });
 }
 
 
 
 onMounted(() => {
 
 
 
 
 
 
 
 });
 
 </script>
 
 
 
 
 <style scoped>
 
 
 
 
 .invest_button{
     font-size:20px;
     padding:15px;
     border-radius:100px;
     border:#000 solid 1px;
     width:250px;
     text-align:center;
     transition: all 0.2s ease-in-out;
     background-color:#fff;
     cursor:pointer;
 }
 
 
 
 .magnetic_wrap {
   display: inline-block;
   position: relative;
   cursor:pointer;
 }
 
 .magnetic_wrap:hover .invest_button{
   background-color:#000;
     color:#fff;
     cursor:pointer;
     border:#fff solid 1px;
 }
 
 .magnetic_size {
   position: absolute;
   bottom: -70px;
   top: -50px;
   left:-50px;
   right: -50px;
   z-index: 10;
   border-radius: 50%;
 }
 
 .invest_button{color:#000}
 
 
 
 
 @media only screen and (min-width: 0px) and (max-width: 576px) {
 
   .invest_button{
     font-size:13px;
     padding:10px;
     width:200px;
     margin-top:-30%
 }
 }
 
 
 @media only screen and (min-width: 576px) and (max-width: 768px) {
 
  .invest_button{
     font-size:13px;
     padding:10px;
     width:250px;
     margin-top:-30%
 }
 
 }
 
 @media only screen and (min-width: 768px) and (max-width: 992px) {
   .invest_button{
     font-size:15px;
     padding:12px;
     width:170px;
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