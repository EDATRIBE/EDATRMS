import {Notify} from 'quasar'

Notify.registerType('success', {
    icon: 'check_circle',
    color: 'dark',
    textColor: 'green',
    position: 'bottom-right',
    group: false,
    timeout: 3000,
    actions: [
        {
            label: 'Dismiss', color: 'green', handler: () => { /* ... */
            }
        }
    ],
})

Notify.registerType('failure', {
    icon: 'error',
    color: 'dark',
    textColor: 'red',
    position: 'bottom-right',
    group: false,
    timeout: 3000,
    actions: [
        {
            label: 'Dismiss', color: 'red', handler: () => { /* ... */
            }
        }
    ],
})
