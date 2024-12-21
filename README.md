# JSONomicon

## What is it?
JSONomicon is a CLI tool for converting configuration files to JSON with syntax error detection

## Flags
**CLI flags are set:**
- The path to the .txt file to be converted

## Example

```
python main.py input.txt
```

## The syntax of the language to be converted
**Comments**
```
{-
This is a
multiline comment
-}
```

**Dictionaries**
```
([
    name: value,
    name: value,
    name: value
])
```

**Names**
```
[a-zA-Z][_a-zA-Z0-9]*
```

**Values**

- Numbers
- Dictionaries

**Declaring a constant**

```
global name = value
```

**Calculating the constant**

```
#{name}
```

## Example of input file

```
{- 
To protect the vessel, the dream… for all that was
-}

global max_users = 100
global base_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

([
    database : ([
        host : "localhost",
        port : 5432,
        user : "admin",
        password : "1111"
    ]),
    logging : ([
        level : "DEBUG",
        file : "/var/log/app_debug.log"
    ]),
    cache : ([
        size : 512,
        timeout : 7200
    ])
])

global connection_timeout = #{max_users}

```