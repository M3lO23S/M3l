#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         M3l - NetGuard Security Suite                         ║
║                       Advanced Network & System Protection                    ║
║                              Version 5.0 - Final                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

M3l - أداة الحماية المتكاملة للشبكات والأنظمة
للاستخدام التعليمي والأمني فقط - استخدم بمسؤولية

المطور:
📱 Telegram: @JYI_L
📸 Instagram: @mo3lzo
🎥 YouTube: @M3_7L0
"""

import subprocess
import socket
import threading
import time
import os
import platform
import json
import sys
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import hashlib
import random
import string

try:
    import psutil
    import netifaces
    import scapy.all as scapy
    import requests
    from ping3 import ping
    import whois
    import dns.resolver
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    print("\033[93m[!] جاري تثبيت المكتبات المطلوبة...\033[0m")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil", "netifaces", "scapy", "ping3", "python-whois", "dnspython", "requests", "colorama"])
    import psutil
    import netifaces
    import scapy.all as scapy
    import requests
    from ping3 import ping
    import whois
    import dns.resolver
    from colorama import init, Fore, Back, Style
    init(autoreset=True)

class M3lSecurity:
    def __init__(self):
        self.version = "5.0.0"
        self.author = "M3L Security Team"
        self.telegram = "@JYI_L"
        self.instagram = "@mo3lzo"
        self.youtube = "@M3_7L0"
        self.os_type = platform.system()
        self.start_time = datetime.now()
        self.results = {
            "scan_id": hashlib.md5(str(time.time()).encode()).hexdigest()[:8],
            "scan_time": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "system_info": {},
            "network_devices": [],
            "background_processes": [],
            "ip_analysis": {},
            "open_ports": [],
            "security_alerts": [],
            "intrusions": [],
            "network_traffic": {}
        }
        
        # الألوان والخلفيات المتقدمة
        self.colors = {
            'BLACK': Fore.BLACK,
            'RED': Fore.RED,
            'GREEN': Fore.GREEN,
            'YELLOW': Fore.YELLOW,
            'BLUE': Fore.BLUE,
            'MAGENTA': Fore.MAGENTA,
            'CYAN': Fore.CYAN,
            'WHITE': Fore.WHITE,
            'RESET': Style.RESET_ALL,
            'BRIGHT': Style.BRIGHT,
            'DIM': Style.DIM,
            'BACK_RED': Back.RED,
            'BACK_GREEN': Back.GREEN,
            'BACK_BLUE': Back.BLUE,
            'BACK_YELLOW': Back.YELLOW,
            'BACK_CYAN': Back.CYAN,
            'BACK_MAGENTA': Back.MAGENTA
        }
        
        self.loading_chars = ['⣾', '⣽', '⣻', '⢿', '⡿', '⣟', '⣯', '⣷']
    
    def print_loading_animation(self, message, duration=1):
        """طباعة أنيميشن تحميل جميل"""
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            sys.stdout.write(f'\r{self.colors["CYAN"]}{self.loading_chars[i % len(self.loading_chars)]} {message}{self.colors["RESET"]}')
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
        sys.stdout.write('\r' + ' ' * (len(message) + 2) + '\r')
    
    def print_banner(self):
        """طباعة الشعار الرئيسي المتطور"""
        banner = f"""
{self.colors['CYAN']}{Style.BRIGHT}╔{'═'*78}╗{Style.RESET_ALL}
{self.colors['RED']}{Style.BRIGHT}║{self.colors['YELLOW']}                                                                              {self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}║{self.colors['WHITE']}   ███╗   ███╗████████╗██╗     ███████╗{self.colors['GREEN']}███████╗███████╗{self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}║{self.colors['WHITE']}   ████╗ ████║╚══██╔══╝██║     ██╔════╝{self.colors['GREEN']}██╔════╝██╔════╝{self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}║{self.colors['WHITE']}   ██╔████╔██║   ██║   ██║     █████╗  {self.colors['GREEN']}███████╗█████╗  {self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}║{self.colors['WHITE']}   ██║╚██╔╝██║   ██║   ██║     ██╔══╝  {self.colors['GREEN']}╚════██║██╔══╝  {self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}║{self.colors['WHITE']}   ██║ ╚═╝ ██║   ██║   ███████╗███████╗{self.colors['GREEN']}███████║███████╗{self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}║{self.colors['WHITE']}   ╚═╝     ╚═╝   ╚═╝   ╚══════╝╚══════╝{self.colors['GREEN']}╚══════╝╚══════╝{self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}║{self.colors['YELLOW']}                                                                              {self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}║{self.colors['CYAN']}{Style.BRIGHT}              🛡️  M3l Security Suite v{self.version}  🛡️                      {self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}║{self.colors['WHITE']}{Style.DIM}                       {self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}║{self.colors['GREEN']}  ╔══════════════════════════════════════════════════════════════════════╗  {self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}║{self.colors['GREEN']}  ║  {self.colors['YELLOW']}📱 Telegram:{self.colors['CYAN']} {self.telegram:<20} {self.colors['MAGENTA']}📸 Instagram:{self.colors['CYAN']} {self.instagram:<15}  {self.colors['GREEN']}║{self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}║{self.colors['GREEN']}  ║  {self.colors['YELLOW']}🎥 YouTube:{self.colors['CYAN']} {self.youtube:<30}                                      {self.colors['GREEN']}║{self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}║{self.colors['GREEN']}  ╚══════════════════════════════════════════════════════════════════════╝  {self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}║{self.colors['WHITE']}{Style.DIM}                                                                              {self.colors['RED']}║
{self.colors['RED']}{Style.BRIGHT}╚{'═'*78}╝{Style.RESET_ALL}

{self.colors['YELLOW']}{Style.BRIGHT}┌──────────────────────────────────────────────────────────────────────────────┐
│  🔒 Advanced Network & System Protection Suite                               │
│  ⚡ Powerd by M3L Security Team - All Rights Reserved                       │
│  🚀 Professional Security Tool - Use Responsibly                            │
└──────────────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}
        """
        print(banner)
    
    def print_header(self, title, icon="🔒"):
        """طباعة عنوان قسم بشكل جميل"""
        print(f"\n{self.colors['CYAN']}{Style.BRIGHT}┌{'─'*76}┐")
        print(f"│ {icon} {title:<73} │")
        print(f"└{'─'*76}┘{Style.RESET_ALL}\n")
    
    def print_success(self, message):
        """طباعة رسالة نجاح"""
        print(f"{self.colors['GREEN']}{Style.BRIGHT}✅ {message}{Style.RESET_ALL}")
    
    def print_error(self, message):
        """طباعة رسالة خطأ"""
        print(f"{self.colors['RED']}{Style.BRIGHT}❌ {message}{Style.RESET_ALL}")
    
    def print_warning(self, message):
        """طباعة تحذير"""
        print(f"{self.colors['YELLOW']}{Style.BRIGHT}⚠️  {message}{Style.RESET_ALL}")
    
    def print_info(self, message):
        """طباعة معلومات"""
        print(f"{self.colors['BLUE']}{Style.BRIGHT}ℹ️  {message}{Style.RESET_ALL}")
    
    def print_table(self, headers, data):
        """طباعة جدول منسق"""
        if not data:
            print(f"{self.colors['YELLOW']}لا توجد بيانات لعرضها{Style.RESET_ALL}")
            return
        
        # حساب عرض الأعمدة
        col_widths = [len(h) for h in headers]
        for row in data:
            for i, cell in enumerate(row):
                if i < len(col_widths):
                    col_widths[i] = max(col_widths[i], len(str(cell)))
        
        # طباعة الرأس
        print(f"\n{self.colors['CYAN']}{Style.BRIGHT}┌{'─'* (sum(col_widths) + 3*(len(headers)-1) + 2)}┐")
        header_line = "│ "
        for i, header in enumerate(headers):
            header_line += f"{header:<{col_widths[i]}} │ "
        print(header_line)
        print(f"├{'─'* (sum(col_widths) + 3*(len(headers)-1) + 2)}┤")
        
        # طباعة البيانات
        for row in data:
            line = "│ "
            for i, cell in enumerate(row):
                if i < len(col_widths):
                    line += f"{str(cell):<{col_widths[i]}} │ "
                else:
                    line += f"{str(cell)} │ "
            print(line)
        
        print(f"└{'─'* (sum(col_widths) + 3*(len(headers)-1) + 2)}┘{Style.RESET_ALL}\n")
    
    def get_system_info(self) -> Dict:
        """جمع معلومات النظام المتقدمة"""
        self.print_loading_animation("جمع معلومات النظام...", 1)
        self.print_header("معلومات النظام", "💻")
        
        boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        
        info = {
            "system": platform.system(),
            "node_name": platform.node(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "cpu_count": psutil.cpu_count(),
            "cpu_freq": psutil.cpu_freq().max if psutil.cpu_freq() else 0,
            "cpu_percent": psutil.cpu_percent(interval=1),
            "boot_time": boot_time,
            "uptime": str(datetime.now() - datetime.fromtimestamp(psutil.boot_time())),
            "memory": {
                "total": psutil.virtual_memory().total / (1024**3),
                "available": psutil.virtual_memory().available / (1024**3),
                "used": psutil.virtual_memory().used / (1024**3),
                "percent": psutil.virtual_memory().percent
            },
            "swap": {
                "total": psutil.swap_memory().total / (1024**3),
                "used": psutil.swap_memory().used / (1024**3),
                "percent": psutil.swap_memory().percent
            },
            "disk": {}
        }
        
        # معلومات الأقراص
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                info["disk"][partition.mountpoint] = {
                    "total": usage.total / (1024**3),
                    "used": usage.used / (1024**3),
                    "free": usage.free / (1024**3),
                    "percent": usage.percent
                }
            except:
                pass
        
        self.results["system_info"] = info
        
        # عرض المعلومات بشكل جميل
        print(f"{self.colors['GREEN']}{Style.BRIGHT}┌─────────────────────────────────────────────────────────────────────┐")
        print(f"│ {self.colors['CYAN']}{Style.BRIGHT}نظام التشغيل{self.colors['GREEN']}: {self.colors['WHITE']}{info['system']} {info['release']:<40} {self.colors['GREEN']}│")
        print(f"│ {self.colors['CYAN']}{Style.BRIGHT}اسم الجهاز{self.colors['GREEN']}: {self.colors['WHITE']}{info['node_name']:<55} {self.colors['GREEN']}│")
        print(f"│ {self.colors['CYAN']}{Style.BRIGHT}المعالج{self.colors['GREEN']}: {self.colors['WHITE']}{info['processor'][:55]:<55} {self.colors['GREEN']}│")
        print(f"│ {self.colors['CYAN']}{Style.BRIGHT}استخدام المعالج{self.colors['GREEN']}: {self.colors['WHITE']}{info['cpu_percent']}% {'█' * int(info['cpu_percent']/2):<50} {self.colors['GREEN']}│")
        print(f"│ {self.colors['CYAN']}{Style.BRIGHT}الذاكرة{self.colors['GREEN']}: {self.colors['WHITE']}{info['memory']['used']:.1f}/{info['memory']['total']:.1f} GB ({info['memory']['percent']}%){' ' * 10} {self.colors['GREEN']}│")
        print(f"│ {self.colors['CYAN']}{Style.BRIGHT}وقت التشغيل{self.colors['GREEN']}: {self.colors['WHITE']}{info['uptime']:<55} {self.colors['GREEN']}│")
        print(f"└─────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}\n")
        
        return info
    
    def get_background_processes(self) -> List[Dict]:
        """كشف التطبيقات التي تعمل في الخلفية بشكل متقدم"""
        self.print_loading_animation("فحص العمليات الخلفية...", 1.5)
        self.print_header("العمليات الخلفية", "🔄")
        
        processes = []
        suspicious_keywords = ['malware', 'virus', 'trojan', 'keylog', 'spy', 'hidden', 'unknown', 
                              'miner', 'crypt', 'backdoor', 'rootkit', 'exploit', 'payload']
        
        # إحصائيات
        total_cpu = 0
        total_memory = 0
        suspicious_count = 0
        
        for proc in psutil.process_iter(['pid', 'name', 'status', 'cpu_percent', 'memory_percent', 'create_time', 'connections', 'exe']):
            try:
                pinfo = proc.info
                if pinfo['cpu_percent'] and pinfo['memory_percent']:
                    total_cpu += pinfo['cpu_percent']
                    total_memory += pinfo['memory_percent']
                
                is_suspicious = any(keyword in pinfo['name'].lower() for keyword in suspicious_keywords)
                
                # فحص إضافي للعمليات المشبوهة
                if is_suspicious:
                    suspicious_count += 1
                    self.results["security_alerts"].append(f"⚠️ عملية مشبوهة مكتشفة: {pinfo['name']} (PID: {pinfo['pid']})")
                
                # جلب الموقع
                exe_path = pinfo.get('exe', 'غير معروف')
                
                proc_data = {
                    "pid": pinfo['pid'],
                    "name": pinfo['name'],
                    "status": pinfo['status'],
                    "cpu_percent": round(pinfo['cpu_percent'] or 0, 1),
                    "memory_percent": round(pinfo['memory_percent'] or 0, 1),
                    "create_time": datetime.fromtimestamp(pinfo['create_time']).strftime('%Y-%m-%d %H:%M:%S'),
                    "is_suspicious": is_suspicious,
                    "path": str(exe_path)[:50]
                }
                
                processes.append(proc_data)
                
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        
        self.results["background_processes"] = processes
        
        # عرض الإحصائيات
        print(f"{self.colors['YELLOW']}📊 إحصائيات العمليات:{Style.RESET_ALL}")
        print(f"   • إجمالي العمليات: {len(processes)}")
        print(f"   • العمليات المشبوهة: {suspicious_count}")
        print(f"   • إجمالي استخدام CPU: {total_cpu:.1f}%")
        print(f"   • إجمالي استخدام RAM: {total_memory:.1f}%")
        
        # عرض العمليات الأكثر استهلاكاً
        top_processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:10]
        
        if top_processes:
            print(f"\n{self.colors['CYAN']}🔥 العمليات الأكثر استهلاكاً للموارد:{Style.RESET_ALL}")
            headers = ["PID", "الاسم", "CPU%", "RAM%", "الحالة"]
            data = [[p['pid'], p['name'][:30], p['cpu_percent'], p['memory_percent'], p['status']] for p in top_processes]
            self.print_table(headers, data)
        
        return processes
    
    def scan_network_devices(self) -> List[Dict]:
        """كشف جميع الأجهزة على الشبكة بشكل متقدم"""
        self.print_loading_animation("مسح الشبكة وجمع معلومات الأجهزة...", 2)
        self.print_header("الأجهزة على الشبكة", "🌐")
        
        devices = []
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        network = '.'.join(local_ip.split('.')[:-1]) + '.1/24'
        
        print(f"{self.colors['BLUE']}البحث عن الأجهزة على الشبكة {network}...{Style.RESET_ALL}\n")
        
        try:
            arp_request = scapy.ARP(pdst=network)
            broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast / arp_request
            answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]
            
            for i, element in enumerate(answered_list, 1):
                device = {
                    "ip": element[1].psrc,
                    "mac": element[1].hwsrc,
                    "hostname": "",
                    "status": "🟢 متصل",
                    "vendor": self.get_mac_vendor(element[1].hwsrc),
                    "response_time": None
                }
                
                # قياس زمن الاستجابة
                try:
                    response_time = ping(device["ip"], timeout=1)
                    if response_time:
                        device["response_time"] = round(response_time * 1000, 2)
                except:
                    pass
                
                # الحصول على الاسم
                try:
                    device["hostname"] = socket.gethostbyaddr(device["ip"])[0]
                except:
                    device["hostname"] = "غير معروف"
                
                devices.append(device)
                
                # عرض النتائج بشكل مباشر
                status_color = self.colors['GREEN'] if device["response_time"] else self.colors['YELLOW']
                print(f"{status_color}{i:2}. {device['ip']:<15} | {device['hostname'][:30]:<30} | {device['mac']} | {device['vendor']}{Style.RESET_ALL}")
            
        except Exception as e:
            self.print_error(f"خطأ في مسح الشبكة: {e}")
        
        self.results["network_devices"] = devices
        self.print_success(f"تم اكتشاف {len(devices)} جهاز على الشبكة")
        
        return devices
    
    def get_mac_vendor(self, mac: str) -> str:
        """الحصول على اسم الشركة المصنعة من MAC address"""
        # قاعدة بيانات بسيطة للشركات المصنعة
        vendors = {
            "00:00:00": "Xerox",
            "00:01:02": "IBM",
            "00:03:93": "Apple",
            "00:05:02": "Cisco",
            "00:08:74": "Samsung",
            "00:0C:29": "VMware",
            "00:50:56": "VMware",
            "08:00:27": "Oracle/VirtualBox",
            "00:1A:11": "Google",
            "00:1B:63": "Intel",
            "00:1E:37": "Dell",
            "00:1F:29": "HP",
            "00:25:9C": "Huawei",
            "00:26:82": "Microsoft",
            "00:1C:42": "Intel",
            "B8:27:EB": "Raspberry Pi",
            "DC:A6:32": "Raspberry Pi",
        }
        
        prefix = mac[:8].upper()
        return vendors.get(prefix, "غير معروف")
    
    def analyze_ip(self, ip_address: str) -> Dict:
        """تحليل IP مفصل ومتقن"""
        self.print_loading_animation(f"تحليل {ip_address}...", 1.5)
        self.print_header(f"تحليل IP: {ip_address}", "🔍")
        
        analysis = {
            "ip": ip_address,
            "hostname": "",
            "geolocation": {},
            "whois_info": {},
            "dns_info": {},
            "open_ports": [],
            "is_vpn": False,
            "is_proxy": False,
            "is_tor": False,
            "is_datacenter": False,
            "risk_score": 0,
            "threat_level": "منخفض"
        }
        
        # الحصول على الاسم
        try:
            analysis["hostname"] = socket.gethostbyaddr(ip_address)[0]
            self.print_success(f"Hostname: {analysis['hostname']}")
        except:
            self.print_warning("لا يمكن الحصول على hostname")
        
        # معلومات الجغرافيا
        try:
            response = requests.get(f"http://ip-api.com/json/{ip_address}", timeout=5)
            if response.status_code == 200:
                geo_data = response.json()
                if geo_data.get('status') == 'success':
                    analysis["geolocation"] = {
                        "country": geo_data.get('country', 'N/A'),
                        "country_code": geo_data.get('countryCode', 'N/A'),
                        "city": geo_data.get('city', 'N/A'),
                        "region": geo_data.get('regionName', 'N/A'),
                        "latitude": geo_data.get('lat', 'N/A'),
                        "longitude": geo_data.get('lon', 'N/A'),
                        "isp": geo_data.get('isp', 'N/A'),
                        "organization": geo_data.get('org', 'N/A'),
                        "as": geo_data.get('as', 'N/A')
                    }
                    
                    # عرض الموقع
                    print(f"\n{self.colors['CYAN']}📍 معلومات الموقع:{Style.RESET_ALL}")
                    print(f"   • البلد: {analysis['geolocation']['country']} ({analysis['geolocation']['country_code']})")
                    print(f"   • المدينة: {analysis['geolocation']['city']}, {analysis['geolocation']['region']}")
                    print(f"   • مزود الخدمة: {analysis['geolocation']['isp']}")
                    print(f"   • التنظيم: {analysis['geolocation']['organization']}")
            else:
                self.print_warning("لا يمكن الحصول على معلومات الموقع")
        except:
            self.print_error("خطأ في الاتصال بخدمة الموقع")
        
        # فحص البورتات المفتوحة
        common_ports = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
            80: "HTTP", 110: "POP3", 135: "RPC", 139: "NetBIOS", 143: "IMAP",
            443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S", 1433: "MSSQL",
            3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 5900: "VNC", 8080: "HTTP-Alt"
        }
        
        print(f"\n{self.colors['CYAN']}🔍 فحص البورتات المفتوحة...{Style.RESET_ALL}")
        open_ports = []
        
        for port, service in common_ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append({"port": port, "service": service})
                print(f"   {self.colors['GREEN']}✅ بورت {port} مفتوح - {service}{Style.RESET_ALL}")
            sock.close()
        
        analysis["open_ports"] = open_ports
        
        # تقييم المخاطر
        risk_score = 0
        if len(open_ports) > 10:
            risk_score += 30
        
        # فحص إذا كان IP من数据中心
        datacenter_keywords = ['aws', 'azure', 'google', 'digitalocean', 'linode', 'vultr', 'ovh', 'hetzner']
        org_lower = analysis["geolocation"].get("organization", "").lower()
        if any(keyword in org_lower for keyword in datacenter_keywords):
            analysis["is_datacenter"] = True
            risk_score += 15
        
        if risk_score >= 50:
            analysis["threat_level"] = "عالي"
        elif risk_score >= 25:
            analysis["threat_level"] = "متوسط"
        else:
            analysis["threat_level"] = "منخفض"
        
        analysis["risk_score"] = risk_score
        
        # عرض تقييم المخاطر
        print(f"\n{self.colors['YELLOW']}⚠️  تقييم المخاطر:{Style.RESET_ALL}")
        threat_color = self.colors['GREEN'] if risk_score < 25 else (self.colors['YELLOW'] if risk_score < 50 else self.colors['RED'])
        print(f"   • مستوى التهديد: {threat_color}{analysis['threat_level']}{Style.RESET_ALL}")
        print(f"   • درجة المخاطرة: {risk_score}/100")
        
        self.results["ip_analysis"][ip_address] = analysis
        return analysis
    
    def scan_open_ports(self, target_ip: str, start_port: int = 1, end_port: int = 1000) -> List[int]:
        """مسح البورتات المفتوحة بشكل متقدم"""
        self.print_header(f"مسح البورتات: {target_ip}", "🔌")
        print(f"{self.colors['BLUE']}جاري مسح البورتات من {start_port} إلى {end_port}...{Style.RESET_ALL}\n")
        
        open_ports = []
        found_services = []
        
        common_services = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
            80: "HTTP", 110: "POP3", 111: "RPC", 135: "RPC", 139: "NetBIOS",
            143: "IMAP", 443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S",
            1080: "SOCKS", 1433: "MSSQL", 1723: "PPTP", 3306: "MySQL",
            3389: "RDP", 5432: "PostgreSQL", 5900: "VNC", 6379: "Redis",
            8080: "HTTP-Alt", 8443: "HTTPS-Alt", 27017: "MongoDB"
        }
        
        def scan_port(port):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.2)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                service = common_services.get(port, "غير معروف")
                open_ports.append(port)
                found_services.append({"port": port, "service": service})
                print(f"   {self.colors['GREEN']}✅ بورت {port:<5} - {service}{Style.RESET_ALL}")
            sock.close()
        
        threads = []
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=scan_port, args=(port,))
            threads.append(thread)
            thread.start()
            
            if len(threads) >= 100:
                for t in threads:
                    t.join()
                threads = []
        
        for t in threads:
            t.join()
        
        self.results["open_ports"] = found_services
        
        # عرض الخلاصة
        print(f"\n{self.colors['CYAN']}{'='*60}{Style.RESET_ALL}")
        self.print_success(f"تم العثور على {len(open_ports)} بورت مفتوح")
        
        if found_services:
            print(f"\n{self.colors['YELLOW']}📋 قائمة البورتات المفتوحة:{Style.RESET_ALL}")
            headers = ["البورت", "الخدمة", "الخطر"]
            data = [[p["port"], p["service"], self.get_port_risk(p["port"])] for p in found_services]
            self.print_table(headers, data)
        
        return open_ports
    
    def get_port_risk(self, port: int) -> str:
        """تحديد مستوى الخطر للبورت"""
        high_risk = [23, 135, 139, 445, 1433, 3306, 3389, 5900]
        medium_risk = [21, 25, 110, 143, 993, 995, 5432]
        
        if port in high_risk:
            return "🔴 عالي"
        elif port in medium_risk:
            return "🟡 متوسط"
        else:
            return "🟢 منخفض"
    
    def monitor_network_traffic(self, duration: int = 10):
        """مراقبة حركة الشبكة بشكل متقدم"""
        self.print_loading_animation("مراقبة حركة الشبكة...", 1)
        self.print_header("مراقبة الشبكة", "📡")
        
        print(f"{self.colors['BLUE']}مراقبة حركة الشبكة لمدة {duration} ثانية...{Style.RESET_ALL}\n")
        
        # عرض أنيميشن أثناء المراقبة
        old_stats = psutil.net_io_counters()
        
        for i in range(duration):
            sys.stdout.write(f"\r{self.colors['CYAN']}⏳ متبقي {duration - i} ثانية {'█' * i}{'░' * (duration - i)} {i*10}%{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(1)
        
        sys.stdout.write("\n")
        new_stats = psutil.net_io_counters()
        
        traffic = {
            "bytes_sent": new_stats.bytes_sent - old_stats.bytes_sent,
            "bytes_recv": new_stats.bytes_recv - old_stats.bytes_recv,
            "packets_sent": new_stats.packets_sent - old_stats.packets_sent,
            "packets_recv": new_stats.packets_recv - old_stats.packets_recv,
            "errin": new_stats.errin - old_stats.errin,
            "errout": new_stats.errout - old_stats.errout,
            "duration": duration
        }
        
        # عرض النتائج
        print(f"\n{self.colors['GREEN']}{'='*60}{Style.RESET_ALL}")
        print(f"{self.colors['CYAN']}{Style.BRIGHT}📊 إحصائيات حركة الشبكة:{Style.RESET_ALL}")
        print(f"   • البيانات المرسلة: {traffic['bytes_sent'] / 1024:.2f} KB ({traffic['packets_sent']} حزمة)")
        print(f"   • البيانات المستقبلة: {traffic['bytes_recv'] / 1024:.2f} KB ({traffic['packets_recv']} حزمة)")
        print(f"   • السرعة الإجمالية: {(traffic['bytes_sent'] + traffic['bytes_recv']) / (duration * 1024):.2f} KB/s")
        
        if traffic['errin'] > 0 or traffic['errout'] > 0:
            self.print_warning(f"تم اكتشاف {traffic['errin']} خطأ في الاستقبال و {traffic['errout']} خطأ في الإرسال")
        
        self.results["network_traffic"] = traffic
        return traffic
    
    def detect_intrusions(self) -> List[Dict]:
        """كشف الاختراقات والتهديدات المتقدمة"""
        self.print_loading_animation("فحص الاختراقات والتهديدات...", 1.5)
        self.print_header("كشف الاختراقات", "🚨")
        
        intrusions = []
        
        # 1. فحص الاتصالات الخارجية المشبوهة
        suspicious_ports = {4444: "Metasploit", 1337: "Misc", 31337: "Back Orifice", 6667: "IRC Bot", 12345: "NetBus", 54321: "PCAnywhere"}
        
        print(f"{self.colors['BLUE']}فحص الاتصالات المشبوهة...{Style.RESET_ALL}")
        for conn in psutil.net_connections(kind='inet'):
            if conn.status == 'ESTABLISHED' and conn.raddr:
                if conn.raddr.port in suspicious_ports:
                    intrusion = {
                        "type": "اتصال بميناء خلفي",
                        "tool": suspicious_ports[conn.raddr.port],
                        "local_port": conn.laddr.port,
                        "remote_ip": conn.raddr.ip,
                        "remote_port": conn.raddr.port,
                        "pid": conn.pid,
                        "severity": "عالي"
                    }
                    intrusions.append(intrusion)
                    self.print_warning(f"تم اكتشاف اتصال بميناء خلفي: {conn.raddr.ip}:{conn.raddr.port} ({suspicious_ports[conn.raddr.port]})")
        
        # 2. فحص العمليات ذات الاستهلاك العالي للموارد
        print(f"{self.colors['BLUE']}فحص العمليات المشبوهة...{Style.RESET_ALL}")
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'connections']):
            try:
                cpu = proc.info['cpu_percent'] or 0
                mem = proc.info['memory_percent'] or 0
                
                if cpu > 80 and mem > 30:
                    intrusion = {
                        "type": "استهلاك مفرط للموارد",
                        "pid": proc.info['pid'],
                        "name": proc.info['name'],
                        "cpu_percent": cpu,
                        "memory_percent": mem,
                        "severity": "متوسط"
                    }
                    intrusions.append(intrusion)
                    self.print_warning(f"عملية {proc.info['name']} (PID: {proc.info['pid']}) تستهلك {cpu}% CPU و {mem}% RAM")
            except:
                pass
        
        # 3. فحص البورتات المفتوحة الخطيرة
        print(f"{self.colors['BLUE']}فحص البورتات المفتوحة الخطيرة...{Style.RESET_ALL}")
        dangerous_ports = [23, 135, 139, 445, 1433, 3389, 5900]
        for port in dangerous_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.3)
            result = sock.connect_ex(('127.0.0.1', port))
            if result == 0:
                intrusion = {
                    "type": "بورت خطير مفتوح",
                    "port": port,
                    "severity": "عالي"
                }
                intrusions.append(intrusion)
                self.print_error(f"بورت {port} مفتوح - هذا يشكل خطراً أمنياً!")
            sock.close()
        
        self.results["intrusions"] = intrusions
        
        # عرض الخلاصة
        print(f"\n{self.colors['CYAN']}{'='*60}{Style.RESET_ALL}")
        if intrusions:
            self.print_error(f"تم اكتشاف {len(intrusions)} اختراق/تهديد!")
            for i, intrusion in enumerate(intrusions, 1):
                print(f"\n{self.colors['RED']}{i}. {intrusion['type']}{Style.RESET_ALL}")
                for key, value in intrusion.items():
                    if key != 'type':
                        print(f"   • {key}: {value}")
        else:
            self.print_success("لم يتم اكتشاف أي اختراقات!")
        
        return intrusions
    
    def generate_security_report(self) -> str:
        """توليد تقرير أمني شامل ومتقن"""
        self.print_loading_animation("إنشاء التقرير الأمني...", 1)
        
        report_lines = []
        report_lines.append(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         M3l - تقرير الأمن الشامل                              ║
║                         Security Audit Report                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

📊 معلومات التقرير:
   • رقم التقرير: {self.results['scan_id']}
   • تاريخ الفحص: {self.results['scan_time']}
   • وقت الفحص: {datetime.now().strftime('%H:%M:%S')}
   • الأداة: M3l Security Suite v{self.version}
   • المطور: @JYI_L | @mo3lzo | @M3_7L0

{'='*80}

💻 معلومات النظام:
""")
        
        # معلومات النظام
        sys_info = self.results.get("system_info", {})
        report_lines.append(f"   • نظام التشغيل: {sys_info.get('system', 'N/A')} {sys_info.get('release', '')}")
        report_lines.append(f"   • اسم الجهاز: {sys_info.get('node_name', 'N/A')}")
        report_lines.append(f"   • المعالج: {sys_info.get('processor', 'N/A')[:50]}")
        report_lines.append(f"   • استخدام المعالج: {sys_info.get('cpu_percent', 0)}%")
        report_lines.append(f"   • الذاكرة المستخدمة: {sys_info.get('memory', {}).get('used', 0):.1f}/{sys_info.get('memory', {}).get('total', 0):.1f} GB ({sys_info.get('memory', {}).get('percent', 0)}%)")
        report_lines.append(f"   • وقت التشغيل: {sys_info.get('uptime', 'N/A')}")
        
        # العمليات
        processes = self.results.get("background_processes", [])
        suspicious_procs = [p for p in processes if p.get('is_suspicious', False)]
        
        report_lines.append(f"""
{'='*80}

🔄 العمليات الخلفية:
   • إجمالي العمليات: {len(processes)}
   • العمليات المشبوهة: {len(suspicious_procs)}
""")
        
        if suspicious_procs:
            report_lines.append("   ⚠️ العمليات المشبوهة المكتشفة:")
            for proc in suspicious_procs[:10]:
                report_lines.append(f"      • {proc['name']} (PID: {proc['pid']}) - CPU: {proc['cpu_percent']}% - RAM: {proc['memory_percent']}%")
        
        # الأجهزة على الشبكة
        devices = self.results.get("network_devices", [])
        report_lines.append(f"""
{'='*80}

🌐 الأجهزة على الشبكة:
   • إجمالي الأجهزة المكتشفة: {len(devices)}
""")
        
        if devices:
            report_lines.append("   قائمة الأجهزة:")
            for device in devices:
                report_lines.append(f"      • {device['ip']} - {device['hostname']} ({device['mac']}) - {device.get('vendor', 'N/A')}")
        
        # البورتات المفتوحة
        open_ports = self.results.get("open_ports", [])
        report_lines.append(f"""
{'='*80}

🔌 البورتات المفتوحة:
   • عدد البورتات المفتوحة: {len(open_ports)}
""")
        
        if open_ports:
            report_lines.append("   قائمة البورتات المفتوحة:")
            for port in open_ports:
                if isinstance(port, dict):
                    report_lines.append(f"      • البورت {port.get('port')}: {port.get('service')} (الخطر: {self.get_port_risk(port.get('port', 0))})")
                else:
                    report_lines.append(f"      • بورت {port}")
        
        # الاختراقات
        intrusions = self.results.get("intrusions", [])
        report_lines.append(f"""
{'='*80}

🚨 تقرير الاختراقات والتهديدات:
""")
        
        if intrusions:
            report_lines.append(f"   ⚠️ تم اكتشاف {len(intrusions)} تهديد أمني!")
            for intrusion in intrusions:
                report_lines.append(f"      • {intrusion.get('type', 'غير معروف')} - الخطورة: {intrusion.get('severity', 'غير محدد')}")
        else:
            report_lines.append("   ✅ لم يتم اكتشاف أي اختراقات أمنية")
        
        # حركة الشبكة
        traffic = self.results.get("network_traffic", {})
        if traffic:
            report_lines.append(f"""
{'='*80}

📡 حركة الشبكة (آخر {traffic.get('duration', 10)} ثانية):
   • البيانات المرسلة: {traffic.get('bytes_sent', 0) / 1024:.2f} KB
   • البيانات المستقبلة: {traffic.get('bytes_recv', 0) / 1024:.2f} KB
   • سرعة النقل: {(traffic.get('bytes_sent', 0) + traffic.get('bytes_recv', 0)) / (traffic.get('duration', 10) * 1024):.2f} KB/s
""")
        
        # التوصيات الأمنية
        report_lines.append(f"""
{'='*80}

🛡️ التوصيات الأمنية:
   1. 🔒 قم بتحديث نظام التشغيل والبرامج بانتظام
   2. 🛡️ استخدم جدار حماية قوي
   3. 🔐 أغلق البورتات غير الضرورية
   4. 📊 راجع العمليات الخلفية بشكل دوري
   5. 🌐 استخدم VPN عند الاتصال بشبكات عامة
   6. 🔑 غير كلمات المرور الافتراضية
   7. 📝 احتفظ بنسخ احتياطية للبيانات المهمة

{'='*80}

📞 معلومات الاتصال بالمطور:
   • Telegram: {self.telegram}
   • Instagram: {self.instagram}
   • YouTube: {self.youtube}

⭐ شكراً لاستخدامك M3l Security Suite
🔒 حماية متكاملة - أداء متميز

توليد بواسطة M3L Security Team | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*80}
""")
        
        # حفظ التقرير
        filename = f"M3l_Security_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report_lines))
        
        self.print_success(f"تم حفظ التقرير في {filename}")
        return '\n'.join(report_lines)
    
    def display_results_summary(self):
        """عرض خلاصة النتائج بشكل جميل"""
        print(f"\n{self.colors['CYAN']}{Style.BRIGHT}{'='*80}{Style.RESET_ALL}")
        print(f"{self.colors['GREEN']}{Style.BRIGHT}🎯 خلاصة الفحص:{Style.RESET_ALL}")
        print(f"{self.colors['CYAN']}{'='*80}{Style.RESET_ALL}")
        
        # إحصائيات سريعة
        print(f"   • عدد العمليات: {len(self.results.get('background_processes', []))}")
        print(f"   • عدد الأجهزة على الشبكة: {len(self.results.get('network_devices', []))}")
        print(f"   • عدد البورتات المفتوحة: {len(self.results.get('open_ports', []))}")
        print(f"   • عدد التنبيهات الأمنية: {len(self.results.get('security_alerts', []))}")
        print(f"   • عدد الاختراقات المكتشفة: {len(self.results.get('intrusions', []))}")
        
        # حالة الأمان
        if len(self.results.get('intrusions', [])) > 0:
            print(f"\n   {self.colors['RED']}🔴 حالة النظام: غير آمن - توجد اختراقات مكتشفة!{Style.RESET_ALL}")
        elif len(self.results.get('security_alerts', [])) > 0:
            print(f"\n   {self.colors['YELLOW']}🟡 حالة النظام: معرض للخطر - توجد تنبيهات أمنية{Style.RESET_ALL}")
        else:
            print(f"\n   {self.colors['GREEN']}🟢 حالة النظام: آمن - لا توجد تهديدات مكتشفة{Style.RESET_ALL}")
        
        print(f"{self.colors['CYAN']}{'='*80}{Style.RESET_ALL}\n")
    
    def run_full_scan(self, target_ip: str = None):
        """تشغيل الفحص الكامل المتقدم"""
        self.print_banner()
        
        if not target_ip:
            target_ip = socket.gethostbyname(socket.gethostname())
        
        print(f"{self.colors['MAGENTA']}{Style.BRIGHT}{'░'*80}")
        print(f"{self.colors['WHITE']}{Style.BRIGHT}🚀 بدء الفحص الشامل للنظام والشبكة".center(80))
        print(f"📡 الجهاز المستهدف: {target_ip}".center(80))
        print(f"🔒 مستوى الأمان: متقدم".center(80))
        print(f"{'░'*80}{Style.RESET_ALL}\n")
        
        start_time = time.time()
        
        # تنفيذ جميع الفحوصات
        self.get_system_info()
        self.get_background_processes()
        self.scan_network_devices()
        self.scan_open_ports(target_ip, 1, 500)
        self.analyze_ip(target_ip)
        self.detect_intrusions()
        self.monitor_network_traffic(5)
        
        elapsed_time = time.time() - start_time
        
        print(f"\n{self.colors['GREEN']}{Style.BRIGHT}{'='*80}")
        print(f"✅ اكتمل الفحص في {elapsed_time:.2f} ثانية")
        print(f"{'='*80}{Style.RESET_ALL}")
        
        self.display_results_summary()
        self.generate_security_report()
        
        return self.results
    
    def interactive_menu(self):
        """قائمة تفاعلية متطورة"""
        while True:
            self.print_banner()
            
            # عرض الإحصائيات السريعة
            print(f"{self.colors['YELLOW']}{Style.BRIGHT}┌──────────────────────────────────────────────────────────────────────┐")
            print(f"│  📊 الإحصائيات السريعة:                                                  │")
            print(f"│  • آخر فحص: {self.results['scan_time'] if self.results.get('scan_time') else 'لم يتم بعد'}                              │")
            print(f"│  • عدد العمليات: {len(self.results.get('background_processes', [])):<3}  |  الأجهزة: {len(self.results.get('network_devices', [])):<3}  |  البورتات: {len(self.results.get('open_ports', [])):<3}  │")
            print(f"│  • الاختراقات: {len(self.results.get('intrusions', [])):<3}  |  التنبيهات: {len(self.results.get('security_alerts', [])):<3}                              │")
            print(f"└──────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}\n")
            
            menu_options = [
                ("1", "🔒", "فحص كامل للنظام والشبكة", "Full System Scan"),
                ("2", "🌐", "كشف الأجهزة على الشبكة", "Network Discovery"),
                ("3", "🔄", "عرض العمليات الخلفية", "Process Monitor"),
                ("4", "🔌", "مسح البورتات المفتوحة", "Port Scanner"),
                ("5", "🔍", "تحليل IP مفصل", "IP Analysis"),
                ("6", "🚨", "كشف الاختراقات", "Intrusion Detection"),
                ("7", "📡", "مراقبة حركة الشبكة", "Traffic Monitor"),
                ("8", "📊", "عرض التقرير الأخير", "View Report"),
                ("9", "💾", "حفظ النتائج كـ JSON", "Export Results"),
                ("0", "🚪", "الخروج من الأداة", "Exit")
            ]
            
            print(f"{self.colors['CYAN']}{Style.BRIGHT}┌──────────────────────────────────────────────────────────────────────┐")
            print(f"│  🎯 القائمة الرئيسية - اختر الخيار المناسب:                               │")
            
            for opt_num, opt_icon, opt_ar, opt_en in menu_options:
                print(f"│  {self.colors['GREEN']}{opt_icon} {opt_num}. {opt_ar:<30} {self.colors['DIM']}{opt_en:<30}{self.colors['CYAN']}│")
            
            print(f"│{self.colors['YELLOW']}  {'─'*68}{self.colors['CYAN']}│")
            print(f"│  💡 نصيحة: استخدم الخيار 1 للحصول على فحص كامل متكامل                     │")
            print(f"└──────────────────────────────────────────────────────────────────────┘{Style.RESET_ALL}")
            
            choice = input(f"\n{self.colors['GREEN']}{Style.BRIGHT}➤ اختر خيار (0-9): {Style.RESET_ALL}").strip()
            
            if choice == '1':
                target = input(f"{self.colors['YELLOW']}أدخل عنوان IP للفحص (Enter للمحلي): {Style.RESET_ALL}")
                self.run_full_scan(target if target else None)
                input(f"\n{self.colors['CYAN']}اضغط Enter للمتابعة...{Style.RESET_ALL}")
            
            elif choice == '2':
                devices = self.scan_network_devices()
                input(f"\n{self.colors['CYAN']}اضغط Enter للمتابعة...{Style.RESET_ALL}")
            
            elif choice == '3':
                processes = self.get_background_processes()
                input(f"\n{self.colors['CYAN']}اضغط Enter للمتابعة...{Style.RESET_ALL}")
            
            elif choice == '4':
                target = input(f"{self.colors['YELLOW']}أدخل عنوان IP: {Style.RESET_ALL}")
                start = int(input(f"{self.colors['YELLOW']}بداية البورتات (1): {Style.RESET_ALL}") or 1)
                end = int(input(f"{self.colors['YELLOW']}نهاية البورتات (1000): {Style.RESET_ALL}") or 1000)
                self.scan_open_ports(target, start, end)
                input(f"\n{self.colors['CYAN']}اضغط Enter للمتابعة...{Style.RESET_ALL}")
            
            elif choice == '5':
                ip = input(f"{self.colors['YELLOW']}أدخل عنوان IP للتحليل: {Style.RESET_ALL}")
                self.analyze_ip(ip)
                input(f"\n{self.colors['CYAN']}اضغط Enter للمتابعة...{Style.RESET_ALL}")
            
            elif choice == '6':
                self.detect_intrusions()
                input(f"\n{self.colors['CYAN']}اضغط Enter للمتابعة...{Style.RESET_ALL}")
            
            elif choice == '7':
                duration = int(input(f"{self.colors['YELLOW']}مدة المراقبة بالثواني (10): {Style.RESET_ALL}") or 10)
                self.monitor_network_traffic(duration)
                input(f"\n{self.colors['CYAN']}اضغط Enter للمتابعة...{Style.RESET_ALL}")
            
            elif choice == '8':
                report = self.generate_security_report()
                print(f"\n{self.colors['GREEN']}{report}{Style.RESET_ALL}")
                input(f"\n{self.colors['CYAN']}اضغط Enter للمتابعة...{Style.RESET_ALL}")
            
            elif choice == '9':
                filename = f"M3l_Security_Data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(self.results, f, indent=2, ensure_ascii=False, default=str)
                self.print_success(f"تم حفظ البيانات في {filename}")
                input(f"\n{self.colors['CYAN']}اضغط Enter للمتابعة...{Style.RESET_ALL}")
            
            elif choice == '0':
                print(f"\n{self.colors['YELLOW']}{Style.BRIGHT}")
                print("╔══════════════════════════════════════════════════════════════════════════════╗")
                print("║                         شكراً لاستخدامك M3l Security Suite                   ║")
                print("║                         حماية متكاملة - أداء متميز                           ║")
                print("║                                                                              ║")
                print("║  📱 تابعنا للمزيد:                                                          ║")
                print("║     Telegram: @JYI_L                                                         ║")
                print("║     Instagram: @mo3lzo                                                       ║")
                print("║     YouTube: @M3_7L0                                                         ║")
                print("╚══════════════════════════════════════════════════════════════════════════════╝")
                print(f"{Style.RESET_ALL}")
                break
            
            else:
                self.print_error("خيار غير صحيح! يرجى الاختيار من 0 إلى 9")
                time.sleep(1)
            
            # مسح الشاشة
            if choice != '0':
                os.system('cls' if platform.system() == 'Windows' else 'clear')

def main():
    """الدالة الرئيسية"""
    # التحقق من الصلاحيات
    if platform.system() != 'Windows' and os.geteuid() != 0:
        print("\033[93m⚠️ يرجى تشغيل الأداة بصلاحيات المدير (sudo) للحصول على نتائج دقيقة\033[0m")
        response = input("\033[96mهل تريد المتابعة مع صلاحيات محدودة؟ (y/n): \033[0m")
        if response.lower() != 'y':
            sys.exit(1)
    
    # إنشاء وتشغيل الأداة
    tool = M3lSecurity()
    
    try:
        tool.interactive_menu()
    except KeyboardInterrupt:
        print(f"\n\n{tool.colors['YELLOW']}⚠️ تم إيقاف الأداة بواسطة المستخدم{tool.colors['RESET']}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{tool.colors['RED']}❌ خطأ غير متوقع: {e}{tool.colors['RESET']}")
        sys.exit(1)

if __name__ == "__main__":
    main()