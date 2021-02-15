<template>
  <div class="home">
    <products></products>
    <about></about>
    <contact></contact>
  </div>
</template>

<script>
import Products from '@/components/products/Products.vue'
import About from '@/components/About.vue'
import Contact from '@/components/Contact.vue'

export default {
  name: 'Home',
  components: {
    "products": Products,
    "about": About,
    "contact": Contact
  },
  created() {
    // const res = await axios.get()
  }
}
</script>