import multiprocessing

def func(num):
    counter = 0
    for _ in range(num):
        counter += 1

def main():
    processes = [multiprocessing.Process(target=func, args=(50_000_000,)) for _ in range(1, 5)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

if __name__ == "__main__":
    import timeit
    print(f'RUNTIME IN SECONDS: {timeit.timeit(main, number=1):.2f}')