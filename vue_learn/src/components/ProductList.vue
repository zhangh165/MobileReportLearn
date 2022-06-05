<template>
  <div>
      <h1>{{title}}</h1>
      <table>
        <tr v-for="product in products">
            <td @click="show_product(product.id)">{{product.title}}</td>
        </tr>
      </table>
  </div>
</template>

<script>
export default {
    data () {
        return {
            title: 'Product list',
            products: [
                {title: 'test'},
                {title: 'test1'}
            ]
        }
    },
    mounted(){
        this.axios.get('/api/products/').then((response)=>{
          this.products = response.data
      })
    },
    methods:{
        show_product: function(product_id){
            this.$router.push({name:'Product',query:{id:product_id}})
        }
    }
}
</script>

<style>
td {
  border-bottom: 1px solid grey;
}
</style>