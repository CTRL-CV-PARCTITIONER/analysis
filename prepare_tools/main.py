import time
timestamp = time.time()
get_mtime = time.gmtime()
local_time = time.localtime()
init_time = time.gmtime(0)

timeftr = time.strftime(
    "%Y-%m-%d %H:%M:%S",
    time.localtime(),
)

timeptr = time.strptime(
    '2017-9-30 11:32:23',
    "%Y-%m-%d %H:%M:%S"
)


print(timeptr)
