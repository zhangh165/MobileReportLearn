<template>
<div>
<p> {{product.title}}</p>
<p>{{product.price}}</p>
<div>{{product.content}}</div>
</div>
</template>

<script>
export default {
  name:'Prdouct Detail',
  data(){
   return {
       product:{
           title: 'default Title',
           content : 'default Content',
           price : 99.99
       }
   }
  },
  mounted(){
      this.axios.get('/api/products/'+this.$route.query.id).then((response)=>{
          this.product = response.data
      },(response)=>{
          console.error(response)
      })
  }
}
</script>

<style scoped>

</style>
