import { useState } from "react";

import api from "../services/api";

import ATSCard from "./ATSCard";
import MatchCard from "./MatchCard";
import CandidateCard from "./CandidateCard";
import StrengthCard from "./StrengthCard";
import WeaknessCard from "./WeaknessCard";
import RecommendationCard from "./RecommendationCard";
import InterviewCard from "./InterviewCard";
import RoadmapCard from "./RoadmapCard";

function UploadForm() {

    const [resume, setResume] = useState(null);

    const [jobDescription, setJobDescription] = useState("");

    const [loading, setLoading] = useState(false);

    const [result, setResult] = useState(null);

    const handleAnalyze = async () => {

        if (!resume) {
            alert("Please upload your resume.");
            return;
        }

        if (!jobDescription.trim()) {
            alert("Please paste the Job Description.");
            return;
        }

        try {

            setLoading(true);

            const formData = new FormData();

            formData.append("resume", resume);

            formData.append("job_description", jobDescription);

            const response = await api.post(
                "/analysis/",
                formData
            );

            setResult(response.data);

        } catch (err) {

            console.error(err);

            alert("Analysis Failed");

        } finally {

            setLoading(false);

        }

    };

    return (

        <>

            <div className="bg-white rounded-2xl shadow-lg p-8">

                <h2 className="text-2xl font-bold mb-6">

                    Upload Resume

                </h2>

                <div className="mb-6">

                    <label className="block mb-2 font-semibold">

                        Resume PDF

                    </label>

                    <input

                        type="file"

                        accept=".pdf"

                        onChange={(e) =>
                            setResume(e.target.files[0])
                        }

                        className="w-full border rounded-lg p-3"

                    />

                </div>

                <div className="mb-6">

                    <label className="block mb-2 font-semibold">

                        Job Description

                    </label>

                    <textarea

                        rows={10}

                        value={jobDescription}

                        onChange={(e) =>
                            setJobDescription(e.target.value)
                        }

                        className="w-full border rounded-lg p-4 resize-none"

                        placeholder="Paste Job Description..."

                    />

                </div>

                <button

                    onClick={handleAnalyze}

                    className="bg-blue-600 hover:bg-blue-700 transition text-white px-8 py-3 rounded-xl font-semibold"

                >

                    {

                        loading

                            ? "Analyzing..."

                            : "Analyze Resume"

                    }

                </button>

            </div>

            {

                result && (

                    <div className="mt-10 space-y-6">

                        <div className="grid md:grid-cols-2 gap-6">

                            <ATSCard

                                ats={
                                    result.data.analysis.ats
                                }

                            />

                            <MatchCard

                                jobMatch={
                                    result.data.analysis.job_match
                                }

                            />

                        </div>

                        <CandidateCard

                            candidate={
                                result.data.candidate
                            }

                        />

                        <div className="grid md:grid-cols-2 gap-6">

                            <StrengthCard

                                strengths={
                                    result.data.analysis.ai_feedback.strengths
                                }

                            />

                            <WeaknessCard

                                weaknesses={
                                    result.data.analysis.ai_feedback.weaknesses
                                }

                            />

                        </div>

                        <RecommendationCard

                            recommendations={
                                result.data.analysis.ai_feedback.recommendations
                            }

                        />

                        <InterviewCard

                            questions={
                                result.data.analysis.ai_feedback.interview_questions
                            }

                        />

                        <RoadmapCard

                            roadmap={
                                result.data.analysis.ai_feedback.learning_roadmap
                            }

                        />

                    </div>

                )

            }

        </>

    );

}

export default UploadForm;