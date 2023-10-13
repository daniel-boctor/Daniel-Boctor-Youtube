import threading

def func(num):
    counter = 0
    for _ in range(num):
        counter += 1

def main():
    threads = [threading.Thread(target=func, args=(50_000_000,)) for _ in range(1, 5)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    import timeit
    print(f'RUNTIME IN SECONDS: {timeit.timeit(main, number=1):.2f}')