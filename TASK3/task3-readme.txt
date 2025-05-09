คู่มือการใช้งาน task3.py
    1.ตรวจสอบว่าในเครื่องต้องมี Python (เวอร์ชัน 3 ขึ้นไป) ในเครื่อง
    2.ติดตั้งไลบรารี third-party ที่จำเป็น
        task1.py ใช้ third-party 3 ตัว คือ BeautifulSoup และ Requests
        Windows:
            เปิด Command Prompt หรือ PowerShell แล้วรันคำสั่ง "pip install requests beautifulsoup4 pandas"
        macOS/Linux:
            เปิด Terminal แล้วรันคำสั่ง "pip install requests beautifulsoup4 pandas"
    3.สามารถใช้งานผ่าน Terminal, Command Line โดยรันคำสั่ง "python task3.py" 
    4.โปรแกรมจะทำการแสดงสถานะการ Request ไปที่เว็บพร้อม Status code, จำนวนตาราง(HTML Tag <table>)ทั้งหมดในหน้าเว็บ, จำนวนหัวข้อที่เราสนใจพร้อมแสดงให้เห็น, และแสดงตารางแบบแยกเป็นหมวดหมู่
    

    ปล. โปรแกรมนี้ใช้ข้อมูลจากเว็บไซต์ https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal) เป็นการใช้ Web Scraping เพื่อดึงข้อมูลแบบ HTML ที่เป็นตาราง สร้าง DataFrame แล้วนำเสนอข้อมูลรายชื่อประเทศจำแนกตาม GDP


คำอธิบายฟังก์ชัน
    print_dataframe(df):    แสดงผลตาราง GDP ที่ได้จาก 3 แหล่ง: IMF, World Bank, United Nations

โมดูลที่ใช้ในโปรแกรม
    requests	            สำหรับส่ง HTTP request เพื่อดึง HTML ของเว็บ
    bs4.BeautifulSoup	    สำหรับแปลง HTML ให้อยู่ในรูปแบบที่ง่ายต่อการวิเคราะห์
    re	                    ใช้ regular expression เพื่อดึงข้อมูลตามรูปแบบ
    pandas                  ใช้ในการนำข้อมูลที่ได้ สร้างเป็นตาราง พร้อมจัดรูปแบบให้อ่านง่าย