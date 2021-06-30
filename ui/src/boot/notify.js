import { Notify } from 'quasar'

Notify.registerType('success', {
  icon: 'check_circle',
  color: 'dark',
  textColor: 'green',
  position: 'top',
  group: false
})

Notify.registerType('failure', {
  icon: 'error',
  color: 'dark',
  textColor: 'red',
  position: 'top',
  group: false,
})
