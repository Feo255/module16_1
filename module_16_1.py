from fastapi import FastAPI
from pydantic import BaseModel

# Создаем экземпляр приложения FastAPI

app = FastAPI()

# Определение базового маршрута

@app.get("/")
async def root():
    return {"message": "Главная страница"}

@app.get("/user")
async def username(username, age):

    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get("/user/admin")
async def admin():
    return {"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_id(user_id: int):
    return {f"Вы вошли как пользователь № {user_id}"}

