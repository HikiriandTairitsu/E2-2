# 导入time模块
import time

# 定义专注段和休息段的时间（单位为秒）
focus_time = 25 * 60
break_time = 5 * 60
long_break_time = 15 * 60

# 定义专注段的数量
focus_count = 0

# 定义一个函数，用于显示倒计时
def countdown(seconds):
    # 将秒数转换为分和秒
    minutes = seconds // 60
    seconds = seconds % 60
    # 循环显示倒计时
    while minutes >= 0 and seconds >= 0:
        # 用\r来覆盖上一行的输出
        print(f"\r{minutes:02d}:{seconds:02d}", end="")
        # 每隔一秒更新一次
        time.sleep(1)
        seconds -= 1
        # 如果秒数为-1，说明一分钟已过，将分钟数减一，秒数重置为59
        if seconds == -1:
            minutes -= 1
            seconds = 59

# 定义一个函数，用于播放提示音
def beep():
    # 用\a来发出提示音
    print("\a")

# 定义一个主函数，用于运行专注时钟
def main():
    # 声明全局变量focus_count
    global focus_count
    # 打印欢迎信息
    print("欢迎使用专注时钟！")
    # 询问用户是否开始专注
    start = input("是否开始专注？（y/n）")
    # 如果用户输入y，开始专注
    if start == "y":
        # 进入一个无限循环
        while True:
            # 打印专注段的信息
            print(f"这是第{focus_count + 1}个专注段，持续时间为{focus_time // 60}分钟。")
            # 调用倒计时函数，传入专注时间
            countdown(focus_time)
            # 播放提示音
            beep()
            # 将专注段的数量加一
            focus_count += 1
            # 判断是否需要长休息
            if focus_count % 4 == 0:
                # 打印长休息的信息
                print(f"恭喜您完成了{focus_count}个专注段，您可以享受{long_break_time // 60}分钟的长休息。")
                # 调用倒计时函数，传入长休息时间
                countdown(long_break_time)
                # 播放提示音
                beep()
            else:
                # 打印短休息的信息
                print(f"您已完成了{focus_count}个专注段，您可以享受{break_time // 60}分钟的短休息。")
                # 调用倒计时函数，传入短休息时间
                countdown(break_time)
                # 播放提示音
                beep()
            # 询问用户是否继续专注
            continue_ = input("是否继续专注？（y/n）")
            # 如果用户输入n，退出专注
            if continue_ == "n":
                # 打印结束信息
                print("感谢您使用专注时钟，祝您工作顺利！")
                # 退出程序
                break

# 调用主函数
main()
