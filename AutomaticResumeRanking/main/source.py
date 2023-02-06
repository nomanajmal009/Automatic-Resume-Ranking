from .resume_parser import resumeparse
import os
import logging
import threading

def perform_parsing(files_path):
    print(files_path)
    enteries = os.listdir(files_path)

    files = len(enteries)
    threads = []
    data = []

    for i in range(files):
        file = os.path.join(files_path,enteries[i])
        logging.info("Main    : create and start thread %d.", i)
        x = threading.Thread(target=resumeparse.resumeparse.read_file,args=[file,data])
        x.start()
        threads.append(x)
        print("\n******  starting new iteration *********\n")

    for t in threads:
        t.join()
    
    for dat in data:
        print("********** data  ************* \n")
        print(dat)

    return data

   




    # for i in enteries:
    #     file = os.path.join(path,i)
    #     data = resumeparse.read_file(file)
    #     print("\n\n*****************  NEW DOC   *********************\n")
    #     print(data)
    #     # print(i)



# path = 'E:\/resume_parser_UCP\data'
# perform_parsing(path)