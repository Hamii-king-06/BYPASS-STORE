import platform

arch = platform.uname().machine
if 'aarch' in arch:
	import esesbe
	esesbe.main()
else:
	exit(' only 64bit supported!')
