<template>

  <div>
    <button @click="showDialog">Создать</button>

    <my-dialog id="create" v-model:show="dialogCreateVisible">
      <my-create v-bind:employees="employeesNoHier" @create="createEmployee"/>
    </my-dialog>

    <my-dialog id="update" v-model:show="dialogUpdateVisible">
      <my-update v-bind:employees="employeesNoHier" v-bind:toChange="employeeToChange" @update="changeEmployee"/>
    </my-dialog>

    <my-emp-list v-bind:employees="employees" @changeMe="changeMe"/>
  </div>

</template>

<script>
import axios from "axios";
export default {
  data () {
    return {
      employees: [],
      employeesNoHier: [],
      dialogCreateVisible: false,
      dialogUpdateVisible: false,
      employeeToChange: {},
    }
  },
  methods: {
    async fetchHierarchy() {
      try {
        const response = await axios.get("http://89.223.123.190:7777/employees/all");
        this.employees = response.data;
        this.employeesNoHier = [];
        this.fillNoHier(this.employees);
      } catch(e) {
        console.log(e);
        alert('Ошибка');
      }
    },
    async sendEmployee(employee) {
      try {
        const response = await axios.post("http://89.223.123.190:7777/employees/new", 
        employee);
      } catch(e) {
        console.log(e);
      }
    },
    async sendChange (employee) {
      try {
        console.log(employee);
        const response = await axios.post("http://89.223.123.190:7777/employees/change",
        employee);
        console.log(response);
      } catch(e) {
        console.log(e);
      }
    },
    showDialog() {
      this.dialogCreateVisible = true;
    },
    showUpdate() {
      this.dialogUpdateVisible = true;
    },
    fillNoHier(team) {

      if (typeof team !== "undefined" && team.length > 0) {

        team.forEach(element => {
          this.fillNoHier(element.team);
          this.employeesNoHier.push(element);
        });
      }
    },
    createEmployee(employee) {
      this.sendEmployee(employee)
      .then(result => this.fetchHierarchy());
      this.dialogCreateVisible = false;
    },
    changeMe(employee) {
      this.employeeToChange = employee;
      this.dialogUpdateVisible = true;
    },
    changeEmployee(employee) {
      this.sendChange(employee)
      .then(result => this.fetchHierarchy());
      this.dialogUpdateVisible = false;
    }
  },
  mounted() {
    this.fetchHierarchy();
  }
}
</script>

<style>

</style>
