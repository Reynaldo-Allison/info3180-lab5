<template>
    <div>
      <h2>Add a New Movie</h2>
      <div v-if="successMessage" class="alert alert-success">{{ successMessage }}</div>
      <div v-if="errors.length" class="alert alert-danger">
        <ul>
          <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
        </ul>
      </div>
  
      <form id="movieForm" @submit.prevent="saveMovie">
        <div>
          <label>Title</label>
          <input type="text" name="title" class="form-control" />
        </div>
  
        <div>
          <label>Description</label>
          <textarea name="description" class="form-control"></textarea>
        </div>
  
        <div>
          <label>Poster</label>
          <input type="file" name="poster" class="form-control" />
        </div>
  
        <button type="submit">Submit</button>
      </form>

    </div>
  </template>

  <script setup>
  import { ref, onMounted } from "vue"
  
  const csrf_token = ref("")
  const errors = ref([])
  const successMessage = ref("")
  
  function getCsrfToken() {
    fetch("/api/v1/csrf-token")
      .then((res) => res.json())
      .then((data) => {
        csrf_token.value = data.csrf_token
      })
  }
  
  function saveMovie() {
    let form = document.getElementById("movieForm")
    let formData = new FormData(form)
  
    fetch("/api/v1/movies", {
      method: "POST",
      body: formData,
      headers: {
        "X-CSRFToken": csrf_token.value,
      },
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.errors) {
          errors.value = Object.values(data.errors).flat()
          successMessage.value = ""
        } else {
          errors.value = []
          successMessage.value = data.message
        }
      })
      .catch((err) => {
        console.log(err)
      })
  }
  
  onMounted(() => {
    getCsrfToken()
  })
  </script>
  