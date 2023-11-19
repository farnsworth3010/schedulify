import { configureStore } from '@reduxjs/toolkit'
import { setupListeners } from '@reduxjs/toolkit/query'
import { scheduleApi } from './api' 
import scheduleSlice from './scheduleSlice'

export const store = configureStore({
  reducer: {
    [scheduleApi.reducerPath]: scheduleApi.reducer,
    schedule: scheduleSlice
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(scheduleApi.middleware),
})

// optional, but required for refetchOnFocus/refetchOnReconnect behaviors
// see `setupListeners` docs - takes an optional callback as the 2nd arg for customization
setupListeners(store.dispatch)