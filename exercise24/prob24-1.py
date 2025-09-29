import re


def split_my_info(info):
    split_info = re.split(":", info)
    split_id = re.split("My ID", split_info[1])
    number = re.search(r'\d+', split_id[1])
    print(f"My name is {split_id[0]}\nMy ID is {number.group()}")


if __name__ == "__main__":
    my_info = "My name:Yen DaHwaMy ID is abc6630407563xyz"
    split_my_info(my_info)