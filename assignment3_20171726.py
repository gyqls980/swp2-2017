import pickle

dbfilename = 'assignment3_hyobin.dat'

def readScoreDB():
	try:
		fH = open(dbfilename, 'rb')
	except FileNotFoundError as e:
		print("New DB: ", dbfilename)
		return []

	scdb = []
	try:
		scdb =  pickle.load(fH)
	except:
		print("Empty DB: ", dbfilename)
	else:
		print("Open DB: ", dbfilename)
	fH.close()
	return scdb


# write data into person DB
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
        while(True):
            try:
                inputstr = (input("Score DB > "))
                # if not inputstr: continue

                if inputstr == "": continue
                else :
                        parse = inputstr.split(" ")

                if parse[0] == 'add':
                        try:
                                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                                scdb += [record]
                                writeScoreDB(scoredb)
                        except IndexError:
                                print("Invalid command(IndexError - add)")

                elif parse[0] == 'show':
                        try:
                                sortKey ='Name' if len(parse) == 1 else parse[1]
                                showScoreDB(scdb, sortKey)
                        except KeyError:
                                print("Invalid Command(KeyError - show)")

                elif parse[0] == 'del':
                        try:

                                int(parse[1])
                                print("Invalid command(IndexError - del)")
                                continue
                        except:

                                k = list(range(len(scdb)))
                                k.sort(reverse=True)
                                for i in k:
                                    for j in range(3):
                                        if scdb[i]['Name'] == parse[1]:
                                            del (scdb[i])
                                            writeScoreDB(scoredb)
                                            break

                elif parse[0] == 'find':
                        try:
                                for i in scdb:
                                    if i['Name'] == parse[1]:
                                        for t, n in i.items():
                                            print(t, " : ", n, end=" ")
                                            writeScoreDB(scoredb)
                                        print()
                        except IndexError:
                            print("Invalid Command(IndexError - find)")

                elif parse[0]=='inc':
                        try:
                                for i in scdb:
                                    if i['Name']==parse[1]:
                                            i['Score']=str(int(i['Score'])+int(parse[2]))
                                            writeScoreDB(scoredb)
                        except IndexError:
                                print("Invalid Command(IndexError - inc)")

                elif parse[0] == 'quit':
                        break

                else:
                        print("Invalid command: " + parse[0])

            except KeyboardInterrupt:
                    print("Invalid command(KeyboardInterrupt)")

def showScoreDB(scdb, keyname):
        for p in sorted(scdb, key=lambda person: person[keyname]):
                for attr in sorted(p):
                        print(attr + "=" + p[attr], end =" ")
                print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)