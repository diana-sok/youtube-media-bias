from pymongo import MongoClient
from pprint import pprint

cluster = MongoClient("mongodb://localhost:27017/")
db = cluster["youtube"]
channel = db["channel"]

print("serverStatus['connections']")
serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult['connections'])

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
    :param choice: a number
                   1 - Get the most subscribed left wing biased channel
                   2 - Get the most subscribed right wing biased channel
                   3 - Get the most subscribed high factual reporting,
                       left wing biased channels
                   4 - Get the most subscribed high factual reporting,
                       right wing biased channels
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
                   16 - Get List of Channels
    :return: documents found
    """
    # temporary implementation, will probably change in future
    result = {}
    if choice == 1:
        cursor = get_most_sub_left()
        print(get_result_string(cursor))
    elif choice == 2:
        cursor = get_most_sub_right()
        print(get_result_string(cursor))
    elif choice == 3:
        max_num = count_most_sub_high_fact_report_left()
        num = input("How many results would you like to see? " +
                    str(max_num) + " possibilities:  ")
        num = int(num)
        cursor = get_most_sub_high_fact_report_left(num)
        print(get_result_string(cursor))
    elif choice == 4:
        max_num = count_most_sub_high_fact_report_right()
        num = input("How many results would you like to see? " +
                    str(max_num) + " possibilities:  ")
        num = int(num)
        cursor = get_most_sub_high_fact_report_right(num)
        print(get_result_string(cursor))
    elif choice == 5:
        num = input("How many results would you like to see?: ")
        num = int(num)
        cursor = get_most_sub_low_fact_report_left(num)
        print(get_result_string(cursor))
    elif choice == 6:
        num = input("How many results would you like to see?: ")
        num = int(num)
        cursor = get_most_sub_low_fact_report_right(num)
        print(get_result_string(cursor))
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
        cursor = get_most_subscribed_channel()
        print(get_result_string(cursor))
    elif choice == 12:
        cursor = get_most_viewed_channel()
        print(get_result_string(cursor))
    elif choice == 13:
        channel_name = input("Enter name of channel: ")
        print("This many documents were deleted:" + str(delete_channel(
            channel_name)))
    elif choice == 14:
        name = input("Name of channel: ")
        desc = input("Description of channel: ")
        print("id of added doc:" + str(create_channel(name, desc)))
    elif choice == 15:
        old_name = input("Name of channel to change: ")
        new_name = input("New name of channel: ")
        print("This many documents changed:" + str(update_channel_name(
            old_name, new_name)))
    elif choice == 16:
        num = input("How many channels fo you want to see: ")
        num = int(num)
        print(get_result_string(get_channel_list(num)))
    else:
        print("invalid choice")


def get_most_sub_left():
    """
    Get the most subscribed left wing biased channel
    :return: a cursor pointing to most subscribed right wing biased channel
    """
    query = {"media.bias": {"$regex": "left", "$options": "i"}}
    sort_parameter = [("statistics.subscriberCount", -1)]
    cursor = channel.find(query).sort(sort_parameter).limit(1)
    return cursor


def get_most_sub_right():
    """
    Get the most subscribed right wing biased channel
    :return: a cursor pointing to most subscribed right wing biased channel
    """
    query = {"media.bias": {"$regex": "right", "$options": "i"}}
    sort_parameter = [("statistics.subscriberCount", -1)]
    cursor = channel.find(query).sort(sort_parameter).limit(1)
    return cursor


def count_most_sub_high_fact_report_left():
    """
    Count the most subscribed high factual reporting, left wing biased channels
    :return: number of possible results
    """
    query = {
        "media.factual_reporting_label": {"$regex": "HIGH", "$options": "i"},
        "media.bias": {"$regex": "left", "$options": "i"}}
    cursor = channel.count_documents(query)
    return int(cursor)


def get_most_sub_high_fact_report_left(num):
    """
    Get the most subscribed high factual reporting, left wing biased channels
    :param num: number of results to return
    :return: a cursor pointing to the high factual reporting,
             left wing biased channels
    """
    query = {
        "media.factual_reporting_label": {"$regex": "HIGH", "$options": "i"},
        "media.bias": {"$regex": "left", "$options": "i"}}
    sort = [("statistics.subscriberCount", -1)]
    cursor = channel.find(query).sort(sort).limit(num)
    return cursor


def count_most_sub_high_fact_report_right():
    """
    Count the most subscribed high factual reporting, right wing biased channel
    :return: number of possible results
    """
    query = {
        "media.factual_reporting_label": {"$regex": "HIGH", "$options": "i"},
        "media.bias": {"$regex": "right", "$options": "i"}}
    cursor = channel.count_documents(query)
    return int(cursor)


def get_most_sub_high_fact_report_right(num):
    """
    Get the most subscribed high factual reporting, right wing biased channels
    :param num: number of results to return
    :return: a cursor pointing to the high factual reporting,
             right wing biased channels
    """
    query = {
        "media.factual_reporting_label": {"$regex": "HIGH", "$options": "i"},
        "media.bias": {"$regex": "right", "$options": "i"}}
    sort = [("statistics.subscriberCount", -1)]
    cursor = channel.find(query).sort(sort).limit(num)
    return cursor


def get_most_sub_low_fact_report_left(num):
    """
    Get the most subscribed low factual reporting, left wing biased channels
    :param num: number of results to return
    :return: a cursor pointing to the high factual reporting,
             left wing biased channels
    """
    query = {
        "media.factual_reporting_label": {"$in": ["MIXED", None]},
        "media.bias": {"$regex": "left", "$options": "i"}}
    sort = [("statistics.subscriberCount", -1)]
    cursor = channel.find(query).sort(sort).limit(num)
    return cursor


def get_most_sub_low_fact_report_right(num):
    """
    Get the most subscribed low factual reporting, right wing biased channels
    :param num: number of results to return
    :return: a cursor pointing to the high factual reporting,
             right wing biased channel
    """
    query = {
        "media.factual_reporting_label": {"$in": ["MIXED", None]},
        "media.bias": {"$regex": "right", "$options": "i"}}
    sort = [("statistics.subscriberCount", -1)]
    cursor = channel.find(query).sort(sort).limit(num)
    return cursor


def get_result_string(cursor):
    """
    Create string representation of query result pointed to by cursor.
    :param cursor: cursor returned by a query
    :return: string representation of query results
    """
    channels = ""
    for doc in cursor:
        channels += get_channel_string(doc) + "\n"
        channels += "---\n"
    return channels


def get_channel_string(doc):
    """
    Create a string representation of a channel doc (represented as a dict).
    :param doc: a dictionary representing a channel document
    :return: the string representation of a channel document
    """
    a_channel = ""
    a_channel += "Channel Name: " + get_channel_name(doc) + "\n"
    a_channel += "Channel Bias: " + get_bias(doc) + "\n"
    a_channel += "Subscribers: " + str(get_subscriber_count(doc)) + "\n"
    a_channel += "Factual Reporting: " + get_fact_label(doc) + "\n"
    return a_channel


def get_fact_label(doc):
    """
    Retrieves the factual reporting label of the channel from doc
    (represented as a dict).
    :param doc: the dictionary to retrieve the factual reporting label
    :return: string containing the factual reporting label
    """
    return str(doc["media"]["factual_reporting_label"])


def get_channel_name(doc):
    """
    Retrieves the name of the channel from doc (represented as a dict).
    :param doc: the dictionary to retrieve the channel name from
    :return: string containing channel name
    """
    return doc["snippet"]["title"]


def get_bias(doc):
    """
    Retrieves the bias of the channel from doc (represented as a dict).
    :param doc: the dictionary to retrieve the channel bias from
    :return: string containing channel bias
    """
    return doc["bias"]


def get_subscriber_count(doc):
    """
    Retrieves the subscriber count of the channel from doc (represented as dict)
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
    sort_parameter = [("statistics.viewCount", -1)]
    cursor = channel.find(query).sort(sort_parameter).limit(1)
    return cursor


def get_most_subscribed_channel():
    """
    Returns a cursor pointing to the most subscribed channel.
    :return: cursor pointing to most subscribed channel
    """
    query = {}
    sort_parameter = [("statistics.subscriberCount", -1)]
    cursor = channel.find(query).sort(sort_parameter).limit(1)
    return cursor


def get_channel_list(channel_count):
    """
    Get the specified amount of channels.
    :param channel_count: the number of channels to retrieve
    :return: a cursor pointing to query results
    """
    query = {}
    cursor = channel.find(query).limit(channel_count)
    return cursor


def delete_channel(channel_name):
    """
    Deletes a single channel with the given name.
    :param channel_name: the name of channel to delete
    :return: the number of documents deleted
    """
    filter_cond = {"snippet.title": channel_name}
    result = channel.delete_one(filter_cond)
    return result.deleted_count


def update_channel_name(old_name, new_name):
    """
    Update a channels name given old name.
    :param old_name: the name used to find old channel
    :param new_name: the new name of the channel
    :return: the number of documents modified
    """
    filter_cond = {"snippet.title": old_name}
    update = {"$set": {"snippet.title": new_name}}
    result = channel.update_one(filter_cond, update)
    return result.modified_count


def create_channel(name, description):
    """
    Create a channel given name and description
    :return: the id of the inserted document
    """
    doc = {"snippet": {"title": name, "description": description}}
    result = channel.insert_one(doc)
    return result.inserted_id


def print_application_options():
    print("1. Get the most subscribed left wing biased channel")
    print("2. Get the most subscribed right wing biased channel")
    print("3. Get the most subscribed, left wing biased, "
          "high factual reporting level channel")
    print("4. Get the most subscribed, right wing biased, "
          "high factual reporting level channel")
    print("5. Get the most subscribed, left wing biased, "
          "low factual reporting level channel")
    print("6. Get the most subscribed, right wing biased, "
          "low factual reporting level channel")
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
    print_application_options()

    # Loop application
    run = True
    while run:
        print("---------------------------------------------------------")
        print("Type 'quit' to quit the application")
        print("Type 'options' to print the menu options")
        print("---------------------------------------------------------")

        # get user's choice of action
        choice = input("Enter the number option for what you would like to "
                       "do: ")

        # perform user's choice of action
        if choice == "quit":
            print("\nBye!")
            run = False
            exit()
        elif choice == "options":
            print_application_options()
        else:
            try:
                execute_choice(int(choice))
            except:
                print("invalid input!")
                print_application_options()


if __name__ == "__main__":
    main()
