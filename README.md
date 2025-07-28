# Installation

> [!NOTE]  
> **Creating a virtual environment is optional. You can skip to step 3 if you’re not interested in using one.**

1. **Create a virtual environment (optional):**  
   ```bash
   sudo apt install python3.12-venv
   python -m venv venv
   ```

2. **Activate the virtual environment:**  
   ```bash
   source venv/bin/activate
   ```

3. **Install the dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Chromium and Chromedriver:**  
   ```bash
   sudo apt update
   sudo apt install -y chromium-browser chromium-chromedriver
   ```

5. **You're ready to go! 🚀**

---

# Compatibility

- [ ] xx530  
- [ ] xx530v2  
- [ ] EX520  
- [ ] EX511  
- [ ] EX220  
- [ ] EX141  
- [ ] G5  
- [ ] C5  
- [ ] C20  

---

# Example Usage

```bash
python main.py --url 192.168.2.254 --senha admin@7777 --pppoe 1234andzilla --modelo xx530
```

**Notes:**

- The `--url` must use `http` or `https`.
- All flags are required and must not be empty.

## Available Flags

| Flag        | Description                |
|-------------|----------------------------|
| `--url`     | Router URL                 |
| `--senha`   | Router password            |
| `--pppoe`   | PPPoE login                |
| `--modelo`  | Router model               |

---

# To-Do

- [ ] Test compatibility with more TP-LINK models  
- [ ] Automatic model detection  
- [x] Allow IP-only in `--url` (without protocol)  
- [ ] Add `/superadmin` to router URL automatically  
- [ ] Add more arguments:
  - [ ] `--band_steering <yes|no>`  
  - [ ] `--ssid "WiFi name"`  
  - [ ] `--ssid_pass "WiFi password"`  
- [x] Make all arguments required by default  
- [x] Validate input data before execution  
- [x] Run in background by default  
- [x] Run without needing a browser installed  
- [x] Tested on Linux  
- [x] Validate router URL and password  
- [x] Tested on Ubuntu Server  
- [x] Log all automation actions to terminal  
- [x] Create a logs directory  
