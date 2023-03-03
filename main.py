from fastapi import FastAPI
from routes.auth_routes import router as authRouter
from routes.order_routes import router as orderRouter

app = FastAPI()


app.include_router(authRouter)
app.include_router(orderRouter)
