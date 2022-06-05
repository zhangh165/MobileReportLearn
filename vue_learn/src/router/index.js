import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import SayHi from '@/components/SayHi'
import ProductsList from '@/components/ProductList'
import Product from '@/components/Product'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/say_hi',
      name: 'SayHi',
      component: SayHi
    },
    {
      path: '/products',
      name: 'Product List',
      component: ProductsList
    },
    {
      path: '/products',
      name: 'Product',
      component : Product
    }
  ]
})
