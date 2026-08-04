import Navbar from "../components/Navbar";
import UploadForm from "../components/UploadForm";

function Home() {
  return (
    <div className="min-h-screen bg-slate-100">
      <Navbar />

      <div className="max-w-7xl mx-auto px-6 py-10">

        {/* Header */}

        <div className="text-center mb-12">

          <h1 className="text-5xl font-bold text-blue-700">
            CareerPilot AI
          </h1>

          <p className="mt-4 text-gray-600 text-lg">
            AI Powered Resume Intelligence Platform
          </p>

        </div>

        {/* Upload Form */}

        <UploadForm />

      </div>
    </div>
  );
}

export default Home;