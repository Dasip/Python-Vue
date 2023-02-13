<template>

    <ul>
        <my-emp v-for="employee1 in employees" :employee="employee1" :key="employee1.id" @changeMe="changeMe"/>
    </ul>

</template>

<script>
export default {
    name: "my-emp-list",
    props: {
        employees: {
            type: Object,
            required: true,
        }
    },
    methods: {
        changeMe(employee) {
            this.$emit("changeMe", employee);
        }
    }
}
</script>

<style>
</style>