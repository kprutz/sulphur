import React, { Suspense } from 'react'
import { Route, Routes } from 'react-router-dom'

import Layout from 'components/Layout'

const AboutPage = React.lazy(() => import('pages/AboutPage'))
const HomePage = React.lazy(() => import('pages/HomePage'))
const PostsPage = React.lazy(() => import('pages/PostsPage'))

const AppRoutes = () => (
  <>
    <Suspense fallback={<div>Loading</div>}>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<HomePage />} />
          <Route path="/posts" element={<PostsPage />} />
          <Route path="/about" element={<AboutPage />} />
        </Route>
      </Routes>
    </Suspense>
  </>
)

export default AppRoutes
