# 单例装饰器
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register(self, name: str, desire_priority: int = 0, **kwargs):
        def wrapper(plugin_cls):
            plugin_cls.name = name
            plugin_cls.priority = desire_priority
            plugin_cls.desc = kwargs.get("desc")
            plugin_cls.author = kwargs.get("author")
            plugin_cls.version = kwargs.get("version") if kwargs.get("version") != None else "1.0"
            plugin_cls.namecn = kwargs.get("namecn") if kwargs.get("namecn") != None else name
            plugin_cls.hidden = kwargs.get("hidden") if kwargs.get("hidden") != None else False
            plugin_cls.enabled = True
            self.plugins[name.upper()] = plugin_cls

        return wrapper


instance = PluginManager()

register = instance.register


@register(
    name="Hello",
    desire_priority=100,
    hidden=True,
    desc="A simple plugin that says hello",
    version="1.0",
    author="lanvent",
)
class Hello:

    def __init__(self):
        print("Hello __init__")

    def test(self):
        print("Hello hello!")


if __name__ == "__main__":
    print("hello main")
    hello = instance.plugins["HELLO"]()

    # hello = Hello()
    hello.test()
