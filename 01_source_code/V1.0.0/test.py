# import zipfile
# import io
# import os

# import requests
# driver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# # options= r"D:\BaiduSyncdisk\LQ\Code\M17\AutoSub\AutoSub2.0\chorme95+\App\chrome.exe"

# ""

# print(os.path.exists(driver_path))
# # print(os.path.exists(options))




# CHROMEDRIVER_URL = f'https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_win32.zip'
# response = requests.get(CHROMEDRIVER_URL)

# # 解压缩并移动到指定目录下
# with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
#     zip_file.extractall('C:/chromedriver')

# # 将ChromeDriver路径添加到系统环境变量中
# os.environ['PATH'] += ';C:/chromedriver'
print("看看在哪个环境运行")