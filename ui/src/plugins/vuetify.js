import '@mdi/font/css/materialdesignicons.css'
import '@fortawesome/fontawesome-free/css/all.css'
import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        dark: false,
        default: 'light',
        disable: false,
        options: {
            cspNonce: undefined,
            customProperties: undefined,
            minifyTheme: undefined,
            themeCache: undefined,
        },
        themes: {
            light: {
                primary: '#0366D6',
                secondary: '#24292E',
                accent: '#82B1FF',
                error: '#FF5252',
                info: '#2196F3',
                success: '#4CAF50',
                warning: '#FB8C00',
            },
            dark: {
                primary: '#2196F3',
                secondary: '#424242',
                accent: '#FF4081',
                error: '#FF5252',
                info: '#2196F3',
                success: '#4CAF50',
                warning: '#FB8C00',
            }
        }
    }
});
