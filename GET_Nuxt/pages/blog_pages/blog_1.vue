<template>
    
    <CircleTransition ref="cicle_tansition"/>
    <Header/>
    
        <GSAPScrollSmoother>

            <img src="~/assets/content/blogs/blog_pages/blog_1/blog_top.jpg"  class="blog_img_top">

            <img data-speed="1.5" src="~/assets/content/blogs/blog_pages/blog_1/blog_side.jpg"  class="blog_img_side">
    
    <h6 class="blog_title">5 Reasons Why Digital Payments Are the Future of Commerce</h6>

    <p class="blog_date">Posted on 04/01/2023</p>

            <div class="main_content">
            <p>The world of payments is changing, and it's not just because of the advent of contactless cards and digital wallets. When you consider all the benefits that merchants get from taking electronic payments, it's clear that this trend isn't going away anytime soon. Here are five reasons why digital payments are about to transform commerce as we know it.</p>

            <p class="subtitle">Digital payments create a better customer experience.</p>

            <p>Digital payments are the future of commerce. Why? Because digital payments create a better customer experience for everyone involved in the transaction.
            <ul>
                <li>Customers can pay with a click of a button, from anywhere, on any device--and they don't have to worry about cash or credit cards. They also won't have to worry about fraud since everything happens directly between you and your customers' bank accounts (or PayPal accounts).</li>
            </ul>
        </p>

        <p class="subtitle">Digital payments are simple and easy to use.</p>

        <p>Digital payments are simple and easy to use.
            <ul>
                <li>Digital payments are quick and easy to set up, making them perfect for businesses that want to get started with digital payments quickly and easily.</li>
                <br>
                <li>You can integrate them into your existing business in just a few minutes, so there's no need for a big overhaul of the way you work or spend time on admin tasks like invoicing, billing and reconciling accounts.</li>
                <br>
                <li>Because they're simple, digital payment methods are also straightforward for customers - which means fewer problems when it comes time to settle up at the end of every month!</li>

            </ul>
        </p>

        <p class="subtitle">Digital payments are a great way to engage millennials.</p>

        <p>Millennials are the largest generation in the US and they're interested in technology, convenience and security. Digital payments provide all three of these things.
            <br><br>
            Millennials are more likely to use digital payments than older generations because they can do so from their phones or computers with just a few taps on the screen. Millennials also value the security and safety that comes with digital payments; many have grown up with credit cards as an integral part of their daily lives and know that Amazon Pay will protect them against fraud or theft if something goes wrong while shopping online.
        </p>


        <p class="subtitle">Digital payments are incredibly convenient and secure.</p>

        <p>As you can see, digital payments are incredibly convenient and secure. They're easy to use, fast and affordable. What more could you ask for in a payment method?</p>

        <p class="subtitle">Digital payments help merchants reduce costs.</p>

        <p>Digital payments offer a number of benefits to merchants. 
            <br><br>
            <ul>
                <li>They're cheaper than traditional payment methods. Merchants pay lower fees to process digital transactions, which can help offset the costs of technology investments and support services. In addition, there are no chargebacks or refunds in the case of fraud--a significant cost savings for businesses that accept credit cards but face high chargeback rates due to fraudsters attempting to commit theft or fraud with stolen cards.</li>
                <br>
                <li>They're safer than traditional payment methods too! While cash is still king when it comes to security (it's hard for criminals to steal something you don't have), digital payments provide an added layer of protection against theft by being less tangible than cash and checks: if someone steals your phone or laptop with all your personal information stored on it, they won't be able to access those funds without authorization from you first (more on this later).
                </li>
            </ul>
        </p>

        <p class="subtitle">Conclusion</p>

        <p>Digital payments are the future of commerce. They're convenient, easy to use and secure. And they can help you engage your customers on a deeper level than ever before. Digital payments can also reduce costs for merchants by eliminating cash handling fees or credit card processing costs.</p>

        </div>


        <div @click="transition_and_route('blog_2')" class="next_container">
        <div class="flex_row">
            <img class="invert_it" src="~/assets/content/homepage/arrow_medium_light.png">
        <h2 class="next_text">NEXT</h2>
    </div>

            <p class="next_blog">Why Private Equity, Why Now?</p>

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
    height:400px
}

.blog_img_side{
    width:200px;
    height:100vh;
    float:right;
    margin-top:30%;
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