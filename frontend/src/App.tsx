import Layout from "./layout/Layout.tsx";
import {RouterProvider} from "react-router";
import objectRoutes from "./ObjectRoutes.tsx";
import './App.css'

function App() {
  return (
      <Layout>
          <RouterProvider router={objectRoutes} />
      </Layout>
  )
}

export default App
