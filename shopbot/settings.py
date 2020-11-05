import os


BREAKPOINT_ON_SUCCESS = bool(os.environ.get("BREAKPOINT_ON_SUCCESS", "False"))
ABORT_ON_FAILURE = bool(os.environ.get("ABORT_ON_FAILURE", "False"))
CVV2 = os.environ["CVV2"]