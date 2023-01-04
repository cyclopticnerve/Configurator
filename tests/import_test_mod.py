
# ------------------------------------------------------------------------------
# this part is only for internal package test without venv install
# import os
# import sys

# curr_dir = os.path.abspath(os.path.dirname(__file__))
# up_one = os.path.abspath(os.path.join(curr_dir, '../src'))
# sys.path.insert(1, up_one)

# ------------------------------------------------------------------------------

import configurator                                        # 1 one
print(configurator.func())

# import configurator as mod                                 # 2 one as
# print(mod.func())

# from configurator import func                              # 3 from one
# print(func())

# from configurator import func as afunc                     # 4 from one as
# print(afunc())

# # THIS ONE IS NOT USED!!!
# import configurator.func                                   # 5 two
# print(configurator.func())                                 # (same as #1)

# # THIS ONE IS NOT USED!!!
# import configurator.func as afunc                          # 6 two as
# print(afunc())                                                  # (same as #4)

# # THIS ONE DOES NOT EXIST!!!
# from configurator.configurator import func            # 7 from two
# print(func())

# # THIS ONE DOES NOT EXIST!!!
# from configurator.configurator import func as afunc   # 8 from two as
# print(afunc())

# # WORKS, BUT NOT RECOMMENDED!!!
# from configurator import *
# print(func())                                                   # (same as #3)
