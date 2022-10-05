# Maps2srs
A tool to convert street names into csv flashcards which can be imported into apps such as Anki. The user will be able to input a town or city and the software will generate flashcards for all the named streets.  A rough outline can be seen below.

CLI User Input
==============
* Optparse

Query Data
==========
* Geocode with Geopy/Nominatim
* Overpass QL/OSMnx
* Save to DB
* If not a [relation](https://wiki.openstreetmap.org/wiki/Relation) or a [way](https://wiki.openstreetmap.org/wiki/Way), try next result (might have to initially query >1 result)

Clean Up Data
=============
* Connect contiguous, homonymous roads. How?

Generate 1 Tile per Sheet
=========================
* At max zoom level that shows entire road ![image](https://user-images.githubusercontent.com/51741333/180865207-79127559-453c-47f3-9b87-05319f1c75cb.png)

* Cascadenik

Create Data Records
============
* Data records will contain a street name and images shown below. Templates will be used to create cards from data records using flashcard software.
* CSV
* Image file <-> street name

![image](https://user-images.githubusercontent.com/51741333/180866513-062fab6f-2a80-4af9-9f81-7cea74998e60.png) &rarr; ![image](https://user-images.githubusercontent.com/51741333/180866390-ed2262a6-caf9-4cc2-b8df-1ce8a5e88b88.png)

![image](https://user-images.githubusercontent.com/51741333/180867062-cf149455-3467-4a97-abd1-72ffc2a0f1e1.png) &rarr; ![image](https://user-images.githubusercontent.com/51741333/180867228-58955833-889f-458c-8c4a-bc7b5fa5892a.png)




Support me (BTC): bc1qa7yyt3q86gcddjg7v4y5qssxn8d8mc3yj050wz
