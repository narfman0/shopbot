import os


BREAKPOINT_ON_SUCCESS = bool(os.environ.get("BREAKPOINT_ON_SUCCESS", "True"))
BUY_NOW = bool(os.environ.get("BUY_NOW", ""))
ABORT_ON_FAILURE = bool(os.environ.get("ABORT_ON_FAILURE", ""))
CVV2 = os.environ["CVV2"]
