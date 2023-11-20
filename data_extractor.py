import glob
from pathlib import Path


def get_diary_contents(filepath):
    with open(filepath,'r') as file:
        date = Path(filepath).stem
        return date,file.read()



def get_files():
    files = glob.glob("diary/*.txt")
    diary_dict= {}
    date =[]
    diary=[]
    for file in files:
        contents = get_diary_contents(file)
        date.append(contents[0])

        diary.append(contents[1])
    diary_dict['date'] = date
    diary_dict['diary'] = diary

    return diary_dict

if __name__  == "__main__":
    print(get_files())