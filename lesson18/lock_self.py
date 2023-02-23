from threading import Lock

l = Lock()

def do_some():
    with l:
        print('doing')

if __name__ == '__main__':
    with l:
        print("hi")
        do_some()