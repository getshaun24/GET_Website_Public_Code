<template>
    
    <CircleTransition ref="cicle_tansition"/>

    <Header/>
    
        <GSAPScrollSmoother>
    
            
            <ScrubText v-bind="scrub_text_1"/>
    
            <div class="topic_column">
                <h3 class="topic">Finance<span class="num"> ( 2 )</span></h3>
                <h3 class="topic">Technology<span class="num"> ( 1 )</span></h3>
                <h3 class="topic">Green Energy<span class="num"> ( 1 )</span></h3>
                <!-- <h3 class="topic">Materials Science<span class="num"> ( 1 )</span></h3>
                <h3 class="topic">MCA Funding<span class="num"> ( 1 )</span></h3>
                <h3 class="topic">Fashion<span class="num"> ( 1 )</span></h3>
                <h3 class="topic">Logistics<span class="num"> ( 1 )</span></h3> -->
                </div>
        
            <div class="blog_grid">
    
                    <div @click="transition_and_route('/blog_pages/blog_2')" data-lag=".1" class="blog_box">
                    <div class="img_box">
                     <img data-speed=".9" class="img" src="../assets/content/blogs/blog_covers/blog_6.jpg">
                    </div>
                     <h3 class="box_text">Why Private Equity, Why Now?</h3>
                     <div class="text_line"></div>
                    </div>
    
                    <div @click="transition_and_route('/blog_pages/blog_3')" data-lag=".1" class="blog_box">
                        <div class="img_box">
                    <img data-speed=".9" class="img" src="../assets/content/blogs/blog_covers/blog_5.jpg">
                     </div>
                     <h3 class="box_text">An Investment in Energy is a Growth Investment</h3> <div class="text_line"></div>
                    </div>
    
                    <div @click="transition_and_route('/blog_pages/blog_4')" data-lag=".1" class="blog_box">
                        <div class="img_box">
                        <img data-speed=".9"  class="img" src="../assets/content/blogs/blog_covers/blog_7.jpg"> 
                    </div>
                    <h3 class="box_text">The Importance of SMBs in the Economy</h3> <div class="text_line"></div>
                </div>
                <div @click="transition_and_route('/blog_pages/blog_1')" data-lag=".1" class="blog_box">
                        <div class="img_box">
                        <img data-speed=".9"  class="img" src="../assets/content/blogs/blog_covers/blog_1.jpg"> 
                    </div>
                    <h3 class="box_text">5 Reasons Why Digital Payments Are the Future of Commerce</h3> <div class="text_line"></div>
                </div>
    
    
    
<!--     

                    <div data-lag=".6" class="blog_box">
                        <div class="img_box">
                        <img data-speed=".9"  class="img" src="../assets/content/blogs/boring_7.jpg"> 
                    </div>
                    <h3 class="box_text">Using AI and Machine Learning to Streamline Financial Operations</h3> <div class="text_line"></div></div>
                    <div data-lag=".1" class="blog_box">
                        <div class="img_box">
                        <img data-speed=".9"  class="img" src="../assets/content/blogs/agile_28.jpg"> 
                    </div>
                    <h3 class="box_text">How Fintech is Making Personal Finance More Accessible to Everyone</h3> <div class="text_line"></div></div>
    
    
    
    
                    <div  data-lag=".1"  class="blog_box">
                        <div class="img_box">
                        <img data-speed=".9"  class="img" src="../assets/content/blogs/social_10.jpg"> 
                    </div>
                    <h3 class="box_text">From Traditional Banking to Digital Banking: The Advantages of Fintech</h3> <div class="text_line"></div></div>
                    <div data-lag=".6" class="blog_box">
                        <div class="img_box">
                        <img data-speed=".9"  class="img" src="../assets/content/blogs/boy_22.jpg"> 
                    </div>
                    <h3 class="box_text">The Importance of Cybersecurity in Fintech: Protecting Your Financial Data</h3> <div class="text_line"></div></div>
                    <div data-lag=".1" class="blog_box">
                        <div class="img_box">
                        <img data-speed=".9"  class="img" src="../assets/content/blogs/neuro_3.jpg"> 
                        <div class="pin_end"></div>
                    </div>
                    <h3 class="box_text">Fintech and Financial Literacy: How Technology Can Help Improve Financial Education</h3> <div class="text_line"></div></div>
    
    
    
    
                    <div class="blog_box">
                        <div class="img_box">
                        <img data-speed=".9"  class="img" src="../assets/content/blogs/thermo_7.jpg"> 
                    </div>
                    <h3 class="box_text">Investing in the Future: How Fintech Is Changing the Investment Landscape</h3> <div class="text_line"></div></div>
                    <div data-lag=".6" class="blog_box">
                        <div class="img_box">
                        <img data-speed=".9"  class="img" src="../assets/content/blogs/instibanc_logo_2.jpg"> 
                    </div>
                    <h3 class="box_text">The Benefits of Cloud-Based Financial Management Solutions</h3> <div class="text_line"></div></div>
                    <div data-lag=".1" class="blog_box">
                    <div class="img_box">
                        <img data-speed=".9"  class="img" src="../assets/content/blogs/get_media_5.jpg"> 
                    </div>
                    <h3 class="box_text">The Future of Banking: Exploring the Possibilities of Open Banking</h3> <div class="text_line"></div>
                </div>
     -->

    
            </div>
 
    
    <Footer/>
        </GSAPScrollSmoother>
    
    
    </template>


<script setup>


const scrub_text_1 = {text:'Blog', duration:40,}



const cicle_tansition = ref('');

function transition_and_route(route_to) {
 cicle_tansition.value.animation_and_route(route_to);
}

</script>
    
    <style scoped>
    
    
    .blog_grid{
        display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(6, 1fr);
    grid-column-gap: 10px;
    grid-row-gap: 8vw;
    width:55vw;
    margin-left:45vw;
    margin-top:20%;
    margin-bottom:20%;
    }
    
    .img_box{
        width:20vw;
        height:20vw;
        border: 1px solid #00000000;
        overflow:hidden
    }
    .blog_box{
        width:70%;
        height:100%;
        border: 1px solid #00000000;
        cursor: pointer;
    
    }
    
    
    .blog_box:hover .text_line{
        border-bottom:3px solid #fff;
        width:80%;
        transition:all ease 2s
    }
    
    .text_line{
        width:0%;
        border-bottom:3px solid #fff;
        margin-top:-20px
    }
    
    .img{
        width:100%;
        height:100%;
        object-fit: cover;
        object-position: center;
    }
    
    
    
    .topic_column{
        position:absolute;
        top:70vh;
        left:5%;
        width:25%
    }

    .num{
        font-size:12px;
        margin-top:-7px;
        color:#fff
    }

    .topic{
        font-size:30px;
        margin-top:10px;
        margin-left:10px;
        color:#fff;
        cursor: pointer;
        white-space: nowrap;
    }

    .topic:hover{
        color:#2580e2;
        transition:all ease 4s
    }

    .topic:hover .num{
        color:#2580e2;
        transition:all ease .3s
    }

    .box_text{
        font-size:18px;
        margin-top:10px;
        margin-left:10px;
        color:#fff;
        cursor: pointer;
        padding-bottom:15px
    }
    
    
    
@media only screen and (min-width: 0px) and (max-width: 576px) {
    .topic{
        font-size:15px;
    }
    .box_text{
        font-size:15px;
    }

    .img_box{
        width:100%;
        height:auto;
        border: 1px solid #00000000;
        overflow:hidden
    }

    .blog_grid{
        display: grid;
    grid-template-columns: repeat(1, 1fr);
    grid-template-rows: repeat(6, 1fr);
    grid-row-gap: 15vw;
    width:50%;
    margin-left:50%;
    margin-top:30%;
    }

    .blog_box{
        width:90%;
        height:100%;
        border: 1px solid #00000000;
        cursor: pointer;
    
    }
    
    
    

}

@media only screen and (min-width: 576px) and (max-width: 768px) {
    .topic{
        font-size:18px;
    }
    .box_text{
        font-size:15px;
    }
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