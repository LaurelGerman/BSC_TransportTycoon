FACTORY_TO_PORT = 2
PORT_TO_A = 4
FACTORY_TO_B = 5

#reverse version of above -- relevant for multiple trips to same dest
PORT_TO_FACTORY = FACTORY_TO_PORT
A_TO_PORT = PORT_TO_A
B_TO_FACTORY = FACTORY_TO_B


class Transport:
    """reps boats n trucks
    """
    def __init__(self, idle_time=0):
        self._idle_time = idle_time

    def on_return(self, arrival_time):
        self._idle_time = arrival_time

    def idle_time(self):
        return self._idle_time


def last_delivery_time(container_schedule):
    all_trucks = [Transport(), Transport()]
    ship = Transport()
    delivery_times = []

    for destination in container_schedule:
        truck = min(all_trucks, key=lambda t: t.idle_time())
        if "A" == destination:
            leave_factory = truck.idle_time()
            arrive_at_port = leave_factory + FACTORY_TO_PORT
            leave_port_at = max(
                arrive_at_port,
                ship.idle_time()
            )
            delivery_time = leave_port_at + PORT_TO_A
            truck_return = arrive_at_port + PORT_TO_FACTORY
            truck.on_return(truck_return)
            ship_return = delivery_time + A_TO_PORT
            ship.on_return(ship_return)
            delivery_times.append(delivery_time)
        if "B" == destination:
            leave_factory = truck.idle_time()
            delivery_time = leave_factory + FACTORY_TO_B
            truck_return = delivery_time + B_TO_FACTORY
            truck.on_return(truck_return)
            delivery_times.append(delivery_time)

    return max(delivery_times)
