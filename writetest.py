from datetime import date

#id: 3,
#        title: 'DTS ENDS',
#        start: new Date(2016, 10, 6, 0, 0, 0),
#        end: new Date(2016, 10, 13, 0, 0, 0),

class Event:

    def __init__(self, event_id, event_name, start_date, end_date, start_time, end_time, description, priority):
        self.event_id = event_id
        self.event_name = event_name
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.priority = priority

#COULD USE TO WRITE ALL EVENTS ON CLOSING APPLICATION
def write_many_events(event_list):
    save_file = open("calendar.txt", "w+")
    for element in event_list:
        save_file.write("{} {} {} {} {} {} {} {}\n".format(element.event_id, element.event_name, element.start_date, element.end_date, element.start_time, element.end_time, element.description, element.priority))
    save_file.close()

#PROBABLY ONE THAT WILL BE USED MOST, WRITING ON CREATION OF EACH EVENT
def write_single_event(element):
    save_file = open("calendar.txt", "w+")
    save_file.write("{} {} {} {} {} {} {} {}\n".format(element.event_id, element.event_name, element.start_date, element.end_date, element.start_time, element.end_time, element.description, element.priority))
    save_file.close()

#READS ALL EVENTS IN THE TEXT SAVE FILE
def read_many_events(filename):
    save_file = open(filename, "r")
    for line in save_file:
        temp = line
        print temp
    save_file.close()

#MAY NEED ANOTHER ARGUMENT TO READ A SPECIFIC EVENT
def read_single_event(element):
    save_file = open("calendar.txt", "r")
    save_file.write("{},{},{},{},{},{},{},{}\n".format(element.event_id, element.event_name, element.start_date, element.end_date, element.start_time, element.end_time, element.description, element.priority))
    save_file.close()

def main():
    #save_file = open("calendar.txt", "w+")
    #save_file.write("{}, {}, {}, {}, {}, {}, {}, {}\n".format(bfp.event_id, bfp.event_name, bfp.start_date, bfp.end_date, bfp.start_time, bfp.end_time, bfp.description, bfp.priority))

    #TEST DATA OBJECTS
    bfp = Event(1, "bigparty", (2016, 10, 6), (2016, 10, 6), (20, 30, 0), (23, 0, 0), "bring booze", 3)
    sfp = Event(2, "smallparty", (2017, 11, 6), (2017, 11, 6), (18, 30, 0), (21, 0, 0), "dont bring booze", 1)
    nfp = Event(3, "normalparty", (2018, 6, 6), (2018, 6, 6), (19, 30, 0), (22, 0, 0), "maybe bring booze", 2)
    party_list = [bfp, sfp, nfp]

    #READ AND WRITE METHOD CALLS
    #read_single_event(calendar.txt)
    #read_many_events("calendar.txt")
    #write_single_event(bfp)
    #write_many_events(party_list)

    #save_file.close()

if __name__ == "__main__":
    main()