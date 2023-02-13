<template>

    <li>
        <div>
            {{ employee.full_name }} {{ employee.position }}
        </div>
        <button @click="changeMe">Изменить</button>
        <ul>
            <Employee v-for="subemployee in employee.team" :employee="subemployee" :key="subemployee.id" @changeMe="changeMeDifferent"/>
        </ul>
    </li>


</template>

<script>
export default {
    name: "my-emp",
    props: {
        employee: {
            type: Object,
            required: true,
        }
    },
    methods: {
        changeMe() {
            const toSend = this.employee;
            if (this.employee.leader_id === null) {
                toSend.leader_id = "none";
            }
            this.$emit("changeMe", toSend);
        },
        changeMeDifferent(employee) {
            this.$emit("changeMe", employee);
        }
    }
}
</script>

<style>
</style>
