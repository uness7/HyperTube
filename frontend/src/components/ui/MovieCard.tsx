// @ts-ignore
const MovieCard = ({ title, duration, image }) => {
    return (
        <div className="group relative overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition-all hover:shadow-md hover:-translate-y-1">
            {/* Image Container with aspect ratio */}
            <div className="aspect-video w-full overflow-hidden bg-gray-100">
                <img
                    src={image}
                    alt={title}
                    className="h-full w-full object-cover transition-transform duration-300 group-hover:scale-105"
                />
            </div>

            {/* Content */}
            <div className="p-4">
                <h3 className="font-semibold text-gray-900 truncate" title={title}>
                    {title}
                </h3>
                <div className="mt-2 flex items-center text-sm text-gray-500">
                    <svg className="mr-1 h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    {duration}
                </div>
            </div>
        </div>
    );
};

export default MovieCard;