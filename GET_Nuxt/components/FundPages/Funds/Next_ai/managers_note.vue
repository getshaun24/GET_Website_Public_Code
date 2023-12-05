<template>
    
    <div style="padding-bottom:10%">
    
        <img data-lag=".2" class="text_section_image" :src="image" />
    
    
    <h3 class="text_section_title">Manager’s Note and Investment Thesis</h3>
    <div class="text_section_container">
    
    <p class="section_text">
        We GET it. OpenAI and Anthropic are red hot right now and yes, that is part of the idea here yet we like to look at our investments from other angles. Whether it is in fact OpenAI or Anthropic, or even Bard or Meta (or a company that hasn’t yet made the headlines) every player at that part of the stack relies on the companies above and below it. GET Equity Partners takes a holistic view of the sector and seeks to get involved at all levels to maximize our successes and the returns for our investors. After all, if this is the AI “gold rush”, we want a fund that invests in the proverbial pickaxe, helmets, and blue jeans makers that are still around today, not just the gold miners themselves.
    </p>
    
    <div class="button_container">
        <FundPagesFundsNextAiReserveMagneticBig/>
    </div>
 
    
    </div>
    
    
    </div>

    
    </template>
    
    
    <script setup>
    
    const props = defineProps(['lower_text', 'image'])
    
    </script>
    
    <style scoped>
    
    
    
   .text_section_container{
        width:80%;
        margin-left:10%;
        margin-top:5%;
        display:grid;
        grid-template-columns: repeat(1, 1fr);
        grid-template-rows: 1fr;
        grid-column-gap: 100px;
        grid-row-gap: 0px;
    }
    
    .company_highlights_inner{
        display:grid;
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: 1fr;
        grid-column-gap: 50px;
        grid-row-gap: 0px;
    }
    .text_section_title{
        margin-left:10%;
        margin-top:10%;
        width:80%
    }
    
    
    
    .text_section_image{
        width:60%;
        margin-left:20%;
        margin-bottom:0%;
        margin-top:15%
    }
    
    .section_text{
        font-size:130%;
    }
    
    
    
    @media only screen and (min-width: 0px) and (max-width: 376px) {
    
   .text_section_container{
    width:80%;
    margin-left:10%;
    margin-top:0%;
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(1, 1fr); 
    grid-column-gap: 0px;
    grid-row-gap: 50px;
    }
    
    .company_highlights_inner{
    margin-top:-30%
    }
    
    .section_text{
        font-size:130%;
    }
    
    .text_section_image{
        margin-top:10%
    }
    
    .text_section_title{
        margin-top:10%
    }
    }
    
    
    @media only screen and (min-width: 376px) and (max-width: 430px) {
    
   .text_section_container{
    width:80%;
    margin-left:10%;
    margin-top:0%;
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(1, 1fr); 
    grid-column-gap: 0px;
    grid-row-gap: 50px;
    }
    
    .company_highlights_inner{
    margin-top:-18%
    }
    
    .section_text{
        font-size:130%;
    }
    
    .text_section_image{
        margin-top:10%
    }
    
    .text_section_title{
        margin-top:10%
    }
    }
    
    
    
    
    
    @media only screen and (min-width: 430px) and (max-width: 500px) {
    
       .text_section_container{
        width:80%;
        margin-left:10%;
        margin-top:0%;
        display:grid;
        grid-template-columns: 1fr;
        grid-template-rows: repeat(1, 1fr); 
        grid-column-gap: 50px;
        grid-row-gap: 0px;
    }
    
    .company_highlights_inner{
        margin-top:-10%
    }
    
    .section_text{
        font-size:130%;
    }
    
    .text_section_image{
        margin-top:0%
    }
    
    .text_section_title{
        margin-top:0%
    }
    
    }
    
    
    @media only screen and (min-width: 500px) and (max-width: 530px) {
    
   .text_section_container{
    width:80%;
    margin-left:10%;
    margin-top:0%;
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    grid-column-gap: 50px;
    grid-row-gap: 0px;
    }
    
    .company_highlights_inner{
    margin-top:-10%
    }
    
    .section_text{
        font-size:130%;
    }
    
    .text_section_image{
        margin-top:0%;
    }
    .text_section_title{
        margin-top:0%
    }
    
    }
    
    
    @media only screen and (min-width: 530px) and (max-width: 576px) {
    
   .text_section_container{
    width:80%;
    margin-left:10%;
    margin-top:0%;
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    grid-column-gap: 50px;
    grid-row-gap: 0px;
    }
    
    .company_highlights_inner{
    margin-top:0%
    }
    
    .section_text{
        font-size:110%;
    }
    
    .text_section_image{
        margin-top:0%
    }
    .text_section_title{
        margin-top:0%
    }
    
    }
    
    
    @media only screen and (min-width: 576px) and (max-width: 650px) {
    
    
    .company_highlights_inner{
    margin-top:-14%
    }
    
    
    }
    
    
    @media only screen and (min-width: 650px) and (max-width: 768px) {
    
    
    .company_highlights_inner{
    margin-top:-12%
    }
    
    
    }
    
    
    
    
    @media only screen and (min-width: 576px) and (max-width: 768px) {
    
       .text_section_container{
    width:80%;
    margin-left:10%;
    margin-top:0%;
    display:grid;
    grid-template-columns: 1fr;
    grid-template-rows: repeat(2, 1fr); 
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    }
    
    .section_text{
        font-size:130%;
    }
    
    
    }
    
    @media only screen and (min-width: 768px) and (max-width: 992px) {
    
    .section_text{
        font-size:130%;
    }
    
    }
    
    @media only screen and (min-width: 992px) and (max-width: 1200px) {
    
        .section_text{
        font-size:130%;
    }
    }
    
    @media only screen and (min-width: 1200px) and (max-width: 1400px) {
    }
    
    @media only screen and (min-width: 1400px) and (max-width: 1600px) {
    }
    
    @media only screen and (min-width: 1600px) and (max-width: 5600px) {
    }
    
    
    
    .button_container{
        margin-top:5%;
        margin-bottom:5%;
    }
    
    
    </style>