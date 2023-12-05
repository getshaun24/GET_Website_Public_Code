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
  question: 'Senior Dev-Ops Engineer',
  answer: 'GET Resources Group is seeking an experienced Senior DevOps Engineer to join our technology team. In this role, you will be responsible for architecting, building, and managing our development and production infrastructure across multiple portfolio companies. As our Senior DevOps Engineer, you will: Design and implement CI/CD pipelines, infrastructure as code, and other DevOps best practices across our various technology stacks. Work closely with developers, SREs, and business stakeholders to understand requirements and deliver technical solutions. Proactively monitor, troubleshoot, and resolve issues across our infrastructure and application stacks. Evaluate and integrate new tools and technologies to improve developer productivity and application reliability/scalability. Coach and mentor junior members of the engineering team on DevOps methodologies and principles. Document infrastructure, configurations, and procedures thoroughly for transparency and maintainability. Requirements: 5+ years experience in a DevOps-focused engineering role, preferably at a finance/investing firm. Deep expertise with CI/CD tools like Jenkins, CircleCI, TravisCI, and Git workflows. Experience managing infrastructure as code through Terraform, CloudFormation, or similar. Proficiency with config management tools like Ansible, Chef, or Puppet. Experience deploying and managing microservices-based architectures. Strong scripting/automation skills and experience with tools like Packer and Kubernetes. Ability to collaborate with stakeholders at all levels, including executive leadership. This is an opportunity to make a significant impact by bringing industry-leading DevOps practices to a growing private equity firm. Core benefits include competitive salary and bonus, full medical/dental coverage, 401(k) matching, professional development budget, generous PTO, and flexible remote work arrangements. To apply, please email your resume to careers@thisisget.com and include "Senior DevOps Engineer" in the subject line. Qualified applicants will be contacted directly by our recruiting team. No third-party solicitations please.'
}

const q_a_prop_2 = {
  question: 'Financial Sales Associate',
  answer: "GET Resources Group is hiring a driven Financial Sales Associate to join our private equity firm, take ownership of developing new LP relationships and capital commitments in your region, be responsible for identifying new investment prospects, scheduling meetings to present our fund offerings and investment strategy, assessing investor needs and providing customized fund terms and structures, negotiating partnership agreements and securing capital commitments, while exceeding annual fundraising targets - top candidates have 5+ years of financial sales experience, excellent communication/presentation/negotiation skills, an entrepreneurial spirit and proven ability to overachieve aggressive targets, deep knowledge of private equity and venture capital markets, and a Bachelor's degree in Finance or related field - competitive compensation includes commission-based earnings, stellar benefits, and huge advancement potential in a growing, reputable private equity group.  To apply, please email your resume to careers@thisisget.com"
}

const q_a_prop_3 = {
  question: "Office Dog",
  answer: 'GET Resources Group seeks an enthusiastic, four-legged Office Dog to join our pack - your responsibilities will include attending meetings and providing stress relief cuddles and belly rubs to employees on demand, keeping spirits high by playing fetch in the office throughout the day, enthusiastically greeting our guests and partners, learning tricks to entertain team members, barking if you hear any non-transparent jargon being used, commandeering conference rooms for power naps when needed, and accepting treats and behind-the-ear scratches as your compensation. Requirements include being a VERY good boy/girl, having soft fur and tons of energy, enjoying loud environments with new people constantly coming and going, and loving to play with toys and chase squeaky things - leash optional, must be housebroken. Benefits include all the ear rubs, head pats and "good dog!"s you can handle!'
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