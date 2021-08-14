import platform
import cpuinfo
uname = platform.uname()
print (f"Processor brand  : {cpuinfo.get_cpu_info()['brand_raw']}")
print(f"Processor: {uname.processor}")
