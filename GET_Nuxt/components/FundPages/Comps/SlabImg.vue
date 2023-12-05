<template>
    

<div class="slab_container">
<img data-speed="auto" class="slab_img" :src="image">
</div>


</template>


<script setup>


const props = defineProps(['margin_top', 'margin_bottom', 'image'])

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
.slab_img{
  position: absolute;
  width: 100vw;
  bottom:0;
  object-fit: cover;
  object-position: center;
}



@media only screen and (min-width: 0px) and (max-width: 376px) {


.slab_img{
  position: absolute;
  width: 200vw;
  bottom:0;
  object-fit: cover;
  object-position: center;
  margin-left:-50%
}

.slab_container{

 margin-top:calc(v-bind('margin_top'));
 margin-bottom:calc(v-bind('margin_bottom'));
}


}




@media only screen and (min-width: 376px) and (max-width: 430px) {


.slab_img{
  position: absolute;
  width: 200vw;
  bottom:0;
  object-fit: cover;
  object-position: center;
  margin-left:-50%
}

.slab_container{

 margin-top:calc(v-bind('margin_top') * -2);
 margin-bottom:calc(v-bind('margin_bottom') * -2);
}


}



@media only screen and (min-width: 430px) and (max-width: 576px) {


.slab_img{
  position: absolute;
  width: 200vw;
  bottom:0;
  object-fit: cover;
  object-position: center;
  margin-left:-50%
}



}

@media only screen and (min-width: 576px) and (max-width: 768px) {


.slab_img{
  position: absolute;
  width: 150vw;
  bottom:0;
  object-fit: cover;
  object-position: center;
  margin-left:-25%
}

}

@media only screen and (min-width: 768px) and (max-width: 992px) {

  .slab_img{
  position: absolute;
  width: 120vw;
  bottom:0;
  object-fit: cover;
  object-position: center;
  margin-left:-10%
}


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