from fastapi import APIRouter
from datetime import datetime
from models import ResponsePriceEstimation, InputRealEstate
from logic.price_estimation import perform_price_estimation

router = APIRouter(
    prefix='/priceEstimation',
    tags=['priceEstimation'],
    responses={400: {'description': 'Bad Request'}}
)


@router.post('/', response_model=ResponsePriceEstimation)
def price_estimation(item: InputRealEstate):
    estimated_price = perform_price_estimation(item)
    return {
        'estimated_price': estimated_price,
        'DateTime': datetime.now()
    }
