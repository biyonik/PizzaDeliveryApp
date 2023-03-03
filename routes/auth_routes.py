from fastapi import APIRouter

router = APIRouter(
    prefix='/api/auth',
    tags=['Authorization']
)


@router.get('')
async def hello():
    return {'message': 'hello from Auth'}