from fastapi import FastAPI
from agent.agent import run_agent

app = FastAPI()

@app.get("/ask")
def ask(question: str):
    answer = run_agent(question)
    return {"response": answer}
