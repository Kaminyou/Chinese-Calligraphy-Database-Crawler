import time
import requests
import multiprocessing as mp

def crawling(word_id):
    r = requests.get(f"https://www.cns11643.gov.tw/wordWrite.jsp?ID={word_id}")
    print(f"{word_id}", end = "\r")
    if "<caption>法帖查詢：" in r.text:
        idx = r.text.find("<caption>法帖查詢：")
        extract = r.text[idx:idx+30]
        word = extract.split("[")[1].split("]")[0]
        return (word_id, word)
    else:
        return (word_id, "NA")


if __name__ == "__main__":
    for i in range(20):
        print(f"---- start crawling {i} ----")

        pool = mp.Pool(processes = 100)
        results = pool.map(crawling, range(80000 + i * 1000, 80000 + (i + 1) * 1000))

        with open("mapping.csv", "a") as f:
            for word_id, word in results:
                f.write(f"{word_id},{word}\n")

        print("---- end crawling ----")
        time.sleep(20)