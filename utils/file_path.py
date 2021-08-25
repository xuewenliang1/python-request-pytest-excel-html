import os

def get_path():
    file_path=os.path.dirname(os.path.dirname(__file__))
    new_path=os.path.join(file_path,"testfile","ceshi.xlsx")
    print(new_path)
    return new_path

if __name__ == '__main__':
    get_path()