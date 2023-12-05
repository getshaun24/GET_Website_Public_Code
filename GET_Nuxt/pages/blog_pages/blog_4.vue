<template>
    
    <CircleTransition ref="cicle_tansition"/>
    <Header/>
    
        <GSAPScrollSmoother>

            <img src="~/assets/content/blogs/blog_pages/blog_4/blog_top.jpg"  class="blog_img_top">

            <img data-speed="1.5" src="~/assets/content/blogs/blog_pages/blog_4/blog_side.jpg"  class="blog_img_side">
    
    <h6 class="blog_title">The Importance of SMBs in the Economy</h6>

    <p class="blog_date">Posted on 04/08/2023</p>

            <div class="main_content">


            <p>Small and medium businesses (SMBs) are the backbone of the American and global economy. They play a critical role in creating jobs, driving innovation, and contributing to economic growth. Despite their importance, SMBs often face challenges that can limit their growth and success. In this blog post, we will discuss why SMBs are the real growth engine of the American and global economy.
            </p>

            <p>Firstly, SMBs are major job creators. According to the Small Business Administration (SBA), small businesses account for 44% of total US economic activity and create two-thirds of net new jobs. In addition, SMBs are responsible for creating 75% of all private-sector jobs in the US. This demonstrates the significant impact that SMBs have on the American job market.
            </p>

            <p>Secondly, SMBs are driving innovation. SMBs are often more agile and adaptable than larger corporations, making them better able to respond to changing market conditions and consumer needs. They are also more likely to pursue new and innovative ideas, which can lead to breakthrough products and services. In fact, a study by the Kauffman Foundation found that SMBs are responsible for more than half of all new innovations in the US.
            </p>

            <p>
                Thirdly, SMBs are major contributors to economic growth. According to a report by the World Bank, SMBs account for more than 90% of all businesses worldwide and contribute up to 50% of GDP. They also play a critical role in developing countries, where they provide a pathway to economic empowerment and poverty reduction.
            </p>


            <p>
                Despite their importance, SMBs often face challenges that can limit their growth and success. These challenges include limited access to financing, regulatory burdens, and competition from larger corporations. However, there are many initiatives aimed at supporting SMBs, such as government programs and private sector initiatives. For example, the SBA provides loans and technical assistance to small businesses, while many corporations offer mentorship and incubation programs to support SMBs.
            </p>

            <p>
                In conclusion, SMBs are the real growth engine of the American and global economy. They create jobs, drive innovation, and contribute to economic growth. While SMBs face challenges that can limit their success, there are many initiatives aimed at supporting them. As the world continues to face economic challenges, it is critical that we continue to support SMBs and recognize their importance as a key driver of economic growth.
            </p>
    
        </div>


        <div @click="transition_and_route('blog_1')" class="next_container">
        <div class="flex_row">
            <img class="invert_it" src="~/assets/content/homepage/arrow_medium_light.png">
        <h2 class="next_text">NEXT</h2>
    </div>

            <p class="next_blog">5 Reasons Why Digital Payments Are the Future of Commerce</p>

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