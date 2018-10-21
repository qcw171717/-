from encode_decode import *
import time

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'


if __name__ == '__main__':
	# 屏幕
	print()
	print(WARNING + 'Ctrl + c即可退出程序' + ENDC)
	print(FAIL + '测试对象若某一刻觉得太傻，请立刻Ctrl + c退出程序。' + ENDC)
	print('\n\n\n')
	time.sleep(2)
	print('为了最佳体验，请确保你的观看系统（Pycharm/Terminal/etc.）已调至为全屏模式。\n若测试对象为程序猿，请不要偷看下行代码，或试图找bug，谢谢配合。')
	inp = input('请输入\"可以\"以继续：\n')
	while inp != '可以':
		inp = input(FAIL + 'Hmm，想确认下你能输入中文。请输入\"可以\"以继续：\n' + ENDC)

	# 开始
	print(OKGREEN + '好滴嘞，完美。' + ENDC)
	for i in range (10):
		time.sleep(0.1)
		print()
	time.sleep(0.5)

	print('先乱入一只疑似Killer cat壮胆！')
	time.sleep(1)

	for i in range (5):
		time.sleep(0.1)
		print()
	time.sleep(1)
	print('_._     _,-\'\"\"`-._\n\
     (,-.`._,\'(       |\`-/|\n\
         `-.-\' \\ )-`( , o/ o)\n\
               `-    \\`_`\"\'-')
	time.sleep(1)
	for i in range (5):
		time.sleep(0.1)
		print()
	time.sleep(0.5)
	print('好嘞，你已进入主程序。')
	time.sleep(0.5)


	while (True):
		inp = input('你想\n1.解读信息\n2.加密信息\n请输入相应数字：')
		while inp != '1' and inp != '2':
			inp = input(FAIL + '暂时不接受' + inp + '选项。朋友请选1或者2😂\n' + ENDC)
		if inp == '1':
			encoded = input(HEADER + '好滴嘞，请输入你想解读的信息：' + ENDC)
			time.sleep(1)
			print('\n运算中...\n')
			for i in range (5):
				time.sleep(0.5)
				print('...\n')
			time.sleep(2)

			while (True):
				try:
					decode(encoded.strip())
					break
				except Exception:
					encoded = input('Hmm，要不再试试，或联系一下本程序的管理猿\n重新输入想解读的信息：')
					time.sleep(1)
					print('\n运算中...\n')
					for i in range (5):
						time.sleep(0.5)
						print('...\n')
					time.sleep(2)

			print('对以上内容如有评论/疑问/回答请微信联系本程序的管理猿。\n\n\n')

		if inp == '2':
			print('\n这边儿功能还不太完善，她很脆弱请小心操作。')
			time.sleep(0.5)
			to_decode = input(HEADER + '请输入你想加密的信息：' + ENDC)

			time.sleep(1)
			print('\n运算中...\n')
			for i in range (5):
				time.sleep(0.5)
				print('...\n')
			time.sleep(2)

			print()
			decode(to_decode)
			print()
			print('请复制粘贴以上加密信息微信发给给本程序的管理猿（目前Alpha测试阶段所有信息要通过中央控制）')





#decode('999 1006 1006 1006 1006 9 1000 68 75 7 1001 590 282 65 22 1002 657 90 186 1003 1004 1 43 1005 999 999 1006 1006 1006 1006 1006 1006 1006 1006 4 9 146 325 333 22 1007 22 267 35 574 1008 17 680 7 22 29 36 42 39 169 975 87 106 125 322 1009 999')







