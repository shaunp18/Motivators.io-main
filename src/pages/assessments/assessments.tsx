import React, { useState } from 'react';
import "./assessments.scss";
import { Button } from '@mui/material';

// Define interfaces for better type checking
interface Assessment {
    id: number;
    name: string;
    content: string;
    description: string;
    level: 'Beginner' | 'Intermediate' | 'Advanced';
  }
interface AssessmentBoxProps {
  assessment: Assessment;
  onOpen: (assessment: Assessment) => void;
}

const AssessmentBox = ({assessment, onOpen}: AssessmentBoxProps) => (

    <div className="assessment">
    <h3>{assessment.name}</h3>
    <p>{assessment.description}</p>
    <div className="level">{assessment.level}</div>
    <Button variant="contained"onClick={() => onOpen(assessment)}>Open Assessment</Button>
  </div>

   
);

const Assessments = () => {
  const [openAssessment, setOpenAssessment] = useState<Assessment | null>(null);

  const handleOpenAssessment = (assessment: Assessment) => {
    console.log(`Opening ${assessment.name}`);
    // Set the open assessment, you could use this to display details about it
    setOpenAssessment(assessment);
  };

  const assessmentsData: Assessment[] = [
    {
        id: 1,
        name: 'Assessment 1',
        content: 'Content for Assessment 1',
        description: 'This is a beginner-level assessment to test your basics.',
        level: 'Beginner',
      },
      {
        id: 2,
        name: 'Assessment 2',
        content: 'Content for Assessment 2',
        description: 'An intermediate-level assessment for those who have mastered the basics.',
        level: 'Intermediate',
      },
    // You can add more assessments here if needed
  ];

  return (
    <div className="home">
      {assessmentsData.map(assessment => (
        <div key={assessment.id} className="box">
          <AssessmentBox assessment={assessment} onOpen={handleOpenAssessment} />
        </div>
      ))}
    </div>
  );
};

export default Assessments;