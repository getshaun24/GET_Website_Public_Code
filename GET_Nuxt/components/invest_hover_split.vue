<template>
    


    <div class="grid_section" v-show="sort_val == 'all' || sort_val == left_topic || sort_val == right_topic"> 


<NuxtLink v-show="sort_val == 'all' || sort_val == left_topic" :to="left_link" class="elm_container" :class="{low_side_container: left_side_small}" id="img_cont">

  <div class="img_container" :class="{low_side: left_side_small}">
    
    <img class="img" data-speed=".9" :src="left_image">


</div>

    <h3 class="invest_title">{{ left_title }}</h3>
    <p class="subtitle">{{ left_subtitle }}</p>
    <div v-if="!ismobile" :class="{low_side_margin: left_side_small}" class="wrapperovertext" data-lag=".2">
    <div class="overText">&nbsp; {{ left_hover_text }} </div>
</div>
</NuxtLink>




<NuxtLink v-show="sort_val == 'all' || sort_val == right_topic" :to="right_link" class=" elm_container" :class="{low_side_container: right_side_small}">


  <div class="img_container" :class="{low_side: right_side_small}">

    <img class="img" data-speed=".9" :src="right_image">




</div>


    <h3 class="invest_title">{{ right_title }}</h3>
    <p class="subtitle">{{ right_subtitle }}</p>
    <div v-if="!ismobile" :class="{low_side_margin: right_side_small}" class="wrapperovertext_2" data-lag=".2">
    <div class="overText_2">&nbsp; {{ right_hover_text }} </div>
  </div>
</NuxtLink>
</div>




</template>



<script setup>
import { useWindowSize } from '@vueuse/core'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
gsap.registerPlugin(ScrollTrigger);


const props = defineProps(['left_title', 'left_subtitle', 'left_hover_text', 'left_link', 'left_image', 'left_topic', 'right_title', 'right_subtitle', 'right_hover_text', 'right_img','right_side_small', 'left_side_small', 'right_link', 'right_image', 'right_topic', 'sort_topic'])


const sort_val = ref(props.sort_topic)
watch(() => props.sort_topic, (newValue) => {
  sort_val.value = newValue
    });


    const ismobile = ref(false)
    const { width, height } = useWindowSize()

    
onMounted(() => {


 if(width.value > 576){start_scroll_text(); ismobile.value = false}
 else{ismobile.value = true}


})




function start_scroll_text(){




let direction = -1; // 1 = forward, -1 = backward scroll

const roll1 = roll(".overText", { duration: 10}),
  scroll = ScrollTrigger.create({
    onUpdate(self) {
      if (self.direction !== direction) {
        direction *= 1;
        gsap.to([roll1], { timeScale: direction, overwrite: true });
      }
    }
  });

// helper function that clones the targets, places them next to the original, then animates the xPercent in a loop to make it appear to roll across the screen in a seamless loop.
function roll(targets, vars, reverse) {
  const tl = gsap.timeline({
    repeat: -1,
    onReverseComplete() {
      this.totalTime(this.rawTime() + this.duration() * 100); // otherwise when the playhead gets back to the beginning, it'd stop. So push the playhead forward 10 iterations (it could be any number)
    }
  });
  vars = vars || {};
  vars.ease || (vars.ease = "none");
  gsap.utils.toArray(targets).forEach((el) => {
    let clone = el.cloneNode(true);
    el.parentNode.appendChild(clone);
    gsap.set(clone.value, {
      position: "absolute",
    });
    tl.to([el, clone], { xPercent: reverse ? 100 : -100, ...vars }, 0);
  });
  return tl;
}








// NOTE: for a responsive version, see https://codepen.io/GreenSock/pen/QWqoKBv

let direction_2 = -1; // 1 = forward, -1 = backward scroll

const roll_2 = roll(".overText_2", { duration: 10}),
  scroll_2 = ScrollTrigger.create({
    onUpdate(self) {
      if (self.direction !== direction_2) {
        direction_2 *= 1;
        gsap.to([roll_2], { timeScale: direction_2, overwrite: true });
      }
    }
  });

// helper function that clones the targets, places them next to the original, then animates the xPercent in a loop to make it appear to roll across the screen in a seamless loop.
function roll(targets, vars, reverse) {
  const tl = gsap.timeline({
    repeat: -1,
    onReverseComplete() {
      this.totalTime(this.rawTime() + this.duration() * 100); // otherwise when the playhead gets back to the beginning, it'd stop. So push the playhead forward 10 iterations (it could be any number)
    }
  });
  vars = vars || {};
  vars.ease || (vars.ease = "none");
  gsap.utils.toArray(targets).forEach((el) => {
    let clone = el.cloneNode(true);
    el.parentNode.appendChild(clone);
    gsap.set(clone.value, {
      position: "absolute",
    });
    tl.to([el, clone], { xPercent: reverse ? 100 : -100, ...vars }, 0);
  });
  return tl;
}


}

</script>








<style scoped>






.img{
    width:100%;
    object-fit:cover;
    mix-blend-mode: difference;
    margin-left:5%;
    height:100%;
    
}

.img_container{
  overflow: hidden;
  height:88%;
  width:90%;
}


.low_side{
    height:60% !important
}





.grid_section{
    display: grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 1fr;
grid-column-gap: 0px;
grid-row-gap: 0px;
margin-top:10%;
overflow: hidden;
width:95%;
margin-left:2.5%;

}


.elm_container{
    overflow:hidden;
    height:105vh;
    padding-bottom:150px
}




.invest_title{
    color:#000;
    line-height: 1;
    font-size:60px;
    margin-left:5%;
    margin-top:22px;
    width:90%;
}

.subtitle{
    font-size:25px;
    color:#000;
    margin-left:5%;
    margin-top:-40px;
}






.wrapperovertext{
  position:relative;
  display: flex;
  z-index:2;
  mix-blend-mode: difference;
  opacity:1;
  margin-top:-80%;
}

.wrapperovertext_2{
  position:relative;
  display: flex;
  z-index:2;
  mix-blend-mode: difference;
  opacity:1;
  margin-top:-80%;
}

.low_side_margin{
    margin-top:-65% !important;
}


.overText{
    font-size:120px;
    font-weight:900;
    mix-blend-mode: difference;
    white-space: nowrap;
    color:#fff;
    text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
    opacity:0;
    transition: opacity .2s ease-in-out;
    transition: margin-top 1s ease-in-out;
    margin-top:15%;
    word-spacing: 10px;
    
}

.overText_2{
    font-size:120px;
    font-weight:900;
    mix-blend-mode: difference;
    white-space: nowrap;
    color:#fff;
    text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;
    opacity:0;
    transition: opacity .2s ease-in-out;
    transition: margin-top 1s ease-in-out;
    margin-top:15%;
    
}



.elm_container:hover .overText{
    opacity:1;
    margin-top:0%;
}

.elm_container:hover .overText_2{
    opacity:1;
    margin-top:0%;
}









@media only screen and (min-width: 0px) and (max-width: 430px) {
  .grid_section{
    display: grid;
grid-template-columns:  1fr;
grid-template-rows:repeat(2, 1fr);
grid-column-gap: 0px;
grid-row-gap: 100px;
margin-top:30%;
overflow: hidden;
width:95%;
margin-left:2.5%
}

.elm_container{
    height:80vh;
}


.low_side{
    height:100% !important;
}

.low_side_container{
  margin-top:-20%
}

.wrapperovertext{
  margin-top:-120%;
}

.wrapperovertext_2{
  margin-top:-130%;
}

.low_side_margin{
    margin-top:-145% !important;
}

.elm_container{
    padding-bottom:200px
}

.overText{
  font-size:80px;
  opacity:1;
}
.overText_2{
  font-size:80px;
  opacity:1;
}

.img{
    mix-blend-mode: normal;
}

.invest_title{
    mix-blend-mode: normal;
}
.subtitle{
  mix-blend-mode: normal;
}
}







@media only screen and (min-width: 430px) and (max-width: 576px) {
  .grid_section{
    display: grid;
grid-template-columns:  1fr;
grid-template-rows:repeat(2, 1fr);
grid-column-gap: 0px;
grid-row-gap: 100px;
margin-top:10%;
overflow: hidden;
width:95%;
margin-left:2.5%
}
.elm_container{
    height:80vh;
}
.low_side{
    height:100% !important
}
.wrapperovertext{
  margin-top:-120%;
}
.wrapperovertext_2{
  margin-top:-120%;
}
.low_side_margin{
    margin-top:-125% !important;
}
.elm_container{
    padding-bottom:200px
}
.overText{
  font-size:80px;
  opacity:1;
}
.overText_2{
  font-size:80px;
  opacity:1;
}
}






@media only screen and (min-width: 576px) and (max-width: 768px) {
  .grid_section{
    display: grid;
grid-template-columns:  1fr;
grid-template-rows:repeat(2, 1fr);
grid-column-gap: 0px;
grid-row-gap: 100px;
margin-top:10%;
overflow: hidden;
width:95%;
margin-left:2.5%
}

.elm_container{
    height:80vh;
}


.low_side{
    height:100% !important
}


.wrapperovertext{
  margin-top:-90%;
}

.wrapperovertext_2{
  margin-top:-90%;
  
}

.low_side_margin{
    margin-top:-95% !important;
}

.elm_container{
    padding-bottom:200px
}

.overText{
  font-size:80px;
  opacity:1;
}
.overText_2{
  font-size:80px;
  opacity:1;
}

.img{
    mix-blend-mode: normal;
}

.invest_title{
    mix-blend-mode: normal;
}
.subtitle{
  mix-blend-mode: normal;
}



}

@media only screen and (min-width: 768px) and (max-width: 992px) {
  .wrapperovertext{
  margin-top:-150%;
}

.wrapperovertext_2{
  margin-top:-150%;
}
.low_side_margin{
    margin-top:-125% !important;
}
.overText{
  font-size:80px;
}
.overText_2{
  font-size:80px;
}

.img{
    mix-blend-mode: normal;
}

.invest_title{
    mix-blend-mode: normal;
}
.subtitle{
  mix-blend-mode: normal;
}
}

@media only screen and (min-width: 992px) and (max-width: 1200px) {

.wrapperovertext{
  margin-top:-100%;
}

.wrapperovertext_2{
  margin-top:-120%;
}

.low_side_margin{
    margin-top:-80% !important;
}

}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
}











</style>