function ATSCard({ ats }) {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">

      <h2 className="text-xl font-bold text-blue-600 mb-4">
        ATS Score
      </h2>

      <div className="text-6xl font-bold text-center text-green-600">
        {ats.ats_score}%
      </div>

      <div className="mt-6 space-y-2 text-gray-700">

        {Object.entries(ats.breakdown).map(([key, value]) => (
          <div
            key={key}
            className="flex justify-between border-b pb-2"
          >
            <span className="capitalize">{key}</span>

            <span>{value}</span>

          </div>
        ))}

      </div>

    </div>
  );
}

export default ATSCard;