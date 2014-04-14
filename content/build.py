import os,sys
import modules.readwrite as rw
import modules.pop
import modules.compress
import config

def getFiles(input_dir):
    result = []
    for path,folders,files in os.walk(input_dir):
        result.extend([path+os.sep+f for f in files])
    return result

if __name__ == "__main__":

    files = getFiles(config.INPUT_DIR)
    items = []
    for f_loc in files:
        item = rw.jsonFromFile(f_loc)
        if "item" in item:
            item = item["item"]
        items.append(item)
    print(len(items))

    #modules.pop.process(items)
    modules.compress.process(items)
    rw.jsonToFile(items, config.OUTPUT_DIR + os.sep + config.OUTPUT_NAME)

