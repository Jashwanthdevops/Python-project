import threading
import requests
import random
import string

created = 0
errors = 0


def random_string(size=10):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(size))


def worker():
    global created, errors

    try:
        response = requests.get("https://httpbin.org/get", timeout=5)

        if response.status_code == 200:
            created += 1
            print(f"Success: {created}")
        else:
            errors += 1

    except Exception as e:
        print("Error:", e)
        errors += 1


if __name__ == "__main__":
    threads = []

    for _ in range(5):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("Finished")
    print("Success:", created)
    print("Errors:", errors)
