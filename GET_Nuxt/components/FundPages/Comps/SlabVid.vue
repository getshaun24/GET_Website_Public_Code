<template>
    


    <div class="slab_container">
        <video data-speed="auto" class="slab_vid"  autoplay muted playsinline loop>
                <source :src="video" type="video/mp4">
</video>


    </div>
    
    
    </template>
    
    
    <script setup>
    
    
    const props = defineProps(['margin_top', 'margin_bottom', 'video'])
    
    </script>
    
    
    <style scoped>
    
    
    .slab_container{
      position: relative;
     height: 70vh;
     width: 100%;
     overflow: hidden;
     object-fit: cover;
     margin-top:v-bind('margin_top');
     margin-bottom:v-bind('margin_bottom');
    }
    .slab_vid{
      position: absolute;
      width: 100vw;
      bottom:0;
      object-fit: cover;
      object-position: center;
      z-index:100
    }
    
    

@media only screen and (min-width: 0px) and (max-width: 430px) {
  .slab_container{
      position: relative;
     height: 70vh;
     width: 100%;
     overflow: hidden;
     object-fit: cover;
     margin-top:-30%;
     margin-bottom:-10%;
    }
}


@media only screen and (min-width: 430px) and (max-width: 576px) {
  .slab_container{
      position: relative;
     height: 70vh;
     width: 100%;
     overflow: hidden;
     object-fit: cover;
     margin-top:0%;
     margin-bottom:-10%;
    }
}



    /* 
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
 */


    
    </style>