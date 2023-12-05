<template>
    



<div v-if="!is_mobile" class="parralax_container">

<div style="padding-top:200px;" class="parralax_section">
<div class="parralax_text_left" data-lag=".1">
  <h6 class="para_title"><strong>Access Private Technology Companies</strong></h6>
  <p class="para_text">Tap into a $500B venture-backed equity class. Invest in GET investment funds which purchase and own the shares on behalf of investors. </p>
  <h6 class="para_title"><strong>Company-Friendly Transactions</strong></h6>
  <p class="para_text">We work closely with companies to understand how best to capitalize their needs, and investors on how to get the best shares and the best price. Whether it’s warrants, shares from early employees, or more typical venture capital equity plays, we work with all parties to achieve the best outcome for all involved.</p>
</div>
<div class="parralax_image_container_right">
  <img class="parralax_img" data-speed="auto" src="~/assets/content/how_it_works/how_it_works_1.jpg" alt="">
</div>
</div>

<div style="padding-top:200px" class="parralax_section">
<div class="parralax_image_container_left">
  <img class="parralax_img" data-speed="auto" src="~/assets/content/how_it_works/how_it_works_6.jpg" alt="">
</div>
<div class="parralax_text_right" data-lag=".1">
    <h6 class="para_title"><strong>Curated Investments</strong></h6>
  <p class="para_text">We provide proprietary analysis including recent price history, valuation and cap tables. While not without risk, we offer companies with proven track-records of raising capital, generally from top-tier venture capital investors.</p>
  <h6 class="para_title"><strong>Guided Transactions</strong></h6>
  <p class="para_text">Our platform guides you through the complex process of transferring equity ownership, and keeps you updated on the progress of your investment. Execute and manage all your investment documents easily on the GET platform.</p>
</div>
</div>
</div>






<div v-else class="parralax_container_mobile">

<div style="padding-top:100px;" class="parralax_section_mobile">

<div class="parralax_text_mobile" data-lag=".1">
  <h6 class="para_title"><strong>Access Private Technology Companies</strong></h6>
  <p class="para_text">Tap into a $500B venture-backed equity class. Invest in GET investment funds which purchase and own the shares on behalf of investors. </p>
</div>

  <div class="parralax_image_container">
  <img class="parralax_img" data-speed="auto" src="~/assets/content/how_it_works/how_it_works_1.jpg" alt="">
</div>

<div class="parralax_text_mobile" data-lag=".1">
  <h6 class="para_title"><strong>Company-Friendly Transactions</strong></h6>
  <p class="para_text">We work closely with companies to understand how best to capitalize their needs, and investors on how to get the best shares and the best price. Whether it’s warrants, shares from early employees, or more typical venture capital equity plays, we work with all parties to achieve the best outcome for all involved.</p>
</div>

</div>


<div class="parralax_section_mobile">

<div class="parralax_text_mobile" data-lag=".1">
    <h6 class="para_title"><strong>Curated Investments</strong></h6>
  <p class="para_text">We provide proprietary analysis including recent price history, valuation and cap tables. While not without risk, we offer companies with proven track-records of raising capital, generally from top-tier venture capital investors.</p>
</div>

  <div class="parralax_image_container">
  <img class="parralax_img" data-speed="auto" src="~/assets/content/how_it_works/how_it_works_6.jpg" alt="">
</div>

<div class="parralax_text_mobile" style="margin-top:-5%" data-lag=".1">
  <h6 class="para_title"><strong>Guided Transactions</strong></h6>
  <p class="para_text">Our platform guides you through the complex process of transferring equity ownership, and keeps you updated on the progress of your investment. Execute and manage all your investment documents easily on the GET platform.</p>
</div>
</div>
</div>



</template>




<script setup>
import { useWindowSize } from '@vueuse/core'

const is_mobile = ref(false)
const { width, height } = useWindowSize()


console.log("🚀 ~ file: text_with_slab.vue:89 ~ width:", width.value)
console.log("🚀 ~ file: text_with_slab.vue:88 ~ is_mobile:", is_mobile.value)


onMounted(() => {
if(width.value < 992){
    is_mobile.value = true
    console.log("🚀 ~ file: text_with_slab.vue:88 ~ is_mobile:", is_mobile.value)
}
})

</script>




<style scoped>




.parralax_container{
    width:80%;
    margin-left:10%;
}

.parralax_container_mobile{
    width:100%;
    margin-left:10%;
    margin-top:10%;
    margin-bottom:-10%
}


.parralax_section {
    align-items: center;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr;
    grid-column-gap: 10px;
    grid-row-gap: 0;
    margin-top: 100px;
    margin-bottom: 100px;
    height: 800px;
    width: 100%;
    position: relative;
}

.parralax_section_mobile {
    align-items: center;
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(3, 1fr); 
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    margin-top: 0px;
    margin-bottom: 0px;
    height: 800px;
    width: 80%;
    position: relative;
}

.parralax_text_right {
    position: relative;
    border-bottom: rgb(78, 152, 242) 1px solid;
    width: 80%;
    margin-left: 0;
    padding-bottom:10px
}
.parralax_text_left {
    position: relative;
    border-bottom: rgb(78, 152, 242) 1px solid;
    width: 80%;
    padding-bottom:10px
}

.parralax_text_mobile{
    position: relative;
    border-bottom: rgb(78, 152, 242) 1px solid;
    width: 100%;
    margin-left: 0%;
    padding-bottom:0px;
}
.parralax_image_container_right {
    position: relative;
    overflow: hidden;
    width: 90%;
    height: 60%;
    border-radius: 10px;
    margin-left: 10%;
}
.parralax_image_container_left {
    position: relative;
    overflow: hidden;
    width: 90%;
    height: 60%;
    border-radius: 10px;
}

.parralax_image_container{
    position: relative;
    overflow: hidden;
    width: 100%;
    height: 80%;
    border-radius: 10px;
    margin-bottom:-40%;
    margin-top:-30%
}

.parralax_img{
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 130%;
    object-fit: cover;
    border-radius: 10px;
    object-position: center;
}



.para_text{
    font-size:90%;
}
.para_title{
    margin-bottom:10px
}







@media only screen and (min-width: 0px) and (max-width: 576px) {
    

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