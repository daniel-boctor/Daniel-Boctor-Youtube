import multiprocessing

counter = multiprocessing.Value('i', 0)

def func(num, counter):
    for _ in range(num):
        counter.value += 1

def main():
    processes = [multiprocessing.Process(target=func, args=(1_000_000, counter)) for _ in range(1, 5)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(f'SHARED COUNTER VALUE: {counter.value}')

if __name__ == "__main__":
    import timeit
    print(f'RUNTIME IN SECONDS: {timeit.timeit(main, number=1):.2f}')