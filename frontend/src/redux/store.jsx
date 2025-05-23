import { configureStore } from '@reduxjs/toolkit'
import shellsReducer from './seaShell/reducers.jsx'
import userReducer from './user/reducers.jsx'

const store = configureStore({
  reducer: {
    shells: shellsReducer,
    user: userReducer,
  }
})

export default store
