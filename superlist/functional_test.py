from selenium import webdriver

br = webdriver.Firefox()
br.get('http://localhost:8000')

assert 'successfully' in br.title