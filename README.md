![Main_Banner](assets/main_banner.png)
---
>**INFO**
>
>I will try to activly update this repo on changes
>
>If you encounter any error, ask under Issues or search before asking

**Full Setup**

Still WIP, only one script at a time

## Already made Scripts
![Logo](assets/nexusmods_banner.png)

**Still WIP**

The Downloader is able to get a direct downloadlink for your downloadmanagers or can directly download a list of mods (specififed in a text file) using curl.

**Features**
- [x] Bugfixing (Problems with Seleniums Element Finder)
- [x] Time Optimizing
- [x] Downloading of required Mods (Automatic)
- [ ] Building to Binary
- [ ] GUI

---
![Logo](assets/fuckingfast_banner.png)
Get direct download links from fuckingfast.co for your Download Manager

**Installation**

*Global*
```bash
  git clone https://github.com/fruhansen/HosterFusion/
  cd HosterFusion/fuckingfast.co/

  #Install requirements
  pip install -r requirements.txt
```

*Virtual Enviroment*
```bash
  git clone https://github.com/fruhansen/HosterFusion/
  cd HosterFusion/fuckingfast.co/

  #Create venv
  python -m venv venv
  #activate
  venv\Scripts\activate

  #Install requirements in venv
  pip install -r requirements.txt
```

**Help**

```
  usage: app.py [-h] --filepath FILEPATH [--save]

A Wrapper for the File Hoster fuckingfast.co!

options:
  -h, --help            show this help message and exit
  --filepath FILEPATH, -f FILEPATH
                        Enter path to your URL List file
  --save, -s

  Made by @fruhansen
```
