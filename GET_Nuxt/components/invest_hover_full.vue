<template>

<div v-show="sort_val == 'all' || sort_val == topic" class="full_section">

    <NuxtLink :to="nuxt_link">


    <div class="slab_container">

      <img data-speed="auto" class="img" :src="image">




    </div>


    <h3 class="invest_title">{{ title }}</h3>
    <p class="subtitle">{{ subtitle }}</p>
    <div v-if="!ismobile" class="wrapperovertext" data-lag=".1">
    <div class="overText">&nbsp; {{ hover_text }} </div>
</div>
</NuxtLink>
</div>

</template>

<script setup>

import { useWindowSize } from '@vueuse/core'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
gsap.registerPlugin(ScrollTrigger);

const props = defineProps(['title', 'subtitle', 'hover_text', 'nuxt_link', 'image', 'topic', 'sort_topic'])


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

  }






</script>

<style scoped>




.slab_container{
  position: relative;
 height: 65vh;
 width: 95%;
 overflow: hidden;
 margin-left:2.5%
}
.img{
  position: absolute;
  bottom: 0;
  height: auto;
    width: 100%;
}






.full_section{
    margin-top:10%;
    height:80vh;
    width:95%;
    margin-left:2.55%;
    margin-bottom:10%;
    overflow: hidden;
    position: relative;
    padding-bottom:100px
}


.invest_title{
    color:#000;
    line-height: 1;
    font-size:60px;
    margin-left:2.5%;
    margin-top:12px
}

.subtitle{
    font-size:25px;
    color:#000;
    margin-left:2.5%;
    margin-top:-40px
}

.wrapperovertext{
  position:relative;
  display: flex;
  z-index:2;
  mix-blend-mode: difference;
  opacity:1;
  margin-top:-32%;
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



.full_section:hover .overText{
    opacity:1;
    margin-top:0%;
}



@media only screen and (min-width: 0px) and (max-width: 430px) {

.wrapperovertext{
  margin-top:-125%;
}

.overText{
opacity:1;
    margin-top:0%;
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

.full_section{
    margin-top:-20%;
}
}

@media only screen and (min-width: 0px) and (max-width: 380px) {
  .slab_container{
    margin-bottom:-10%
}
.wrapperovertext{
  margin-top:-125%;
}

}

@media only screen and (min-width: 380px) and (max-width: 430px) {
  .slab_container{
    margin-bottom:-40%
}
.full_section{
    margin-bottom:-40%;
}
.wrapperovertext{
  margin-top:-110%;
}

}

@media only screen and (min-width: 430px) and (max-width: 576px) {
  .slab_container{
    margin-bottom:-10%
}
.wrapperovertext{
  margin-top:-95%;
}
.overText{
opacity:1;
    margin-top:0%;
}
}



@media only screen and (min-width: 576px) and (max-width: 768px) {

  .slab_container{
    margin-bottom:-10%
}
.wrapperovertext{
  margin-top:-90%;
}

.overText{
opacity:1;
    margin-top:0%;
}

}

@media only screen and (min-width: 768px) and (max-width: 992px) {
  .wrapperovertext{
  margin-top:-60%;
}

}


@media only screen and (min-width: 992px) and (max-width: 1200px) {

  .wrapperovertext{
  margin-top:-40%;
}


}


</style>