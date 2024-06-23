# Uncomment this to pass the first stage
import socket
import concurrent.futures

def handle_client(conn):
    while True:
        data = conn.recv(1024)
        if data:
            pong = b"+PONG\r\n"
            conn.send(pong)
        else:
            break

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)

    try:
        while True:
            conn, addr = server_socket.accept() # wait for client
            print(f"Got connection from {addr}")
    
            executor.submit(handle_client, conn)
    except:
        print("Server shutting down...")
    

if __name__ == "__main__":
    main()
