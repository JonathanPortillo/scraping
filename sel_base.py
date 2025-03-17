from seleniumbase import Driver

driver = Driver(uc=True)
url = "https://www.indeed.com/jobs?q=software+engineer&l=Thousand+Oaks%2C+CA&from=searchOnDesktopSerp%2Cwhatautocomplete&vjk=0c81e5d45f483dc8"
driver.uc_open_with_reconnect(url, 4)
driver.uc_gui_click_captcha()
# Save the page source to an HTML file
with open("software.html", "w", encoding="utf-8") as file:
    file.write(driver.page_source)
driver.quit()