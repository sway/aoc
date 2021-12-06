count=0; prev=9999999999999; cat input | while read i; do if [ $i -gt $prev ]; then (( count = $count + 1 )); fi; done; echo $count
