import sys
from collections import deque
import time

# เปลี่ยนการเข้ารหัสของ sys.stdout เป็น utf-8
sys.stdout.reconfigure(encoding='utf-8')

# สร้างคิวใหม่
queue = deque()

# กำหนดขนาดสูงสุดของคิว
MAX_SIZE = 5

# ฟังก์ชันเพื่อแสดงสถานะของคิว
def display_queue(operation):
    print(f"Queue after {operation}:", list(queue))

# ลูปเพื่อเพิ่มและนำข้อมูลออกจากคิว
for i in range(10):
    if len(queue) >= MAX_SIZE:
        # นำข้อมูลออกจากคิวถ้าคิวเต็ม
        queue.popleft()
    
    # เพิ่มข้อมูลใหม่เข้าไปในคิว
    queue.append(f'Item {i}')
    
    # แสดงสถานะของคิวหลังการ Enqueue
    display_queue('Enqueue')
    
    # รอ 2 วินาทีเพื่อดูผลลัพธ์ในคอนโซล
    time.sleep(2)
    
    # นำข้อมูลออกจากคิว
    if queue:  # ตรวจสอบว่าคิวไม่ว่าง
        queue.popleft()
    
    # แสดงสถานะของคิวหลังการ Dequeue
    display_queue('Dequeue')
    
    # รอ 2 วินาทีเพื่อดูผลลัพธ์ในคอนโซล
    time.sleep(2)
