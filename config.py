import pickle
import sys
class likeDB:

    def saveObject(name,Object):
        try:
            name = str("DB_object/"+name) + '.pkl'
            with open(name, 'wb') as f:
                pickle.dump(Object, f, pickle.HIGHEST_PROTOCOL)
        except Exception as e:
            print(e, file=sys.stderr)
    #to load object with run code again
    def loadObject(name):
        try :
            name = str(name) + '.pkl'
            with open("DB_object/"+name, 'rb') as f:
                return pickle.load(f) 
        except Exception as e:
            print(e, file=sys.stderr)
