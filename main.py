import socket
import threading
import time

def computer_1():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 12345))
    s.listen(1)
    print("[Computer 1] Czekanie na połączenie...")
    conn, addr = s.accept()
    print("[Computer 1] Połączono z", addr)

    try:
        while True:
            # Odbieranie wiadomości
            received_message = conn.recv(1024).decode("utf-8")
            if not received_message:
                break
            print("[Computer 1] Otrzymano:", received_message)

            # Wysyłanie wiadomości
            response_message = input("[Computer 1] Wpisz wiadomość: ")
            conn.send(response_message.encode("utf-8"))

    except KeyboardInterrupt:
        pass
    finally:
        conn.close()
        s.close()

def computer_2():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(1)
    s.connect(("127.0.0.1", 12345))

    try:
        while True:
            # Wysyłanie wiadomości
            message = input("[Computer 2] Wpisz wiadomość: ")
            s.send(message.encode("utf-8"))

            # Odbieranie wiadomości
            response = s.recv(1024).decode("utf-8")
            if not response:
                break
            print("[Computer 2] Otrzymano:", response)

    except KeyboardInterrupt:
        pass
    finally:
        s.close()

t1 = threading.Thread(target=computer_1)
t2 = threading.Thread(target=computer_2)

t1.start()
t2.start()

t1.join()
t2.join()

print("Symulacja zakończona.")
