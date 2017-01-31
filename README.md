# Steam Store Apps Dumper

Simple Python program to request API data and save a file for every app available in the Steam Store.

First, it collects a list of all apps, then it cycles through it for available Steam Store data; which, if valid, is saved in a file identified by the appid.

There are no smart web verifications; which means you are expected to have a stable internet connection and avoid hitting the API cap. Maybe I might put some work on this later on.

