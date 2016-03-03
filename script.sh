#!bin/bash
 for file in templates/*.Pnw; do
        Pweave --figure-directory images -f pandoc $file
 done
