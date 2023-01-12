<template>
  <main>
    <fieldset class="element2">
      <h1 class="login">Log in</h1>
      <br />
      <br />

      <FormKit
        class="login-form"
        type="form"
        @submit="submitHandler"
      >
        <FormKit
          name="username"
          label="Username"
          validation="required"
          v-model="formData.username"
          :rules="[(val) => !!val || 'Username is required']"
        />
        <FormKit
          type="password"
          name="password"
          label="Password"
          validation="required"
          v-model="formData.password"
          :rules="[(val) => !!val || 'Password is required']"
        />
      </FormKit>
    </fieldset>
  </main>
</template>

<script>
import axios from 'axios';

export default {
  name: "Login",
  components: {},
  data() {
    return {
      formData: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    submitHandler() {
      // Send a POST request to the backend
      axios
        .post("https://8092-163-5-23-68.eu.ngrok.io/login", this.formData)
        .then((response) => {
          // Handle successful login
        })
        .catch((error) => {
          // Handle login failure
        });
    },
  },
};
</script>

<style>
.input {
  color: rgb(0, 0, 0);
  background-color: rgb(178, 238, 150);
  text-align: center;
  text-decoration: none;
  font-size: 18px;
  cursor: pointer;
  margin-bottom: 16px !important;
  padding: 9px 13px;
  vertical-align: middle;
  overflow: hidden;
  border-radius: 40px;
  margin-left: 135px;
}

fieldset {
  border-radius: 60px;
  margin-top: 700px;
  min-width: 0;
  padding-left: 100px;
  border-top: 2px;
  border-top-style: solid;
  border-bottom: 2px;
  border-bottom-style: solid;
  border-left: 2px;
  border-left-style: solid;
  border-right: 2px;
  border-right-style: solid;
}

h1 {
  font-family: var(--fk-font-family-label);
  -webkit-text-stroke: 1px rgb(178, 238, 150);
  font-style: inherit;
  font-family: var(--fk-font-family-label);
}

.element2 {
  padding-top: 45px;
  margin-right: 700px;
  margin-left: 600px;
}
</style>
