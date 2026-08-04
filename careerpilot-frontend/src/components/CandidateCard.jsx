function CandidateCard({ candidate }) {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">

      <h2 className="text-xl font-bold text-blue-600 mb-6">
        Candidate Information
      </h2>

      <div className="grid md:grid-cols-2 gap-6">

        <div>

          <p className="font-semibold">
            Email
          </p>

          <p className="text-gray-600">
            {candidate.email}
          </p>

        </div>

        <div>

          <p className="font-semibold">
            Phone
          </p>

          <p className="text-gray-600">
            {candidate.phone}
          </p>

        </div>

      </div>

      <div className="mt-8">

        <h3 className="font-semibold mb-3">
          Skills
        </h3>

        <div className="flex flex-wrap gap-3">

          {candidate.skills.map((skill) => (
            <span
              key={skill}
              className="bg-blue-100 text-blue-700 px-3 py-2 rounded-full"
            >
              {skill}
            </span>
          ))}

        </div>

      </div>

    </div>
  );
}

export default CandidateCard;