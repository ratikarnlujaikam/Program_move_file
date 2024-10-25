import os
import win32com.client

# กำหนดเส้นทางของไฟล์ต้นฉบับและที่เก็บใหม่
target_file = 'E:/Delete.txt'  # เปลี่ยนเส้นทางไฟล์ที่ต้องการให้เป็น shortcut
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
shortcut_name = 'MyShortcut.lnk'
shortcut_path = os.path.join(desktop_path, shortcut_name)

# สร้าง shortcut
shell = win32com.client.Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = target_file
shortcut.WorkingDirectory = os.path.dirname(target_file)
shortcut.save()

# ใช้การเข้ารหัส UTF-8 เพื่อพิมพ์ข้อความ
print(f'Shortcut ถูกสร้างที่: {shortcut_path}')
