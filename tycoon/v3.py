FACTORY_TO_PORT = 2
PORT_TO_A = 4
FACTORY_TO_B = 5

#reverse version of above -- relevant for multiple trips to same dest
PORT_TO_FACTORY = FACTORY_TO_PORT
A_TO_PORT = PORT_TO_A
B_TO_FACTORY = FACTORY_TO_B


class Transport:
    """reps boats n trucks. self._idle_time is more like
    total travel time for the isntance of transport
    """
    def __init__(self, idle_time=0):
        self._idle_time = idle_time

    def on_return(self, arrival_time):
        self._idle_time = arrival_time

    def idle_time(self):
        return self._idle_time


def get_truck_travel_time(transport, travel_time):
    """
    Trucks currently only transport a single package
    (so travel_time to and from a destination are the same)
    """
    leave_factory = transport.idle_time()
    reach_dest = leave_factory + travel_time
    transport.on_return(reach_dest + travel_time)
    return transport.idle_time()

def get_ship_travel_time(portDeliveryTimesList):
    """
    """
    firstArrivalAtPort = portDeliveryTimesList[0]
    shipTrips = 0
    if len(portDeliveryTimesList) > 1\
    and portDeliveryTimesList[0] == portDeliveryTimesList[1]:
        del portDeliveryTimesList[1], portDeliveryTimesList[0]
        shipTrips += 1
    while portDeliveryTimesList:
        _presentPackages = [i for i in portDeliveryTimesList if i <= (shipTrips * PORT_TO_A * 2)]
        print("_presentPackages:", _presentPackages)
        # _presentPackages = list()
        # for i in portDeliveryTimesList:
        #     if i <= (shipTrips * PORT_TO_A * 2):
        #        _presentPackages.append(i)
        presentPackages = _presentPackages[:2] #filters to first two, if more than 0
        for i in presentPackages:
            del portDeliveryTimesList[0]
        shipTrips += 1
    totalTravelTimeToA = firstArrivalAtPort + (shipTrips * PORT_TO_A * 2)
    return totalTravelTimeToA

def last_delivery_time(container_schedule):
    all_trucks = [Transport(), Transport()]
    ship = Transport()
    port_delivery_times = []
    b_delivery_times = 0
    for destination in container_schedule:
        truck = min(all_trucks, key=lambda t: t.idle_time())
        if destination == "A":
            arrival_time = get_truck_travel_time(truck, FACTORY_TO_PORT)
            port_delivery_times.append(arrival_time)
        if destination == "B":
            arrival_time = get_truck_travel_time(truck, FACTORY_TO_B)
            b_delivery_times += arrival_time


    return max(
        get_ship_travel_time(port_delivery_times)
        ,b_delivery_times
    )




    # while port_delivery_times:
    #     port_arrival_time = port_delivery_times.pop(0)
    #     a_arrival_time = port_arrival_time + PORT_TO_A
    #     ship.on_return(a_arrival_time + A_TO_PORT)

        # if ship is in port
            # set time_ship_leaves_port = arrival_time
        # if ship is not in port
            # if 1 item on ship
                # if arrival_time < time_ship_leaves_port
                    # [add this item to the ship]

        #   ship.on_return(arrival_time + PORT_TO_A + A_TO_PORT)
        # if len(port_delivery_times) > 1:
            
        #     if port_delivery_times[0] == port_delivery_times[1]:
        #         port_delivery_times.pop(0)
        #         port_delivery_times.pop(0)
                # process ship bringing two packages to A
            

    #for time in port_delivery_times:

    # for destination in container_schedule:
    #     truck = min(all_trucks, key=lambda t: t.idle_time())
    #     if "A" == destination:
    #         leave_factory = truck.idle_time()
    #         arrive_at_port = leave_factory + FACTORY_TO_PORT
    #         leave_port_at = max(
    #             arrive_at_port,
    #             ship.idle_time()
    #         )
    #         delivery_time = leave_port_at + PORT_TO_A
    #         truck_return = arrive_at_port + PORT_TO_FACTORY
    #         truck.on_return(truck_return)
    #         ship_return = delivery_time + A_TO_PORT
    #         ship.on_return(ship_return)
    #         delivery_times.append(delivery_time)
    #     if "B" == destination:
    #         leave_factory = truck.idle_time()
    #         delivery_time = leave_factory + FACTORY_TO_B
    #         truck_return = delivery_time + B_TO_FACTORY
    #         truck.on_return(truck_return)
    #         delivery_times.append(delivery_time)

    #return max(delivery_times)
