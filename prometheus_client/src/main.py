import os
import time

from prometheus_client import push_to_gateway
from prometheus_client import CollectorRegistry
from prometheus_client import Gauge

if __name__ == "__main__":
    os.environ["NO_PROXY"] = "localhost"
    print("python client sample")
    registry = CollectorRegistry()
    g = Gauge("mochimochi_value", "this is mochimochi value", registry=registry)

    while(True):
        try:
            g.set_to_current_time()
            push_to_gateway("localhost:9091",
                            job="sample_job",
                            registry=registry)
            time.sleep(10)
        except InterruptedError:
            print("catch InterruptedError.")
            break
        except Exception as error:
            print(error)
            print("なんらかエラー")
            break
