<template>
  <div class="expense-tracker">
    <h1>Expense Tracker</h1>
    
    <!-- Tabs for switching between expenses, income, and categories -->
    <div class="tabs">
      <button 
        :class="{ 'active': activeTab === 'expenses' }" 
        @click="activeTab = 'expenses'"
      >
        Expenses
      </button>
      <button 
        :class="{ 'active': activeTab === 'income' }" 
        @click="activeTab = 'income'"
      >
        Income
      </button>
      <button 
        :class="{ 'active': activeTab === 'categories' }" 
        @click="activeTab = 'categories'"
      >
        Categories
      </button>
    </div>
    
    <!-- Expenses Tab -->
    <div v-if="activeTab === 'expenses'">
      <h2>Expenses</h2>
      
      <!-- Add Expense Form -->
      <form @submit.prevent="addExpense" class="form">
        <input v-model="newExpense.amount" type="number" step="0.01" placeholder="Amount" required />
        <input v-model="newExpense.description" type="text" placeholder="Description" />
        <select v-model="newExpense.category" required>
          <option value="" disabled>Select Category</option>
          <option v-for="category in categories" :key="category.id" :value="category.id">
            {{ category.name }}
          </option>
        </select>
        <input v-model="newExpense.recipient" type="text" placeholder="Recipient" required />
        <button type="submit">Add Expense</button>
      </form>
      
      <!-- Expenses List -->
      <div v-if="expenses.length === 0" class="empty-state">No expenses recorded yet.</div>
      <table v-else class="data-table">
        <thead>
          <tr>
            <th>Amount</th>
            <th>Date</th>
            <th>Description</th>
            <th>Category</th>
            <th>Recipient</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="expense in expenses" :key="expense.id">
            <td>${{ expense.amount }}</td>
            <td>{{ formatDate(expense.date) }}</td>
            <td>{{ expense.description }}</td>
            <td>{{ getCategoryName(expense.category) }}</td>
            <td>{{ expense.recipient }}</td>
            <td>
              <button @click="deleteExpense(expense.id)" class="btn-delete">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    
    <!-- Income Tab (similar structure to Expenses) -->
    <div v-if="activeTab === 'income'">
      <h2>Income</h2>
      
      <!-- Add Income Form -->
      <form @submit.prevent="addIncome" class="form">
        <input v-model="newIncome.amount" type="number" step="0.01" placeholder="Amount" required />
        <input v-model="newIncome.description" type="text" placeholder="Description" />
        <select v-model="newIncome.category" required>
          <option value="" disabled>Select Category</option>
          <option v-for="category in categories" :key="category.id" :value="category.id">
            {{ category.name }}
          </option>
        </select>
        <input v-model="newIncome.source" type="text" placeholder="Source" required />
        <button type="submit">Add Income</button>
      </form>
      
      <!-- Income List -->
      <div v-if="incomes.length === 0" class="empty-state">No income recorded yet.</div>
      <table v-else class="data-table">
        <thead>
          <tr>
            <th>Amount</th>
            <th>Date</th>
            <th>Description</th>
            <th>Category</th>
            <th>Source</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="income in incomes" :key="income.id">
            <td>${{ income.amount }}</td>
            <td>{{ formatDate(income.date) }}</td>
            <td>{{ income.description }}</td>
            <td>{{ getCategoryName(income.category) }}</td>
            <td>{{ income.source }}</td>
            <td>
              <button @click="deleteIncome(income.id)" class="btn-delete">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    
    <!-- Categories Tab -->
    <div v-if="activeTab === 'categories'">
      <h2>Categories</h2>
      
      <!-- Add Category Form -->
      <form @submit.prevent="addCategory" class="form">
        <input v-model="newCategory.name" type="text" placeholder="Category Name" required />
        <input v-model="newCategory.description" type="text" placeholder="Description" />
        <button type="submit">Add Category</button>
      </form>
      
      <!-- Categories List -->
      <div v-if="categories.length === 0" class="empty-state">No categories created yet.</div>
      <table v-else class="data-table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="category in categories" :key="category.id">
            <td>{{ category.name }}</td>
            <td>{{ category.description }}</td>
            <td>
              <button @click="deleteCategory(category.id)" class="btn-delete">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ExpenseTracker',
  data() {
    return {
      activeTab: 'expenses',
      expenses: [],
      incomes: [],
      categories: [],
      newExpense: {
        amount: '',
        description: '',
        category: '',
        recipient: ''
      },
      newIncome: {
        amount: '',
        description: '',
        category: '',
        source: ''
      },
      newCategory: {
        name: '',
        description: ''
      }
    };
  },
  created() {
    this.fetchExpenses();
    this.fetchIncomes();
    this.fetchCategories();
  },
  methods: {
    // Fetch data from API
    async fetchExpenses() {
      try {
        const response = await axios.get('/api/expenses/');
        this.expenses = response.data;
      } catch (error) {
        console.error('Error fetching expenses:', error);
      }
    },
    async fetchIncomes() {
      try {
        const response = await axios.get('/api/incomes/');
        this.incomes = response.data;
      } catch (error) {
        console.error('Error fetching incomes:', error);
      }
    },
    async fetchCategories() {
      try {
        const response = await axios.get('/api/categories/');
        this.categories = response.data;
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    },
    
    // Add new items
    async addExpense() {
      try {
        await axios.post('/api/expenses/', this.newExpense);
        this.fetchExpenses();
        this.newExpense = { amount: '', description: '', category: '', recipient: '' };
      } catch (error) {
        console.error('Error adding expense:', error);
      }
    },
    async addIncome() {
      try {
        await axios.post('/api/incomes/', this.newIncome);
        this.fetchIncomes();
        this.newIncome = { amount: '', description: '', category: '', source: '' };
      } catch (error) {
        console.error('Error adding income:', error);
      }
    },
    async addCategory() {
      try {
        await axios.post('/api/categories/', this.newCategory);
        this.fetchCategories();
        this.newCategory = { name: '', description: '' };
      } catch (error) {
        console.error('Error adding category:', error);
      }
    },
    
    // Delete items
    async deleteExpense(id) {
      if (confirm('Are you sure you want to delete this expense?')) {
        try {
          await axios.delete(`/api/expenses/${id}/`);
          this.fetchExpenses();
        } catch (error) {
          console.error('Error deleting expense:', error);
        }
      }
    },
    async deleteIncome(id) {
      if (confirm('Are you sure you want to delete this income?')) {
        try {
          await axios.delete(`/api/incomes/${id}/`);
          this.fetchIncomes();
        } catch (error) {
          console.error('Error deleting income:', error);
        }
      }
    },
    async deleteCategory(id) {
      if (confirm('Are you sure you want to delete this category?')) {
        try {
          await axios.delete(`/api/categories/${id}/`);
          this.fetchCategories();
        } catch (error) {
          console.error('Error deleting category:', error);
        }
      }
    },
    
    // Helper functions
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleDateString();
    },
    getCategoryName(categoryId) {
      const category = this.categories.find(cat => cat.id === categoryId);
      return category ? category.name : 'Unknown';
    }
  }
};
</script>

<style scoped>
.expense-tracker {
  max-width: 1000px;
  margin: 0 auto;
  padding: 20px;
}

.tabs {
  display: flex;
  margin-bottom: 20px;
}

.tabs button {
  padding: 10px 20px;
  background-color: #f1f1f1;
  border: none;
  cursor: pointer;
}

.tabs button.active {
  background-color: #4CAF50;
  color: white;
}

.form {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 20px;
}

.form input,
.form select,
.form button {
  padding: 8px;
}

.form button {
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
}

.data-table th,
.data-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

.btn-delete {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
}

.empty-state {
  padding: 20px;
  text-align: center;
  color: #666;
  font-style: italic;
}
</style>