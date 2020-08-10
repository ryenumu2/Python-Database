#command-line tool 

def main(argv):
    if not (4 <= len(argv) <= 5): #if number of arguments is not 4 or 5
        usage()
        return ('Error: Need a database name, method, key, and optional value')
    
    dbname, method, key, value = (argv[1:] + [None])[:4] 
    #this will account for both len(argv) == 4 and len(argv) == 5:
    #if len(argv) == 4, then dbname = argv[1], method = argv[2], 
    #key = argv[3], and value = None. 
    #if len(argv == 5, then dbname = argv[1], method = argv[2], 
    #key = argv[3], and value = argv[4].
    
    if method not in {'get', 'set', 'delete'}: #if method is not equal to 'get', 'set', or 'delete'
        usage()
        return ('Error:' + ' ' + str(method) + ' ' + 'is an invalid method name')

    database = dbdb.connect(dbname) #if none of the errors above occur, connect to the user passed dbname

    try:
        if method == 'get': #output the corresponding value for the key you passed
            sys.stdout.write(database[key])
        elif method == 'set': #set the value of the key you passed to the value you passed 
            database[key] = value
            database.commit()
        else:
            del database[key] #delete the value of the key you passed 
            database.commit()
    
    except KeyError: #if key is not found in the database
        print('Key not found', file=sys.stderr)
        return ('Error: The key you passed is not found in database ' + str(dbname))
    return ('SUCCESS') #return success if none of the return errors above are triggered

    
