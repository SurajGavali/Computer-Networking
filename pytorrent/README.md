# Python BitTorrent

This is a CLI tool that downloads files from the BitTorrent network.

You first need to wait for the program to connect to some peers first, then it starts downloading.
This tool needs a lot of improvements, but it does its job, you can :
-	Read a torrent file
-	Scrape udp or http trackers
-	Connect to peers
-	Ask them for the blocks you want
-	Save a block in RAM, and when a piece is completed and checked, write the data into your hard drive
-	Deal with the one-file or multi-files torrents
-	Leech or Seed to other peers

But you can’t :
-	Download more than one torrent at a time
-	Benefit of a good algorithm to ask your peers for blocks (code of rarest piece algo is implemented but not used yet)
-	Pause and resume download

Don't hesitate to ask me questions if you need help, or send me a pull request for new features or improvements.

### Installation
You can run the following command to install the dependencies using pip

`pip install -r requirements.txt`


### Running the program
Simply run:
`python3 main.py torrentfilename`

The files will be downloaded in the same path as your main.py script.


