#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         M3l - NetGuard Security Suite                         ║
║                       Advanced Network & System Protection                    ║
║                              Version 6.0 - Ultimate                           ║
╚══════════════════════════════════════════════════════════════════════════════╝

مصنع بحبكم - من مطوركم M3L
📱 Telegram: @JYI_L
📸 Instagram: @mo3lzo
🎥 YouTube: @M3_7L0
🐙 GitHub: https://github.com/M3lO23S

أداة سيبرانية متكاملة - شغالة على طول من غير تعقيد
"""

import sys
import os
import platform
import socket
import threading
import time
from datetime import datetime
import json

# ==================== الجزء الأول: المكتبات المضمنة ====================
# احنا مش هنستخدم أي مكتبة خارجية - كل حاجة جاهزة في بايثون نفسها

# بنحاول نستورد المكتبات، لو مش موجودة نشتغل من غيرها
try:
    import subprocess
    HAS_SUBPROCESS = True
except:
    HAS_SUBPROCESS = False

try:
    import psutil
    HAS_PSUTIL = True
except:
    HAS_PSUTIL = False

try:
    import requests
    HAS_REQUESTS = True
except:
    HAS_REQUESTS = False


class M3lSecurity:
    def __init__(self):
        # بيانات المطور
        self.version = "6.0.0"
        self.author = "M3L Security Team"
        self.telegram = "@JYI_L"
        self.instagram = "@mo3lzo"
        self.youtube = "@M3_7L0"
        self.github = "https://github.com/M3lO23S"
        
        # متغيرات النظام
        self.os_type = platform.system()
        self.start_time = datetime.now()
        
        # الألوان (بتشتغل على كل الأنظمة)
        self.colors = {
            'RED': '\033[91m',
            'GREEN': '\033[92m',
            'YELLOW': '\033[93m',
            'BLUE': '\033[94m',
            'MAGENTA': '\033[95m',
            'CYAN': '\033[96m',
            'WHITE': '\033[97m',
            'RESET': '\033[0m',
            'BOLD': '\033[1m',
            'DIM': '\033[2m'
        }
        
        # لو ويندوز، الألوان بتشتغل برضه
        if self.os_type == 'Windows':
            os.system('color')
        
        # تخزين النتائج
        self.results = {
            "scan_id": str(int(time.time()))[-6:],
            "scan_time": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "system_info": {},
            "network_devices": [],
            "background_processes": [],
            "ip_analysis": {},
            "open_ports": [],
            "security_alerts": [],
            "intrusions": []
        }
        
        # قائمة بالأجهزة اللي اتكشفت
        self.discovered_devices = []
        
        # الأوامر المتاحة
        self.commands = {
            "help": "عرض قائمة الأوامر",
            "h": "عرض قائمة الأوامر",
            "full": "فحص كامل للنظام والشبكة",
            "f": "فحص كامل",
            "network": "كشف الأجهزة على الشبكة",
            "net": "كشف الأجهزة على الشبكة",
            "processes": "عرض العمليات الخلفية",
            "ps": "عرض العمليات الخلفية",
            "ports": "مسح البورتات - استخدم: ports <IP> <بداية> <نهاية>",
            "scan": "مسح البورتات - استخدم: scan <IP> <بداية> <نهاية>",
            "analyze": "تحليل IP - استخدم: analyze <IP>",
            "ip": "تحليل IP - استخدم: ip <IP>",
            "intrusions": "كشف الاختراقات",
            "hack": "كشف الاختراقات",
            "monitor": "مراقبة الشبكة - استخدم: monitor <ثواني>",
            "watch": "مراقبة الشبكة",
            "report": "عرض التقرير الأمني",
            "save": "حفظ التقرير",
            "clear": "مسح الشاشة",
            "cls": "مسح الشاشة",
            "exit": "الخروج من الأداة",
            "quit": "الخروج",
            "q": "الخروج"
        }

    # ==================== دوال العرض والواجهة ====================
    
    def print_banner(self):
        """شاشة الدخول الجميلة"""
        banner = f"""
{self.colors['CYAN']}{self.colors['BOLD']}╔{'═'*70}╗
║{self.colors['YELLOW']}{self.colors['BOLD']}                                                                  {self.colors['CYAN']}║
║{self.colors['RED']}{self.colors['BOLD']}   ███╗   ███╗████████╗██╗     ███████╗{self.colors['GREEN']}███████╗███████╗{self.colors['CYAN']}      ║
║{self.colors['RED']}{self.colors['BOLD']}   ████╗ ████║╚══██╔══╝██║     ██╔════╝{self.colors['GREEN']}██╔════╝██╔════╝{self.colors['CYAN']}      ║
║{self.colors['RED']}{self.colors['BOLD']}   ██╔████╔██║   ██║   ██║     █████╗  {self.colors['GREEN']}███████╗█████╗  {self.colors['CYAN']}      ║
║{self.colors['RED']}{self.colors['BOLD']}   ██║╚██╔╝██║   ██║   ██║     ██╔══╝  {self.colors['GREEN']}╚════██║██╔══╝  {self.colors['CYAN']}      ║
║{self.colors['RED']}{self.colors['BOLD']}   ██║ ╚═╝ ██║   ██║   ███████╗███████╗{self.colors['GREEN']}███████║███████╗{self.colors['CYAN']}      ║
║{self.colors['RED']}{self.colors['BOLD']}   ╚═╝     ╚═╝   ╚═╝   ╚══════╝╚══════╝{self.colors['GREEN']}╚══════╝╚══════╝{self.colors['CYAN']}      ║
║{self.colors['YELLOW']}{self.colors['BOLD']}                                                                  {self.colors['CYAN']}║
║{self.colors['MAGENTA']}{self.colors['BOLD']}              🛡️  M3l Security Suite v{self.version}  🛡️                      {self.colors['CYAN']}║
║{self.colors['CYAN']}{self.colors['BOLD']}╠{'═'*70}╣
║{self.colors['GREEN']}  📱 Telegram:{self.colors['YELLOW']} {self.telegram:<25} {self.colors['MAGENTA']}📸 Instagram:{self.colors['YELLOW']} {self.instagram:<15}  {self.colors['CYAN']}║
║{self.colors['GREEN']}  🎥 YouTube:{self.colors['YELLOW']} {self.youtube:<30} {self.colors['MAGENTA']}🐙 GitHub:{self.colors['YELLOW']} {self.github:<20}  {self.colors['CYAN']}║
║{self.colors['CYAN']}{self.colors['BOLD']}╚{'═'*70}╝{self.colors['RESET']}

{self.colors['YELLOW']}┌{'─'*68}┐
│  🔒 نظام حماية متكامل - شبكات، أنظمة، اختراقات                 │
│  ⚡ شغالة على طول - من غير تعقيد - من غير مكتبات برة            │
│  🚀 استخدم الأمر {self.colors['GREEN']}help{self.colors['YELLOW']} عشان تشوف كل الأوامر                         │
└{'─'*68}┘{self.colors['RESET']}
"""
        print(banner)

    def print_help(self):
        """عرض المساعدة والأوامر"""
        print(f"\n{self.colors['CYAN']}{self.colors['BOLD']}{'═'*68}{self.colors['RESET']}")
        print(f"{self.colors['GREEN']}{self.colors['BOLD']}📖 قائمة الأوامر المتاحة:{self.colors['RESET']}")
        print(f"{self.colors['CYAN']}{'═'*68}{self.colors['RESET']}")
        
        # تقسيم الأوامر لمجموعات
        main_commands = ['full', 'network', 'processes', 'ports', 'analyze', 'intrusions', 'monitor', 'report']
        system_commands = ['clear', 'help', 'save', 'exit']
        
        print(f"\n{self.colors['YELLOW']}🎯 الأوامر الرئيسية:{self.colors['RESET']}")
        for cmd in main_commands:
            if cmd in self.commands:
                print(f"  {self.colors['GREEN']}{cmd:<12}{self.colors['RESET']} - {self.commands[cmd]}")
        
        print(f"\n{self.colors['YELLOW']}⚙️  أوامر النظام:{self.colors['RESET']}")
        for cmd in system_commands:
            if cmd in self.commands:
                print(f"  {self.colors['GREEN']}{cmd:<12}{self.colors['RESET']} - {self.commands[cmd]}")
        
        print(f"\n{self.colors['CYAN']}{'═'*68}{self.colors['RESET']}")
        print(f"{self.colors['WHITE']}💡 مثال: {self.colors['GREEN']}ports 192.168.1.1 1 100{self.colors['RESET']}")
        print(f"{self.colors['WHITE']}💡 مثال: {self.colors['GREEN']}analyze 8.8.8.8{self.colors['RESET']}")
        print(f"{self.colors['WHITE']}💡 مثال: {self.colors['GREEN']}monitor 10{self.colors['RESET']}")
        print(f"{self.colors['CYAN']}{'═'*68}{self.colors['RESET']}\n")

    def print_success(self, msg):
        print(f"{self.colors['GREEN']}✅ {msg}{self.colors['RESET']}")
    
    def print_error(self, msg):
        print(f"{self.colors['RED']}❌ {msg}{self.colors['RESET']}")
    
    def print_warning(self, msg):
        print(f"{self.colors['YELLOW']}⚠️  {msg}{self.colors['RESET']}")
    
    def print_info(self, msg):
        print(f"{self.colors['BLUE']}ℹ️  {msg}{self.colors['RESET']}")
    
    def clear_screen(self):
        os.system('cls' if self.os_type == 'Windows' else 'clear')

    # ==================== دوال الفحص الأساسية ====================
    
    def get_system_info(self):
        """جمع معلومات النظام من غير psutil"""
        self.print_info("جمع معلومات النظام...")
        
        info = {
            "system": self.os_type,
            "node_name": socket.gethostname(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor() or "غير معروف"
        }
        
        # معلومات الرام والCPU باستخدام أوامر النظام
        if HAS_PSUTIL:
            info["cpu_count"] = psutil.cpu_count()
            info["cpu_percent"] = psutil.cpu_percent(interval=0.5)
            info["memory_total"] = round(psutil.virtual_memory().total / (1024**3), 2)
            info["memory_used"] = round(psutil.virtual_memory().used / (1024**3), 2)
            info["memory_percent"] = psutil.virtual_memory().percent
        else:
            info["cpu_count"] = os.cpu_count() or 1
            info["cpu_percent"] = "غير متاح"
            info["memory_total"] = "غير متاح"
            info["memory_used"] = "غير متاح"
            info["memory_percent"] = "غير متاح"
        
        self.results["system_info"] = info
        
        # عرض المعلومات
        print(f"\n{self.colors['GREEN']}{self.colors['BOLD']}┌{'─'*60}┐")
        print(f"│{self.colors['CYAN']} نظام التشغيل{self.colors['GREEN']}: {self.colors['WHITE']}{info['system']} {info['release']:<35} {self.colors['GREEN']}│")
        print(f"│{self.colors['CYAN']} اسم الجهاز{self.colors['GREEN']}: {self.colors['WHITE']}{info['node_name']:<50} {self.colors['GREEN']}│")
        print(f"│{self.colors['CYAN']} المعالج{self.colors['GREEN']}: {self.colors['WHITE']}{info['processor'][:50]:<50} {self.colors['GREEN']}│")
        print(f"│{self.colors['CYAN']} الرام{self.colors['GREEN']}: {self.colors['WHITE']}{info['memory_used']} / {info['memory_total']} GB ({info['memory_percent']}%){self.colors['GREEN']}│")
        print(f"└{'─'*60}┘{self.colors['RESET']}\n")
        
        return info

    def scan_network_devices(self):
        """كشف الأجهزة على الشبكة باستخدام ARP و ping"""
        self.print_info("بص بقى نشوف مين متصل معاك على الشبكة...")
        
        devices = []
        
        try:
            # جبنا الايبي بتاع الجهاز نفسه
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            ip_parts = local_ip.split('.')
            network_base = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}"
            
            print(f"{self.colors['YELLOW']}🔍 بدور على الأجهزة في النطاق {network_base}.1 - {network_base}.254{self.colors['RESET']}")
            
            # نجرب نستخدم ARP لو في لينكس، غير كذا نستخدم ping
            found = 0
            
            for i in range(1, 255):
                ip = f"{network_base}.{i}"
                # بنبعت ping للجهاز
                response = os.system(f"ping -n 1 -w 200 {ip} > nul 2>&1" if self.os_type == 'Windows' 
                                    else f"ping -c 1 -W 0.2 {ip} > /dev/null 2>&1")
                
                if response == 0:
                    try:
                        host = socket.gethostbyaddr(ip)[0]
                    except:
                        host = "غير معروف"
                    
                    device = {
                        "ip": ip,
                        "hostname": host,
                        "status": "متصل"
                    }
                    devices.append(device)
                    found += 1
                    print(f"{self.colors['GREEN']}  ✅ {ip} - {host}{self.colors['RESET']}")
                
                # عشان نعرف نسبة التقدم
                if i % 50 == 0:
                    print(f"{self.colors['BLUE']}  ⏳ فحص {i}/254 ...{self.colors['RESET']}")
            
            self.results["network_devices"] = devices
            self.discovered_devices = devices
            
            print(f"\n{self.colors['GREEN']}{self.colors['BOLD']}🎉 لقيت {found} جهاز على الشبكة!{self.colors['RESET']}\n")
            
        except Exception as e:
            self.print_error(f"حصلت مشكلة في المسح: {e}")
        
        return devices

    def scan_ports(self, target, start_port=1, end_port=500):
        """مسح البورتات المفتوحة"""
        self.print_info(f"بفتح بقى على {target} أشوف مين واقف على الباب...")
        
        open_ports = []
        
        # الخدمات المعروفة لكل بورت
        services = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
            80: "HTTP", 110: "POP3", 135: "RPC", 139: "NetBIOS", 143: "IMAP",
            443: "HTTPS", 445: "SMB", 993: "IMAPS", 995: "POP3S",
            3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 5900: "VNC", 8080: "HTTP-Alt"
        }
        
        for port in range(start_port, end_port + 1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.2)
                result = sock.connect_ex((target, port))
                if result == 0:
                    service = services.get(port, "غير معروف")
                    open_ports.append({"port": port, "service": service})
                    print(f"{self.colors['GREEN']}  ✅ بورت {port} مفتوح - {service}{self.colors['RESET']}")
                sock.close()
            except:
                pass
            
            # نبين التقدم كل 50 بورت
            if port % 50 == 0 and port > start_port:
                print(f"{self.colors['BLUE']}  ⏳ فحصت {port - start_port + 1} بورت لحد دلوقتي...{self.colors['RESET']}")
        
        self.results["open_ports"] = open_ports
        print(f"\n{self.colors['GREEN']}🎉 لقيت {len(open_ports)} بورت مفتوح!{self.colors['RESET']}\n")
        return open_ports

    def analyze_ip(self, ip_address):
        """تحليل عنوان IP"""
        self.print_info(f"هحلللك الـ IP ده: {ip_address}")
        
        analysis = {
            "ip": ip_address,
            "hostname": "",
            "location": {},
            "risk_level": "غير معروف"
        }
        
        # نجيب الاسم
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
            analysis["hostname"] = hostname
            self.print_success(f"الاسم: {hostname}")
        except:
            analysis["hostname"] = "مش معروف"
            self.print_warning("الاسم مش معروف")
        
        # نجيب معلومات الموقع (لو في نت)
        location_info = ""
        if HAS_REQUESTS:
            try:
                response = requests.get(f"http://ip-api.com/json/{ip_address}", timeout=3)
                if response.status_code == 200:
                    data = response.json()
                    if data.get('status') == 'success':
                        analysis["location"] = {
                            "country": data.get('country', 'N/A'),
                            "city": data.get('city', 'N/A'),
                            "isp": data.get('isp', 'N/A')
                        }
                        location_info = f"{data.get('city', '')}, {data.get('country', '')}"
                        print(f"{self.colors['GREEN']}  📍 الموقع: {location_info}{self.colors['RESET']}")
                        print(f"{self.colors['GREEN']}  📡 مزود الخدمة: {data.get('isp', 'N/A')}{self.colors['RESET']}")
            except:
                pass
        
        # بنحدد مستوى الخطر (تقدير سريع)
        risk = "منخفض"
        if ip_address.startswith(('10.', '172.16.', '192.168.')):
            risk = "آمن (شبكة داخلية)"
        elif analysis["hostname"] and any(x in analysis["hostname"].lower() for x in ['proxy', 'vpn', 'tor']):
            risk = "متوسط -可能有 proxy أو VPN"
        else:
            risk = "منخفض - عادي"
        
        analysis["risk_level"] = risk
        self.results["ip_analysis"][ip_address] = analysis
        
        print(f"\n{self.colors['YELLOW']}⚠️ مستوى الخطورة: {self.colors['WHITE']}{risk}{self.colors['RESET']}\n")
        
        return analysis

    def get_background_processes(self):
        """جلب العمليات الخلفية"""
        self.print_info("بشوف بقى مين شغال في الخلفية من غير ما تحس...")
        
        processes = []
        
        if HAS_PSUTIL:
            suspicious_keywords = ['malware', 'virus', 'trojan', 'keylog', 'spy', 'miner', 'crypt', 'hidden']
            
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
                try:
                    pinfo = proc.info
                    is_suspicious = any(kw in pinfo['name'].lower() for kw in suspicious_keywords)
                    
                    proc_data = {
                        "pid": pinfo['pid'],
                        "name": pinfo['name'],
                        "cpu": round(pinfo['cpu_percent'] or 0, 1),
                        "memory": round(pinfo['memory_percent'] or 0, 1),
                        "suspicious": is_suspicious
                    }
                    processes.append(proc_data)
                    
                    if is_suspicious:
                        print(f"{self.colors['RED']}  ⚠️ عملية مشبوهة: {pinfo['name']} (PID: {pinfo['pid']}){self.colors['RESET']}")
                except:
                    pass
            
            self.results["background_processes"] = processes
            
            # نعرض أهم العمليات
            print(f"\n{self.colors['CYAN']}📊 أهم العمليات من حيث الاستهلاك:{self.colors['RESET']}")
            top_cpu = sorted(processes, key=lambda x: x['cpu'], reverse=True)[:10]
            for p in top_cpu:
                color = self.colors['RED'] if p['suspicious'] else self.colors['WHITE']
                print(f"  {color}PID {p['pid']:<6} {p['name'][:25]:<25} CPU: {p['cpu']}%  RAM: {p['memory']}%{self.colors['RESET']}")
        
        else:
            self.print_warning("مكتبة psutil مش موجودة - هجيب العمليات بطريقة بسيطة")
            # طريقة بديلة باستخدام أوامر النظام
            if self.os_type == 'Windows':
                result = os.popen('tasklist').read()
                print(result[:500])
            else:
                result = os.popen('ps aux').read()
                print(result[:500])
        
        return processes

    def detect_intrusions(self):
        """كشف الاختراقات"""
        self.print_info("بفتش بقى لو في حد داخل عليك من وراك...")
        
        intrusions = []
        
        # بنفحص المنافذ الخطيرة
        dangerous_ports = [23, 135, 445, 1433, 3389, 4444, 5555, 6667, 1337, 31337]
        
        for port in dangerous_ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.2)
                result = sock.connect_ex(('127.0.0.1', port))
                if result == 0:
                    intrusions.append({
                        "type": "بورت خطر مفتوح",
                        "port": port,
                        "severity": "عالي"
                    })
                    self.print_error(f"بورت {port} مفتوح - ده خطيييير!")
                sock.close()
            except:
                pass
        
        # بنشوف لو في عمليات مشبوهة
        if HAS_PSUTIL:
            suspicious_names = ['nc.exe', 'ncat', 'meterpreter', 'shell', 'backdoor']
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    if proc.info['name'] and proc.info['name'].lower() in suspicious_names:
                        intrusions.append({
                            "type": "عملية مشبوهة",
                            "name": proc.info['name'],
                            "pid": proc.info['pid'],
                            "severity": "عالي"
                        })
                        self.print_error(f"عملية {proc.info['name']} شغالة - دي علامة خطر!")
                except:
                    pass
        
        # بنشوف الاتصالات الخارجية
        try:
            connections = []
            for conn in psutil.net_connections(kind='inet'):
                if conn.status == 'ESTABLISHED' and conn.raddr:
                    connections.append(conn.raddr.ip)
            
            if len(connections) > 20:
                self.print_warning(f"عندك {len(connections)} اتصال مفتوح - كتير شوية!")
        except:
            pass
        
        self.results["intrusions"] = intrusions
        
        if intrusions:
            print(f"\n{self.colors['RED']}{self.colors['BOLD']}🚨 تم اكتشاف {len(intrusions)} خطر أمني!{self.colors['RESET']}")
        else:
            self.print_success("الحمد لله مفيش اختراقات واضحة!")
        
        return intrusions

    def monitor_network(self, duration=10):
        """مراقبة الشبكة"""
        self.print_info(f"هتفرج على النت معاك لمدة {duration} ثانية...")
        
        # نجيب الإحصائيات الأولية
        if HAS_PSUTIL:
            old_stats = psutil.net_io_counters()
            
            for i in range(duration):
                time.sleep(1)
                percent = int((i + 1) / duration * 100)
                bar = '█' * (percent // 2) + '░' * (50 - (percent // 2))
                sys.stdout.write(f"\r{self.colors['BLUE']}⏳ مراقبة: [{bar}] {percent}%{self.colors['RESET']}")
                sys.stdout.flush()
            
            new_stats = psutil.net_io_counters()
            
            sent = (new_stats.bytes_sent - old_stats.bytes_sent) / 1024
            recv = (new_stats.bytes_recv - old_stats.bytes_recv) / 1024
            total_speed = (sent + recv) / duration
            
            print(f"\n\n{self.colors['GREEN']}{self.colors['BOLD']}📊 النتائج:{self.colors['RESET']}")
            print(f"  📤 بيانات مرسلة: {sent:.2f} KB")
            print(f"  📥 بيانات واردة: {recv:.2f} KB")
            print(f"  ⚡ السرعة: {total_speed:.2f} KB/s")
        else:
            self.print_error("مكتبة psutil مش موجودة عشان أراقب الشبكة")

    def generate_report(self):
        """توليد التقرير"""
        self.print_info("بجهزلك التقرير يا كبير...")
        
        report_lines = []
        report_lines.append(f"""
{'═'*60}
                    M3l - تقرير الأمن
{'═'*60}

📅 التاريخ: {self.results['scan_time']}
🔑 رقم الفحص: {self.results['scan_id']}

{'─'*40}
💻 معلومات الجهاز:
{'─'*40}""")
        
        for key, value in self.results.get('system_info', {}).items():
            report_lines.append(f"   • {key}: {value}")
        
        report_lines.append(f"\n{'─'*40}\n🌐 الأجهزة على الشبكة ({len(self.results.get('network_devices', []))}):\n{'─'*40}")
        for device in self.results.get('network_devices', [])[:20]:
            report_lines.append(f"   • {device['ip']} - {device['hostname']}")
        
        report_lines.append(f"\n{'─'*40}\n🔌 البورتات المفتوحة ({len(self.results.get('open_ports', []))}):\n{'─'*40}")
        for port in self.results.get('open_ports', [])[:20]:
            if isinstance(port, dict):
                report_lines.append(f"   • بورت {port['port']} - {port['service']}")
            else:
                report_lines.append(f"   • بورت {port}")
        
        report_lines.append(f"\n{'─'*40}\n🚨 الاختراقات المكتشفة ({len(self.results.get('intrusions', []))}):\n{'─'*40}")
        for intrusion in self.results.get('intrusions', []):
            report_lines.append(f"   • {intrusion.get('type', 'غير معروف')}")
        
        report_lines.append(f"""
{'─'*40}
👨‍💻 المطور:
   • Telegram: {self.telegram}
   • Instagram: {self.instagram}
   • YouTube: {self.youtube}
   • GitHub: {self.github}

{'═'*60}
                تم التقرير - خليك في أمان
{'═'*60}
""")
        
        # نحفظ التقرير
        filename = f"M3l_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report_lines))
        
        self.print_success(f"التقرير اتسحب في ملف: {filename}")
        print('\n'.join(report_lines))
        
        return report_lines

    # ==================== معالج الأوامر ====================
    
    def execute_command(self, command_line):
        """تنفيذ الأوامر"""
        parts = command_line.strip().split()
        if not parts:
            return
        
        cmd = parts[0].lower()
        
        # help
        if cmd in ['help', 'h']:
            self.print_help()
        
        # full scan
        elif cmd in ['full', 'f']:
            self.full_scan()
        
        # network scan
        elif cmd in ['network', 'net']:
            self.scan_network_devices()
        
        # processes
        elif cmd in ['processes', 'ps']:
            self.get_background_processes()
        
        # ports scan
        elif cmd in ['ports', 'scan']:
            if len(parts) >= 2:
                target = parts[1]
                start = int(parts[2]) if len(parts) > 2 else 1
                end = int(parts[3]) if len(parts) > 3 else 500
                self.scan_ports(target, start, end)
            else:
                self.print_error("استخدم: ports <IP> <بداية> <نهاية>")
        
        # analyze IP
        elif cmd in ['analyze', 'ip']:
            if len(parts) >= 2:
                self.analyze_ip(parts[1])
            else:
                self.print_error("استخدم: analyze <IP>")
        
        # intrusions
        elif cmd in ['intrusions', 'hack']:
            self.detect_intrusions()
        
        # monitor
        elif cmd in ['monitor', 'watch']:
            duration = int(parts[1]) if len(parts) > 1 else 10
            self.monitor_network(duration)
        
        # report
        elif cmd in ['report']:
            self.generate_report()
        
        # save
        elif cmd in ['save']:
            filename = f"M3l_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.results, f, indent=2, ensure_ascii=False, default=str)
            self.print_success(f"البيانات اتحفظت في {filename}")
        
        # clear
        elif cmd in ['clear', 'cls']:
            self.clear_screen()
            self.print_banner()
        
        # exit
        elif cmd in ['exit', 'quit', 'q']:
            print(f"\n{self.colors['YELLOW']}سلام عليكم - متنساش تتابع المطورين 😊{self.colors['RESET']}")
            return False
        
        # unknown command
        else:
            self.print_error(f"أمر {cmd} مش معروف - اكتب help عشان تشوف الأوامر")
        
        return True

    def full_scan(self):
        """الفحص الكامل"""
        self.print_banner()
        print(f"\n{self.colors['MAGENTA']}{self.colors['BOLD']}{'█'*68}")
        print(f"{self.colors['WHITE']}{self.colors['BOLD']}🚀 بدء الفحص الشامل...{' ' * 45}")
        print(f"{self.colors['MAGENTA']}{'█'*68}{self.colors['RESET']}\n")
        
        start = time.time()
        
        self.get_system_info()
        self.scan_network_devices()
        self.get_background_processes()
        self.detect_intrusions()
        
        # نجيب الايبي المحلي ونفحصه
        local_ip = socket.gethostbyname(socket.gethostname())
        self.scan_ports(local_ip, 1, 200)
        
        elapsed = time.time() - start
        
        print(f"\n{self.colors['GREEN']}{self.colors['BOLD']}{'═'*68}")
        print(f"✅ الفحص اكتمل في {elapsed:.2f} ثانية")
        print(f"📊 النتائج: {len(self.results['network_devices'])} جهاز | {len(self.results['open_ports'])} بورت | {len(self.results['intrusions'])} خطر")
        print(f"{'═'*68}{self.colors['RESET']}\n")
        
        self.generate_report()

    def interactive_mode(self):
        """الوضع التفاعلي - القيادة بالأوامر"""
        print(f"\n{self.colors['GREEN']}{self.colors['BOLD']}🎯 دخلت على وضع الأوامر! اكتب {self.colors['YELLOW']}help{self.colors['GREEN']} عشان تشوف كل حاجة{self.colors['RESET']}")
        print(f"{self.colors['DIM']}أمثلة: full, network, analyze 8.8.8.8, ports 192.168.1.1 1 100{self.colors['RESET']}\n")
        
        while True:
            try:
                cmd = input(f"{self.colors['CYAN']}M3l> {self.colors['RESET']}").strip()
                if not cmd:
                    continue
                
                if not self.execute_command(cmd):
                    break
                    
            except KeyboardInterrupt:
                print(f"\n{self.colors['YELLOW']}Ctrl+C - عايز تخرج؟ اكتب exit{self.colors['RESET']}")
            except Exception as e:
                self.print_error(f"حصلت مشكلة: {e}")


# ==================== الدالة الرئيسية ====================

def main():
    tool = M3lSecurity()
    tool.clear_screen()
    tool.print_banner()
    
    # شوف لو في أمر من سطر الأوامر
    if len(sys.argv) > 1:
        command = ' '.join(sys.argv[1:])
        tool.execute_command(command)
    else:
        # شغال الوضع التفاعلي
        tool.interactive_mode()


if __name__ == "__main__":
    main()
