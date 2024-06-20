# Uncomment this to pass the first stage
import socket
import concurrent.futures

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, addr = server_socket.accept() # wait for client

    pong = "+PONG\r\n"

    def send_pong():
        while True:
            data = conn.recv(1024)
            if data:
                conn.send(pong)
            else:
                break
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(send_pong)


if __name__ == "__main__":
    main()
