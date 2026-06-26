import os
import sqlite3
from datetime import datetime
from flask import Flask, request, jsonify, render_template, redirect, url_for, g

app = Flask(__name__)
app.config['DATABASE'] = os.path.join(os.path.dirname(__file__), 'devices.db')

# Hardware catalog for suggestions
HARDWARE_CATALOG = {
    "cpu": [
        "Intel Pentium (Original) - 75MHz", "Intel Pentium MMX - 166MHz",
        "Intel Pentium II - 233MHz", "Intel Pentium II - 350MHz", "Intel Pentium II - 450MHz",
        "Intel Pentium III - 500MHz", "Intel Pentium III - 800MHz", "Intel Pentium III - 1.0GHz",
        "Intel Pentium 4 - 1.5GHz", "Intel Pentium 4 - 2.4GHz", "Intel Pentium 4 - 3.0GHz", "Intel Pentium 4 - 3.4GHz",
        "Intel Pentium D - 2.8GHz", "Intel Pentium D - 3.0GHz",
        "Intel Pentium Dual-Core - E2160", "Intel Pentium Dual-Core - E5200", "Intel Pentium Dual-Core - E6300",
        "Intel Celeron - 400MHz", "Intel Celeron D - 2.4GHz", "Intel Celeron D - 3.2GHz",
        "Intel Celeron Dual-Core - E1200", "Intel Celeron G440", "Intel Celeron G1610",
        "Intel Core 2 Duo - E4300", "Intel Core 2 Duo - E6300", "Intel Core 2 Duo - E7200",
        "Intel Core 2 Duo - E8400", "Intel Core 2 Duo - E8500", "Intel Core 2 Duo - T7500",
        "Intel Core 2 Quad - Q6600", "Intel Core 2 Quad - Q8200", "Intel Core 2 Quad - Q9400", "Intel Core 2 Quad - Q9650",
        "Intel Core i3-530", "Intel Core i3-2100", "Intel Core i3-3220", "Intel Core i3-4130", "Intel Core i3-6100", "Intel Core i3-7100", "Intel Core i3-8100", "Intel Core i3-9100F", "Intel Core i3-10100F",
        "Intel Core i5-650", "Intel Core i5-2400", "Intel Core i5-3470", "Intel Core i5-4570", "Intel Core i5-6400", "Intel Core i5-7400", "Intel Core i5-8400", "Intel Core i5-9400F", "Intel Core i5-10400F",
        "Intel Core i5-11400F", "Intel Core i5-12400F", "Intel Core i5-13400F", "Intel Core i5-13600K", "Intel Core i5-14400F", "Intel Core i5-14600K",
        "Intel Core i7-860", "Intel Core i7-2600K", "Intel Core i7-3770K", "Intel Core i7-4770K", "Intel Core i7-6700K", "Intel Core i7-7700K", "Intel Core i7-8700K", "Intel Core i7-9700K", "Intel Core i7-10700K", "Intel Core i7-11700K",
        "Intel Core i7-12700K", "Intel Core i7-13700K", "Intel Core i7-14700K",
        "Intel Core i9-9900K", "Intel Core i9-10900K", "Intel Core i9-11900K",
        "Intel Core i9-12900K", "Intel Core i9-13900K", "Intel Core i9-14900K",
        "Intel Core Ultra 5 225H", "Intel Core Ultra 7 265K", "Intel Core Ultra 9 285K",
        "AMD K6-2 - 333MHz", "AMD K6-2 - 450MHz",
        "AMD Athlon - 500MHz", "AMD Athlon - 1.0GHz", "AMD Athlon - 1.4GHz",
        "AMD Athlon XP - 1800+", "AMD Athlon XP - 2500+", "AMD Athlon XP - 3200+",
        "AMD Athlon 64 - 3000+", "AMD Athlon 64 - 3200+", "AMD Athlon 64 - 3500+",
        "AMD Athlon 64 X2 - 4200+", "AMD Athlon 64 X2 - 5000+", "AMD Athlon 64 X2 - 6400+",
        "AMD Phenom - X3 8450", "AMD Phenom - X4 9650",
        "AMD Phenom II - X2 550", "AMD Phenom II - X4 945", "AMD Phenom II - X4 955", "AMD Phenom II - X6 1055T",
        "AMD FX-4100", "AMD FX-6100", "AMD FX-6300", "AMD FX-8120", "AMD FX-8320", "AMD FX-8350",
        "AMD A4-3300", "AMD A6-3670K", "AMD A8-3850", "AMD A8-5600K", "AMD A10-5800K", "AMD A10-7850K",
        "AMD Ryzen 3 1200", "AMD Ryzen 3 2200G", "AMD Ryzen 3 3100", "AMD Ryzen 3 3300X", "AMD Ryzen 3 4100", "AMD Ryzen 3 5100", "AMD Ryzen 3 7100", "AMD Ryzen 3 8100", "AMD Ryzen 3 9100",
        "AMD Ryzen 5 1400", "AMD Ryzen 5 1600", "AMD Ryzen 5 2600", "AMD Ryzen 5 3600", "AMD Ryzen 5 4500", "AMD Ryzen 5 5500", "AMD Ryzen 5 5600X", "AMD Ryzen 5 7600X", "AMD Ryzen 5 9600X",
        "AMD Ryzen 7 1700", "AMD Ryzen 7 1800X", "AMD Ryzen 7 2700X", "AMD Ryzen 7 3700X", "AMD Ryzen 7 3800X", "AMD Ryzen 7 5700X3D", "AMD Ryzen 7 5800X", "AMD Ryzen 7 7700X", "AMD Ryzen 7 7800X3D", "AMD Ryzen 7 8700G", "AMD Ryzen 7 9800X3D",
        "AMD Ryzen 9 3900X", "AMD Ryzen 9 3950X", "AMD Ryzen 9 5900X", "AMD Ryzen 9 5950X", "AMD Ryzen 9 7900X", "AMD Ryzen 9 7950X", "AMD Ryzen 9 9950X",
    ],
    "gpu": [
        "NVIDIA GeForce 2 MX - 200", "NVIDIA GeForce 2 MX - 400",
        "NVIDIA GeForce 4 MX - 420", "NVIDIA GeForce 4 MX - 440", "NVIDIA GeForce 4 Ti - 4200",
        "NVIDIA GeForce FX - 5200", "NVIDIA GeForce FX - 5700", "NVIDIA GeForce FX - 5900",
        "NVIDIA GeForce 6200", "NVIDIA GeForce 6600", "NVIDIA GeForce 6800",
        "NVIDIA GeForce 7300 GT", "NVIDIA GeForce 7600 GT", "NVIDIA GeForce 7800 GTX",
        "NVIDIA GeForce 8400 GS", "NVIDIA GeForce 8600 GT", "NVIDIA GeForce 8800 GT", "NVIDIA GeForce 8800 GTX",
        "NVIDIA GeForce 9400 GT", "NVIDIA GeForce 9500 GT", "NVIDIA GeForce 9600 GT", "NVIDIA GeForce 9800 GT",
        "NVIDIA GeForce GT 210", "NVIDIA GeForce GT 220", "NVIDIA GeForce GT 240",
        "NVIDIA GeForce GT 430", "NVIDIA GeForce GT 440", "NVIDIA GeForce GT 610", "NVIDIA GeForce GT 710", "NVIDIA GeForce GT 730", "NVIDIA GeForce GT 1030",
        "NVIDIA GeForce GTX 260", "NVIDIA GeForce GTX 275", "NVIDIA GeForce GTX 285",
        "NVIDIA GeForce GTX 460", "NVIDIA GeForce GTX 470", "NVIDIA GeForce GTX 480",
        "NVIDIA GeForce GTX 550 Ti", "NVIDIA GeForce GTX 560", "NVIDIA GeForce GTX 570", "NVIDIA GeForce GTX 580",
        "NVIDIA GeForce GTX 650", "NVIDIA GeForce GTX 650 Ti", "NVIDIA GeForce GTX 660", "NVIDIA GeForce GTX 670", "NVIDIA GeForce GTX 680",
        "NVIDIA GeForce GTX 750", "NVIDIA GeForce GTX 750 Ti", "NVIDIA GeForce GTX 760", "NVIDIA GeForce GTX 770", "NVIDIA GeForce GTX 780", "NVIDIA GeForce GTX 780 Ti",
        "NVIDIA GeForce GTX 950", "NVIDIA GeForce GTX 960", "NVIDIA GeForce GTX 970", "NVIDIA GeForce GTX 980", "NVIDIA GeForce GTX 980 Ti",
        "NVIDIA GeForce GTX 1050", "NVIDIA GeForce GTX 1050 Ti", "NVIDIA GeForce GTX 1060", "NVIDIA GeForce GTX 1070", "NVIDIA GeForce GTX 1070 Ti", "NVIDIA GeForce GTX 1080", "NVIDIA GeForce GTX 1080 Ti",
        "NVIDIA GeForce GTX 1650", "NVIDIA GeForce GTX 1650 Super", "NVIDIA GeForce GTX 1660", "NVIDIA GeForce GTX 1660 Super", "NVIDIA GeForce GTX 1660 Ti",
        "NVIDIA GeForce RTX 2060", "NVIDIA GeForce RTX 2060 Super", "NVIDIA GeForce RTX 2070", "NVIDIA GeForce RTX 2070 Super", "NVIDIA GeForce RTX 2080", "NVIDIA GeForce RTX 2080 Super", "NVIDIA GeForce RTX 2080 Ti",
        "NVIDIA GeForce RTX 3050", "NVIDIA GeForce RTX 3060", "NVIDIA GeForce RTX 3060 Ti",
        "NVIDIA GeForce RTX 3070", "NVIDIA GeForce RTX 3070 Ti", "NVIDIA GeForce RTX 3080",
        "NVIDIA GeForce RTX 3080 Ti", "NVIDIA GeForce RTX 3090", "NVIDIA GeForce RTX 3090 Ti",
        "NVIDIA GeForce RTX 4060", "NVIDIA GeForce RTX 4060 Ti", "NVIDIA GeForce RTX 4070",
        "NVIDIA GeForce RTX 4070 Super", "NVIDIA GeForce RTX 4070 Ti", "NVIDIA GeForce RTX 4080",
        "NVIDIA GeForce RTX 4080 Super", "NVIDIA GeForce RTX 4090",
        "NVIDIA GeForce RTX 5060", "NVIDIA GeForce RTX 5070", "NVIDIA GeForce RTX 5080", "NVIDIA GeForce RTX 5090",
        "AMD Radeon 7000 - 64MB", "AMD Radeon 8500 - 128MB",
        "AMD Radeon 9200 Pro", "AMD Radeon 9550", "AMD Radeon 9600 Pro", "AMD Radeon 9800 Pro",
        "AMD Radeon X300", "AMD Radeon X600", "AMD Radeon X800",
        "AMD Radeon HD 2400 Pro", "AMD Radeon HD 2600 XT",
        "AMD Radeon HD 3450", "AMD Radeon HD 3650", "AMD Radeon HD 3850", "AMD Radeon HD 3870",
        "AMD Radeon HD 4350", "AMD Radeon HD 4650", "AMD Radeon HD 4830", "AMD Radeon HD 4850", "AMD Radeon HD 4870", "AMD Radeon HD 4890",
        "AMD Radeon HD 5450", "AMD Radeon HD 5550", "AMD Radeon HD 5670", "AMD Radeon HD 5750", "AMD Radeon HD 5770", "AMD Radeon HD 5850", "AMD Radeon HD 5870",
        "AMD Radeon HD 6450", "AMD Radeon HD 6570", "AMD Radeon HD 6670", "AMD Radeon HD 6750", "AMD Radeon HD 6770", "AMD Radeon HD 6850", "AMD Radeon HD 6870", "AMD Radeon HD 6950", "AMD Radeon HD 6970",
        "AMD Radeon HD 7750", "AMD Radeon HD 7770", "AMD Radeon HD 7850", "AMD Radeon HD 7870", "AMD Radeon HD 7950", "AMD Radeon HD 7970",
        "AMD Radeon R5 230", "AMD Radeon R5 240",
        "AMD Radeon R7 240", "AMD Radeon R7 250", "AMD Radeon R7 260", "AMD Radeon R7 265", "AMD Radeon R7 370",
        "AMD Radeon R9 270", "AMD Radeon R9 270X", "AMD Radeon R9 280", "AMD Radeon R9 280X", "AMD Radeon R9 290", "AMD Radeon R9 290X", "AMD Radeon R9 380", "AMD Radeon R9 390", "AMD Radeon R9 390X", "AMD Radeon R9 Fury X",
        "AMD Radeon RX 460", "AMD Radeon RX 470", "AMD Radeon RX 480", "AMD Radeon RX 550", "AMD Radeon RX 560", "AMD Radeon RX 570", "AMD Radeon RX 580", "AMD Radeon RX 590",
        "AMD Radeon RX 5500 XT", "AMD Radeon RX 5600 XT", "AMD Radeon RX 5700", "AMD Radeon RX 5700 XT",
        "AMD Radeon RX 6400", "AMD Radeon RX 6500 XT",
        "AMD Radeon RX 6600", "AMD Radeon RX 6600 XT", "AMD Radeon RX 6700 XT",
        "AMD Radeon RX 6800", "AMD Radeon RX 6800 XT", "AMD Radeon RX 6900 XT",
        "AMD Radeon RX 7600", "AMD Radeon RX 7600 XT", "AMD Radeon RX 7700 XT",
        "AMD Radeon RX 7800 XT", "AMD Radeon RX 7900 GRE", "AMD Radeon RX 7900 XT", "AMD Radeon RX 7900 XTX",
        "AMD Radeon RX 9060 XT", "AMD Radeon RX 9070", "AMD Radeon RX 9070 XT",
    ],
    "motherboard": [
        "Intel 430TX (Socket 7)",
        "Intel 440BX (Slot 1)", "Intel 440LX (Slot 1)",
        "Intel 810 (Socket 370)", "Intel 815 (Socket 370)",
        "Intel 845 (Socket 478)", "Intel 865 (Socket 478)", "Intel 875P (Socket 478)",
        "Intel 915 (LGA775)", "Intel 945 (LGA775)", "Intel 965 (LGA775)",
        "Intel G31 (LGA775)", "Intel G41 (LGA775)", "Intel G45 (LGA775)",
        "Intel P35 (LGA775)", "Intel P43 (LGA775)", "Intel P45 (LGA775)",
        "Intel X38 (LGA775)", "Intel X48 (LGA775)",
        "Intel H55 (LGA1156)", "Intel P55 (LGA1156)",
        "Intel H61 (LGA1155)", "Intel B75 (LGA1155)", "Intel H77 (LGA1155)", "Intel Z77 (LGA1155)",
        "Intel H81 (LGA1150)", "Intel B85 (LGA1150)", "Intel H97 (LGA1150)", "Intel Z97 (LGA1150)",
        "Intel H110 (LGA1151)", "Intel B150 (LGA1151)", "Intel B250 (LGA1151)", "Intel Z170 (LGA1151)", "Intel Z270 (LGA1151)",
        "Intel H310 (LGA1151v2)", "Intel B360 (LGA1151v2)", "Intel B365 (LGA1151v2)", "Intel Z390 (LGA1151v2)",
        "Intel H410 (LGA1200)", "Intel B460 (LGA1200)", "Intel B560 (LGA1200)", "Intel Z490 (LGA1200)", "Intel Z590 (LGA1200)",
        "Intel H610 (LGA1700)", "Intel B660 (LGA1700)", "Intel B760 (LGA1700)", "Intel Z690 (LGA1700)", "Intel Z790 (LGA1700)",
        "ASUS ROG STRIX Z790-E GAMING", "ASUS ROG STRIX B760-F GAMING",
        "ASUS TUF GAMING Z790-PLUS", "ASUS TUF GAMING B760-PLUS",
        "ASUS PRIME Z790-A", "ASUS PRIME B760M-A",
        "ASUS ROG STRIX X670E-E GAMING", "ASUS ROG STRIX B650-A GAMING",
        "ASUS TUF GAMING X670E-PLUS", "ASUS TUF GAMING B650-PLUS",
        "ASUS PRIME X670-P", "ASUS PRIME B650M-A",
        "MSI MPG Z790 CARBON MAX", "MSI MAG Z790 TOMAHAWK",
        "MSI PRO Z790-A WIFI", "MSI MAG B760 TOMAHAWK",
        "MSI MPG X670E CARBON", "MSI MAG X670E TOMAHAWK",
        "MSI PRO X670-P WIFI", "MSI MAG B650 TOMAHAWK",
        "Gigabyte Z790 AORUS MASTER", "Gigabyte Z790 AORUS ELITE",
        "Gigabyte B760 AORUS ELITE", "Gigabyte B760 GAMING X",
        "Gigabyte X670E AORUS MASTER", "Gigabyte X670 AORUS ELITE",
        "Gigabyte B650 AORUS ELITE", "Gigabyte B650 GAMING X",
        "ASRock Z790 PG LIGHTNING", "ASRock B760 PRO RS",
        "ASRock X670E TAICHI", "ASRock B650E PG RIPTIDE",
        "AMD 760 (Socket A)", "AMD 761 (Socket A)",
        "AMD 780G (AM2+)", "AMD 790GX (AM2+)",
        "AMD 770 (AM3)", "AMD 790X (AM3)", "AMD 790FX (AM3)",
        "AMD 870 (AM3)", "AMD 880G (AM3)", "AMD 890FX (AM3)",
        "AMD 970 (AM3+)", "AMD 990X (AM3+)", "AMD 990FX (AM3+)",
        "AMD A55 (FM1)", "AMD A75 (FM1)",
        "AMD A58 (FM2+)", "AMD A68H (FM2+)", "AMD A78 (FM2+)",
        "AMD A320 (AM4)", "AMD B350 (AM4)", "AMD B450 (AM4)", "AMD B550 (AM4)", "AMD X370 (AM4)", "AMD X470 (AM4)", "AMD X570 (AM4)",
        "AMD B650 (AM5)", "AMD X670 (AM5)", "AMD X870 (AM5)",
    ],
    "ram": [
        "DDR 256MB - 266MHz", "DDR 512MB - 266MHz", "DDR 512MB - 333MHz", "DDR 1GB - 333MHz", "DDR 1GB - 400MHz",
        "DDR2 512MB - 533MHz", "DDR2 1GB - 533MHz", "DDR2 1GB - 667MHz", "DDR2 2GB - 667MHz", "DDR2 2GB - 800MHz",
        "DDR3 1GB - 1066MHz", "DDR3 2GB - 1066MHz", "DDR3 2GB - 1333MHz", "DDR3 4GB - 1333MHz", "DDR3 4GB - 1600MHz", "DDR3 8GB - 1600MHz",
        "DDR4 4GB - 2133MHz", "DDR4 4GB - 2400MHz", "DDR4 8GB - 2400MHz", "DDR4 8GB - 2666MHz", "DDR4 8GB - 3200MHz",
        "DDR4 16GB - 2666MHz", "DDR4 16GB - 3200MHz", "DDR4 16GB - 3600MHz", "DDR4 32GB - 3200MHz", "DDR4 32GB - 3600MHz",
        "DDR5 16GB - 4800MHz", "DDR5 16GB - 5200MHz", "DDR5 16GB - 5600MHz",
        "DDR5 32GB - 5200MHz", "DDR5 32GB - 5600MHz", "DDR5 32GB - 6000MHz", "DDR5 32GB - 6400MHz",
        "DDR5 64GB - 6000MHz", "DDR5 64GB - 6400MHz",
    ],
    "storage": [
        "HDD 40GB IDE", "HDD 80GB IDE", "HDD 120GB IDE", "HDD 160GB IDE", "HDD 250GB IDE",
        "HDD 160GB SATA", "HDD 250GB SATA", "HDD 320GB SATA", "HDD 500GB SATA", "HDD 750GB SATA",
        "HDD 1TB SATA", "HDD 1.5TB SATA", "HDD 2TB SATA", "HDD 3TB SATA", "HDD 4TB SATA",
        "SSD 60GB SATA", "SSD 120GB SATA", "SSD 240GB SATA", "SSD 256GB SATA", "SSD 480GB SATA", "SSD 512GB SATA", "SSD 960GB SATA", "SSD 1TB SATA", "SSD 2TB SATA",
        "SSD 256GB NVMe", "SSD 512GB NVMe", "SSD 1TB NVMe", "SSD 2TB NVMe", "SSD 4TB NVMe",
        "NVMe 256GB", "NVMe 512GB", "NVMe 1TB", "NVMe 2TB", "NVMe 4TB",
    ],
    "power_supply": [
        "250W PSU", "300W PSU", "350W PSU", "400W PSU", "450W PSU", "500W PSU",
        "550W PSU", "600W PSU", "650W PSU", "700W PSU", "750W PSU",
        "800W PSU", "850W PSU", "1000W PSU", "1200W PSU", "1600W PSU",
        "450W Bronze", "500W Bronze", "550W Bronze", "600W Bronze", "650W Bronze",
        "650W Gold", "750W Gold", "850W Gold", "1000W Gold", "1200W Gold",
        "750W Platinum", "850W Platinum", "1000W Platinum", "1200W Platinum",
    ],
    "case": [
        "Mini Tower", "Mid Tower", "Full Tower", "Super Tower", "SFF (Small Form Factor)",
        "Desktop Case", "HTPC Case", "ITX Case", "Micro-ATX Case",
        "Server Rack Case", "Wall-Mount Case", "Open Bench Case",
    ],
    "condition": [
        "Excellent - Like New", "Very Good - Minor Wear", "Good - Normal Use", "Fair - Visible Wear", "Poor - Heavy Wear",
        "For Parts / Not Working", "Refurbished", "New (Sealed)", "Open Box",
    ],
}


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(app.config['DATABASE'])
    db.execute("PRAGMA foreign_keys = ON")
    db.executescript("""
        CREATE TABLE IF NOT EXISTS devices (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            serial_number TEXT,
            customer_name TEXT,
            category TEXT NOT NULL DEFAULT 'CUSTOMER',
            sub_category TEXT,
            status TEXT NOT NULL DEFAULT 'PENDING_INSPECTION',
            cpu TEXT,
            ram TEXT,
            gpu TEXT,
            storage TEXT,
            motherboard TEXT,
            power_supply TEXT,
            case_field TEXT,
            condition_field TEXT,
            notes TEXT,
            entry_date TEXT NOT NULL DEFAULT (datetime('now')),
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            updated_at TEXT NOT NULL DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS repair_records (
            id TEXT PRIMARY KEY,
            device_id TEXT NOT NULL,
            probable_cause TEXT,
            issue_description TEXT,
            symptoms TEXT,
            diagnostic_notes TEXT,
            checked_parts TEXT,
            replaced_parts TEXT,
            repair_actions TEXT,
            tests_performed TEXT,
            test_results TEXT,
            repair_status TEXT NOT NULL DEFAULT 'PENDING',
            technician_notes TEXT,
            repair_cost REAL,
            assigned_technician TEXT,
            entry_date TEXT NOT NULL DEFAULT (datetime('now')),
            expected_completion_date TEXT,
            completion_date TEXT,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            updated_at TEXT NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (device_id) REFERENCES devices(id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS activity_logs (
            id TEXT PRIMARY KEY,
            device_id TEXT NOT NULL,
            action TEXT NOT NULL,
            description TEXT,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            FOREIGN KEY (device_id) REFERENCES devices(id) ON DELETE CASCADE
        );
    """)
    db.commit()
    db.close()


def generate_id():
    import uuid
    return uuid.uuid4().hex[:12]


# ----- PAGES -----

@app.route('/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/add-system')
def add_system():
    return render_template('add_system.html')


@app.route('/systems')
def all_systems():
    return render_template('all_systems.html')


@app.route('/systems/<device_id>')
def system_detail(device_id):
    return render_template('system_detail.html', device_id=device_id)


@app.route('/systems/customer')
def customer_systems():
    return render_template('customer.html')


@app.route('/systems/for-sale')
def for_sale_systems():
    return render_template('for_sale.html')


@app.route('/systems/internal')
def internal_systems():
    return render_template('internal.html')


@app.route('/repair')
def repair_center():
    return render_template('repair_center.html')


@app.route('/repair/<repair_id>')
def repair_detail(repair_id):
    return render_template('repair_detail.html', repair_id=repair_id)


@app.route('/settings')
def settings():
    return render_template('settings.html')


# ----- API: Dashboard -----

@app.route('/api/dashboard')
def api_dashboard():
    db = get_db()
    total = db.execute("SELECT COUNT(*) FROM devices").fetchone()[0]
    customer = db.execute("SELECT COUNT(*) FROM devices WHERE category='CUSTOMER'").fetchone()[0]
    for_sale = db.execute("SELECT COUNT(*) FROM devices WHERE category='FOR_SALE'").fetchone()[0]
    internal = db.execute("SELECT COUNT(*) FROM devices WHERE category='INTERNAL'").fetchone()[0]
    damaged = db.execute("SELECT COUNT(*) FROM devices WHERE status='DAMAGED'").fetchone()[0]
    in_repair = db.execute("SELECT COUNT(*) FROM devices WHERE status='IN_REPAIR'").fetchone()[0]
    ready = db.execute("SELECT COUNT(*) FROM devices WHERE status='READY'").fetchone()[0]
    recent = db.execute(
        "SELECT id, name, category, status, created_at FROM devices ORDER BY created_at DESC LIMIT 10"
    ).fetchall()

    return jsonify({
        'total': total,
        'customer': customer,
        'forSale': for_sale,
        'internal': internal,
        'damaged': damaged,
        'inRepair': in_repair,
        'ready': ready,
        'recentDevices': [dict(r) for r in recent],
    })


# ----- API: Devices -----

@app.route('/api/devices', methods=['GET'])
def api_devices_list():
    db = get_db()
    query = "SELECT d.*, (SELECT COUNT(*) FROM repair_records WHERE device_id=d.id) as repairs_count, (SELECT COUNT(*) FROM activity_logs WHERE device_id=d.id) as activities_count FROM devices d WHERE 1=1"
    params = []

    category = request.args.get('category')
    status = request.args.get('status')
    sub_category = request.args.get('subCategory')
    search = request.args.get('search')

    if category:
        query += " AND d.category=?"
        params.append(category)
    if status:
        statuses = status.split(',')
        placeholders = ','.join(['?' for _ in statuses])
        query += f" AND d.status IN ({placeholders})"
        params.extend(statuses)
    if sub_category:
        query += " AND d.sub_category=?"
        params.append(sub_category)
    if search:
        query += " AND (d.name LIKE ? OR d.serial_number LIKE ? OR d.cpu LIKE ? OR d.notes LIKE ?)"
        s = f"%{search}%"
        params.extend([s, s, s, s])

    query += " ORDER BY d.created_at DESC"
    devices = db.execute(query, params).fetchall()
    return jsonify([dict(d) for d in devices])


@app.route('/api/devices', methods=['POST'])
def api_devices_create():
    db = get_db()
    data = request.json
    device_id = generate_id()
    now = datetime.now().isoformat()

    db.execute("""
        INSERT INTO devices (id, name, serial_number, customer_name, category, sub_category, status,
            cpu, ram, gpu, storage, motherboard, power_supply, case_field, condition_field, notes, entry_date, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        device_id, data['name'], data.get('serial_number'), data.get('customerName'),
        data.get('category', 'CUSTOMER'),
        data.get('subCategory'), data.get('status', 'PENDING_INSPECTION'),
        data.get('cpu'), data.get('ram'), data.get('gpu'), data.get('storage'),
        data.get('motherboard'), data.get('powerSupply'), data.get('case_'), data.get('condition'),
        data.get('notes'), data.get('entryDate', now), now, now
    ))

    db.execute("INSERT INTO activity_logs (id, device_id, action, description, created_at) VALUES (?, ?, ?, ?, ?)",
               (generate_id(), device_id, 'CREATED', f'System "{data["name"]}" was created', now))
    db.commit()

    device = db.execute("SELECT * FROM devices WHERE id=?", (device_id,)).fetchone()
    return jsonify(dict(device)), 201


@app.route('/api/devices/<device_id>', methods=['GET'])
def api_device_get(device_id):
    db = get_db()
    device = db.execute("SELECT * FROM devices WHERE id=?", (device_id,)).fetchone()
    if not device:
        return jsonify({'error': 'Device not found'}), 404

    repairs = db.execute("SELECT * FROM repair_records WHERE device_id=? ORDER BY created_at DESC", (device_id,)).fetchall()
    activities = db.execute("SELECT * FROM activity_logs WHERE device_id=? ORDER BY created_at DESC", (device_id,)).fetchall()

    result = dict(device)
    result['repairs'] = [dict(r) for r in repairs]
    result['activities'] = [dict(a) for a in activities]
    return jsonify(result)


@app.route('/api/devices/<device_id>', methods=['PUT'])
def api_device_update(device_id):
    db = get_db()
    existing = db.execute("SELECT * FROM devices WHERE id=?", (device_id,)).fetchone()
    if not existing:
        return jsonify({'error': 'Device not found'}), 404

    data = request.json
    now = datetime.now().isoformat()
    changes = []

    fields = ['name', 'serial_number', 'category', 'sub_category', 'status',
              'cpu', 'ram', 'gpu', 'storage', 'motherboard', 'power_supply',
              'case_field', 'condition_field', 'notes']
    mapping = {
        'name': 'name', 'serialNumber': 'serial_number', 'customerName': 'customer_name',
        'category': 'category',
        'subCategory': 'sub_category', 'status': 'status', 'cpu': 'cpu', 'ram': 'ram',
        'gpu': 'gpu', 'storage': 'storage', 'motherboard': 'motherboard',
        'powerSupply': 'power_supply', 'case_': 'case_field', 'condition': 'condition_field',
        'notes': 'notes'
    }

    updates = []
    params = []
    for json_key, db_key in mapping.items():
        if json_key in data:
            updates.append(f"{db_key}=?")
            params.append(data[json_key])
            if db_key == 'status' and data[json_key] != existing['status']:
                changes.append(f"status changed from {existing['status']} to {data[json_key]}")

    if updates:
        updates.append("updated_at=?")
        params.append(now)
        params.append(device_id)
        db.execute(f"UPDATE devices SET {', '.join(updates)} WHERE id=?", params)

        if changes:
            db.execute("INSERT INTO activity_logs (id, device_id, action, description, created_at) VALUES (?, ?, ?, ?, ?)",
                       (generate_id(), device_id, 'UPDATED', f"System updated: {', '.join(changes)}", now))
        db.commit()

    device = db.execute("SELECT * FROM devices WHERE id=?", (device_id,)).fetchone()
    return jsonify(dict(device))


@app.route('/api/devices/<device_id>', methods=['DELETE'])
def api_device_delete(device_id):
    db = get_db()
    db.execute("DELETE FROM devices WHERE id=?", (device_id,))
    db.commit()
    return jsonify({'message': 'Device deleted'})


# ----- API: Category endpoints -----

@app.route('/api/systems/customer')
def api_customer_systems():
    db = get_db()
    devices = db.execute("""
        SELECT d.*, (SELECT COUNT(*) FROM repair_records WHERE device_id=d.id) as repairs_count,
               (SELECT COUNT(*) FROM activity_logs WHERE device_id=d.id) as activities_count
        FROM devices d WHERE d.category='CUSTOMER' ORDER BY d.created_at DESC
    """).fetchall()
    return jsonify([dict(d) for d in devices])


@app.route('/api/systems/for-sale')
def api_for_sale_systems():
    db = get_db()
    devices = db.execute("""
        SELECT d.*, (SELECT COUNT(*) FROM repair_records WHERE device_id=d.id) as repairs_count,
               (SELECT COUNT(*) FROM activity_logs WHERE device_id=d.id) as activities_count
        FROM devices d WHERE d.category='FOR_SALE' ORDER BY d.created_at DESC
    """).fetchall()
    return jsonify([dict(d) for d in devices])


@app.route('/api/systems/internal')
def api_internal_systems():
    db = get_db()
    sub_category = request.args.get('subCategory')
    if sub_category:
        devices = db.execute("""
            SELECT d.*, (SELECT COUNT(*) FROM repair_records WHERE device_id=d.id) as repairs_count,
                   (SELECT COUNT(*) FROM activity_logs WHERE device_id=d.id) as activities_count
            FROM devices d WHERE d.category='INTERNAL' AND d.sub_category=? ORDER BY d.created_at DESC
        """, (sub_category,)).fetchall()
    else:
        devices = db.execute("""
            SELECT d.*, (SELECT COUNT(*) FROM repair_records WHERE device_id=d.id) as repairs_count,
                   (SELECT COUNT(*) FROM activity_logs WHERE device_id=d.id) as activities_count
            FROM devices d WHERE d.category='INTERNAL' ORDER BY d.created_at DESC
        """).fetchall()
    return jsonify([dict(d) for d in devices])


@app.route('/api/systems/status', methods=['PUT'])
def api_update_status():
    db = get_db()
    data = request.json
    device_id = data.get('id')
    status = data.get('status')
    if not device_id or not status:
        return jsonify({'error': 'id and status are required'}), 400

    now = datetime.now().isoformat()
    db.execute("UPDATE devices SET status=?, updated_at=? WHERE id=?", (status, now, device_id))
    db.execute("INSERT INTO activity_logs (id, device_id, action, description, created_at) VALUES (?, ?, ?, ?, ?)",
               (generate_id(), device_id, 'STATUS_CHANGED', f"Status changed to {status}", now))
    db.commit()
    device = db.execute("SELECT * FROM devices WHERE id=?", (device_id,)).fetchone()
    return jsonify(dict(device))


# ----- API: Repairs -----

@app.route('/api/repairs', methods=['GET'])
def api_repairs_list():
    db = get_db()
    device_id = request.args.get('deviceId')
    repair_status = request.args.get('repairStatus')

    query = """
        SELECT r.*, d.id as device_id_ref, d.name as device_name, d.category as device_category, d.status as device_status
        FROM repair_records r JOIN devices d ON r.device_id = d.id WHERE 1=1
    """
    params = []
    if device_id:
        query += " AND r.device_id=?"
        params.append(device_id)
    if repair_status:
        query += " AND r.repair_status=?"
        params.append(repair_status)

    query += " ORDER BY r.created_at DESC"
    repairs = db.execute(query, params).fetchall()

    result = []
    for r in repairs:
        d = dict(r)
        d['device'] = {'id': d['device_id_ref'], 'name': d['device_name'], 'category': d['device_category'], 'status': d['device_status']}
        del d['device_id_ref'], d['device_name'], d['device_category'], d['device_status']
        result.append(d)
    return jsonify(result)


@app.route('/api/repairs', methods=['POST'])
def api_repairs_create():
    db = get_db()
    data = request.json
    repair_id = generate_id()
    now = datetime.now().isoformat()

    db.execute("""
        INSERT INTO repair_records (id, device_id, probable_cause, issue_description, symptoms,
            diagnostic_notes, checked_parts, replaced_parts, repair_actions, tests_performed,
            test_results, repair_status, technician_notes, repair_cost, assigned_technician,
            entry_date, expected_completion_date, completion_date, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        repair_id, data['deviceId'], data.get('probableCause'), data.get('issueDescription'),
        data.get('symptoms'), data.get('diagnosticNotes'), data.get('checkedParts'),
        data.get('replacedParts'), data.get('repairActions'), data.get('testsPerformed'),
        data.get('testResults'), data.get('repairStatus', 'PENDING'), data.get('technicianNotes'),
        data.get('repairCost'), data.get('assignedTechnician'),
        now, data.get('expectedCompletionDate'), data.get('completionDate'), now, now
    ))

    db.execute("UPDATE devices SET status='IN_REPAIR', updated_at=? WHERE id=?", (now, data['deviceId']))
    db.execute("INSERT INTO activity_logs (id, device_id, action, description, created_at) VALUES (?, ?, ?, ?, ?)",
               (generate_id(), data['deviceId'], 'REPAIR_STARTED', 'Repair record created for device', now))
    db.commit()

    repair = db.execute("SELECT * FROM repair_records WHERE id=?", (repair_id,)).fetchone()
    return jsonify(dict(repair)), 201


@app.route('/api/repairs/<repair_id>', methods=['GET'])
def api_repair_get(repair_id):
    db = get_db()
    repair = db.execute("SELECT * FROM repair_records WHERE id=?", (repair_id,)).fetchone()
    if not repair:
        return jsonify({'error': 'Repair record not found'}), 404

    device = db.execute("SELECT * FROM devices WHERE id=?", (repair['device_id'],)).fetchone()
    all_repairs = db.execute("SELECT * FROM repair_records WHERE device_id=? ORDER BY created_at DESC", (repair['device_id'],)).fetchall()

    result = dict(repair)
    result['device'] = dict(device)
    result['device']['repairs'] = [dict(r) for r in all_repairs]
    return jsonify(result)


@app.route('/api/repairs/<repair_id>', methods=['PUT'])
def api_repair_update(repair_id):
    db = get_db()
    existing = db.execute("SELECT * FROM repair_records WHERE id=?", (repair_id,)).fetchone()
    if not existing:
        return jsonify({'error': 'Repair record not found'}), 404

    data = request.json
    now = datetime.now().isoformat()

    mapping = {
        'probableCause': 'probable_cause', 'issueDescription': 'issue_description',
        'symptoms': 'symptoms', 'diagnosticNotes': 'diagnostic_notes',
        'checkedParts': 'checked_parts', 'replacedParts': 'replaced_parts',
        'repairActions': 'repair_actions', 'testsPerformed': 'tests_performed',
        'testResults': 'test_results', 'repairStatus': 'repair_status',
        'technicianNotes': 'technician_notes', 'assignedTechnician': 'assigned_technician',
        'expectedCompletionDate': 'expected_completion_date', 'completionDate': 'completion_date'
    }

    updates = []
    params = []
    for json_key, db_key in mapping.items():
        if json_key in data:
            updates.append(f"{db_key}=?")
            params.append(data[json_key])

    if 'repairCost' in data:
        updates.append("repair_cost=?")
        params.append(float(data['repairCost']) if data['repairCost'] else None)

    if updates:
        updates.append("updated_at=?")
        params.append(now)
        params.append(repair_id)
        db.execute(f"UPDATE repair_records SET {', '.join(updates)} WHERE id=?", params)

        if data.get('repairStatus') == 'COMPLETED':
            db.execute("UPDATE devices SET status='READY', updated_at=? WHERE id=?", (now, existing['device_id']))
            db.execute("INSERT INTO activity_logs (id, device_id, action, description, created_at) VALUES (?, ?, ?, ?, ?)",
                       (generate_id(), existing['device_id'], 'REPAIR_COMPLETED', 'Repair completed for device', now))

        db.commit()

    repair = db.execute("SELECT * FROM repair_records WHERE id=?", (repair_id,)).fetchone()
    return jsonify(dict(repair))


# ----- API: Hardware Catalog -----

@app.route('/api/hardware')
def api_hardware():
    return jsonify(HARDWARE_CATALOG)

# ----- API: Hardware Suggestions -----

@app.route('/api/hardware/suggest')
def api_hardware_suggest():
    q = request.args.get('q', '').lower()
    type_ = request.args.get('type', '')  # cpu, gpu, motherboard, ram, storage, power_supply, case, condition
    if type_ not in HARDWARE_CATALOG:
        return jsonify([])
    items = HARDWARE_CATALOG[type_]
    if q:
        items = [item for item in items if q in item.lower()]
    return jsonify(items[:20])


if __name__ == '__main__':
    init_db()
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
