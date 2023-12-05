
<template>
    
    <Teleport v-if="isMounted" to="body">
  
          
      <div class="transition_overlay" ></div>
      <div class="white_circle_1" ></div>
      <div class="white_circle_2" ></div>
  
  
  </Teleport>
  
  
  </template>
  
  
  
  
  
  
  
  
  
  
  <script setup>
  
  
  
  
  // sleep time expects milliseconds
  function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
  }
  
  
  console.log('circle_transition_component - 1')
  
  const circle_white_margin_left = ref("120%")
  const circle_white_margin_top = ref("-70%")
  const circle_white_opacity = ref(0)
  const circle_black_margin_left = ref("0%")
  const circle_black_margin_top = ref("0%")
  const circle_black_opacity = ref(0)
  const overlay_opacity = ref(0)
  const white_scale = ref(1)
  const black_scale = ref(1)
  const display_it = ref("none")
  const isMounted = ref(false)


  onMounted(() => {
    isMounted.value = true
  })
  
  
  function animation_and_route(route_to){
    preloadRouteComponents(route_to)
  
      display_it.value = "block"
  
      console.log('circle_transition_component - 2')
  
      sleep(10).then(() => {
  
  circle_white_margin_left.value = "0%"
  circle_white_margin_top.value = "0%"
  circle_white_opacity.value = 1
  circle_black_margin_left.value = "80%"
  circle_black_margin_top.value = "-80%"
  circle_black_opacity.value = 1
  overlay_opacity.value = 1
  white_scale.value = 6.5
  black_scale.value = 3
  console.log('circle_transition_component - 3')
      })
  
  
    console.log('route_to ->', route_to)
  
    sleep(2000).then(() => {
      console.log('circle_transition_component - 4')
  navigateTo(route_to)
  
    })
  
    sleep(2100).then(() => {
      display_it.value = "none"
      circle_white_margin_left.value = "120%"
      circle_white_margin_top.value = "-70%"
      circle_white_opacity.value = 0
      circle_black_margin_left.value = "0%"
      circle_black_margin_top.value = "0%"
      circle_black_opacity.value = 0
      overlay_opacity.value = 0
      white_scale.value = 1
      black_scale.value = 1
    })
  
  
  }
  
  
  defineExpose({
      animation_and_route
  })
  
  </script>
  
  
  
  
  
  <style scoped>
  
  
  
  
  
  .transition_overlay{
      width:100vw;
      height:200vh;
      background-color:rgba(114, 114, 114, 0.4);
      z-index:2300;
      position:fixed;
      bottom:0;
      left:0;
      transition: all 1.5s ease-in-out;
      opacity: v-bind(overlay_opacity);
      display: v-bind(display_it);
  }
  
  
  
  
  
  .white_circle_1{
    width:50vw;
    height:50vw;
    border-radius:100%;
    background-color:#fff;
    z-index:2500;
    margin-left:v-bind(circle_white_margin_left);
    /* left:150%;
    top:0%; */
    margin-top:v-bind(circle_white_margin_top);
    opacity:v-bind(circle_white_opacity);
    position:fixed;
    transform: scale(v-bind(white_scale));
    transition: margin-top 3.5s ease-in-out, margin-left 3.5s ease-in-out, transform 2.5s ease-in;
    display: v-bind(display_it);
    mix-blend-mode: normal;
  }
  
  
  .white_circle_2{
    width:100vw;
    height:100vw;
    border-radius:100%;
    background-color:#000;
    z-index:2400;
    margin-left:v-bind(circle_black_margin_left);
    left:-100%;
    top:100%;
    margin-top:v-bind(circle_black_margin_top);
    opacity:v-bind(circle_black_opacity);
    position:fixed;
    transform: scale(v-bind(black_scale));
    transition: margin-top 2s ease-in-out, margin-left 2s ease-in, transform 2.5s ease-in;
    display: v-bind(display_it);
    mix-blend-mode: normal;
  }
  
  </style>






