import sqlite3
import random
from datetime import datetime, timedelta

def random_date(start, end):
    return (start + timedelta(days=random.randint(0, (end - start).days))).isoformat()

def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def random_mac():
    return ":".join(f"{random.randint(0, 255):02x}" for _ in range(6))

start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 1, 1)

conn = sqlite3.connect("sample.db")
cursor = conn.cursor()

# Table definitions (10 tables)
tables = {
    "system_info": """CREATE TABLE system_info (
        id INTEGER PRIMARY KEY, hostname TEXT, os_version TEXT, last_boot_time TEXT,
        ip_address TEXT, mac_address TEXT, manufacturer TEXT, model TEXT, system_type TEXT, serial_number TEXT);""",
    "installed_software": """CREATE TABLE installed_software (
        id INTEGER PRIMARY KEY, system_id INTEGER, software_name TEXT, version TEXT,
        install_date TEXT, vendor TEXT, license_key TEXT, install_path TEXT, size_mb REAL, category TEXT);""",
    "running_processes": """CREATE TABLE running_processes (
        id INTEGER PRIMARY KEY, system_id INTEGER, process_name TEXT, pid INTEGER,
        cpu_usage REAL, memory_usage REAL, start_time TEXT, user TEXT, path TEXT, status TEXT);""",
    "services": """CREATE TABLE services (
        id INTEGER PRIMARY KEY, system_id INTEGER, service_name TEXT, display_name TEXT,
        status TEXT, start_type TEXT, path TEXT, user TEXT, description TEXT, startup_time TEXT);""",
    "network_connections": """CREATE TABLE network_connections (
        id INTEGER PRIMARY KEY, system_id INTEGER, local_address TEXT, local_port INTEGER,
        remote_address TEXT, remote_port INTEGER, protocol TEXT, state TEXT, process TEXT, timestamp TEXT);""",
    "startup_programs": """CREATE TABLE startup_programs (
        id INTEGER PRIMARY KEY, system_id INTEGER, name TEXT, path TEXT, publisher TEXT,
        status TEXT, user TEXT, command TEXT, location TEXT, type TEXT);""",
    "event_logs": """CREATE TABLE event_logs (
        id INTEGER PRIMARY KEY, system_id INTEGER, log_name TEXT, source TEXT, event_id INTEGER,
        level TEXT, user TEXT, message TEXT, created_time TEXT, computer TEXT);""",
    "users": """CREATE TABLE users (
        id INTEGER PRIMARY KEY, system_id INTEGER, username TEXT, domain TEXT, sid TEXT,
        full_name TEXT, last_login TEXT, account_type TEXT, status TEXT, email TEXT);""",
    "usb_devices": """CREATE TABLE usb_devices (
        id INTEGER PRIMARY KEY, system_id INTEGER, device_name TEXT, vendor_id TEXT,
        product_id TEXT, serial_number TEXT, connect_time TEXT, disconnect_time TEXT, device_type TEXT, manufacturer TEXT);""",
    "scheduled_tasks": """CREATE TABLE scheduled_tasks (
        id INTEGER PRIMARY KEY, system_id INTEGER, task_name TEXT, status TEXT, trigger TEXT,
        action TEXT, last_run_time TEXT, next_run_time TEXT, user TEXT, path TEXT);"""
}

# Create tables
for sql in tables.values():
    cursor.execute(sql)

# Insert 150 rows into each table
for i in range(1, 151):
    system_id = random.randint(1, 10)

    cursor.execute("INSERT INTO system_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        i, f"HOST-{i}", f"Windows 10 Build {random.randint(10000, 19000)}", random_date(start_date, end_date),
        random_ip(), random_mac(), f"Manufacturer-{random.randint(1,5)}", f"Model-{random.randint(100,999)}",
        "x64-based PC", f"SN-{random.randint(100000,999999)}"
    ))

    cursor.execute("INSERT INTO installed_software VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        i, system_id, f"Software-{random.randint(1,20)}", f"{random.randint(1,5)}.{random.randint(0,9)}.{random.randint(0,999)}",
        random_date(start_date, end_date), f"Vendor-{random.randint(1,5)}", f"KEY-{random.randint(100000,999999)}",
        f"C:/Program Files/Software-{random.randint(1,20)}", round(random.uniform(5.0, 2000.0), 2), random.choice(["Utility", "Security", "Productivity"])
    ))

    cursor.execute("INSERT INTO running_processes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        i, system_id, f"process_{i}.exe", random.randint(1000, 9999), round(random.uniform(0.1, 80.0), 2),
        round(random.uniform(10.0, 500.0), 2), random_date(start_date, end_date), f"user{i}",
        f"C:/Processes/process_{i}.exe", random.choice(["Running", "Sleeping"])
    ))

    cursor.execute("INSERT INTO services VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        i, system_id, f"Service-{i}", f"Display Service {i}", "Running", "Automatic",
        f"C:/Services/Service-{i}.exe", f"user{i}", f"Service {i} description", random_date(start_date, end_date)
    ))

    cursor.execute("INSERT INTO network_connections VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        i, system_id, random_ip(), random.randint(1000, 65000), random_ip(), random.randint(1000, 65000),
        "TCP", "ESTABLISHED", f"proc_{i}.exe", random_date(start_date, end_date)
    ))

    cursor.execute("INSERT INTO startup_programs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        i, system_id, f"StartupProgram{i}", f"C:/Startup/Program{i}.exe", f"Publisher-{random.randint(1,5)}",
        "Enabled", f"user{i}", f"cmd /c start Program{i}", "Registry", "Startup"
    ))

    cursor.execute("INSERT INTO event_logs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        i, system_id, "System", f"Source-{random.randint(1,5)}", random.randint(1000, 9999),
        "Information", f"user{i}", f"Message content for log {i}", random_date(start_date, end_date), f"HOST-{i}"
    ))

    cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        i, system_id, f"user{i}", "DOMAIN", f"S-1-5-21-{random.randint(1000000000,9999999999)}",
        f"User Fullname {i}", random_date(start_date, end_date),
        random.choice(["Admin", "Standard"]), "Active", f"user{i}@example.com"
    ))

    cursor.execute("INSERT INTO usb_devices VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        i, system_id, f"USB Device {i}", "ABCD", "1234", f"SN-{random.randint(10000,99999)}",
        random_date(start_date, end_date), random_date(start_date, end_date), "Storage", f"Manufacturer-{random.randint(1,5)}"
    ))

    cursor.execute("INSERT INTO scheduled_tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        i, system_id, f"Task-{i}", "Ready", "Daily", f"Run Task {i}",
        random_date(start_date, end_date), random_date(start_date, end_date), f"user{i}", f"C:/Tasks/Task-{i}.exe"
    ))

# Commit and close
conn.commit()
conn.close()
