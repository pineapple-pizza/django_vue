import store from '@/store'
import axios from '@/plugins/axios.js'

store.subscribe((mutation) => {
    switch(mutation.type) {
        case 'auth/SET_TOKEN':
            if(mutation.payload) {
                axios.defaults.headers.common['Authorization'] = `Bearer ${mutation.payload}` 
                sessionStorage.setItem('token', mutation.payload)
            } else {
                axios.defaults.headers.common['Authorization'] = null
                sessionStorage.clear()
                localStorage.removeItem('token')
            }
            break;
    }
})