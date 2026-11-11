from fastapi import FastAPI
import uvicorn

klu=FastAPI(title="AI Tutor",
            description="AI Tutor PBL project",
            version="1.0.0"
            )
@klu.get("/")
def home():
    return {"message":"Welcome to AI Tutor Project"}

@klu.get("/demo")
def demo():
    return {"message":"KL University"}

@klu.get("/askquestion")
def ask():
    return {"message":"What is LLM","Answer":" large language model"}
@klu.get("/student")
def student():
    return {"id": 1, "Name": "Ram", "gender": "male", "Course": "DSA"}
@klu.get("/students")
def getstudents():
    return [{"id": 1, "Name": "Ram", "gender": "male", "Course": "DSA"},
            {"id": 2, "Name": "Klu", "gender": "male", "Course": "DSA"},
            {"id": 3, "Name": "Seetha", "gender": "female", "Course": "DSA"}]

if __name__ == "__main__":
    uvicorn.run("main:klu", host="127.0.0.1", port=2027,reload=True)