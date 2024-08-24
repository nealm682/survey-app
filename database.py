from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_DETAILS = os.getenv("MONGO_URI")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.survey_db
survey_collection = database.get_collection("survey_responses")

# Helper function to format MongoDB response
def survey_helper(survey) -> dict:
    return {
        "id": str(survey["_id"]),
        "age_range": survey["age_range"],
        "profession": survey["profession"],
        "current_work": survey.get("current_work"),
        "work_type": survey["work_type"],
        "motivations": survey["motivations"],
        "challenges": survey["challenges"],
        "flexibility": survey["flexibility"],
        "work_preference": survey["work_preference"],
        "desired_features": survey["desired_features"],
        "training_interest": survey["training_interest"],
        "specific_work": survey.get("specific_work"),
        "additional_features": survey.get("additional_features"),
    }

# Add a new survey response
async def add_survey(survey_data: dict) -> dict:
    survey = await survey_collection.insert_one(survey_data)
    new_survey = await survey_collection.find_one({"_id": survey.inserted_id})
    return survey_helper(new_survey)

