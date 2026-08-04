function RoadmapCard({ roadmap }) {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">

      <h2 className="text-xl font-bold text-indigo-600 mb-5">
        Learning Roadmap
      </h2>

      <div className="space-y-4">

        {roadmap.map((step, index) => (

          <div
            key={index}
            className="border-l-4 border-indigo-500 pl-4"
          >
            <p>{step}</p>
          </div>

        ))}

      </div>

    </div>
  );
}

export default RoadmapCard;