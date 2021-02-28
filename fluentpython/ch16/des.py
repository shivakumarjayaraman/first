from collections import namedtuple
from queue import PriorityQueue as pq

Event = namedtuple('Event', 'time proc action')

def taxi_process(ident, trips, start_time=0) :
    time = yield Event(start_time, ident, "leave garage")
    for i in range(trips) :
        time = yield Event(time, ident, "Pick up passenger")
        time = yield Event(time, ident, "Drop off passenger")

    yield Event(time, ident, "Go home")

class Simulator :
    def __init__(self, procs_map) :
        self.events = pq()
        self.procs = dict(procs_map)

    def run(self, end_time) :
        for _, proc in sorted(self.procs.items()) :
            first = next(proc)
            self.events.put(first)

        sim_time = 0
        while (sim_time < end_time) :
            if (self.events.empty()) :
                print ("*** end of events ***")
                break
            
            curr = self.events.get()
            sim_time, proc_id, prev_action = curr
            print ("taxi:", proc_id, proc_id * '    ', curr)
            active = self.procs[proc_id]
            next_time = sim_time + 15
            try :
                next_event = active.send(next_time)
            except StopIteration :
                del self.procs[proc_id]
            else :
                self.events.put(next_event)
        else :
            print ("Events pending ", self.events.qsize())
