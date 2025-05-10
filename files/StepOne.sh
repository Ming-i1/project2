#!/bin/bash

echo -e "\n\033[1;34m===== 此文件不应当有任何错误，例如找不到xxx命令 =====\033[0m\n"

echo -e "\n\033[1;34m===== 系统基本信息检测 =====\033[0m\n"
# 1. 系统信息
echo -e "\033[1;32m[系统信息]\033[0m" >> ./outputs/output1.txt
echo "主机名: $(hostname)" >> ./outputs/output1.txt
echo "操作系统: $(lsb_release -d | cut -f2-)" >>./outputs/output1.txt
echo "内核版本: $(uname -r)" >>./outputs/output1.txt
echo "系统架构: $(uname -m)" >>./outputs/output1.txt
echo "系统时间: $(date)" >>./outputs/output1.txt
echo "运行时间: $(uptime -p | sed 's/up //')" >>./outputs/output1.txt

# 2. CPU信息
echo -e "\n\033[1;32m[CPU信息]\033[0m" >>./outputs/output1.txt
echo "CPU型号: $(grep 'model name' /proc/cpuinfo | head -n1 | cut -d':' -f2 | sed 's/^[ \t]*//')" >>./outputs/output1.txt
echo "CPU核心数: $(grep -c 'processor' /proc/cpuinfo)" >>./outputs/output1.txt
echo "CPU使用率: $(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}')" >>./outputs/output1.txt

# 3. 内存信息
echo -e "\n\033[1;32m[内存信息]\033[0m" >>./outputs/output1.txt
free -h | awk '/^Mem:/ {print "总内存: " $2 "\n已用内存: " $3 "\n可用内存: " $4 "\n内存使用率: " $3/$2*100 "%"}'  >>./outputs/output1.txt

# 4. 磁盘信息
echo -e "\n\033[1;32m[磁盘信息]\033[0m" >>./outputs/output1.txt
df -h --output=source,size,used,avail,pcent | grep -v 'tmpfs' | awk 'NR==1 {print "设备\t总大小\t已用\t可用\t使用率"} NR>1 {print $0}' >>./outputs/output1.txt

# 5. 网络信息
echo -e "\n\033[1;32m[网络信息]\033[0m" >>./outputs/output1.txt
echo "IP地址: $(hostname -I | awk '{print $1}')" >>./outputs/output1.txt
echo "公网IP: $(curl -s ifconfig.me || echo "无法获取")" >>./outputs/output1.txt
echo "默认网关: $(ip route | grep default | awk '{print $3}')" >>./outputs/output1.txt

# 6. 登录用户
echo -e "\n\033[1;32m[用户信息]\033[0m" >>./outputs/output1.txt
echo "当前用户: $(whoami)" >>./outputs/output1.txt
echo "登录用户数: $(who | wc -l)" >>./outputs/output1.txt
echo "最近登录用户:" >>./outputs/output1.txt
last -n 3 | grep -v 'reboot' | awk '{print $1}' | uniq | head -n 3 >>./outputs/output1.txt

# 7. 系统负载
echo -e "\n\033[1;32m[系统负载]\033[0m" >>./outputs/output1.txt
echo "1分钟负载: $(uptime | awk -F'load average: ' '{print $2}' | cut -d, -f1)" >>./outputs/output1.txt
echo "5分钟负载: $(uptime | awk -F'load average: ' '{print $2}' | cut -d, -f2)" >>./outputs/output1.txt
echo "15分钟负载: $(uptime | awk -F'load average: ' '{print $2}' | cut -d, -f3)" >>./outputs/output1.txt

echo -e "\n\033[1;34m===== 检测完成 =====\033[0m\n" >>./outputs/output1.txt
