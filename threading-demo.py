import time
import concurrent.futures

def work(n):
    print(f'I am going to sleep {n} seconds')
    time.sleep(n)
    return f'I slept {n} seconds'


if __name__ == "__main__":
    time_sleep = [5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(work, time_sleep)

        for result in results:
            print(result)


    end_time = time.time()

    print(f'T = {end_time - start_time}')