## BASIC REGEX FOR USING GREP AND OTHERS

to specify that the line starts with [expression] : "^expression"

to specify that a special character is actually a normal expression: "\CHARACTER"

to specify a range of values or letters in a position (character class): "[start-end]"  Note: if the hyphen (-) is at the start or end of the expression it is taken as the languages with a hypen at that point: ex: [-a] : -hello

the negation in a character class is specified as: "[^expression]"

you can specify more using parenthesys () and a regexpression inside of it (if you need to specify that a line contains () use [(]*[)], otherwise
the grep command interprets it as a regex.

if you need to specify that (expression) appears n times use: "(expression){n}" , for a range use {n,m} and for an open one {n,} = {n,+oo}

the dot character outside of a character class means any character except \n \r \u2028 \u2029

There is an entire cheatsheet at https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet

^ means start of string
$ means end of input
\ means a special character 
L* has the meaning equal to a language as L* (any set constructed with L any number of times including 0)
L+ has the same meaning as L{1,}
L? means that L appears 0 or 1 times, same meaning as L{0,1}

\d : any arabic numeral (any digit)
\D : any non arabic numeral
\w : any alphanumeric character = [A-Za-z0-9_]
\W : any non alphanumeric character 

