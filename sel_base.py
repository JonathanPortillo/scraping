from seleniumbase import Driver

driver = Driver(uc=True)
url = "https://www.indeed.com/l-Thousand-Oaks,-CA-jobs.html?vjk=3cad71c3648c3c7a"
driver.uc_open_with_reconnect(url, 4)
driver.uc_gui_click_captcha()
# Save the page source to an HTML file
with open("gitlab_sign_in.html", "w", encoding="utf-8") as file:
    file.write(driver.page_source)
driver.quit()