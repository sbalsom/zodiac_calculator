from ..calc import Calculator
from datetime import datetime

class ChartCalculator(Calculator):
    def __init__(self, *args):
        Calculator.__init__(self, *args)
        self.new_arg = 'new arg'
