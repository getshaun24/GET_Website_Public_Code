<template>
    
    <CircleTransition ref="cicle_tansition"/>
    
<div>
    <div @click="transition_and_route('../../invest_flow/step_1')" class="magnetic_wrap" ref="mwrap">
      <div class="js_magnetic_area magnetic_size" @mouseover="mouseEnter" @mousemove="mouseMove" @mouseleave="mouseLeave" ref="marea"></div>
      <div class="js_magnetic_content" ref="mcontent">
        <div class="invest_button">Invest Now</div>
      </div></div>

    </div>


</template>


<script setup>
import { ref, onMounted } from 'vue'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
//import { TweenMax } from 'gsap/TweenMax'
import { gsap } from 'gsap'

const mwrap = ref(null)
const mcontent = ref(null)
const marea = ref(null)


const cicle_tansition = ref(null);

function transition_and_route(route_to) {
cicle_tansition.value.animation_and_route(route_to);
}



function parallaxIt(e, mcontent, marea, movement = 1) {
  var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  var boundingRect = marea.value.getBoundingClientRect();
  var halfDiff = Math.abs(boundingRect.width - boundingRect.height) / 2;
  var relX = e.pageX - boundingRect.left - halfDiff;
  var relY = e.pageY - boundingRect.top;
  gsap.to(mcontent.value, {
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

  parallaxIt(e, mcontent, marea);
}

function mouseLeave(e) {
  gsap.to(mcontent.value, {
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
    font-size:40px;
    padding:12px;
    border-radius:100px;
    border:#4478C4 solid 1px;
    width:300px;
    text-align:center;
    transition: all 0.2s ease-in-out;
    background-color:#fff;
    cursor:pointer;
    color:#4478C4
}



.magnetic_wrap {
  display: inline-block;
  position: relative;
  cursor:pointer;
}

.magnetic_wrap:hover .invest_button{
  background-color:#4478C4;
    color:#fff;
    cursor:pointer;
    border:#4478C4 solid 1px;
}

.magnetic_size {
  position: absolute;
  bottom: -125px;
  top: -125px;
  left:50px;
  right: -50px;
  z-index: 10;
  border-radius: 50%;
}







@media only screen and (min-width: 0px) and (max-width: 576px) {


.invest_button{
    font-size:30px;
    padding:10px;
    width:250px;
}

.magnetic_size {
  position: absolute;
  bottom: -75px;
  top: -125px;
  left:-10px;
  right: -50px;
}





}

@media only screen and (min-width: 576px) and (max-width: 768px) {

  .invest_button{
    font-size:30px;
    padding:10px;
    width:250px;
}

.magnetic_size {
  position: absolute;
  bottom: -75px;
  top: -125px;
  left:-10px;
  right: -50px;
}



}

@media only screen and (min-width: 768px) and (max-width: 992px) {

  .invest_button{
    font-size:30px;
    padding:10px;
    width:250px;
}

.magnetic_size {
  position: absolute;
  bottom: -75px;
  top: -125px;
  left:-10px;
  right: -50px;
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