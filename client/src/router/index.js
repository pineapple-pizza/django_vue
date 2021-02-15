import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '@/components/auth/Login.vue'
import Signin from '@/components/auth/Signin.vue'
import token_validation from '@/components/auth/token_validation.vue'
import Products from '@/components/products/Products.vue'
import MyProducts from '@/components/products/MyProducts.vue'
import SearchResults from '@/components/products/SearchResults.vue'
import SingleProduct from '@/components/products/SingleProduct.vue'
import Account from '@/components/Account.vue'
import Terms from '@/components/Terms.vue'
import store from '@/store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Account
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/logout',
    name: 'logout',
  },
  {
    path: '/signin',
    name: 'signin',
    component: Signin
  },
  {
    path: '/search',
    name: 'products',
    component: Products,
    beforeEnter: (to, from, next) => {
      if(!store.getters['auth/authenticated']) {
        return next({
          name: 'signin'
        })
      }
      next()
    } 
  },
  {
    path: '/products',
    name: 'MyProducts',
    component: MyProducts,
    beforeEnter: (to, from, next) => {
      if(!store.getters['auth/authenticated']) {
        return next({
          name: 'signin'
        })
      }
      next()
    } 
  },
  {
    path: '/search/:search',
    name: 'searchResults',
    component: SearchResults,
    beforeEnter: (to, from, next) => {
      if(!store.getters['auth/authenticated']) {
        return next({
          name: 'signin'
        })
      }
      next()
    } 
  },
  {
    path: '/search/:id',
    name: 'singleProduct',
    component: SingleProduct,
    beforeEnter: (to, from, next) => {
      if(!store.getters['auth/authenticated']) {
        return next({
          name: 'signin'
        })
      }
      next()
    } 
  },
  {
    path:'/email-verify/',
    query: {token: 'token'},
    name: 'email-verify',
    component: token_validation
  },
  {
    path: '/terms',
    name: 'Terms',
    component: Terms
  }
]



const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior (to, from, savedPosition) {
    if (to.hash) {
            return { selector: to.hash }
        } else if (savedPosition) {
            return savedPosition;
        } else {
            return { x: 0, y: 0 }
        }
      }
})

export default router
