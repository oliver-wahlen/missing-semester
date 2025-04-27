#! /bin/bash


#use source to make script persist

#simple program to save current dir and to return to it easily
marco () {
	foo=$(pwd)
}

polo () {
	cd "$foo"
}
