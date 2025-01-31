import { configureStore } from '@reduxjs/toolkit'
import shellsReducer from './reducers.jsx'

const store = configureStore({
  reducer: {
    shells: shellsReducer
  }
})

export default store
