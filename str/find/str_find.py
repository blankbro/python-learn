def find_kv(line) -> [str, str]:
    line = line.strip()
    index = line.find(":")
    if index == -1:
        index = line.find("：")
        if index == -1:
            return

    key = line[:index].strip()
    value = line[index + 1:].strip()
    return key, value


if __name__ == '__main__':
    line = "回复内容：123"
    key, value = find_kv(line)
    print(f"key = {key}, value = {value}")
