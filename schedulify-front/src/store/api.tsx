import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const scheduleApi = createApi({
  reducerPath: 'scheduleApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://localhost:8585/api.php' }),
  endpoints: (builder) => ({
    getSchedule: builder.query({
      query: (id) => `?group_id=${id}`,
    }),
  }),
})

export const { useGetScheduleQuery } = scheduleApi 