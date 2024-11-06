import os
while 1:
    print('''
————————————————————————————————————————————————————————adb工具————————————————————————————————————————————————————————————————————————
    请输入选项：
    
        (1)查看已连接的设备
        (2)安装软件
        (3)卸载软件
        (4)启动软件
        (5)重启设备
        (6)列出所有第三方软件
        (7)按下home键
        (8)按下返回键
        (9)按下多任务键
        (10)按下菜单键
        (11)连接WLAN设备:
    ''')
    it = input('')
    if it == '1':
        os.system("adb devices")
    elif it == '2' :
        irj = input('输入安装包路径（系统不会自动转义斜杠）')
        os.system("adb install "+irj)
    elif it == '3' :
        irj = input('请输入软件包名：')
        os.system("adb uninstall "+irj)
    elif it == '4' :
        irj = input('请输入包名和activity,用空格隔开：')
        irj = irj.split()
        os.system("adb shell am start "+irj[0]+"/"+irj[1])
    elif it == '5' :
        a = input('''请输入选项：
        (1) 重启到rec
        (2) 重启到fastboot
        (3) 重启到9008
        (4) 重启到挖煤
        (5) 重启到bootloader
        (6)普通重启
        ''')
        if a == '1':
            os.system("adb reboot recovery")
        elif a == '2' :
            os.system("adb reboot fastboot")
        elif a == '3' :
            os.system("adb reboot edl")
        elif a == '4' :
            os.system("adb reboot download")
        elif a == '5' :
            os.system("adb reboot bootloader")
        elif a == '6' :
            os.system("adb reboot")
        else :
            print('输入错误！')
    elif it == '6' :
        os.system("adb shell pm list packages -3")
    elif it == '7' :
        os.system("adb shell input keyevent KEYCODE_HOME")
    elif it == '8' :
        os.system("adb shell input keyevent BACK")
    elif it == '9' :
        os.system("adb shell input keyevent 187")
    elif it == '10' :
        os.system("adb shell input keyevent 82")
    elif it == '11' :
        ip = input('请输入ip: ')
        os.system("adb connect "+ip)
    else :
        print('输入错误！')
