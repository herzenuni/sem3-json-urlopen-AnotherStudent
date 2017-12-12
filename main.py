from urllib.request import urlopen
import json
import pprint

print('Введите свой id:')
id = input()

request = "https://api.vk.com/method/users.get?user_ids={id}&fields=nickname,sex,city,site&v=5.69".format(id = id)
print('Сформированный запрос:', request)

try:
	request_obj = urlopen(request)
	obj = json.loads(request_obj.read())
except:
	print('Ошибка соединения с сервером!, Проверьте соединение!')

if obj.get('response') != None:
	print('Ответ сервера:')
	pprint.pprint(obj)
else:
	if obj.get('error'):
		print('Сервер вернул ошибку:')
		pprint.pprint(obj['error'])
	else:
		print('Неизвестная ошибка!');

