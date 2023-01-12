<script>
import { RouterLink, RouterView } from "vue-router";
import Login from "./components/Login.vue";
import Home from "./components/Home.vue";
import Register from "./components/Register.vue";

export default {
  name: "App",
  components: {
    Home,
    Login,
    Register,
  },
};
</script>

<template>
  <div id="app">
    <nav
      class="navbar py-4 navbar-expand-lg"
      style="background-color: rgb(178, 238, 150)"
    >
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/">
          AirBnb Calculator
        </router-link>

        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" id="border3" href="#">About us</a>
            </li>
          </ul>
        </div>
        <div
          class="collapse navbar-collapse justify-content-end"
          id="navbarCollapse"
        >
          <ul class="navbar-nav">
            <span class="border border-success" id="border1">
              <li class="nav-item">
                <router-link class="nav-link" to="/Login"> Login </router-link>
              </li>
            </span>
            <span class="border border-success" id="border2">
              <li class="nav-item">
                <router-link class="nav-link" to="/Register">
                  Register
                </router-link>
              </li>
            </span>
          </ul>
        </div>
      </div>
    </nav>
    <br />
    <br />
    <br />
    <RouterView />
  </div>

  <br />
  <br />
  <br />
  <footer>
    <div class="footer">
      <div class="col-1">
        <h4>Useful Links</h4>
        <router-link class="special" to="/"> Home </router-link>
        <a class="special" href="#">About us</a>
        <router-link class="special" to="/Login"> Login </router-link>
        <router-link class="special" to="/Register"> Register </router-link>
      </div>
      <div class="col-2">
        <h4>AirBnb</h4>
        <a class="special" href="https://www.airbnb.fr/"
          >AirBnb Official Site</a
        >
        <a class="special" href="https://www.airbnb.fr/host/homes"
          >Put up a Rental</a
        >
      </div>
      <div class="col-3">
        <h4>Location</h4>
        <p>24 Rue Pasteur, 94270 <br />Le Kremlin-Bicetre, France</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
* {
  font-family: var(--bs-body-font-family);
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.footer {
  margin-top: 150px;
  width: 100%;
  padding: 100px 15%;
  background: #333;
  color: #efefef;
  display: flex;
}

.footer div {
  text-align: center;
}
.col-2 {
  flex-grow: 2;
}

.footer div h4 {
  font-weight: 300;
  margin-bottom: 30px;
  letter-spacing: 1px;
  color: rgb(178, 238, 150);
}

.special {
  display: block;
  text-decoration: none;
  color: #efefef;
  margin-bottom: 10px;
}

.border {
    border-radius: 3px;
}

router-link {
  display: block;
  text-decoration: none;
  color: #efefef;
  margin-bottom: 10px;
}

.navbar-brand {
  font-weight: 400;
  font-size: 130%;
  padding-left: 10px;
  font-style: initial;
  margin-left: 20px;
}

#border1 {
  padding-right: 10px;
  margin-right: 20px;
  border-radius: 3px;
  padding-left: 10px;
}

#border2 {
  margin-right: 60px;
  padding-left: 10px;
  padding-right: 10px;
}

#border3 {
  margin-left: 20px;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }
}
</style>
