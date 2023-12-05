<template>
    <div>
    <div class="spacer_1"></div>
    <div class="accordions">
      <div class="accordion">
        <div class="title">
          Manager Video
        </div>
        <iframe data-speed="1.05" src="https://player.vimeo.com/video/845070355" class="vimeo" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

        <div class="text">
            The approach is proven, simple, and effective: using our collective capital contributions, we bid on stock through GET Equity Partners connections and relationships, waiting for the right timing and valuation to maximize each invested dollar.
            <br><br>
                A selection of the companies in the space that we are considering are (but not limited to):
        </div>
      </div>
      <div class="accordion">
        <div class="title">Open AI</div>
        <div class="text">
            OpenAI is a leading artificial intelligence research lab consisting of both for-profit and non-profit arms. It focuses on ensuring artificial general intelligence (AGI) benefits all of humanity by building safe and beneficial AGI directly, while also striving to aid others in achieving these outcomes. OpenAI's advanced AI models, like ChatGPT, transform the way we interact with technology, offering applications from writing assistance to education, gaming, and beyond.
        </div>
      </div>
      <div class="accordion">
        <div class="title"> MidJourney </div>
        <div class="text">
          Midjourney, a San Francisco-based AI company, has created a unique generative AI program that transforms text prompts into images, akin to OpenAI's DALL-E. Under the leadership of David Holz, co-founder of Leap Motion, the company entered open beta in July 2022 and has been profitably operating while continuously enhancing its algorithms. The platform is currently accessible via a Discord bot, with plans for a web interface in progress. Artists use Midjourney for rapid prototyping of concepts, and industries like advertising leverage it for efficient content creation. 
        </div>
      </div>
      <div class="accordion">
        <div class="title">Anthropic</div>
        <div class="text">Anthropic is an AI startup, founded by former OpenAI researchers, specializing in developing general AI systems and language models like its chatbot, Claude. It's currently working on a "frontier model", a next-gen algorithm for AI self-teaching, with plans to invest billions in the development of this technology, which is anticipated to automate large portions of the economy. With high-profile investors such as Google, Anthropic is positioning itself as a major player in the AI field, ready to compete with established organizations like OpenAI
</div>
      </div>
      <div class="accordion">
        <div class="title">Runway ML</div>
        <div class="text">Runway ML is a pioneering company in the realm of artificial intelligence, Runway ML is enhancing the field with its user-friendly and innovative approaches. Founded by the visionary Cristóbal Valenzuela, Runway ML has made a name for itself by developing a platform that empowers creators by providing them with easy access to machine learning models. The company's software is designed to be user-friendly, with a focus on delivering complex AI technologies in a way that is accessible to a wide audience, enabling them to interact and create with AI without needing a background in coding. One of their notable offerings is their 5.1 model which has shown proficiency in working better with more literal prompts.</div>
      </div>

      <div class="accordion">
        <div class="title">Nano-C</div>
        <div class="text">Nano-C is a pioneering company in nanocarbon engineering, directly impacting the field of computing in general and AI specifically. Their high-quality fullerenes and carbon nanotubes enable the creation of smaller, faster, and more energy-efficient semi-conductors, step-wise elevating current computational capabilities. Further, Nano-C's breakthroughs in solar cell efficiency and battery storage also contribute to sustainable energy solutions, aligning with the demand for environmentally friendly technologies in AI and computing.</div>
      </div>
    </div>
    <div class="spacer_2"></div>
</div>
</template>




<script setup>


import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);


        // sleep time expects milliseconds
        function sleep (time) {
          return new Promise((resolve) => setTimeout(resolve, time));
        }



        onMounted(async () => {
          await nextTick();
          sleep(1000).then(() => {

            // run_gasp()

          })
        })

// function run_gasp(){
// const tl = gsap.timeline({
//   scrollTrigger: {
//     trigger: '.accordions',
//     pin: true,
//     start: 'top 5%',
//     end: 'bottom top',
//     scrub: 1,
//     ease: 'linear' } });

//     tl.to('.accordion .vimeo', {
//   height: 0,
//   width: 0,
//   paddingBottom: 0,
//   opacity: 0,
//   scrub: .1,
//   margin:0,
//   ease: 'linear'
// });

// tl.to('.accordion .text', {
//   height: 0,
//   paddingBottom: 0,
//   opacity: 0,
//   stagger: .2 });


// tl.to('.accordion', {
//   marginBottom: 1,
//   stagger: .1 },
// '<');

// }
            







</script>


<style scoped>


.accordions {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom:-70%
}

.accordion {
  width: 60%;
  padding: 14px 30px 0px;
  border-radius: 15px;
  margin-bottom: 40px;
  box-shadow: 0 30px 30px -10px rgba(0, 0, 0, 0.5);
}

.accordion:nth-child(1) {
    background: linear-gradient(200deg, #05335d 13.57%, #000000 98.38%);
    border: 1px solid #3b3b3b6f;
}

.accordion:nth-child(2) {
  background: linear-gradient(200deg, #1d91fc 13.57%, #5a36c0 98.38%);
}
.accordion:nth-child(3) {
  background: linear-gradient(200deg, #65bb76 13.57%, #466fab 98.38%);
}
.accordion:nth-child(4) {
  background: linear-gradient(200deg, #c215d1 13.57%, #3b003f 98.38%);
}

.accordion:nth-child(5) {
  background: linear-gradient(200deg, #09822d  13.57%, #023316 98.38%);
}

.accordion:nth-child(6) {
  background: linear-gradient(200deg, #85a6f2 13.57%, #8d0694 98.38%);
}

.accordion:nth-child(2):hover {
  cursor: url('~/assets/content/fund_pages/next_ai/next_logos/next_logo_2_1.png'), auto;
}

.accordion:nth-child(3):hover {
  cursor: url('~/assets/content/fund_pages/next_ai/next_logos/next_logo_1_1.png'), auto;
}

.accordion:nth-child(4):hover {
  cursor: url('~/assets/content/fund_pages/next_ai/next_logos/next_logo_3_1.png'), auto;
}

.accordion:nth-child(5):hover {
  cursor: url('~/assets/content/fund_pages/next_ai/next_logos/next_logo_4_1.png'), auto;
}

.accordion:nth-child(6):hover {
  cursor: url('~/assets/content/fund_pages/next_ai/next_logos/next_logo_6.png'), auto;
}
.title {
  font-size: max(2vw, 24px);
  line-height: 1.1;
  padding-bottom: 0.4em;
  color: white;
  text-shadow: 0 2px 2px rgba(0, 0, 0, 0.1);
}

.text {
  font-size: max(1vw, 15px);
  line-height: 1.4;
  overflow: hidden;
  padding-bottom: 30px;
  padding-top:10px;
  color: rgba(255, 255, 255, 0.75);
}

.spacer_1 {
  height: 20vh;
}

.spacer_2 {
  height: 0vh;
}


@media (max-width: 480px) {
  .accordion {
    padding: 15px 20px 8px;
  }

  .title {
    font-size: 20px;
  }
}



.vimeo{
    width:100% !important;
    height:400px ;
    z-index:3;
    margin:5% 0%;
    border-radius: 20px !important;
    transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}



@media only screen and (min-width: 0px) and (max-width: 576px) {
.spacer_1 {
  height: 0vh;
}
}


@media only screen and (min-width: 0px) and (max-width: 400px) {

.accordions {
  margin-bottom:-735%
}
}

@media only screen and (min-width: 400px) and (max-width: 425px) {

.accordions {
  margin-bottom:-650%
}
}


@media only screen and (min-width: 425px) and (max-width: 475px) {

.accordions {
  margin-bottom:-565%
}
}

@media only screen and (min-width: 475px) and (max-width: 525px) {

.accordions {
  margin-bottom:-475%
}
}

@media only screen and (min-width: 525px) and (max-width: 550px) {

.accordions {
  margin-bottom:-420%
}
}

@media only screen and (min-width: 550px) and (max-width: 576px) {

.accordions {
  margin-bottom:-380%
}
}

@media only screen and (min-width: 576px) and (max-width: 625px) {
.accordions {
  margin-bottom:-360%
}
}

@media only screen and (min-width: 625px) and (max-width: 685px) {
.accordions {
  margin-bottom:-320%
}
}

@media only screen and (min-width: 685px) and (max-width: 768px) {
.accordions {
  margin-bottom:-250%
}
}

@media only screen and (min-width: 768px) and (max-width: 992px) {
    .vimeo{
    height:300px ;
}

}

@media only screen and (min-width: 768px) and (max-width: 850px) {
.accordions {
  margin-bottom:-200%
}
}

@media only screen and (min-width: 850px) and (max-width: 940px) {
.accordions {
  margin-bottom:-170%
}
}

@media only screen and (min-width: 940px) and (max-width: 992px) {
.accordions {
  margin-bottom:-155%
}
}

@media only screen and (min-width: 992px) and (max-width: 1200px) {
    .vimeo{
    height:350px ;
}
}


@media only screen and (min-width: 992px) and (max-width: 1100px) {

.accordions {
  margin-bottom:-145%
}
}

@media only screen and (min-width: 1100px) and (max-width: 1200px) {

.accordions {
  margin-bottom:-115%
}
}

@media only screen and (min-width: 1200px) and (max-width: 1400px) {
    .vimeo{
    height:400px ;
}
.accordions {
  margin-bottom:-95%
}
}

@media only screen and (min-width: 1400px) and (max-width: 1600px) {
  .accordions {
  margin-bottom:-70%
}
}

@media only screen and (min-width: 1600px) and (max-width: 5600px) {
  .accordions {
  margin-bottom:-70%
}
}

</style>
