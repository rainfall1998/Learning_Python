from tqdm import tqdm
from time import sleep

if __name__ == '__main__':
    #############################
    # text = ''
    # for char in tqdm(["a", "b", "c", "d"]):
    #     sleep(0.25)
    #     text = text + char
    # print(text)
    ############################
    # pbar = tqdm(["a", "b", "c", "d"])
    # for char in pbar:
    #     sleep(0.25)
    #     pbar.set_description("Processing %s" % char)
    ############################
    pbar = tqdm(total=1000,colour='green')
    for i in range(100):
        sleep(0.1)
        pbar.set_description("Processing %s" % i)
        pbar.update(10)
    pbar.close()