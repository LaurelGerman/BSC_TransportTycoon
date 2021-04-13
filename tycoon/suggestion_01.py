def get_ship_travel_time(portDeliveryTimesList):
    """
    """
    pdt = portDeliveryTimesList
    firstArrivalAtPort = pdt[0]
    shipTrips = 0
    if len(pdt) > 1\
    and pdt[0] == pdt[1]:
        del pdt[1], pdt[0]
        shipTrips += 1
    while pdt:
        _presentPackages = [i for i in pdt if i < (shipTrips * PORT_TO_A * 2)]
        presentPackages = _presentPackages[:2]
        for i in presentPackages:
            del pdt[0]
        shipTrips += 1
    totalTravelTimeToA = firstArrivalAtPort + shipTrips * PORT_TO_A * 2
    return totalTravelTimeToA
        
        