import { createApp } from 'vue';
import App from './App.vue';
import components from "@/components";
import ui from "@/components/UI";

const app = createApp(App);

components.forEach(component => {
    app.component(component.name, component)
})
ui.forEach(ui => {
    app.component(ui.name, ui)
})

app.mount('#app')
