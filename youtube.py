import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb://localhost:27017/")
db = cluster["youtube"]
channel = db["channel"]

# to check if database exists
db_list = cluster.list_database_names()
if "youtube" in db_list:
    print("The database exists.")
else:
    print("youtube database does not exist")

# check if collection exists
collection_list = db.list_collection_names()
if "channel" in collection_list:
    print("The youtube.channel collection exists.")
else:
    print("youtube.channel collection does not exist")


def execute_choice(choice):
    """
    Performs the action specified by user.
    :param choice: 1 - Get the most subscribed left wing biased channel
                   2 - Get the most subscribed right wing biased channel
                   3 - Get the high factual reporting, left wing biased
                       channels
                   4 - Get the high factual reporting, right wing biased
                       channels
                   5 - Get the most subscribed, left wing biased, low factual
                       reporting level channel
                   6 - Get the most subscribed, right wing biased, low factual
                       reporting level channel
                   7 - Get the most viewed left wing biased channel
                   8 - Get the left wing biased channel with the most videos
                   9 - Get the right wing biased channel with the most videos
                   10 - Get the most viewed right wing biased channel
                   11 - Get the most subscribed channel
                   12 - Get the most viewed channel
                   13 - Delete a channel
                   14 - Add a channel
                   15 - Update a channel’s name
    :return: documents found
    """
    # temporary implementation, will probably change in future
    result = {}
    if choice == 1:
        # exec function
        print("execute choice to be done")
    elif choice == 2:
        # exec function
        print("execute choice to be done")
    elif choice == 3:
        # exec function
        print("execute choice to be done")
    elif choice == 4:
        # exec function
        print("execute choice to be done")
    elif choice == 5:
        # exec function
        print("execute choice to be done")
    elif choice == 6:
        # exec function
        print("execute choice to be done")
    elif choice == 7:
        # exec function
        print("execute choice to be done")
    elif choice == 8:
        # exec function
        print("execute choice to be done")
    elif choice == 9:
        # exec function
        print("execute choice to be done")
    elif choice == 10:
        # exec function
        print("execute choice to be done")
    elif choice == 11:
        # exec function
        print("execute choice to be done")
    elif choice == 12:
        cursor = get_most_viewed_channel()
        print(get_result_string(cursor))
    elif choice == 13:
        channel_name = input("Enter name of channel: ")
        delete_channel(channel_name)
    elif choice == 14:
        # exec function
        print("execute choice to be done")
    elif choice == 15:
        # exec function
        print("execute choice to be done")
    elif choice == 16:
        num = input("How many channels fo you want to see: ")
        num = int(num)
        print(get_result_string(get_channel_list(num)))
    else:
        print("invalid choice")


def get_result_string(cursor):
    """
    Create string representation of query result pointed to by cursor.
    :param cursor:
    :return:
    """
    channels = ""
    for doc in cursor:
        channels += get_channel_string(doc) + "\n"
        channels += "---\n"
    return channels


def get_channel_string(doc):
    """
    Create a string representation of channel document
    :param doc:
    :return:
    """
    a_channel = ""
    a_channel += "Channel Name: " + get_channel_name(doc) + "\n"
    a_channel += "Channel Bias: " + get_bias(doc) + "\n"
    a_channel += "Subscribers: " + str(get_subscriber_count(doc)) + "\n"
    return a_channel


def get_channel_name(doc):
    """
    Retrieves the name of the channel from doc.
    :param doc: the document to retrieve the channel name from
    :return: string containing channel name
    """
    return doc["snippet"]["title"]


def get_bias(doc):
    """
    Retrieves the bias of the channel from doc.
    :param doc: the document to retrieve the channel bias from
    :return: string containing channel bias
    """
    return doc["bias"]


def get_subscriber_count(doc):
    """
    Retrieves the subscriber count of the channel from doc.
    :param doc: the document to retrieve the subscriber count from
    :return: number representing the subscriber count
    """
    return doc["statistics"]["subscriberCount"]


def get_most_viewed_channel():
    """
    Returns a cursor pointing to the most viewed channel.
    :return: cursor pointing to most viewed channel
    """
    query = {}
    sort_parameter = [("statistics.videoCount", -1)]
    cursor = channel.find(query).sort(sort_parameter).limit(1)
    return cursor


# this is a sample function
def get_channel_list(channel_count):
    """
    Get the specified amount of channels.
    :param channel_count:
    :return: cursor pointing to a
    """
    query = {}
    cursor = channel.find(query).limit(channel_count)
    return cursor


def delete_channel(channel_name):
    """
    Deletes a single channel with the given name.
    :param channel_name:
    :return:
    """
    filter_cond = {"snippet.title": channel_name}
    channel.delete_one(filter_cond)


def print_application_options():
    print("1. Get the most subscribed left wing biased channel")
    print("2. Get the most subscribed right wing biased channel")
    print("3. Get the high factual reporting, left wing biased channels")
    print("4. Get the high factual reporting, right wing biased channels")
    print("5. Get the most subscribed, left wing biased, low factual reporting level channel")
    print("6. Get the most subscribed, right wing biased, low factual reporting level channel")
    print("7. Get the most viewed left wing biased channel")
    print("8. Get the left wing biased channel with the most videos")
    print("9. Get the right wing biased channel with the most videos")
    print("10. Get the most viewed right wing biased channel")
    print("11. Get the most subscribed channel")
    print("12. Get the most viewed channel ")
    print("13. Delete a channel")
    print("14. Add a channel")
    print("15. Update a channel’s name")
    print("16. Get List of Channels")


def main():
    print("---------------------------------------------------------")
    print("Youtube Media Bias")
    print("Check the media bias of Youtube Channels with this application!")

    # Loop application
    run = True
    while run:
        print("---------------------------------------------------------")
        print_application_options()
        print("---------------------------------------------------------")
        print("Type 'quit' to quit the application")
        print("Type 'options' to print the menu options")
        print("---------------------------------------------------------")
        choice = input("Enter the number option for what you would like to "
                       "do: ")
        if choice == "quit":
            run = False
            exit()
        if choice == "options":
            print_application_options()
        execute_choice(int(choice))



if __name__ == "__main__":
    main()
