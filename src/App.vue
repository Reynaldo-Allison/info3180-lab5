<script setup>
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
</script>

<template>
  <AppHeader />

  <main id="app">
    <router-view />
  </main>

  <AppFooter />
</template>

<style>
body {
  padding-top: 75px;
}
</style>
