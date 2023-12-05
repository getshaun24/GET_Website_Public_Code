<template>
    
    <div>
    
        <img data-lag=".2" class="text_section_image" :src="image" />
    
    
    <h4 class="text_section_title">30 Years of Experience</h4>
    <div class="text_section_container">
    
    <p class="section_text" v-html="lower_text">
    
    </p>
    
    
 
    
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
        margin-top:10%
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
    grid-template-rows: repeat(2, 1fr); 
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
    grid-template-rows: repeat(2, 1fr); 
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
    
    
    
    
    
    
    </style>