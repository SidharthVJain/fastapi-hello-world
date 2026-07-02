from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return "Hello from my API!"

@app.get("/about")
async def read_about():
    return {
        'name': 'Aswathy Santhosh',
        'bio': 'Hi, I\'m  a third year undergraduate student at St. Joseph\'s College of Engineering. I am currently pursuing my B.Tech in Computer Science and Engineering(AI). I have a keen interest in web development, machine learning, and data science. In my free time, I enjoy reading tech blogs, exploring new programming languages, and contributing to open-source projects.'
    }

@app.get("/greet/{name}")
async def greet(name: str):
    return f"Hello, {name}! Welcome to my API."