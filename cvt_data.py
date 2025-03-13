from pandas import Timestamp

def cvt_data(text):
    text = text.split("/")
    text = Timestamp(int(text[2]), int(text[1]), int(text[0]))
    return text

def cvt_data_fra(text):
    text = text.split("-")
    text = Timestamp(int(text[0]), int(text[1]), int(text[2]))
    return text

if __name__ == "__main__":
    data = "27/04/2024"
    data2 = "2020-03-19"

    data = cvt_data(data)
    data2 = cvt_data_fra(data2)

    print(data)
    print(data2)