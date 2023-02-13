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

    <button @click="changeFinal">Изменить</button>

</template>

<script>

export default {
    name: "my-update",
    props: {
        employees: {
            type: Object,
            required: true,
        },
        toChange: {
            type: Object,
            required: true,
        }
    },
    data() {
        return {
            full_name: this.toChange.full_name,
            position: this.toChange.position,
            salary: this.toChange.salary,
            start_date: this.toChange.start_date,
            leader_id: this.toChange.leader_id.toString(),
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
        changeFinal() {
            const newSettings = {};
            newSettings.id = this.toChange.id;
            newSettings.full_name = this.full_name;
            newSettings.position = this.position;
            newSettings.salary = this.salary;
            newSettings.start_date = this.start_date;
            if (this.leader_id !== "none") {
                newSettings.leader_id = this.leader_id;
            }
            this.$emit("update", newSettings);
            this.full_name = "";
            this.position = "";
            this.salary = 0;
            this.start_date = Date.now();
            this.leader_id = "none";
        }
        
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