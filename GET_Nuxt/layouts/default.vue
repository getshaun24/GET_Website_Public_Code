<template>

<div>
      <slot></slot>
    </div>

  </template>

<script setup>
await preloadComponents(['Header', 'GSAPScrollSmoother'])

useHead(() => ({
  script: [
    {
      src: 'https://www.googletagmanager.com/gtag/js?id=G-1HTW2DMCZQ',
      async: true,
    },
    {
      innerHTML: `
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-1HTW2DMCZQ');
      `,
    },
  ]
}))




</script>


  
  <style>













.page-scale-enter-to{
  z-index:-100000!important;
}


.page-scale-leave-from,
  .page-scale-leave-active,
  .page-scale-leave-to
     {

    transition: clip-path 1.5s ease, opacity .5s ease 1s;
    will-change: clip-path, opacity;
  }

  .page-scale-leave-from{
    z-index:2000!important
  }
  
  .page-scale-leave-active {
    clip-path: circle(100vw at center);
    z-index:2000!important;
    position:fixed;
    top:50vh;
    left:50vw;
  }

  .page-scale-leave-to {
    clip-path: circle(10px at 50% 25%);
    /* clip-path: circle(10px at center); */
    z-index:2000!important;
    overflow:hidden;
    opacity:0;

    
  } 


  </style>