from fastapi import FastAPI

app = FastAPI()  # 创建 api 对象


@app.get("/")  # 根路由
def root():
    return {"tianjin": "加油！！！"}


@app.get("/say/{data}")
def say(data: str, q: int):
    return {"data": data, "item": q}
