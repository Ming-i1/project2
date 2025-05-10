import platform
import sys
import subprocess
import importlib
import time
import os
from datetime import datetime
import io

def print_header(title):
    print("\n" + "="*50)
    print(f"{title:^50}")
    print("="*50)

def print_section(title):
    print("\n" + "-"*50)
    print(f"{title:^50}")
    print("-"*50)

def get_system_info():

    print_header("系统基本信息")
    print("\n[操作系统信息]")
    print(f"系统类型: {platform.system()}")
    print(f"系统版本: {platform.version()}")
    print(f"系统发行版: {platform.platform()}")
    print(f"机器架构: {platform.machine()}")
    print(f"处理器信息: {platform.processor()}")

    print("\n[Python环境]")
    print(f"Python版本: {platform.python_version()}")
    print(f"Python实现: {platform.python_implementation()}")
    print(f"Python路径: {sys.executable}")

def test_pytorch():
    print_section("PyTorch 测试")
    try:
        torch = importlib.import_module('torch')
        print(f"此脚本与pytorch不兼容")
        return False
    except Exception as e:
        os.system("nvidia-smi")
        return True

if __name__=='__main__':
    with open('./outputs/output3.txt', 'w') as file:
        original_stdout = sys.stdout
        
        # file = io.TextIOWrapper(file.buffer, encoding='utf-8')
        sys.stdout = file
        get_system_info()
        test_pytorch()
        sys.stdout = original_stdout

else:
    print("错误")
