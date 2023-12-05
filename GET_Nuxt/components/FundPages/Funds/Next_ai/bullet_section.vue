<template>

<CircleTransition ref="cicle_tansition"/>
<FundPagesFundsNextAiReserveModal ref="open_it"/>
    
    <div class="main_container">
        <h6 class="revenue_title">Building a Balanced Portfolio<br>- Not all AI is Equal</h6>
        <div class="revenue_container">
        
        <div class="revenue_text" data-lag=".1">
            <div class="revenue_text_container">
    
            <p class="para">
                As we move towards building our portfolio, we do not solely focus on what's trending but strive to invest across a balanced spectrum of the AI stack. This involves an understanding that not all AI is equal; there are different forms, applications, and technologies that require varied expertise and resources. Our approach is to strike the right balance in investing in the game-changing technologies and also the foundational layers that enable those technologies.
            </p>
            </div>
        </div>
        
        <img data-lag=".5" class="revenue_image" src="~/assets/content/fund_pages/next_ai/next_9.jpg" />
        
        
        </div>
    
        <p class="full_text">
            We are constantly scanning and analyzing a diverse range of AI companies, from the breakthrough innovators shaping the landscape to the infrastructural giants enabling the AI revolution. This includes machine learning, neural networks, robotics, natural language processing, and more. Our portfolio is purposefully diverse, reflecting our belief in the transformative power of AI across sectors - from healthcare and education to finance, energy, and beyond.<br><br>
            
            <span class="bullet_sect">
                <b>Our Investment Guidlines:</b> 
                <br><br><span class="bullet_margin">⚫ AI Equality: We value all AI equally, investing in diverse potential areas from innovative AI technologies to foundational systems.</span>
                <br><br><span class="bullet_margin">⚫ Balanced Investments: We strike a balance between disruptive technologies and stable platforms in our AI investments.</span>
                <br><br><span class="bullet_margin">⚫ Sector-Agnostic Approach: We believe in AI's transformative potential across industries - healthcare, education, finance, energy, etc.</span>
                <br><br><span class="bullet_margin">⚫ Continuous Analysis: We constantly evaluate a wide range of AI companies to keep our portfolio fresh and dynamic.</span>
                <br><br><span class="bullet_margin">⚫ Embracing AI Forms: Our portfolio spans across all forms of AI technologies - machine learning, neural networks, robotics, NLP, etc.</span>
                <br><br><span class="bullet_margin">⚫ Future-Focused: We invest in future-shaping AI companies for sustainable returns and growth.</span>
        </span>
        <button @click="open_popup_modal()" class="next_button">Get Started</button>
    </p>


    
        
    </div> 
        
    <div class="main_container_mobile">
        <div class="revenue_container_mobile">
        
            <img data-lag=".5" class="revenue_image" src="~/assets/content/fund_pages/next_ai/next_9.jpg" />
        
        <div class="revenue_text" data-lag=".1">
            <div class="revenue_text_container">
            <h2 class="title_mobile">Building a Balanced Portfolio - Not all AI is Equal</h2>
            <p class="para para_mobile">
                As we move towards building our portfolio, we do not solely focus on what's trending but strive to invest across a balanced spectrum of the AI stack. This involves an understanding that not all AI is equal; there are different forms, applications, and technologies that require varied expertise and resources. Our approach is to strike the right balance in investing in the game-changing technologies and also the foundational layers that enable those technologies.
           
               
            </p>
            </div>
        </div>
        
        </div>
    
        <p class="full_text">
            We are constantly scanning and analyzing a diverse range of AI companies, from the breakthrough innovators shaping the landscape to the infrastructural giants enabling the AI revolution. This includes machine learning, neural networks, robotics, natural language processing, and more. Our portfolio is purposefully diverse, reflecting our belief in the transformative power of AI across sectors - from healthcare and education to finance, energy, and beyond.<br><br>
            
            <span class="bullet_sect">
                <b>Our Investment Guidlines:</b> 
                <br><br><span class="bullet_margin">⚫ AI Equality: We value all AI equally, investing in diverse potential areas from innovative AI technologies to foundational systems.</span>
                <br><br><span class="bullet_margin">⚫ Balanced Investments: We strike a balance between disruptive technologies and stable platforms in our AI investments.</span>
                <br><br><span class="bullet_margin">⚫ Sector-Agnostic Approach: We believe in AI's transformative potential across industries - healthcare, education, finance, energy, etc.</span>
                <br><br><span class="bullet_margin">⚫ Continuous Analysis: We constantly evaluate a wide range of AI companies to keep our portfolio fresh and dynamic.</span>
                <br><br><span class="bullet_margin">⚫ Embracing AI Forms: Our portfolio spans across all forms of AI technologies - machine learning, neural networks, robotics, NLP, etc.</span>
                <br><br><span class="bullet_margin">⚫ Future-Focused: We invest in future-shaping AI companies for sustainable returns and growth.</span>
        </span>
        <button @click="open_popup_modal()" class="next_button">Get Started</button>
    </p>
        </div>
        
        
        
        
        </template>
        
        
        <script setup>
        
        const cicle_tansition = ref(null);

function transition_and_route(route_to) {
cicle_tansition.value.animation_and_route(route_to);
}


const open_it = ref(null);
function open_popup_modal() {
  open_it.value.open_modal();
}


        
        </script>
        
        
        
        <style scoped>
    

    .next_button{
    width:80%;
    height:40px;
    background-color:rgb(25, 120, 237) ;
    margin-left: 10%;
    margin-top:10%;
    border-radius:100px;
    border:#fff solid 0px;
    cursor:pointer;
    font-size:2vw;
    color:#fff;
    box-shadow: 0px 5px 12px rgba(0, 0, 0, 0.2);
    outline: 0px solid rgba(19, 218, 218, 0.6);
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
    z-index:2;
    mix-blend-mode:normal !important;
    filter: invert(1);
}


.next_button:hover{
  box-shadow: 0px 10px 15px rgb(25, 120, 237, .5);
  transform: translateY(-3px);
  outline: 3px solid rgba(19, 218, 218, 0.6);
  transition: outline 12s ease 1s;
} 
    
        .full_text{
            color:#fff;
            width:70%;
            margin-left:15%;
        }

        .bullet_sect{
            width:60%;
            text-align: justify;
            padding-left: 2.5em;
        text-indent:-2.5em;
        display: block; /* This makes the span behave like a block level element, which respects width */
        }

        .bullet_margin {
    margin-left: -2em;
}
        
        
        .revenue_container{
            display:grid;
            grid-template-columns: repeat(2, 1fr);
            grid-template-rows: 1fr;
            grid-column-gap: 20px;
            grid-row-gap: 0px;
            width:90%;
            margin-left:5%;
            margin-top:10%;
            margin-bottom:10%
        }
        
        .main_container_mobile{
            display:grid;
            grid-template-columns: 1fr;
            grid-template-rows: repeat(2, 1fr); 
            grid-column-gap: 0px;
            grid-row-gap: 0px;
            width:90%;
            margin-left:5%;
            margin-top:-20%;
            margin-bottom:10%
        }
        
        .revenue_title{
            color:#fff;
            margin-top:15%;
            width:70%;
            margin-left:15%;
        }
        
        .revenue_image{
            width:80%;
            margin-left:-5%;
        }
        
        .revenue_text{
            margin-left:10%
        }
        
        .revenue_text_container{
            margin-top:30%
        }
        
        .para{
            width:80%;
            color:#000;
            margin-top:-40%
        }
    
        .para_mobile{
            margin-top:0%;
        }
    
        .title_mobile{
                color:#000;
                margin-top:-10%;
            }
        
    
            @media only screen and (min-width: 0px) and (max-width: 380px) {
        
                .main_container{
                    display:none; 
                }
        .title_mobile{
            font-size:310%;
            color:#000;
            margin-top:-15%;
        }

        .revenue_image{
            width:80%;
            margin-left:-10%;
            margin-top:50%
        }
    }
    
        
        
        @media only screen and (min-width: 380px) and (max-width: 500px) {
        
            .main_container{
                    display:none; 
                }
            .title_mobile{
                font-size:310%;
                color:#000;
                margin-top:-8%;
            }
            .revenue_image{
            width:80%;
            margin-left:-10%;
            margin-top:30%
        }

        .full_text{
            margin-top:-75%
        }
        
        
        }
        
        @media only screen and (min-width: 0px) and (max-width: 576px) {

            .next_button{
    margin-top:30%;
    font-size:3vw;
    margin-bottom:20%;
    width:100%
}
        
            .main_container{
                    display:none; 
                }
        
        .revenue_container{
            display:none;
        }
        
        .revenue_text_container{
            margin-top:0%
        }
        
        .revenue_image{
            width:90%;
            margin-left:5%;
            margin-bottom:20%;
        }
        
        
        .para{
            width:90%
        }
        
        .revenue_title{
            color:#fff;
    
        }


        .full_text{
            margin-top:-75%
        }

        .bullet_sect{
            width:85%;
        }
        
        
        }

        @media only screen and (min-width: 0px) and (max-width: 410px) {

        .full_text{
            margin-top:-60%
        }

        }

        @media only screen and (min-width: 410px) and (max-width: 450px) {

        .full_text{
            margin-top:-55%
        }
        
        }

        @media only screen and (min-width: 450px) and (max-width: 500px) {
        .full_text{
            margin-top:-35%
        }
        }

        @media only screen and (min-width: 500px) and (max-width: 576px) {
        .full_text{
            margin-top:-5%
        }
        .revenue_image{
            margin-top:20%
        }
        }
        
        @media only screen and (min-width: 576px) and (max-width: 768px) {
            .main_container{
                    display:none; 
                }
        
            .revenue_container{
            display:none;
        }
        
        .revenue_text_container{
            margin-top:0%
        }
        
        .revenue_image{
            width:90%;
            margin-left:5%;
            margin-bottom:20%;
            margin-top:20%
        }
        
        
        .para{
            width:90%
        }
        
    
        .revenue_title{
            color:#fff;
        }

        .full_text{
            margin-top:0%
        }

        .bullet_sect{
            width:85%;
        }
        
        }

        @media only screen and (min-width: 576px) and (max-width: 650px) {
            .full_text{
            margin-top:0%
        }

        
    }

        @media only screen and (min-width: 650px) and (max-width: 768px) {
            .full_text{
            margin-top:10%
        }
        

        }
        
        @media only screen and (min-width: 768px) and (max-width: 992px) {
        .revenue_container{
            display:none;
        }
        
        .revenue_text_container{
            margin-top:0%
        }
        
        .revenue_image{
            width:90%;
            margin-left:5%;
            margin-bottom:20%;
            margin-top:20%
        }
        
        
        .para{
            width:90%
        }
        .revenue_title{
            color:#fff;
        }

        .main_container{
                    display:none; 
                }
        
                .main_container_mobile{
                    margin-bottom:-30%
                }

                .bullet_sect{
            width:75%;
        }
        
        }
        
        @media only screen and (min-width: 992px) and (max-width: 1200px) {
            .main_container_mobile{
                display:none;
            }
            .bullet_sect{
            width:65%;
        }
        }
        
        @media only screen and (min-width: 1200px) and (max-width: 1400px) {
            .main_container_mobile{
                display:none;
            }

            .bullet_sect{
            width:70%;
        }
        
        }
        
        @media only screen and (min-width: 1400px) and (max-width: 1600px) {
            .main_container_mobile{
                display:none;
            }
            
        }
        
        @media only screen and (min-width: 1600px) and (max-width: 5600px) {
            .main_container_mobile{
                display:none;
            }
        }
        
        
        
        
        
        </style>