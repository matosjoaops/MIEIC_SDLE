import zmq

context = zmq.Context()

us_zip_filter = "10001"
us_port = "5556"

pt_zip_filter = "1001"
pt_port = "5557"

print("Collecting updates from the weather servers...")
us_socket = context.socket(zmq.SUB)
us_socket.connect(f"tcp://localhost:{us_port}")
us_socket.setsockopt_string(zmq.SUBSCRIBE, us_zip_filter)

pt_socket = context.socket(zmq.SUB)
pt_socket.connect(f"tcp://localhost:{pt_port}")
pt_socket.setsockopt_string(zmq.SUBSCRIBE, pt_zip_filter)

poller = zmq.Poller()
poller.register(us_socket, zmq.POLLIN)
poller.register(pt_socket, zmq.POLLIN)

us_total_temp = 0
pt_total_temp = 0
us_update_nbr = 0
pt_update_nbr = 0

while True:
    try:
        socks = dict(poller.poll())
    except KeyboardInterrupt:
        break

    if us_socket in socks:
        string = us_socket.recv_string()
        zipcode, temperature, relhumidity = string.split()
        us_total_temp += int(temperature)
        us_update_nbr += 1
        print((f"Average temperature for US zipcode " f"'{us_zip_filter}' was {us_total_temp / (us_update_nbr)} F"))

    if pt_socket in socks:
        string = pt_socket.recv_string()
        zipcode, temperature, relhumidity = string.split()
        pt_total_temp += int(temperature)
        pt_update_nbr += 1
        print((f"Average temperature for PT zipcode " f"'{pt_zip_filter}' was {pt_total_temp / (pt_update_nbr)} F"))
    
    if pt_update_nbr >= 5 and us_update_nbr >= 5:
        break
