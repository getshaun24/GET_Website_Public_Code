<template>

         <client-only>  <ve-progress :progress="progress" :legend="progress" /></client-only>


         <p class="refresh_text">Please do not refresh</p>
   
   </template>
   
   <script setup>

const props = defineProps(['start_loader', 'number_of_transfers']) 


   const maxLegendValue = ref(100);
     const legend = ref(0);
const progress = ref(0)
const interval_time = ref(((props.number_of_transfers ** 2) / 40) + 225)




if (props.start_loader) {
     setInterval(() => {
  legend.value += 1;
  progress.value = (legend.value * 100) / maxLegendValue.value;
}, interval_time.value)
} else{
     legend.value = 0;
     progress.value = 0;
}





   </script>


<style scoped>

.refresh_text{
   color:rgb(25, 120, 237);
   position:absolute;
   margin-top:50vh;
   font-weight: bold;
}


</style>