
<template>

<ClientOnly>
<Teleport to="body">
<Transition name="transition_overlay">
<div v-show="modal_val" class="transition_overlay" ></div>
</Transition>

  <Transition name="white_circle">
    <div v-show="modal_val" class="white_circle"></div>
</Transition>

  <Transition v-show="modal_val"  name="black_circle">
    <div class="black_circle"></div>
</Transition>


<Transition name="underlay_box">
    <div v-show="modal_val" class="underlay_box"></div>
</Transition>

<Transition name="underlay_box_from_header" appear>
    <div v-show="from_header" class="underlay_box"></div>
</Transition>

<!-- <div class="underlay_boxX"></div> -->
</Teleport>
</ClientOnly> 

</template>



<script setup>
import { from_header_menu } from "../stores/menu_transition.js"

// sleep time expects milliseconds
function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}



const from_header = ref(true)



sleep(10).then(() => { from_header.value = false })


const props = defineProps(['modal_transition'])

const modal_val = ref(props.modal_transition)
watch(() => props.modal_transition, (newValue) => {
    modal_val.value = newValue
    // alert('modal_val.value = ' + modal_val.value)
    });

</script>

<style scoped>


.transition_overlay-enter-from{
opacity: 0;
} 

.transition_overlay-enter-to {
    opacity: 1;
}


.white_circle-enter-from{
  transform: translateX(-100%), translateY(-100%);
  transform: scale(1.5);
} 

.white_circle-enter-to {
    transform: translateX(100%), translateY(150%);
  transform: scale(6.5);
}



.black_circle-enter-from{
  transform: translateX(100%), translateY(0%);
  transform: scale(2);
} 

.black_circle-enter-to {
    transform: translateX(-50%), translateY(100%);
  transform: scale(6.5);
}


.underlay_box-enter-from{
    opacity:0
} 

.underlay_box-enter-to {
  opacity:1;
  transition: all .1s ease-in-out 1.2s;
}



.underlay_box-leave-to {
  transform: translateY(100%);
  opacity:1;
  transition: all 1.7s ease-in-out;
}


.underlay_box_from_header-enter-from{
    opacity:1
} 

.underlay_box_from_header-enter-to {
  transform: translateY(100%);
  opacity:1;
  transition: all 1.7s ease-in-out;
}

.underlay_box_from_header-leave-to {
  transform: translateY(100%);
  opacity:1;
  transition: all 1.7s ease-in-out;
}






.transition_overlay{
    width:100vw;
    height:100vh;
    background-color:rgba(114, 114, 114, 0.3);
    z-index:100;
    position:fixed;
    top:0;
    left:0;
}




.white_circle{
  width:50vw;
  height:50vw;
  border-radius:100%;
  background-color:#fff;
  z-index:500;
  left:-50%;
  top:100%;
  opacity:1;
  position:fixed;
  transition: transform 1.4s ease-in-out;

}


.black_circle{
  width:100vw;
  height:100vw;
  border-radius:100%;
  background-color:#000;
  z-index:400;
  left:150%;
  top:-150%;
  position:fixed;
  transition: all 1.8s ease-in-out;
}


.underlay_box{
  width:130vw;
  height:120vw;
  border-top-left-radius: 50%;
  border-top-right-radius: 50%;
  background-color:#fff;
  z-index:600;
  margin-left:-15vw;
  margin-top:-25vw;
  position:fixed;
}


.underlay_boxX{
  width:130vw;
  height:120vw;
  border-top-left-radius: 50%;
  border-top-right-radius: 50%;
  background-color:blue;
  z-index:600;
  margin-left:-15vw;
  margin-top:-25vw;
  position:fixed;
}



@media only screen and (min-width: 0px) and (max-width: 768px) {
  .black_circle{
  margin-left:calc(v-bind(circle_black_margin_left) + 100px);
  margin-top:calc(v-bind(circle_black_margin_top) - 800px);
  width:300vw;
  height:300vw;
}

.white_circle{
  width:200vw;
  height:200vw;
  margin-left:v-bind(circle_white_margin_left);
  margin-top:v-bind(circle_white_margin_top);
}

}


</style>