<template>


<div class="white_background">
<Header/>

<GSAPScrollSmoother :refresh_it="refresh_it">


    <div class="investments_big">Investments</div>

    <div class="sorter"><span @click="topic_sort('all')" class="topic">All.</span> --- <span @click="topic_sort('materials')" class="topic">Materials Science</span> --- <span  @click="topic_sort('energy')" class="topic">Green Energy</span> --- <span  @click="topic_sort('fashion')" class="topic">Fashion</span> --- <span  @click="topic_sort('funding')" class="topic">Funding</span> --- <span @click="topic_sort('biotech')" class="topic">BioTech</span></div>

    <InvestHoverFull v-bind="invest_full_props_4" :sort_topic="sort_topic" />

<InvestHoverSplit v-bind="invest_split_props_1" :sort_topic="sort_topic" />

<InvestHoverFull v-bind="invest_full_props_1" :sort_topic="sort_topic" />

<InvestHoverSplit v-bind="invest_split_props_2" :sort_topic="sort_topic" />

<InvestHoverFull v-bind="invest_full_props_2" :sort_topic="sort_topic" />

<InvestHoverSplit v-bind="invest_split_props_3" :sort_topic="sort_topic" />

<InvestHoverFull v-bind="invest_full_props_3" :sort_topic="sort_topic" />

<div style="padding-bottom:10vh"></div>

        <Footer/>
</GSAPScrollSmoother>
  </div>



</template>



<script setup>

import image_split_1 from "~/assets/content/investments/invest_1.jpg"
import image_split_2 from "~/assets/content/investments/oil_gas_1.jpg"
import image_split_3 from "~/assets/content/investments/neural_inv_2_1.jpg"
import image_split_4 from "~/assets/content/investments/gww_inv_1.jpg"
import image_split_5 from "~/assets/content/investments/invest_10.jpg"
import image_split_6 from "~/assets/content/investments/helpul_offices_1.jpg"



import image_full_1 from "~/assets/content/investments/invest_5.jpg";
import image_full_2 from "~/assets/content/investments/invest_8.jpg"
import image_full_3 from "~/assets/content/investments/agile_3.jpg"
import image_full_4 from "~/assets/content/investments/hand_2.jpg"



const invest_split_props_1 = {
  left_title: 'NanoCarbon',
  left_subtitle: 'The Next Generation of Superconductors',
  left_hover_text: ' NanoCarbon  NanoCarbon  NanoCarbon ',
  left_link:'fund_pages/nano',
  left_image: image_split_1,
  left_topic: 'materials',
  right_title: 'Revitalization Fund',
  right_subtitle: 'Green Oil & Gas',
  right_hover_text: ' Revitalization  Revitalization  Revitalization ',
  left_side_small: false,
  right_side_small: true,
  right_link: 'fund_pages/eco',
  right_image: image_split_2,
  right_topic: 'energy',
}

const invest_split_props_2 = {
  left_title: 'Neuralink',
  left_subtitle: 'Merging With Our A.I. Overloards',
  left_hover_text: ' Neuralink  Neuralink  Neuralink ',
  left_link:'fund_pages/neuralink',
  left_image: image_split_3,
  left_topic: 'biotech',
  right_title: 'Green Worldwide',
  right_subtitle: 'Securing Our Energy Future',
  right_hover_text: ' Green Worldwide  Green Worldwide  Green Worldwide ',
  left_side_small: true,
  right_side_small: false,
  right_link: 'fund_pages/green_worldwide',
  right_image: image_split_4,
  right_topic: 'energy',
}

const invest_full_props_1 = {
  title: 'Impossible Foods',
  subtitle: ' Making Fake Food Tasty',
  hover_text: ' Impossible Impossible Impossible ',
  nuxt_link: 'fund_pages/impossible',
  image: image_full_1,
  topic: 'biotech'
}

const invest_full_props_2 = {
  title: 'Boysterous Couture',
  subtitle: ' Be Bold. Be Boysterous.',
  hover_text: ' Boysterous Boysterous Boysterous ',
  nuxt_link: 'fund_pages/boysterous',
  image: image_full_2,
  topic: 'fashion'
}


const invest_split_props_3 = {
  left_title: 'Social Wise',
  left_subtitle: 'An Artificial Intelligence Background Check',
  left_hover_text: ' Social  A.I.  Social A.I. ',
  left_link:'fund_pages/social_wise',
  left_image: image_split_5,
  left_topic: 'computer_science',
  right_title: 'Helpful+ Fund',
  right_subtitle: 'A New Distributed Investment Model',
  right_hover_text: ' Helpful+  Helpful+  Helpful+ Helpful+ ',
  left_side_small: false,
  right_side_small: true,
  right_link: 'fund_pages/helpful',
  right_image: image_split_6,
  right_topic: 'funding',
}

const invest_full_props_3 = {
  title: 'Agile Elements',
  subtitle: ' An Immune System For Your Fabrics.',
  hover_text: ' Agile Agile Agile ',
  nuxt_link: 'fund_pages/agile_elements',
  image: image_full_3,
  topic: 'materials'
}


const invest_full_props_4 = {
  title: 'NEXT AI',
  subtitle: ' Your NEXT Investment',
  hover_text: ' NEXT A.I. NEXT A.I. NEXT A.I. ',
  nuxt_link: 'fund_pages/next_ai',
  image: image_full_4,
  topic: 'materials'
}


const sort_topic = ref('all')
const refresh_it = ref(0)
function topic_sort(topic){
    console.log(topic)
    sort_topic.value = topic
    refresh_it.value += 1

}


</script>


<style scoped>


.white_background{
    background-color: #fff;
    height:200vh;
    width:100%;
    position:fixed;
    padding-top:5px;
    top:0;
    left:0;
    overflow: hidden;
}

.investments_big{
    font-size: 10vw;
    font-weight: 900;
    margin-left:5%;
    margin-top:15%;
    color:#000;
    line-height: .5;
}


.sorter{
  font-size: 250%;
    font-weight: 500;
    margin-left:5%;
    margin-top:10%;
    color:#000;
    line-height: 2;
    margin-right:5%
}


.topic{
    cursor: pointer;
}

.topic:hover{
    font-weight: 900;
    transition: all .2s ease;
}
















@media only screen and (min-width: 0px) and (max-width: 576px) {

  .sorter{
    font-size: 150%;
    line-height: 2;
    margin-right:5%
}

.investments_big{
    margin-top:18%;
}



}





@media only screen and (min-width: 576px) and (max-width: 768px) {
  .sorter{
    font-size: 150%;
    line-height: 2;
    margin-right:5%
}

.investments_big{
    margin-top:18%;
}




}

@media only screen and (min-width: 768px) and (max-width: 992px) {
  .sorter{
    font-size: 150%;
    line-height: 2;
    margin-right:5%
}

.investments_big{
    margin-top:18%;
}

}










</style>