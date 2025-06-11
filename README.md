# FixPad - Akshit

**FixPad** is a 3-key macropad designed to boost productivity and help you stay focused—whether you're studying, coding, or working. It features shortcut keys, website toggling, and even anti-sleep functionality to keep your computer awake when you are!

---

## Inspiration

I often found myself repeating the same actions—editing my millions of typing mistakes, opening tools/applications/websites, or keeping my laptop from sleeping during long research sessions (espeically to keep my code running throughout the night!). Instead of reaching for a full keyboard shortcut every time, I wanted a compact, dedicated helper. That’s where the idea of **FixPad** came from—a small macropad to automate simple but essential productivity tasks. 

---

## Features

- 3 mechanical keys, each mapped to a useful productivity function:
  - **Autocorrect** shortcut (after highlighting the text I want to edit, I press the button and it autocorrects the grammar and spelling for me)
  - **Website toggle** (open/close a designated URL by binding this key to any other key combination)
  - **Anti-sleep mode** (subtle mouse movements to keep the screen awake)
- Uses **KMK firmware** (Python-based, flexible)
- USB-powered, plug-and-play with any computer

---

## Hardware Specs

- **Microcontroller:** Seeed XIAO RP2040  
- **Switches:** 3× Cherry MX  
- **Keycaps:** 3× DSA profile  
- **Case:** Custom-designed, 2-part print (snap-fit, no screws!)

---

## CAD Design

- Designed in **TinkerCAD**
- Compact and portable (under 200×200 mm total size)
- Snap-fit case (no screws required)
- Clean separation between base and top housing in one `.stl` file

**Final Case File:** `FixPad.stl`

![Alt text](https://hc-cdn.hel1.your-objectstorage.com/s/v3/78de14682c3709a7524ff2030e27d2c7ab67444e_case1.png)
![Alt text](https://hc-cdn.hel1.your-objectstorage.com/s/v3/ba3ae3aac205f08522297d190cd3744027b3b67e_case2.png)

---

## PCB & Schematic

- Designed using **KiCad**
- Simple and optimized routing for beginners
- Easily modifiable for more buttons or RGB in future versions

**Final Schematic:** `FixPad_Schematic.kicad_sch`

![Alt text](https://hc-cdn.hel1.your-objectstorage.com/s/v3/1272fe644b1aa734ab4d0d3803552320e7c9b321_schematic.png)

**Final PCB Layout:** `FixPad_PCB.kicad_pcb`

![Alt text](https://hc-cdn.hel1.your-objectstorage.com/s/v3/359cfbdff54a60db288da27a50660031333753c7_pcb.png)

---

## Firmware

- Written in **Python** using the **KMK** firmware framework
- Easy to read, edit, and extend
- Autocorrect and tab toggle features use clever key sequences and clipboard shortcuts

**Firmware File:** `main.py`

---

## Bill of Materials (BOM)

| Item                  | Quantity |
|-----------------------|----------|
| Cherry MX Switches    | 3        |
| DSA Keycaps           | 3        |
| EC11 Rotary Encoder   | 1        |
| XIAO RP2040           | 1        |
| 3D-Printed Case       | 1 (2 parts) |

---

## Challenges

This was my first serious electronics + CAD project. I learned about:
- Schematic and PCB design using **KiCad**
- Mechanical CAD with **TinkerCAD** (with help from friends!)
- Writing event-based keyboard firmware in **Python**

---

## What's Next?

Future improvements I’d like to add:
- OLED screen support  
- Per-key RGB lighting  
- Multiple layers for macro switching  

---

> **Made for HackPad 2025 | Built with curiosity, trial, and lots of CTRL+C.**
