<template>
  <div>
    <h2 class="text-center">Meet our team</h2>
    <div class="card-deck d-flex justify-content-center">
      <div class="card" v-for="member in teamMembers" :key="member.id">
        <img
          class="card-img-top rounded-circle"
          :src="member.img"
          alt="Card image cap"
        />
        <div class="card-body">
          <h5 class="card-title">{{ member.name }}</h5>
          <p class="card-text">{{ member.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "About",
  data() {
    return {
      teamMembers: [
        {
          id: 1,
          name: "Dorijan Kos",
          img: "../../public/Snapchat-37253659.jpg",
          description: "Front-End developer",
        },
        {
          id: 2,
          name: "Aqsa Muzaffar Ahmed",
          img: "https://via.placeholder.com/150",
          description: "Back-End developer",
        },
        {
          id: 3,
          name: "Vera Koliverda",
          img: "https://via.placeholder.com/150",
          description: "A.I. developer",
        },
      ],
    };
  },
};
</script>

<style>
.card-deck {
  width: 100%;
}
.card-img-top {
  height: 280px;
  width: 280px;
  margin-top: 100px;
}

.card-body {
    font-family: var(--fk-font-family-label)
}

.card {
  margin-top: 150px;
  margin: 80px;
  border-radius: 20px;
  box-shadow: 2px 2px 10px #c6d8ff;
  background-color: #dae6ff;
  border: 2px solid #c6d8ff;
}

h2 {
    margin-top: 40px;
    font-size: 2em;
    font-weight: bold;
    font-family: var(--fk-font-family-label)  }
</style>
