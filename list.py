from ec import explorationCompression, commandlineArguments
from utilities import eprint
from listPrimitives import primitives
import cPickle as pickle

if __name__ == "__main__":
    try:
        with open("data/list_tasks.pkl") as f:
            tasks = pickle.load(f)
    except Exception as e:
        from makeListTasks import main
        main()
        with open("data/list_tasks.pkl") as f:
            tasks = pickle.load(f)

    eprint("Got {} list tasks".format(len(tasks)))

    explorationCompression(primitives, tasks,
                           outputPrefix="experimentOutputs/list",
                           **commandlineArguments(frontierSize=10**4,
                                                  a=1,
                                                  iterations=10,
                                                  pseudoCounts=10.0))

