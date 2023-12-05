<template>
    


<div class="slab_container" :style="{'height':height + 400 + 'px'}">
<img data-speed="auto" class="slab_img" src="~assets/content/how_it_works/how_it_works_3.jpg">
<div class="faq_container" ref="el">

<HIWFaqsFaqElm v-bind="q_a_prop_1" />
<HIWFaqsFaqElm v-bind="q_a_prop_2" />
<HIWFaqsFaqElm v-bind="q_a_prop_3" />



</div>
</div>


</template>

<script setup>

import { ref } from 'vue'
import { useElementSize } from '@vueuse/core'

const props = defineProps(['q_a_prop_1', 'q_a_prop_2', 'q_a_prop_3'])


const el = ref(null)
const { height } = useElementSize(el)

const q_a_prop_1 = {
  question: 'Are GET Equity Partners deals registered with the SEC?',
  answer: "Currently GET's deals are registered for exemption under Regulation D with the SEC. \n \n Learn more here. \n https://www.investor.gov/introduction-investing/investing-basics/glossary/rule-506-regulation-d"
}

const q_a_prop_2 = {
  question: 'Is GET Equity Partners a broker dealer?',
  answer: 'No. GET currently only offers deals which are exempt from registration with the SEC and regulatory bodies. '
}

const q_a_prop_3 = {
  question: 'How are my investments in a GET fund "safe"?',
  answer: 'GET Equity Partners deals differ so please see the PPM and Operating Agreements for Risk Factors and other such warranties made by the company and manager. Generally speaking while the investments are being held, and before they are invested per the operating agreement, the capital is held at an FDIC insured bank.'
}



</script>



<style scoped>





.slab_container{
  position: relative;
 min-height: 80vh;
 width: 100%;
 overflow: hidden;
 margin-top:15%;
}
.slab_img{
  position: absolute;
  bottom: 0;
  height: 120%;
}


.faq_container{
    background-color:#fff;
    width:60%;
    margin-top:20vh;
    position: absolute;
    margin-left:20%;
    border-radius:10px;
}




@media only screen and (min-width: 0px) and (max-width: 576px) {
  .faq_container{
    width:80%;
    margin-top:20vh;
    margin-left:10%;
}

}

@media only screen and (min-width: 576px) and (max-width: 768px) {

  .faq_container{
    width:80%;
    margin-top:20vh;
    margin-left:10%;
}

}

@media only screen and (min-width: 768px) and (max-width: 992px) {

  .faq_container{
    width:70%;
    margin-top:20vh;
    margin-left:15%;
}

}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
  .faq_container{
    width:70%;
    margin-top:20vh;
    margin-left:15%;
}

}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
}




</style>