# WeblogicScan

Forked from https://github.com/dr0op/WeblogicScan

# Install

```
pip3 install -r requirements.txt
```

# Usage

```
Usage :
	python3 WeblogicScan.py -u [URL]
	python3 WeblogicScan.py -f [FILENAME]
	python3 WeblogicScan.py -n [CVE]
	python3 WeblogicScan.py -n [CVE] -e [CMD]
Example :
	python3 WeblogicScan.py -u http://127.0.0.1:7001/
	python3 WeblogicScan.py -f targets.txt
	python3 WeblogicScan.py -n CVE-2019-2725
	python3 WeblogicScan.py -n CVE-2019-2725 -e whoami
```

# Diff

支持批量检测，检测结果记录在 `Weblogic.log`

支持 HTTPS

支持单个漏洞检测 / 一键利用

添加了对 Weblogic 12.1.3 `CVE-2019-2725` / `CVE-2019-2729` 检测

添加 `pocs/CVE-2020-2551.py`

添加 `exps/CVE-2019-2725.py`

添加 `exps/CVE-2019-2729.py`

# Todo

添加 `pocs/CVE-2020-2555.py`

添加 `pocs/CVE-2020-2883.py`

添加对部分漏洞的一键利用（无需外连 / 多版本适用）

更新 / 删除年代比较久远的 POC 