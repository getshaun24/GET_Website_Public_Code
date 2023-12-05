<template>
    
    <CircleTransition ref="cicle_tansition"/>
    <Header/>
    
        <GSAPScrollSmoother>

            <img src="~/assets/content/blogs/blog_pages/blog_3/blog_top.jpg"  class="blog_img_top">

            <img data-speed="1.5" src="~/assets/content/blogs/blog_pages/blog_3/blog_side.jpg"  class="blog_img_side">
    
    <h6 class="blog_title">An Investment in Energy is a Growth Investment</h6>

    <p class="blog_date">Posted on 04/07/2023</p>

            <div class="main_content">
            <p><i>Regardless of the industry, one thing is sure: the need for cheap, clean, reliable energy in only increasing.
            </i></p>

            <p>In today's world, the demand for energy is constantly increasing, and as a result, GET Equity Partners believes that the need for clean and sustainable energy solutions is increasingly important. The rise of energy startups, which are companies that are focused on developing innovative energy technologies and solutions to meet the growing demand for energy in a sustainable manner represent a massive investment opportunity. These startups are particularly important investments currently for a number of reasons.
            </p>

            <p>Firstly, energy startups are addressing a major global issue that is at the forefront of people's minds. Climate change is a major concern for many individuals and organizations, and energy startups are playing a critical role in developing clean energy solutions that can help mitigate the effects of climate change. As a result, investing in energy startups not only offers the potential for financial returns, but also the opportunity to contribute to a cause that is important to many people.
            </p>

            <p>Thirdly, energy startups have the potential to provide significant returns for investors. Many energy startups are venture-backed and have the potential to become unicorns, which are startups valued at over $1 billion. For example, Tesla, which is now a publicly-traded company, was once a startup that received significant venture capital investment. Investing in energy startups can offer the potential for significant returns, especially for those that are able to identify the most promising companies early on.
            </p>

            <p>
                Finally, energy startups are attracting a significant amount of funding from investors. According to a report by Cleantech Group, global venture capital investment in energy startups reached $7.5 billion in 2020, up from $5.2 billion in 2019. This demonstrates that investors are recognizing the importance of energy startups and the potential for significant returns.
            </p>


            <p>
                In conclusion, energy startups are particularly important investments currently due to their ability to address a major global issue, disrupt traditional energy markets, provide significant returns, and attract significant funding from investors. Investing in energy startups offers the potential for financial returns, as well as the opportunity to contribute to a cause that is important to many individuals and organizations. As the demand for clean and sustainable energy solutions continues to grow, energy startups are well-positioned to play a critical role in meeting this demand.
            </p>
    
        </div>


        <div @click="transition_and_route('blog_4')" class="next_container">
        <div class="flex_row">
            <img class="invert_it" src="~/assets/content/homepage/arrow_medium_light.png">
        <h2 class="next_text">NEXT</h2>
    </div>

            <p class="next_blog">The Importance of SMBs in the Economy</p>

    </div>

    <Footer/>
        </GSAPScrollSmoother>
</template>


<script setup>


const cicle_tansition = ref('');

function transition_and_route(route_to) {
 cicle_tansition.value.animation_and_route(route_to);
}



</script>


<style scoped>

.blog_title{
    width:80%;
    margin-left:10%;
    margin-bottom:3%
}


.blog_img_top{
    max-height:400px;
    width:100%
}

.blog_img_side{
    width:300px;
    height:100vh;
    float:right;
    margin-top:50vh;
}

.main_content{
    width:60%;
    margin-left:10%;
    margin-bottom:15%;
    padding-top:2.5%
}

.subtitle{
    text-decoration: underline;
    text-underline-offset: 5px;
    text-decoration-thickness: 2px;
    text-decoration-color: #1978ed;
    margin:15% 0% 5%;
    font-size:35px;
}

.blog_date{
    margin-left:10%;
    margin-bottom:5%;
    font-size:13px;
    text-decoration: underline;
    text-underline-offset: 5px;
    text-decoration-thickness: 1px;
    text-decoration-color: #1978ed;
    }




    .next_container{
        display:flex;
        flex-direction: column;
        justify-content:center;
        align-items:center;
        margin-top: -10%;
        cursor: pointer;
        margin-bottom: 15%;
        width:60%;
        margin-left:20%;
    }

    .flex_row{
        display:flex;
        flex-direction: row;
        justify-content:center;
        align-items:center;
        margin-bottom:-12%
    }
    .next_text{
        color:#000;
        text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff;
    }

    .next_blog{
        color:#000;
        text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff;
        font-size:40px;
        text-align: center;
    }

.invert_it{
    filter: invert(1);
    width:125px;
    margin-left:-125px;
    opacity: 0;
}

.next_container:hover .invert_it{
    opacity: 1;
    margin-left:100px;
    transition: all .75s ease;
}

.next_container:hover .next_text{
    margin-left:20px;
    transition: all 1s ease;
}

.next_container:hover .next_blog{
    color:#1978ed;
    text-shadow: -1px -1px 0 #ffffff00, 1px -1px 0 #ffffff00, -1px 1px 0 #ffffff00, 1px 1px 0 #ffffff00;
    transition: all 1s ease;
}







@media only screen and (min-width: 0px) and (max-width: 576px) {

.blog_img_side{
    display:none;
}

.main_content{
    width:80%;
    margin-left:10%;
    margin-bottom:15%;
    padding-top:2.5%
}

.blog_img_top{
    height:180px
}


.next_blog{
        font-size:30px;
        width:120%
    }

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