import Header from './Header';
import Footer from './Footer';

// Use the special 'children' prop to render whatever is inside the layout
// @ts-ignore
const Layout = ({ children }) => {
    return (
        <div className="flex min-h-screen flex-col">
            <Header />

            {/* 'flex-grow' pushes the footer down if content is short */}
            <main className="flex-grow container mx-auto px-4 py-8">
                {children}
            </main>

            <Footer />
        </div>
    );
};

export default Layout;