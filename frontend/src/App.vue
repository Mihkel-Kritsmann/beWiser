<template>
  <div id="app">
    <header>
      <h1>Financial Tracker</h1>
    </header>
    <main>
      <ExpenseTracker />
    </main>
    <footer>
      <p>&copy; 2025 Financial Tracker</p>
    </footer>
  </div>
</template>

<script>
import ExpenseTracker from './components/ExpenseTracker.vue';

export default {
  name: 'App',
  components: {
    ExpenseTracker
  }
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

header, footer {
  padding: 20px;
  text-align: center;
}

footer {
  margin-top: 40px;
  font-size: 14px;
  color: #666;
}
</style>