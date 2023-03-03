from fastapi import APIRouter

router = APIRouter(
    prefix='/api/orders',
    tags=['Orders']
)


@router.get('')
async def hello():
    return {'message': 'hello from Order'}