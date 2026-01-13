import {useEffect, useState} from 'react';
import MovieCard from '../components/ui/MovieCard'

interface Movie {
    id: number,
    title: string,
    duration: string,
    size: string,
    thumbnail: string,
}

const MoviesPage = () => {
    const [isLoading, setIsLoading] = useState(true)
    const [movies, setMovies] = useState([])

    useEffect(() => {
        const fetchMovies = async () => {
            try {
                const response = await fetch('/api/v1/movies/');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                console.log("data " + data.results)
                setMovies(data.results);
            } catch (error) {
                console.log("Something went wrong")
            } finally {
                setIsLoading(false);
            }
        }
        fetchMovies()
    }, [])

    if (isLoading) {
        return <div className="text-center mt-10">Loading movies...</div>;
    }

    return (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {movies.map((movie: Movie) => (
                <MovieCard
                    key={movie.id}
                    title={movie.title}
                    image={movie.thumbnail}
                    duration={movie.duration}
                />
            ))}
        </div>
    );
};

export default MoviesPage;