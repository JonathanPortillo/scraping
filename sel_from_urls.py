from seleniumbase import Driver
import time
# driver = Driver(uc=True)
# url = "https://www.indeed.com/jobs?q=software+engineer&l=Thousand+Oaks%2C+CA&from=searchOnDesktopSerp%2Cwhatautocomplete&vjk=0c81e5d45f483dc8"
# driver.uc_open_with_reconnect(url, 4)
# driver.uc_gui_click_captcha()
# # Save the page source to an HTML file
# with open("software.html", "w", encoding="utf-8") as file:
#     file.write(driver.page_source)
# driver.quit()

def read_urls_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        urls = [line.strip() for line in file.readlines()]
    return urls

urls = read_urls_from_file("job_links.txt")

print(urls)
count = 0
driver = Driver(uc = True)
for url in urls:
    driver.uc_open_with_reconnect(url, 4)
    with open(f"{count}.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    time.sleep(2)
    count += 1

