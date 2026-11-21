[English](README.md) | [ภาษาไทย (Thai)](README.th.md)

# AGQuota-Swarm (`/agquota-swarm`)

**สกิลจัดทัพ Multi-Model Swarm แบบเช็กโควต้า `%` สดอัตโนมัติ สำหรับ Antigravity (ใช้ได้ทั้งในหน้า Antigravity App และ Antigravity IDE)**

AGQuota-Swarm จะช่วยตรวจสอบโควต้า `%` ที่เหลืออยู่จริงของแต่ละโมเดลใน Antigravity (`Gemini 4 Argon`, `Gemini 4 Neon`, `Gemini 4 Hydrogen`, `Claude Opus 5.5`, `Claude Sonnet 5.5`, `GPT-OSS 120B` และอื่นๆ) แล้วกระจายงานให้ worker ทำงานขนานกันอย่างปลอดภัย ไม่แก้ไขไฟล์ชนกัน พร้อมโหมดดูรายชื่อทีมก่อนสั่งรันจริง

---

## จุดเด่นของ AGQuota-Swarm

- **บาลานซ์โควต้าอัตโนมัติ:** เรียก `swarm(action="models", all=True)` ทุกครั้งก่อนเปิด worker เพื่อไม่ให้โควต้าโมเดลหลักหมดเร็วเกินไป
- **เลือกโหมดการทำงานได้ 2 แบบ:**
  - **Council & Blueprint Mode (`/agquota-swarm วางแผนก่อน <งาน>` หรือเมื่อใช้ 3+ workers):** ประชุมวางแผนก่อนด้วยมุมมองสถาปัตยกรรม หลักคิดตั้งต้น และคุณภาพงาน แล้วแสดง **ตารางพิมพ์เขียวทีม (Swarm Blueprint)** ระบุสกิลหลัก โหมดเสริม MCP โมเดล effort โควต้า `%` และขอบเขตไฟล์ให้ตรวจอนุมัติก่อนสร้าง worker
  - **Fast-Track Launch Mode (`/agquota-swarm <งาน>` สำหรับ 1–2 workers หรือสั่ง *"ลุยเลย"*):** เช็กโควต้า จับคู่สกิล/MCP ลงในใบสั่งงาน เปิด Swarm UI และสรุปผลให้ทันที
- **กำหนดสกิลและ MCP รายตัว (1 สกิลหลัก + สูงสุด 2 โหมดเสริม):** ส่งใบสั่งงานโครงสร้าง 5 บรรทัดให้ worker แต่ละตัวอ่าน `SKILL.md` และใช้ MCP ที่อนุญาต ส่วนคำสั่งโต้ตอบกับผู้ใช้อย่าง `/learn` จะทำที่ระดับ coordinator หลังจบงานเท่านั้น
- **แบ่งขอบเขตไฟล์ชัดเจน:** ป้องกัน worker แก้ไฟล์ทับกัน (`inherit` เมื่อไฟล์ไม่ซ้อนทับ หรือ `share`/`branch` เมื่อทำงานในโค้ดเบสเดียวกัน)
- **พกพาสะดวก ไร้ข้อมูลส่วนตัว:** ติดตั้งได้ทุกไดรฟ์และทุกระบบปฏิบัติการ (Windows, macOS, Linux) ไม่มี path ส่วนตัวหรือ API key ปะปนใน Repo

---

## การติดตั้ง (ลงได้ทุกไดรฟ์ / ทุกระบบ)

Clone Repo นี้ไปไว้ที่ไหนก็ได้ตามต้องการ (เช่น `C:\`, `D:\`, `~/tools/`):

```bash
git clone https://github.com/<your-org>/agquota-swarm.git
cd agquota-swarm
```

### Windows (PowerShell)

```powershell
# ทดสอบดู path ปลายทางก่อนติดตั้งจริง
./scripts/install.ps1 -WhatIf

# ติดตั้ง (คัดลอก SKILL.md ไปยัง %USERPROFILE%\.gemini\config\skills\agquota-swarm\)
./scripts/install.ps1

# ทางเลือก: ติดตั้งแบบ Symlink (ต้องเปิด Developer Mode หรือรันแบบ Admin)
./scripts/install.ps1 -Symlink

# ทางเลือก: ระบุโฟลเดอร์ปลายทางเอง
./scripts/install.ps1 -TargetDir "X:\custom\skills\agquota-swarm"
```

### macOS / Linux

```bash
chmod +x ./scripts/install.sh
./scripts/install.sh

# ทางเลือก: ใช้ Symlink แทนการคัดลอก
./scripts/install.sh --symlink

# ทางเลือก: ระบุโฟลเดอร์ปลายทางเอง
./scripts/install.sh --target "/custom/path/skills/agquota-swarm"
```

### ติดตั้งด้วยตนเอง

คัดลอกไฟล์ `SKILL.md` ไปวางในโฟลเดอร์สกิลของ Antigravity:
- Windows: `%USERPROFILE%\.gemini\config\skills\agquota-swarm\SKILL.md`
- macOS / Linux: `~/.gemini/config/skills/agquota-swarm/SKILL.md`

---

## การตรวจสอบความถูกต้อง

รันสคริปต์ตรวจสอบโครงสร้างไฟล์และสแกนหาข้อมูลลับ/path ส่วนตัว:

```bash
python tests/validate_repo.py
```

---

## สัญญาอนุญาตและคำชี้แจง

เผยแพร่ภายใต้ [MIT License](LICENSE)

*หมายเหตุ: AGQuota-Swarm เป็นโปรเจกต์ Open Source อิสระ ไม่ได้มีความเกี่ยวข้อง สนับสนุน หรือรับรองอย่างเป็นทางการจาก Google, Anthropic หรือ OpenAI*
