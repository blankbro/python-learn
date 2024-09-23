def make_pretty(func):
    def inner():
        print("我被装饰了")
        func()

    return inner


@make_pretty
def ordinary():
    print("我是普通的函数")


if __name__ == "__main__":
    ordinary()
