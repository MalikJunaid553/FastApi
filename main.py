from fastapi import FastAPI
from agent.assistant import assistant_agent

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/products")
def read_root():
    return {"Name": "Iphone 17 pro max"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/ask")
def ask_agent(query:str):
    response= assistant_agent.invoke(
        {"messages":[{"role":"user", "content": query}]}
    )
    return{"response":response['messages'][-1].content}