from typing import Dict
from typing import List, Tuple
#include "master.h"
#include "global.h"
#include "tools.h"
from master import *
from global_ import *
from register_is import resister_is
import tools
import splitter
import check_storage
import rpair
import set_flag_register

breakpoints: Dict[int, bool] = {}

def check_breakpoint(key: int) -> bool:
    if key not in breakpoints:
        return False
    else:
        return breakpoints[key]
