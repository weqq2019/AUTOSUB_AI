from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService


# 指定 chromedriver.exe 文件的路径
service =ChromeService(executable_path=r"C:\path\to\chromedriver.exe")

# 创建 Chrome 浏览器实例
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# driver = webdriver.Chrome(driver_path, options=options)
driver = webdriver.Chrome(service=service, options=options)



# 打开网页
driver.get("https://www.google.com")

# 在搜索框中输入关键字
search_box = driver.find_element_by_name("q")
search_box.send_keys("Python")
search_box.send_keys(Keys.RETURN)

# 等待搜索结果加载完成
driver.implicitly_wait(10)

# 获取搜索结果
results = driver.find_elements_by_css_selector("div.g")

# 输出搜索结果标题和链接
for result in results:
    title = result.find_element_by_css_selector("h3").text
    link = result.find_element_by_css_selector("a").get_attribute("href")
    print(title, link)

# 关闭浏览器
driver.quit()