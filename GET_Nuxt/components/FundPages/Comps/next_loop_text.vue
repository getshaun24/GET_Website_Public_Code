<template>
    

<div class="wrapperRollingText">
  <div class="rollingText_Next" data-lag=".1" >
    Next<span class="period_color">.</span> Next<span class="period_color">.</span>
    Next<span class="period_color">.</span> Next<span class="period_color">.</span>
    Next<span class="period_color">.</span> Next<span class="period_color">.</span>
    Next<span class="period_color">.</span> Next<span class="period_color">.</span>
    Next<span class="period_color">.</span> Next<span class="period_color">.</span>&nbsp;

  </div>
</div>




</template>



<script setup>

import { onMounted, onUnmounted, onBeforeMount, ref } from 'vue';
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
gsap.registerPlugin(ScrollTrigger);



            // sleep time expects milliseconds
            function sleep (time) {
              return new Promise((resolve) => setTimeout(resolve, time));
            }



const headings = ref()
        const headingIndex = ref()
        const mySplitText = ref()
        const chars = ref()
        const tl2 = ref()
        const tl3 = ref()

        let direction = ref(1); // 1 = forward, -1 = backward scroll
        const roll1 = ref()
        const tl = ref()
        let clone = ref()
        const scroll = ref()


        const uncover = ref()




onMounted(() => {

  sleep(2100).then(() => { 


// NOTE: for a responsive version, see https://codepen.io/GreenSock/pen/QWqoKBv

let direction_next = -1; // 1 = forward, -1 = backward scroll

const rollNext = nextroll(".rollingText_Next", { duration: 40}),
  scroll_next = ScrollTrigger.create({
    onUpdate(self) {
      if (self.direction !== direction_next) {
        direction_next *= 1;
        gsap.to([rollNext], { timeScale: direction_next, overwrite: true });
      }
    }
  });

// helper function that clones the targets, places them next to the original, then animates the xPercent in a loop to make it appear to roll across the screen in a seamless loop.
function nextroll(targets, vars, reverse) {
  const tl_next = gsap.timeline({
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
    tl_next.to([el, clone], { xPercent: reverse ? 100 : -100, ...vars }, 0);
  });
  return tl_next;
}

// make sure there is a background to the text to mask the overlapping text



})




})


onUnmounted(() => {
    
  ScrollTrigger.refresh();

      console.log('REFRESHED')

    })

</script>





<style scoped>




         .rollingText_Next {
   font-size: 4vw;
   padding-left: 10px;
   font-weight: 900;
   word-spacing: 20px;
   white-space: nowrap;
     margin-top:1%;
    width:5000vw;
    background-color:black;
    text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff;


 }


.wrapperRollingText{
  position:relative;
  display: flex;
  overflow: hidden;
}




.period_color{
    color:#4478C4;
    text-shadow: -1px -1px 0 #4478C4, 1px -1px 0 #4478C4, -1px 1px 0 #4478C4, 1px 1px 0 #4478C4;
}



</style>