FACTORY_TO_PORT = 1
PORT_TO_A = 4
FACTORY_TO_B = 5

PORT_TO_FACTORY = FACTORY_TO_PORT
A_TO_PORT = PORT_TO_A
B_TO_FACTORY = FACTORY_TO_B


class Transport:
    def __init__(self, idle_time=0):
        self._idle_time = idle_time

    def on_return(self, arrival_time):
        self._idle_time = arrival_time

    def idle_time(self):
        return self._idle_time


def last_delivery_time(container_schedule):
    fleet = [Transport(), Transport()]
    ship = Transport()
    delivery_times = []

    for destination in container_schedule:
        best_truck = min(fleet, key=lambda t: t.idle_time())
        if "A" == destination:
            leave_factory = best_truck.idle_time()
            arrive_at_port = leave_factory + FACTORY_TO_PORT
            leave_port_at = max(
                arrive_at_port,
                ship.idle_time()
            )
            arrive_at_a = leave_port_at + PORT_TO_A
            truck_return = arrive_at_port + PORT_TO_FACTORY
            best_truck.on_return(truck_return)
            ship_return = arrive_at_a + A_TO_PORT
            ship.on_return(ship_return)
            delivery_times.append(arrive_at_a)
        if "B" == destination:
            leave_factory = best_truck.idle_time()
            arrive_at_b = leave_factory + FACTORY_TO_B
            truck_return = arrive_at_b + B_TO_FACTORY
            best_truck.on_return(truck_return)
            delivery_times.append(arrive_at_b)

    return max(delivery_times)
