import sys
from traceback import format_tb
import traceback

try:
    etetet
except Exception as e:
    exc, exc_value, tb = sys.exc_info()
    # print('\n'.join(format_tb(tb)))
    traceback.print_exc()
