#test another file here
from tqdm import tqdm
import time

# for i in tqdm (range (10), desc="Loading..."):
#     print(i)
#     time.sleep(0.5)

word_list = ["hello", "hello", "hello", "hello"]

# for index, word in tqdm (enumerate(word_list), desc="Loading..."):
#     print(word)
#     time.sleep(0.5)

for i in tqdm(range(len(word_list)), desc="loading..."):
    time.sleep(1)