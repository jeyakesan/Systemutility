import psutil
import platform
import cpuinfo
uname = platform.uname()
print (f"Processor brand  : {cpuinfo.get_cpu_info()['brand_raw']}")
print(f"Processor: {uname.processor}")
print("No.of cores:", psutil.cpu_count(logical=False))
print("No.of Threads (i.e order of instructions that can be passed in a single core):", psutil.cpu_count(logical=True))

