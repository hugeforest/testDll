import os
import ctypes
dll = ctypes.WinDLL("mfcdll2.dll")

x=dll.add(1,2)
print(x)

