function StrengthCard({ strengths }) {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6 h-full">
      <h2 className="text-xl font-bold text-green-600 mb-4">
        Strengths
      </h2>

      <ul className="space-y-3">
        {strengths.map((item, index) => (
          <li
            key={index}
            className="flex gap-3 items-start"
          >
            <span className="text-green-600 font-bold">
              ✓
            </span>

            <span>{item}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default StrengthCard;