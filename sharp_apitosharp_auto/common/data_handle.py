from common.read_ftpfile import read_sa_file
def sa_handle():
    stand = {
        "SAHD ": [4,1,4,4,5,6,6,5,6,6,6],
        "SA021":[4,1,4,4,1,7,20,20,1,13,13,6,13,10,10,1],
        "SA022":[4,1,4,4,1,6,6,25,4,10,5,5,6,6,5,4],
        "SA023":[4,1,4,4,13,2,3,1,13,2,3,1,13,1,3,6,13],
        "SA03 ":[4,1,4,4,1,7,4,2,4,4,4,1,9,3,1,1,13,1,3,13,13,13,13,2],
        "SA041":[4,1,4,4,1,7,2,14,9,13,13,15,5,2,7,13,13],
        "SA042":[4,1,4,4,7,9,7,9,7,9,7,9,7,9,4,13,13],
        "SA05 ":[4,1,4,4,1,7,2,7,1,4,4,9,9,9,7,1,3],
        "SA99 ":[4,1,4,4,5]
    }
    datalist=read_sa_file()
    