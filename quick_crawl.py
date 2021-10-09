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

    print("---- start crawling ----")

    pool = mp.Pool(processes = 20)
    results = pool.map(crawling, range(100000))

    with open("mapping.csv", "w") as f:
        for word_id, word in results:
            f.write(f"{word_id},{word}\n")

    print("---- end crawling ----")