function InterviewCard({ questions }) {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6">

      <h2 className="text-xl font-bold text-purple-600 mb-5">
        Interview Questions
      </h2>

      <ol className="list-decimal pl-6 space-y-3">
        {questions.map((item, index) => (
          <li key={index}>
            {item}
          </li>
        ))}
      </ol>

    </div>
  );
}

export default InterviewCard;