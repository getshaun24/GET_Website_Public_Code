
<template>
    
<div class="footer_container" ref="target">
<div class="footer_move">

        
    

    <FundPagesCompsNextLoopText/>
    

    <div @click="add_padding_for_transition" class="next_grid">
    <div>
    <h4 class="next_company" v-html="title"></h4>
    </div>
    <div class="next_grid_inner_images">
    <div class="arrow_container">
    <img class="next_image_arrow" src="~/assets/content/fund_pages/nano/next_arrow.png" />
    </div>
    <div class="next_image_container">
    <img class="next_image" data-lag=".5" :src="image" />
    </div>
    </div>
</div>
    
    <p class="next_footer_legal_solo">Some opportunities posted on this website are "private placements" of GET Holdings and are not publicly traded, yet are subject to holding period requirements which are intended for investors who do not need a liquid investment. Investing in private companies may be considered highly speculative and involves a high degree of risk, including the risk of substantial loss of investment. Investors must be able to afford the loss of their entire investment. See our Risk Factors for a more detailed explanation of the risks involved in investing in GET Resources Holdings. GET Resource Holdings LLC (“GET Holdings”) is a subsidiary of GET Resources LLC, a private company. ThisisGET.com is a website operated by GET Resources LLC ("GET"). By accessing this site and any pages thereof, you agree to be bound by our Terms of Use. GET and logo are owned by GET Resources LLC. Other trademarks are property of their respective owners. © 2020 GET Resources LLC. All rights reserved.</p>
    
    </div>
</div>

    
    </template>
    
    
    
    <script setup>
    
  
    import { useIntersectionObserver } from '@vueuse/core'
    

const props = defineProps(['title', 'image', 'nuxt_link'])
preloadRouteComponents(props.nuxt_link)

const pad_bottom = ref('0vh')

const target = ref(null)
const targetIsVisible = ref(false)
const footer_scroll_height = ref("100%")

    const { stop } = useIntersectionObserver( target,
      ([{ isIntersecting }], observerElement) => {
        targetIsVisible.value = isIntersecting
        if (targetIsVisible.value == true){
            footer_scroll_height.value = "0%"
        } else{
            footer_scroll_height.value = "100%"
        }
      },
    )


    function add_padding_for_transition(){
        pad_bottom.value = "100vh"
        navigateTo(props.nuxt_link)
    }
    
    
    </script>
    <style scoped>
    

.footer_container{
    height:75vh;
    background-color: #000; 
    z-index:1000; 
    padding-bottom: v-bind(pad_bottom);
        transition: padding-bottom 1s ease
}


.footer_move{
    background-color: #000; 
    height:70vh;
    z-index:100;
    transform: translateY(v-bind(footer_scroll_height));
    transition: transform .9s ease .5s;
}








    
    .next_grid{
            width:90%;
            margin-left:5%;
            display:grid;
            grid-template-columns: repeat(2, 1fr);
        grid-template-rows: 1fr;
        grid-column-gap: 0px;
        grid-row-gap: 0px;
        margin-top:5%;
        height:100%;
        cursor:pointer;
        }
    


    .next_image{
            width:125%;
            border-radius: 100%;
            transition:width ease .5s;
        }

        
        .next_image:hover{
            filter: invert();
            width:130%
        }

    
    
        .next_image_container{
            width:100%;
            margin-top:-5%;
            margin-left:-80%;
            transition:all ease .5s;
            margin-bottom:100%
        }
    
        .next_company{
            background-color: #000;
            font-weight: 900;
            color:#fff;
            text-decoration: underline;
            text-decoration-color: rgb(14, 85, 166);
            text-underline-offset: 12px;
        }
    
        .arrow_container{
            overflow: hidden;
        }
    
        .next_image_arrow{
            filter: invert(1);
            width:95%;
            margin-top:35%;
            margin-left:-100%;
            transition:all ease .5s;
            opacity:0;
        }
    

        .next_grid_inner_images{
            width:100%;
            display:grid;
            grid-template-columns: repeat(2, 1fr);
        grid-template-rows: 1fr;
        grid-column-gap: 100px;
        grid-row-gap: 0px;
        margin-left:-10%;
        margin-right:-20%
        }
    
    
        .next_grid:hover .next_image_arrow{
            transition:margin-left ease .85s, opacity ease 1.25s;
            margin-left:2.5%;
            opacity:1;
        }
    
    
        .next_grid:hover .next_image_container{
            margin-left:-10%;
            transition:margin-left ease 1.5s;
        }

        .next_footer_legal_solo{
            font-size:8.5px;
            width:95%;
            padding-left:2.5%;
            position: absolute;
            bottom: 0;
            line-height: 1;
        }
    
        .next_line{
            width:90%;
            height:2px;
            background-color:rgb(0, 122, 204);
            margin-top:-80px
        }


        @media only screen and (min-width: 0px) and (max-width: 376px) {

            .next_image_container{
            width:85%;
            margin-top:0%;
            margin-left:-20%;
            transition:all ease .5s;
            margin-bottom:0%;
        }


        .next_grid{
            grid-template-columns: 1fr;
        grid-template-rows:repeat(2, 1fr); 
        margin-top:-10%;
        }
    
        .next_grid_inner_images{
            width:85%;
            display:grid;
            grid-template-columns: repeat(2, 1fr);
        grid-template-rows: 1fr;
        grid-column-gap: 20px;
        grid-row-gap: 0px;
        margin-left:0%;
        margin-right:0%;
        margin-top:-3.5%;
        }

        .next_image_arrow{
            width:65%;
            margin-top:40%;
            margin-left:2.5% !important;
            opacity:1;
        }

        .next_footer_legal_solo{
            position: absolute;
            bottom: -30px;
        }

        }

   
    
        @media only screen and (min-width: 376px) and (max-width: 430px) {

            .next_image_container{
            width:125%;
            margin-top:0%;
            margin-left:-20%;
            transition:all ease .5s;
            margin-bottom:0%;
        }


        .next_grid{
            grid-template-columns: 1fr;
        grid-template-rows:repeat(2, 1fr); 
        }
    
        .next_grid_inner_images{
            width:85%;
            display:grid;
            grid-template-columns: repeat(2, 1fr);
        grid-template-rows: 1fr;
        grid-column-gap: 20px;
        grid-row-gap: 0px;
        margin-left:0%;
        margin-right:0%;
        margin-top:-22.5%;
        }

        .next_image_arrow{
            width:85%;
            margin-top:50%;
            margin-left:2.5% !important;
            opacity:1;
        }

        .next_footer_legal_solo{
            position: absolute;
            bottom: -30px;
        }
        }


        @media only screen and (min-width: 430px) and (max-width: 576px) {

.next_image_container{
width:70%;
margin-top:0%;
margin-left:5%;
transition:all ease .5s;
margin-bottom:0%;
}


.next_grid{
grid-template-columns: 1fr;
grid-template-rows:repeat(2, 1fr); 
margin-top:-2%;
}

.next_grid_inner_images{
width:85%;
display:grid;
grid-template-columns: repeat(2, 1fr);
grid-template-rows: 1fr;
grid-column-gap: 20px;
grid-row-gap: 0px;
margin-left:0%;
margin-right:0%;
margin-top:-10%;
}

.next_image_arrow{
width:65%;
margin-top:25%;
margin-left:10% !important;
opacity:1;
}

.next_footer_legal_solo{
position: absolute;
bottom: -30px;
}
}
    
    </style>



