function MatchCard({ jobMatch }) {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">

      <h2 className="text-xl font-bold text-purple-600 mb-4">
        Job Match
      </h2>

      <div className="text-6xl font-bold text-center text-blue-600">
        {jobMatch.match_score}%
      </div>

      <div className="mt-6">

        <h3 className="font-semibold mb-2">
          Matched Skills
        </h3>

        <div className="flex flex-wrap gap-2">

          {jobMatch.matched_skills.map((skill) => (
            <span
              key={skill}
              className="bg-green-100 text-green-700 px-3 py-1 rounded-full"
            >
              {skill}
            </span>
          ))}

        </div>

      </div>

      <div className="mt-6">

        <h3 className="font-semibold mb-2">
          Missing Skills
        </h3>

        <div className="flex flex-wrap gap-2">

          {jobMatch.missing_skills.length === 0 ? (
            <span className="text-green-600">
              None
            </span>
          ) : (
            jobMatch.missing_skills.map((skill) => (
              <span
                key={skill}
                className="bg-red-100 text-red-600 px-3 py-1 rounded-full"
              >
                {skill}
              </span>
            ))
          )}

        </div>

      </div>

    </div>
  );
}

export default MatchCard;