import { createSlice } from '@reduxjs/toolkit'
const scheduleSlice = createSlice({
    name: "scheduleSlice",
    initialState: {
        currentGroup: ""
    },
    reducers: {
        setGroup: (state, action) => {
            state.currentGroup = action.payload
        }
    }
})

export const {setGroup} = scheduleSlice.actions
export default scheduleSlice.reducer