<template>
    <div class="movies">
      <h2>All Movies</h2>
      <div v-for="movie in movies" :key="movie.id" class="card">
        <img :src="movie.poster" alt="Poster" />
        <h3>{{ movie.title }}</h3>
        <p>{{ movie.description }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue"
  
  const movies = ref([])
  
  function fetchMovies() {
    fetch("/api/v1/movies")
      .then((res) => res.json())
      .then((data) => {
        movies.value = data.movies
      })
  }
  
  onMounted(() => {
    fetchMovies()
  })
  </script>
  