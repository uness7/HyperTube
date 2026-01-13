import {isRouteErrorResponse, useRouteError} from "react-router-dom";

function ErrorPage() {
    const err = useRouteError()
    console.log(err)

    if (isRouteErrorResponse(err)) {
        return (
            <div>
                <h1>{err.status} ----- {err.statusText}</h1>
                <p>{err.data}</p>
            </div>
        );
    }

    return (
        <div>
            <h1>Oops! An unexpected error occurred.</h1>
            {/*<p>{err?.message || "Unknown error"}</p>*/}
            <p>{"Unknown error"}</p>
        </div>
    );
}

export default ErrorPage