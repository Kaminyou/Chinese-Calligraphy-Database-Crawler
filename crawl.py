import requests

if __name__ == "__main__":
    with open("mapping.csv", "w") as f:
        for i in range(80000, 100000):
            r = requests.get(f"https://www.cns11643.gov.tw/wordWrite.jsp?ID={i}")
            if "<caption>法帖查詢：" in r.text:
                idx = r.text.find("<caption>法帖查詢：")
                extract = r.text[idx:idx+30]
                word = extract.split("[")[1].split("]")[0]
                print(f"{i:<6} || {word}")
                f.write(f"{i},{word}\n")
            else:
                print(f"{i:<6} || None")
