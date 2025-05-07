คู่มือการใช้งาน task1.py
    1.ตรวจสอบว่าในเครื่องต้องมี Python (เวอร์ชัน 3 ขึ้นไป) ในเครื่อง
    2.ติดตั้งไลบรารี third-party ที่จำเป็น
        task1.py ใช้ third-party 2 ตัว คือ BeautifulSoup และ Requests
        Windows:
            เปิด Command Prompt หรือ PowerShell แล้วรันคำสั่ง "pip install requests beautifulsoup4"
        macOS/Linux:
            เปิด Terminal แล้วรันคำสั่ง "pip install requests beautifulsoup4"
    3.สามารถใช้งานผ่าน Terminal, Command Line โดยรันคำสั่ง "python task1.py" 
    4.โปรแกรมจะทำการแสดงลิงก์ทั้งหมดบนหน้าเว็บ, หมายเลขหนังสือ Ebook 100 อันแรกที่ตรวจเจอ, และรายชื่อหนังสือ Ebook 100 อันดับยอดนิยมของเมื่อวานนี้
    5.หากไม่ต้องการให้โปรแกรมแสดงส่วนไหน สามารถใช้ Code Editor ทำการ Comment(#) ด้านหน้าคำสั่งในส่วนที่ระบุไว้ได้

    ปล. โปรแกรมนี้ใช้ข้อมูลจากเว็บไซต์ https://www.gutenberg.org/browse/scores/top เป็นการใช้ Web Scraping เพื่อดึงข้อมูลแบบ HTML แล้วแยกออกเป็นลิงก์และข้อความ

คำอธิบายฟังก์ชัน
    check_response(r)
        ตรวจสอบสถานะการเชื่อมต่อเว็บไซต์ (HTTP Status Code)
        ถ้าเชื่อมต่อสำเร็จ (code 200) จะพิมพ์ข้อความยืนยัน (Web request success !)
        หากไม่สำเร็จ จะพิมพ์ข้อความ (Web request failed !)
    
    get_all_href_on_page(soup)
        รับ BeautifulSoup object
        ดึง href ทั้งหมดจากแท็ก <a> ในหน้าเว็บ แล้วแสดงผลทั้งหมด

    get_top100_filenumbers_on_page(href_lists)
        กรองเฉพาะลิงก์ที่ขึ้นต้นด้วย /ebooks/
        ใช้ regex เพื่อดึงเฉพาะหมายเลขไฟล์ (File ID)
        คืนรายการหมายเลขหนังสือ (สูงสุด 100 รายการ) ผ่าน List

    get_top100_ebooks_Yesterday(soup)
        แยกข้อความจากหน้าเว็บทีละบรรทัด
        ค้นหาหัวข้อ "Top 100 EBooks yesterday"
        ดึงชื่อหนังสือที่อยู่ถัดจากหัวข้อนั้น (100 รายการ)
        แสดงชื่อหนังสือที่ได้

โมดูลที่ใช้ในโปรแกรม
    requests	            สำหรับส่ง HTTP request เพื่อดึง HTML ของเว็บ
    bs4.BeautifulSoup	    สำหรับแปลง HTML ให้อยู่ในรูปแบบที่ง่ายต่อการวิเคราะห์
    re	                    ใช้ regular expression เพื่อดึงข้อมูลตามรูปแบบ