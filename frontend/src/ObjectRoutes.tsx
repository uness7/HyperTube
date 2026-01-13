import {createBrowserRouter} from "react-router";
import ErrorPage from "./pages/ErrorPage.tsx";
import MoviesPage from "./pages/MoviesPage.tsx";
import SignInPage from "./pages/SignInPage.tsx";
import SignUpPage from "./pages/SignUpPage.tsx";

const router = createBrowserRouter([
    {
        path: "/",
        element: <MoviesPage />,
        errorElement: <ErrorPage />
    },
    {
        path: "/sign-in",
        element: <SignInPage />,
    },
    {
        path: "/create-account",
        element: <SignUpPage />
    },
])

export default router