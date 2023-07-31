#!/bin/bash

# Check the status of the database
while true; do
  if curl --fail --silent http://localhost:7474; then
    break
  else
    echo "Waiting for neo4j to be ready..."
    sleep 3
  fi
done
echo "Neo4j is ready for recieving import script!"

cat /var/lib/neo4j/import/questions_import.cypher | cypher-shell
echo "Import script finished!"
exit 0