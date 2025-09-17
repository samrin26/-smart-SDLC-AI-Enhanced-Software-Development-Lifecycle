# Smart SDLC – Simple Python Backend

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# User input format
class UserInput(BaseModel):
    prompt: str | None = None
    code: str | None = None


# 1. Requirement Upload & Classification
@app.post("/classify")
def classify_requirement(data: UserInput):
    return {
        "requirement": data.prompt,
        "classified_phase": "Requirement Analysis"
    }


# 2. AI Code Generator (Simple Mock)
@app.post("/generate")
def generate_code(data: UserInput):
    generated = f"# Auto-generated code for: {data.prompt}\nprint('Hello from AI!')"
    return {"code": generated}


# 3. Bug Fixer
@app.post("/fix")
def bug_fixer(data: UserInput):
    try:
        compile(data.code, "<string>", "exec")
        return {"status": "No errors", "fixed_code": data.code}
    except SyntaxError as e:
        return {"status": "Syntax Error", "line": e.lineno,