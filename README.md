# Transport Tycoon Exercise

Based on the [Transport Tycoon][1] exercise created
by Rinat Abdullin.

Adapted for Boston Software Crafters, April 2021.

![tt-1-exercise.png][2]

We're creating a shipping simulator; moving containers
from the factory to destinations `A` or `B`.

The simulation includes two trucks; either truck may
carry a single container from the factory to the port
(with a one hour travel time) or to `B` (with a
five hour travel time).  Trucks, after delivering
a container, return empty to the factory (the
travel time is the same in both directions).

The simulation also includes a single boat, capable
of carrying a single container from the port to `A`
(with a four hour travel time).  After delivering
the container, the boat returns empty to the port
(with the same travel time).

In this simulation, loading and unloading the container
is a "free action", taking no time.

For each simulation, the input is a ordered sequence
of container destinations - containers leave the factory
in the order specified by the input.  The output is
the earliest time at which all containers have reached
their destination.

For example, when we have a single container to deliver
to `A`, that container arrives at the port after one hour,
and arrives at `A` after five hours, so the answer is five
(the ship still has to return to port, but we don't
include that time in this simulation).

----

`v1.py` includes an implementation of the calculator to
get you started.

`test_v1.py` includes a handful of example simulations,
which demonstrate that the calculator is working correctly.

Bonus challenge: no changes may be made to the `test_v1`
file itself; that test should always be passing.  (Note
that this means that `tycoon.v1.last_delivery_time` must
always return the same answers for the original problem,
even after you extend it to solve other problems).

----

## Part One

Take time to understand the calculations being made by
`tycoon.v1.last_delivery_time`; refactor that code
(if necessary) to ensure that the design of the code
matches the way you are thinking about the problem.

## Part Two

Change the travel time between the factory and the
port from one hour to two hours.

```
A -> 6
A, A -> 14
A, A, B -> 14
A, B -> 6
A, B, B -> 9
B, B, A -> 16
B, B, A, A -> 24 
```

## Part Three

Change the capacity of the ship from one container
to two containers.

The ship still leaves as soon as there is at least
one container available to take to `A`; but if more
than one container waiting at the port, the ship
can take two containers in a single trip without
changing the travel time.

```
A -> 6
A, A -> 6
A, A, B -> 9
A, B -> 6
A, B, A -> 14
A, B, B -> 9
B, B, A -> 16
B, B, A, A -> 16 
```


[1]: https://github.com/Softwarepark/exercises/blob/master/transport-tycoon.md
[2]: ./doc/tycoon-diagram.png