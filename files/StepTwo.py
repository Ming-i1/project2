#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform
import sys
import subprocess
import importlib
import time
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

def test_numpy():
    print_section("NumPy 测试")
    try:
        numpy = importlib.import_module('numpy')
        print(f"NumPy版本: {numpy.__version__}")

        # 基本功能测试
        a = numpy.array([1, 2, 3])
        b = numpy.array([4, 5, 6])
        dot_product = numpy.dot(a, b)

        print("\nNumPy 基本运算测试:")
        print(f"数组 a: {a}")
        print(f"数组 b: {b}")
        print(f"点积结果: {dot_product} (应为32)")

        return True
    except Exception as e:
        print(f"NumPy 测试失败: {str(e)}")
        return False

def test_pytorch():
    print_section("PyTorch 测试")
    try:
        torch = importlib.import_module('torch')
        print(f"PyTorch版本: {torch.__version__}")
        print(f"CUDA可用: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"CUDA版本: {torch.version.cuda}")
            print(f"当前设备: {torch.cuda.get_device_name(0)}")

        # 基本功能测试
        x = torch.rand(2, 3)
        y = torch.rand(3, 2)
        z = torch.mm(x, y)

        print("\nPyTorch 基本运算测试:")
        print(f"矩阵 x:\n{x}")
        print(f"矩阵 y:\n{y}")
        print(f"矩阵乘法结果:\n{z}")

        return True
    except Exception as e:
        print(f"PyTorch 测试失败: {str(e)}")
        return False

def test_matplotlib():
    print_section("Matplotlib 测试")
    try:
        plt = importlib.import_module('matplotlib.pyplot')
        plt1 = importlib.import_module('matplotlib')
        numpy = importlib.import_module('numpy')
        print(f"Matplotlib版本: {plt1.__version__}")

        # 基本绘图测试
        x = numpy.linspace(0, 10, 100)
        y = numpy.sin(x)

        plt.figure(figsize=(8, 4))
        plt.plot(x, y, label='sin(x)')
        plt.title('Matplotlib Test')
        plt.xlabel('x')
        plt.ylabel('sin(x)')
        plt.legend()

        # 保存图片而不是显示，避免阻塞脚本
        filename = f"OutImage.png"
        plt.savefig(filename)
        plt.close()

        print(f"\n测试图表已保存为: {filename}")
        return True
    except Exception as e:
        print(f"Matplotlib 测试失败: {str(e)}")
        return False

def main():
    start_time = time.time()

    print_header("Python 环境测试工具")
    print(f"测试开始时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    get_system_info()

    # 测试各模块
    results = {
        "NumPy": test_numpy(),
        "PyTorch": test_pytorch(),
        "Matplotlib": test_matplotlib()
    }

    # 总结报告
    print_header("测试总结")
    for name, success in results.items():
        status = "√ 通过" if success else "× 失败"
        print(f"{name:>12}: {status}")

    elapsed = time.time() - start_time
    print(f"\n测试总耗时: {elapsed:.2f} 秒")
    print(f"测试完成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    with open('./outputs/output2.txt', 'w') as file:
        original_stdout = sys.stdout
        sys.stdout = file
        # sys.stdout = io.TextIOWrapper(file.buffer, encoding='utf-8')
        main()
        sys.stdout = original_stdout