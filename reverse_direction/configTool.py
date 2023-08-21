import configparser

from typing import Any, Dict

conf = configparser.ConfigParser()

# 获取用户数量
def user_info_total(file:str) -> int:
    conf.read(file)
    return len(conf.sections())

# 保留用户信息
def add_user_info(file:str, section:str, **kwargs) -> None :
    # 初始化
    # conf = configparser.ConfigParser()
    # 获取配置文件
    conf.read(file, encoding='utf-8')
    
    # 添加section
    conf.add_section(section)

    # 设置section下option的value
    for key in kwargs.keys():
        conf.set(section, key, kwargs[key])

    with open(file, 'w', encoding='utf-8') as f:
        conf.write(f)
    
# 判断用户是否存在
def has_user_info(file:str, section:str) -> bool:
    conf.read(file)

    if not conf.has_section(section):
        return False
    else:
        return True
    
# 列出用户
def print_user_info(file:str) -> None:
    conf.read(file)

    print('已存在用户')
    for section in conf.sections():
        print(f"1\t{conf.get(section, 'username')}")

# 选择用户
def select_user_info(file:str, section:str) -> Dict:
    conf.read(file)

    return {'user': conf.get(section, 'username'), 'pwd': conf.get(section, 'password')}



if __name__ == '__main__':
    print(user_info_total('config.ini'))
    # if has_user_info('config.ini', 'User'):
    #     print_user_info('config.ini', 'User')
    # else:
    #     add_user_info('config.ini', 'User', username='209030111', password='3174511')
