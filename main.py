

from fastapi import FastAPI

app = FastAPI() # 创建API实例

# async def是定义异步函数的方法
# 127.0.0.1/
@app.get("/")
async def root():
    return {"message": "Hello World"}
