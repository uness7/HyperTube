const Header = () => {
    return (
        <header className="sticky top-0 z-50 w-full border-b border-gray-200 bg-white/80 backdrop-blur-md">
            <div className="container mx-auto flex h-16 items-center justify-between px-4">
                <div className="text-xl font-extrabold text-blue-600">HyperTube</div>
                <nav className="flex gap-6">
                    <a href="#" className="text-sm font-medium hover:text-blue-600 transition-colors">sign up</a>
                    <a href="#" className="text-sm font-medium hover:text-blue-600 transition-colors">log in</a>
                </nav>
            </div>
        </header>
    )
}

export default Header;
