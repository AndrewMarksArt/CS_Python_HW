#
# starting example for ist341, week6 "Web as Input"
#

import requests
import json


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# Problem 1 starter code (Apple API)
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#
# Andrew Marks
#

def apple_api(artist_name):
    """ 
    """
    ### Use the search url to get an artist's itunes ID
    search_url = "https://itunes.apple.com/search"
    parameters = {"term":artist_name,"entity":"musicArtist","media":"music","limit":200}
    result = requests.get(search_url, params=parameters)
    data = result.json()

    # save to a local file so we can examine it
    filename_to_save = "appledata.json"
    f = open( filename_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
    # print("\nfile", filename_to_save, "written.")

    # Here, you should return the artist id:
    artist_id = data["results"][0]['artistId']
    # Note: it's helpful to find the iTunes artistId and return it here
    # (this hasn't been done yet... try it!) 

    return  int(artist_id)  # This is probably _not_ the correct answer...


#
# 
#
def apple_api_lookup(artistId):
    """ 
    Takes an artistId and grabs a full set of that artist's albums.
    "The Beatles"  has an id of 136975
    "Kendrick Lamar"  has an id of 368183298
    "Taylor Swift"  has an id of 159260351

    Then saves the results to the file "appledata_full.json"

    This function is complete, though you'll likely have to modify it
    to write more_productive( , ) ...
    """
    lookup_url = "https://itunes.apple.com/lookup"    
    parameters = {"entity":"album","id":artistId}    
    result = requests.get(lookup_url, params=parameters)
    data = result.json()

    # save to a file to examine it...
    filename_to_save="appledata_full.json"
    f = open( filename_to_save, "w" )     # opens the file for writing
    string_data = json.dumps( data, indent=2 )  # this writes it to a string
    f.write(string_data)                        # then, writes that string to a file...
    f.close()                                   # and closes the file
    # print("\nfile", filename_to_save, "written.")
    num = int(data["resultCount"])

    # we'll leave the processing to another function...
    return num



#
#
#
def apple_api_lookup_process():
    """ example opening and accessing a large appledata_full.json file...
        You'll likely want to do more!
    """
    filename_to_read="appledata_full.json"
    f = open( filename_to_read, "r", encoding="utf-8" )
    string_data = f.read()
    data = json.loads( string_data )
    # print("the raw json data is\n\n", data, "\n")

    # for live investigation, here's the full data structure
    return data



#
# main()  for testing problem 2's functions...
#
def main():
    # routine for getting the artistId
    if True:
        artistId = apple_api("The Beatles") # should return 136975
        #artistId = apple_api("Kendrick Lamar") # should return 368183298
        #artistId = apple_api("Taylor Swift") # should return 159260351
        #artistId = apple_api("Maroon 5") # should return 1798556
        # print("artistId is", artistId)


    if True:
        apple_api_lookup(1798556)
        data = apple_api_lookup_process()
        return data

    # more_productive( "Katy Perry", "Steve Perry" )
    # get each one's id
    # get each one's file
    # compare number of albums! Done!
    # then ask two of your own questions


# main()


def more_productive(artist1, artist2):
    """
    Takes two strings that are artist names, looks them up on iTunes and find out which one has more
    collections or ablums.
    :return: no return just prints the more productive artist
    """
    artist1_id = apple_api(artist1)
    artist2_id = apple_api(artist2)

    artist1_count = apple_api_lookup(artist1_id)
    artist2_count = apple_api_lookup(artist2_id)

    print(artist1_id, artist2_id)
    print(artist1_count, artist2_count)

    if artist2_count > artist1_count:
        print("The More productive artist is: ", artist2)
    elif artist1_count > artist2_count:
        print("The More productive artist is: ", artist1)
    else:
        print(artist1 + ' and ' + artist2 + ' produced the same amount')

    return

more_productive("The Beatles", "Taylor Swift")

def avg_price_for_collection( artist1):
    """
    Takes an artist's name as a string, looks them up on iTunes grabs the prices for their albums, then figures out the
    average price of an album
    :return: float, the average collection or album price for the artist
    """
    artist1_id = apple_api(artist1)

    lookup_url = "https://itunes.apple.com/lookup"
    parameters = {"entity": "album", "id": artist1_id}
    result = requests.get(lookup_url, params=parameters)
    data = result.json()

    # save to a file to examine it...
    filename_to_save = "appledata_full.json"
    f = open(filename_to_save, "w")  # opens the file for writing
    string_data = json.dumps(data, indent=2)  # this writes it to a string
    f.write(string_data)  # then, writes that string to a file...
    f.close()  # and closes the file
    # print("\nfile", filename_to_save, "written.")

    prices = []
    for i in range(len(data['results'])):
        for k, v in data['results'][i].items():
            if k == 'collectionPrice':
                prices.append(v)

    avg_price = sum(prices) / len(prices)

    return avg_price

artist = "The Beatles"
collection_price = avg_price_for_collection(artist)
print("The average price for a collection/album for", artist, "is: $", round(collection_price, 2))