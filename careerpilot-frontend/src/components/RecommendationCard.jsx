function RecommendationCard({ recommendations }) {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">

      <h2 className="text-xl font-bold text-blue-600 mb-5">
        AI Recommendations
      </h2>

      <ol className="list-decimal pl-6 space-y-3">
        {recommendations.map((item, index) => (
          <li key={index}>
            {item}
          </li>
        ))}
      </ol>

    </div>
  );
}

export default RecommendationCard;