import uvicorn
from fastapi import FastAPI
from routers import router as inventory_router
app = FastAPI(title="Medical Inventory",
    description="Система управления медицинским инвентарем",
    version="1.0.0")

app.include_router(inventory_router, prefix="/api/v1", tags=["Inventory"])

@app.get("/")
def root():
    return {"message": "Welcome to Medical System API"}

if __name__ == "__main__":
    # Запускаем сервер uvicorn
    uvicorn.run(
        "main:app",      # "имя_файла:переменная_FastAPI"
        host="127.0.0.1",
        port=8000,
        reload=True      # Автоперезагрузка при сохранении кода
    )