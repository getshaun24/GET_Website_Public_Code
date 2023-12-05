<template>
    
    <CircleTransition ref="cicle_tansition"/>
    <Header/>
    
        <GSAPScrollSmoother>

            <img src="~/assets/content/blogs/blog_pages/blog_2/blog_top.jpg"  class="blog_img_top">

            <img data-speed="1.5" src="~/assets/content/blogs/blog_pages/blog_2/blog_side.jpg"  class="blog_img_side">
    
    <h6 class="blog_title">Why Private Equity, Why Now?</h6>

    <p class="blog_date">Posted on 04/06/2023</p>

            <div class="main_content">
            <p><i>With the economy going sideways, Private Equity investment offers many benefits to sophisticated investors.

            </i></p>

            <p>Private equity has become an increasingly popular investment option in today's volatile public markets. Private equity firms raise capital from institutional investors, such as pension funds, insurance companies, and high net worth individuals, to invest in private companies or acquire public companies that they take private. These investments are typically held for several years before being sold or taken public again.</p>

            <p>Private equity can provide several benefits in today's volatile public markets, including:
            </p>

            <p><span class="subtitle">Greater Flexibility:</span> Private equity investors have more control over their investments and can make decisions without the constraints of public markets. This flexibility allows private equity firms to take a longer-term view and invest in companies that may not meet the short-term demands of public markets.
            </p>

            <p><span class="subtitle">Access to Unlisted Companies:</span> Private equity provides investors with access to a broader range of investment opportunities, including unlisted companies. Many of these companies are in high-growth industries and are not yet ready to go public, making private equity a great way to invest in these opportunities.
            </p>

            <p><span class="subtitle">Active Management:</span> Private equity investors take an active role in the management of their investments, working closely with company management teams to improve operational efficiencies and drive growth. This active management approach can result in better returns than passive investments in public markets.
            </p>

            <p><span class="subtitle">Diversification:</span> Private equity investments can provide diversification benefits for investors. Private equity funds invest in a wide range of industries and geographies, helping to reduce risk and provide exposure to different economic cycles.
            </p>

            <p><span class="subtitle">Higher Returns:</span>Private equity investors have more control over their investments and can make decisions without the constraints of public markets. This flexibility allows private equity firms to take a longer-term view and invest in companies that may not meet the short-term demands of public markets.
            </p>


            <p><span class="subtitle">Greater Flexibility:</span> Private equity investments have historically generated higher returns than public market investments. This is due in part to the active management approach of private equity firms, as well as the longer holding periods and the ability to invest in high-growth companies.
            </p>


            <p>However, it is important to note that private equity investments are generally illiquid and require a long-term investment horizon. Additionally, private equity investments may involve higher fees and expenses compared to traditional public market investments.
            </p>


            <p>In conclusion, private equity can provide several benefits in today's volatile public markets, including greater flexibility, access to unlisted companies, active management, diversification, and higher returns. While private equity investments may not be suitable for all investors, those with a longer-term investment horizon and a tolerance for illiquidity may find private equity to be a valuable addition to their investment portfolios.
            </p>
    
        </div>


        <div @click="transition_and_route('blog_3')" class="next_container">
        <div class="flex_row">
            <img class="invert_it" src="~/assets/content/homepage/arrow_medium_light.png">
        <h2 class="next_text">NEXT</h2>
    </div>

            <p class="next_blog">An Investment in Energy is a Growth Investment</p>

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