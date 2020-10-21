from . import bp
from .calc import ChartCalculator
from datetime import datetime

@bp.route('/hello', methods=(['GET']))
def hello():
    dt = datetime(1992, 5, 12, 7, 21, 0)
    chart = ChartCalculator(dt, 33.65768, 33.5467658, 'W')
    return f'{chart.lon} {chart.utc_offset()}'
