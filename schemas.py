from pydantic import BaseModel, Field
from typing import Optional

class SurveyResponse(BaseModel):
    age_range: str = Field(...)
    profession: str = Field(...)
    current_work: Optional[str]
    work_type: str = Field(...)
    motivations: str = Field(...)
    challenges: str = Field(...)
    flexibility: int = Field(...)
    work_preference: str = Field(...)
    desired_features: str = Field(...)
    training_interest: int = Field(...)
    specific_work: Optional[str]
    additional_features: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "age_range": "60-69",
                "profession": "Engineer",
                "current_work": "Consulting",
                "work_type": "Consulting, Writing",
                "motivations": "Need for additional income, Staying active",
                "challenges": "Age bias from employers, Competing with younger freelancers",
                "flexibility": 5,
                "work_preference": "Remote",
                "desired_features": "Job matching based on skills and experience",
                "training_interest": 4,
                "specific_work": "Technical writing",
                "additional_features": "Access to a community of like-minded professionals",
            }
        }
