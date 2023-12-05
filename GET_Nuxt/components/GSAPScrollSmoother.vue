
        <template>
        <div id="smooth-wrapper">
        <div id="smooth-content">
        <slot></slot>
        </div>
        </div>
        </template>

        <script setup>


        import { onMounted, onUnmounted, onBeforeMount, ref } from 'vue';
        import { gsap } from 'gsap'
        import { ScrollTrigger } from 'gsap/ScrollTrigger'
        import { ScrollSmoother } from 'gsap/ScrollSmoother'
        import { SplitText } from 'gsap/SplitText'
        import { useWindowSize } from '@vueuse/core'
        import { useWindowScroll } from '@vueuse/core'
        import { useElementSize } from '@vueuse/core'
        import { page_to } from "../stores/page_to.js"

        if (process.client) {
          gsap.registerPlugin(
            ScrollTrigger,
            ScrollSmoother,
            SplitText,
            {
              useNativeDriver: true,
            }
          );
        }


        // sleep time expects milliseconds
        function sleep (time) {
          return new Promise((resolve) => setTimeout(resolve, time));
        }




        // Determine if the current browser is Safari
        function isSafari() {
        return typeof window !== 'undefined' && /^((?!chrome|android).)*safari/i.test(window.navigator.userAgent);
      }

      function isIPhone() {
        return typeof window !== 'undefined' && /(iPhone|iPod|iPad)/i.test(window.navigator.userAgent);
      }


        // Determine if the current device is a mobile
        function isMobile() {
          return typeof window !== 'undefined' && /Mobi|Android/i.test(window.navigator.userAgent);
        }

        // Use ScrollSmoother for non-Safari desktop browsers
        // const useSmoothScroll = isSafari() && isMobile();
        const useSmoothScroll = isMobile();





        const current_route = useRoute()
        console.log('this_route', current_route.name)


        const smoothy = ref()
      //  const sections = ref()
        let maxWidth = ref()
        let agile_pin = ref()
        let agile_pin_1 = ref()

        const mySplitText = ref()
        const chars = ref()
        const split_anim_1 = ref()
        const split_anim_2 = ref()

        const { width, height } = useWindowSize()
        const { x, y } = useWindowScroll()

        const sleep_for = ref(100)
        const previouslyCreatedSmoother = ref()



        const props = defineProps(['refresh_it'])
        // used for resetting investments page on/after sorting function
        watch(() => props.refresh_it, (newValue) => {
          ScrollTrigger.refresh();
          smoothy.value.refresh()
          sleep(50).then(() => { ScrollTrigger.refresh() })
            });





  const route_to = page_to()







        // Initialize the smooth scroll plugin
        onMounted(() => {

          document.addEventListener('scroll', function(e) {
            e.preventDefault();
          });



        
          
          if (String(route_to.current_page_to).includes('fund_pages')) {
            sleep_for.value = 1850
   

// Adjust ScrollSmoother parameters for Safari
if (useSmoothScroll) {
      smoothy.value = ScrollSmoother.create({
        smooth: 0, // Adjust the smoothness for Safari
        effects: false, 
        autoStart: false,
        scrollDuration: 0,
        scrollSpeed: 0,
        scrollEasing: "linear",
        smoothTouch: 0,
        normalizeScroll: true,
        normalizeScroll: {
          allowNestedScroll: true,
        },
      });
    } else {
      // Original settings for non-Safari browsers
      smoothy.value = ScrollSmoother.create({
        smooth: 2.5,
        effects: true,
        normalizeScroll: true,
        normalizeScroll: {
          allowNestedScroll: true,
        },
        smoothTouch: 0.001,
      });
    }


            smoothy.value.paused(false)
           smoothy.value.scrollTo(y.value, true)

            sleep(1500).then(() => { 
              smoothy.value.paused(false)
      
              smoothy.value.scrollTo(0, false)

              ScrollTrigger.refresh();
            })

          } 
          
          else {
            sleep_for.value = 100
          }

        



  // sleep for a few milli-seconds longer then the page transition time
  sleep(sleep_for.value).then(() => { 




ScrollTrigger.refresh();

          

// Adjust ScrollSmoother parameters for Safari
if (useSmoothScroll) {
      smoothy.value = ScrollSmoother.create({
        smooth: 0, // Adjust the smoothness for Safari
        effects: true, 
        autoStart: false,
        scrollDuration: 0,
        scrollSpeed: 0,
        scrollEasing: "linear",
        smoothTouch: .5,
        // normalizeScroll: true,
        // normalizeScroll: {
        //   allowNestedScroll: true,
        // },
      });
    } else {
      // Original settings for non-Safari browsers
      smoothy.value = ScrollSmoother.create({
        smooth: 2.5,
        effects: true,
        normalizeScroll: true,
        normalizeScroll: {
          allowNestedScroll: true,
        },
        smoothTouch: 0.001,
      });
    }


    smoothy.value.scrollTo(0, false)

    if (String(route_to.current_page_to) == '/'){
            sleep(5000).then(() => { ScrollTrigger.refresh() })
          }

    

    // ------------------------------ Footer ------------------------------
// ------------------------------ Footer ------------------------------


// if (!(current_route.name).includes('fund_pages')){


//           // Account for gsap calc after page transitions
//           if (String(route_to.current_page_to) == '/'){
//             sleep(5000).then(() => { ScrollTrigger.refresh() })
//           }

//           // if(width.value < 992){
//   ScrollTrigger.create({
//         trigger: "footer",
//         start: "bottom bottom", 
//         // end: "bottom 1000px",
//         pin: "footer",
//         pinSpacing: true,
//       });
//     // }



//     }

// ------------------------------ Home ------------------------------
// ------------------------------ Home ------------------------------



if (current_route.name == 'index'){


  ScrollTrigger.refresh()
mySplitText.value = new SplitText(".landing_title_home", { 
  type: "lines,words,chars",
  linesClass: "split-line"
});

chars.value = mySplitText.value.chars; //an array of all the divs that wrap each character

// Set up the anim
split_anim_1.value = gsap.from(chars.value, {
  scrollTrigger: {
    trigger: 'html',
    toggleActions: "restart play resume reverse",
    start: "top bottom",
  },
  duration: .5, 
  ease: "cubic-bezier(0.33, 1, 0.68, 1)", 
  y: 150, 
  delay: 1.15,
  stagger: 0.125,
});





mySplitText.value = new SplitText(".invest_text", { 
  type: "lines,words,chars",
  linesClass: "split-line"
});

chars.value = mySplitText.value.chars; //an array of all the divs that wrap each character

// Set up the anim
split_anim_2.value = gsap.from(chars.value, {
  scrollTrigger: {
    trigger: '.invest_text',
    toggleActions: "restart pause resume reverse",
    start: "center bottom",
  },
  duration: .5, 
  ease: "cubic-bezier(0.33, 1, 0.68, 1)", 
  y: 120, 
  stagger: 0.125,
});



if(width.value < 992){
            ScrollTrigger.create({
        trigger: ".pinned_text",
        start: "bottom center", 
        end: "bottom -3050px",
        pin: ".pinned_text",
      });
    }else{

                        ScrollTrigger.create({
        trigger: ".pinned_text",
        start: "center center", 
        end: "bottom -3150px",
        pin: ".pinned_text",
      });

    }


      ScrollTrigger.create({
        trigger: ".pin_scroll_video",
        start: "center center", 
        end: "bottom -2950px",
        pin: ".pin_scroll_video",
      });

      ScrollTrigger.create({
        trigger: ".video_overlay",
        start: "center center", 
        end: "bottom -3000px",
        pin: ".video_overlay",
      });



      if(width.value < 576){
      smoothy.value.effects(".white_container_home_circle", {speed: 0});
      smoothy.value.effects(".home_partner_section", {speed: 0});
      } else{
      smoothy.value.effects(".white_container_home_circle", {speed: "auto"});
      smoothy.value.effects(".home_partner_section", {speed: 1.5});
      }

    }
      
// ------------------------------ How it Works Page ------------------------------
// ------------------------------ How it Works Page ------------------------------


if (current_route.name == 'HowItWorks'){

      const sections = gsap.utils.toArray("section");


const getMaxWidth = () => {
 maxWidth.value = 0;
 sections.forEach((section) => {
   maxWidth.value += section.offsetWidth;
 });
};
getMaxWidth();
ScrollTrigger.addEventListener("refreshInit", getMaxWidth);

gsap.to(sections, {
 x: () => `-${maxWidth.value / 2 + 45}`,
 ease: "none",
 scrollTrigger: {
   trigger: ".landing_elments",
   pin: true,
   scrub: true,
   end: () => `+=${maxWidth.value}`,
   invalidateOnRefresh: true,
   markers: false
 }
});




agile_pin.value = ScrollTrigger.create({
       trigger: ".landing_big_text_container_1",
       pin: ".landing_big_text_container_1",
       start: "top center",
       end:`+=${maxWidth.value}`,
       scrub: 0.1,
     });


     agile_pin_1.value = ScrollTrigger.create({
       trigger: ".landing_big_text_container_2",
       pin: ".landing_big_text_container_2",
       start: "top center",
       end:`+=${maxWidth.value}`,
       scrub: 0.1,
     });




gsap.to(".cube_hiw", {
        scrollTrigger: {
            trigger: ".cube_hiw",
            scrub: 1,
            start: 'center center',
            endTrigger: '.cube_end_elm',
            pin: true,
        },
        rotationX: -360,
        rotationY: 360,
        rotateZ: 360,
        duration: 5,
    });




    const HIW_anchor_cookie = useCookie('HIW_anchor_cookie', {default:()=> '', watch:true, maxAge:30})



if (HIW_anchor_cookie.value != '') {
  
  sleep(1250).then(() => { 
    smoothy.value.scrollTo(HIW_anchor_cookie.value, true)
    // gsap.to(window, {duration: .45, scrollTo: {y: HIW_anchor_cookie.value, offsetY: 20} });
  
  })

}



  }
// ------------------------------ ABOUT PAGE ------------------------------ //
// ------------------------------ ABOUT PAGE ------------------------------ //


if (current_route.name == 'about'){



  if(width.value > 576){
smoothy.value.effects(".hero__image-cont", {
 speed: () => gsap.utils.random(0.55, 0.85, 0.05)
});

gsap.to(".anim-swipe", {
 yPercent: 200,
 delay: 0.2,
 duration: 3,
 stagger: {
  from: "random",
  each: 0.1
 },
 ease: "sine.out"
});

gsap.to(".hero__image-cont > img", {
 scale: 1.75,
 xPercent: 20,
 scrollTrigger: {
  trigger: ".hero",
  start: "top top",
  end: "+=3000px",
  scrub: true,
  snap: 0
 }
});

  }


        const get_height = document.getElementById("get_height");
  
gsap.to(".partners_container_line", {
        scrollTrigger: {
            trigger: ".partners_container_line",
            scrub: 1,
            start: 'top center',
      //      end: "bottom center"
  //          pin: true,
        },
         height: (get_height.clientHeight - get_height.clientHeight/9) + 'px',
    });



  }


// ------------------------------ BLOG PAGE ------------------------------ //
// ------------------------------ BLOG PAGE ------------------------------ //


if (current_route.name == 'blogs'){

ScrollTrigger.create({
        trigger: ".topic_column",
        start: "top 300px", 
        endTrigger: '.pin_end',
        pin: ".topic_column",
      });


    }
      // ------------------------------ CONTACT PAGE ------------------------------ //
      // ------------------------------ CONTACT PAGE ------------------------------ //

      if (current_route.name == 'contact'){

      ScrollTrigger.create({
        trigger: ".contact_img",
        start: "top top", 
        end: "bottom top",
        endTrigger:"html",
        pin: ".contact_img",
      });




      if(width.value < 576){

      ScrollTrigger.create({
        trigger: ".map_button",
        start: "center 71%", 
        end: "bottom top",
        endTrigger:"html",
        pin: ".map_button",
      });

      ScrollTrigger.create({
        trigger: ".top_line",
        start: "top top", 
        end: "bottom -15px",
        pin: ".top_line",
      });

    }else if(width.value < 650){
      
      ScrollTrigger.create({
        trigger: ".map_button",
        start: "center 80%", 
        end: "bottom top",
        endTrigger:"html",
        pin: ".map_button",
      });

      ScrollTrigger.create({
        trigger: ".top_line",
        start: "top top", 
        end: "bottom -15px",
        pin: ".top_line",
      });
      
    }

  else if(width.value < 768){
      
      ScrollTrigger.create({
        trigger: ".map_button",
        start: "center 90%", 
        end: "bottom top",
        endTrigger:"html",
        pin: ".map_button",
      });

      ScrollTrigger.create({
        trigger: ".top_line",
        start: "top top", 
        end: "bottom -10px",
        pin: ".top_line",
      });
      
    }

    else if(width.value < 992){
      
      ScrollTrigger.create({
        trigger: ".map_button",
        start: "center 78%", 
        end: "bottom top",
        endTrigger:"html",
        pin: ".map_button",
      });

      ScrollTrigger.create({
        trigger: ".top_line",
        start: "top top", 
        end: "bottom 8px",
        pin: ".top_line",
      });
      
    }

    else if(width.value < 1200){
      
      ScrollTrigger.create({
        trigger: ".map_button",
        start: "center 68%", 
        end: "bottom top",
        endTrigger:"html",
        pin: ".map_button",
      });

      ScrollTrigger.create({
        trigger: ".top_line",
        start: "top top", 
        end: "bottom -15px",
        pin: ".top_line",
      });
      
    }
    
    else{

      ScrollTrigger.create({
        trigger: ".map_button",
        start: "center 65%", 
        end: "bottom top",
        endTrigger:"html",
        pin: ".map_button",
      });

      ScrollTrigger.create({
        trigger: ".top_line",
        start: "top top", 
        end: "bottom -15px",
        pin: ".top_line",
      });

    }

  }


   
  if (current_route.name == 'fund_pages-next_ai' || current_route.name == 'fund_pages-fund_landing_pages-next_ai_landing'){


    const tl = gsap.timeline({
  scrollTrigger: {
    trigger: '.accordions',
    pin: true,
    start: 'top 5%',
    end: 'bottom top',
    scrub: 1,
    ease: 'linear' } });

    tl.to('.accordion .vimeo', {
  height: 0,
  width: 0,
  paddingBottom: 0,
  opacity: 0,
  scrub: .1,
  margin:0,
  ease: 'linear'
});

tl.to('.accordion .text', {
  height: 0,
  paddingBottom: 0,
  opacity: 0,
  stagger: .2 });


tl.to('.accordion', {
  marginBottom: 1,
  stagger: .1 },
'<');


  }

})
        })









onUnmounted(() => {
    // Proper clean-up to prevent memory leaks
    // smoothy.value.kill();
})

        </script>



<style scoped>
#smooth-content {
  /* will-change: transform; */
  border-top: 1px solid transparent;
   border-bottom: 1px solid transparent
}
</style>

