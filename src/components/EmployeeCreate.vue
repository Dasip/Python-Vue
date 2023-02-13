<template>

    <form>

    <input type="text" @input="inputFullName" v-bind:value="full_name" placeholder="ФИО">
    <input type="text" @input="inputPosition" v-bind:value="position" placeholder="Позиция">
    <input type="number" @input="inputSalary" v-bind:value="salary" placeholder="Зарплата">
    <input type="date" @input="inputStartDate" v-bind:value="start_date" placeholder="Дата приема на работу">
    <select id="leader" @input="inputLeaderId" v-bind:value="leader_id" name="Руководитель">
        <option value="none">Нет руководителя</option>
        <option v-for="emp in employees" :value="emp.id" :key="emp.id"> {{ emp.full_name }}</option>
    </select>

    </form>

    <button @click="createEmployee">Создать</button>

</template>

<script>

export default {
    name: "my-create",
    props: {
        employees: {
            type: Object,
            required: true,
        }
    },
    data() {
        return {
            full_name: '',
            position: '',
            salary: 0,
            start_date: Date.now(),
            leader_id: "none",
        }
    },
    methods: {
        inputFullName(event){
            this.full_name = event.target.value;
        },
        inputPosition(event){
            this.position = event.target.value;
        },
        inputSalary(event){
            this.salary = event.target.value;
        },
        inputStartDate(event){
            this.start_date = event.target.value;
        },
        inputLeaderId(event){
            this.leader_id = event.target.value;
        },
        createEmployee(){
            const newEmployee = {};
            newEmployee.full_name = this.full_name;
            newEmployee.position = this.position;
            newEmployee.salary = this.salary;
            newEmployee.start_date = this.start_date;
            if (this.leader_id !== "none") {
                newEmployee.leader_id = this.leader_id;
            }
            this.$emit("create", newEmployee);
            this.full_name = "";
            this.position = "";
            this.salary = 0;
            this.start_date = Date.now();
            this.leader_id = "none";

        },
    }
}
</script>

<style scoped>

form {
    display: flex;
    flex-direction: column;
}

* {
    margin: 10px;
}

</style>