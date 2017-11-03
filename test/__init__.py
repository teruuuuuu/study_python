from os import path
import sys
APP_ROOT = path.dirname( path.abspath( __file__ ) ) + "/../src/"
TEST_SCRIPT = path.dirname( path.abspath( __file__ ) ) + "/basic/index_count_spec.py"
sys.path.append(APP_ROOT)
sys.path.append(TEST_SCRIPT)
