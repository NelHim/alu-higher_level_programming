#!/bin/bash
# display Content-Length
<<<<<<< HEAD
curl -sI "$1" | grep 'Content-Length' | cut -d " " -f201
~
=======
curl -sI "$1" | grep 'Content-Length' | cut -d " " -f2
>>>>>>> 3bfa8008a2e7cafd04bde96a2eaaf1243c0e123a
