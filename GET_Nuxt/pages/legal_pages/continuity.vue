<template>
    
    <Header/>
    
        <GSAPScrollSmoother>
    
<h5 class="page_title" data-speed="0.6" data-lag="0.2">Business Continuity Plan</h5>


<div class="main_text">

<p>
    Your business matters to us. GET Resource Group LLC (the “Firm”) maintains a Business Continuity Plan (BCP) designed to protect the safety of its employees, ensure the continuity of our business so we can continue to serve you, and protect the interests of its clients. The plan details the Firm’s response to a variety of business disruptions, including localized business interruptions, widespread disasters, and financial insolvency.

Under the plan, the Firm takes proactive steps to prepare for such disruptions and to minimize any resultant harm. These steps include establishing an emergency system for communication in a crisis, protecting firm data using redundant technical systems and periodic review of its emergency procedures.

In the case of an interruption or disaster, once its employees are safe, the Firm is committed to resuming business operations as soon as it is prudent to do so. Depending on the circumstances, our management may take any of the following steps, if appropriate:
    <ul>
     <li> Communicating with appropriate regulatory agencies</li>
     <li> Communicating with key stakeholders including the Firm’s clients</li>
     <li> Operating from an alternative location</li>
     <li> Dispersing of assets orderly, if and only if, as a result of the contingency, continued operation is not appropriate</li>
    </ul>
In the case of financial insolvency, the Firm will diligently seek to raise additional financing, including from affiliates, or, if necessary, orderly proceed in accordance with applicable law. In the event of the Firm’s insolvency, its Manager will continue to work through any issues to best resolve allocation of ownership/capital entitled to owner.
</p>


</div>








<Footer/>
        </GSAPScrollSmoother>
    

</template>

<script setup>

const title_move = ref('100%');


onMounted(() => {
title_move.value = '35%';
})

</script>


<style scoped>

.page_title{
    background-color:#fff;
    background-image: url('~/assets/content/careers/careers_2.jpg');
    padding:25px;
    width:65%;
    margin-left:v-bind(title_move);
    text-align: center;
    border-top-left-radius: 10px;
    border-bottom-left-radius: 10px;
    z-index:10000;
    color: #fff;
    filter: drop-shadow(5px 3px 5px #ffffff21);
    transition: margin-left 1.75s ease 1.5s;
}

.main_text{
    width:80%;
    margin-left:10%;
    margin-bottom:10%;
    margin-top:30%
}

.section_title{
    font-size:35px
}

.section_subtitle{
    text-decoration: underline;
    text-underline-offset: 5px;
    text-decoration-thickness: 1px;
    text-decoration-color: #1978ed;
}

</style>