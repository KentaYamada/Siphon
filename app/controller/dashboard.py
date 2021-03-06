from datetime import datetime
from calendar import monthrange
from flask import Blueprint
from app.libs.api_response import ApiResponse
from app.libs.jwt_handler import api_required
from app.model.sales_item import PopularSalesItemSearchOption
from app.model.monthly_sales import MonthlySalesSearchOption
from app.model.mapper.sales_mapper import SalesMapper
from app.model.mapper.sales_item_mapper import SalesItemMapper


bp = Blueprint('dashboard', __name__, url_prefix='/api/dashboard')


@bp.route('/<int:year>/<int:month>', methods=['GET'])
@api_required
def index(year, month):
    monthly_sales = __get_monthly_sales(year, month)
    items = __get_popular_items(year, month)
    return ApiResponse(
        200,
        data={'monthly_sales': monthly_sales, 'popular_items': items}
    )


def __get_monthly_sales(year, month):
    # 月末日取得
    _, last = monthrange(year, month)
    option = MonthlySalesSearchOption(
        sales_date_from=datetime(year, month, 1).date(),
        sales_date_to=datetime(year, month, last).date()
    )
    mapper = SalesMapper()
    return mapper.find_monthly_sales(year, month, option)


def __get_popular_items(year, month):
    # 月末日取得
    _, last = monthrange(year, month)
    option = PopularSalesItemSearchOption(
        start_date=datetime(year, month, 1).date(),
        end_date=datetime(year, month, last).date()
    )
    mapper = SalesItemMapper()
    return mapper.find_popular_items(option)
