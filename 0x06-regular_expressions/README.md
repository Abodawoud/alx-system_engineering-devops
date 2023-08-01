# REGEX
# This way if you want to make file test
1 - Make file test

2 - Make file ruby script
```
#!/usr/bin/env ruby

filename = ARGV[0]
input_string = File.read(filename)

matches = input_string.scan(/REGEX/m)

puts matches.join
```
    ./1-repetition_token_0.rb test.txt | cat -e
