 #!/usr/bin/env bash

error="empty"
count=0

while [ "$error" != "The error was using magic numbers" ]; do
	((count++))
	error=$($1 2>&1 > /dev/null)
done

echo "Error $error after $count times"
