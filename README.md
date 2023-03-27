# pp_cmd_range
Postprocessing command "range"
## Description
Command adds column to dataframe (or create a new one if it is first command), fills columns with values from `a` to `b`.  
Depending on the arguments, it uses one of two numpy functions to fill the column:    
- (numpy.linspace)[ https://numpy.org/doc/stable/reference/generated/numpy.linspace.html ]
- (numpy.arrange)[ https://numpy.org/doc/stable/reference/generated/numpy.arange.html ]

**Length of input dataframe must be equal number of values**

### Arguments
- column - positional argument, text, column name for values
- a - positional argument, number, start of interval. The interval includes this value. 
- b - positional argument, number, end of interval. The interval does not include this value, except in some cases where step is not an integer and floating point round-off affects the length of out
- step - keyword argument, number, not required, default vaule is `1`, for arrange function. Spacing between values. For any output out, this is the distance between two adjacent values.
- number - keyword argument, number, not required, for linspace function. Number of samples to generate. 
- dtype - keyword argument, text, not required. The type of the output array. If dtype is not given, the data type is inferred from `a` and `b`

### Usage example

```
| range "column_name", 10, 30, step=5
```
```
   column_name
0           10
1           15
2           20
3           25

```
```
range "column_name", 2,3, step=0.3
```
```
   column_name
0          2.0
1          2.3
2          2.6
3          2.9

```
```
query: range "column_name", 2,3, number=7
```
```
   column_name
0     2.000000
1     2.166667
2     2.333333
3     2.500000
4     2.666667
5     2.833333
6     3.000000
```
```
otl_v1 <# makeresults count=2 #> | range "new_col", 2, 7, step=3
```
```
            _time  new_col
Index                     
0      1679906285        2
1      1679906285        5

```
When length of input dataframe not equal the number of values  
```
otl_v1 <# makeresults count=3 #> | range "new_col", 2, 7, step=3 
```
```
ValueError: Length of values (2) does not match length of index (3)
```


## Getting started
### Installing
1. Create virtual environment with post-processing sdk 
```bash
    make dev
```
That command  
- downloads [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- creates python virtual environment with [postprocessing_sdk](https://github.com/ISGNeuroTeam/postprocessing_sdk)
- creates link to current command in postprocessing `pp_cmd` directory 

2. Configure `otl_v1` command. Example:  
```bash
    vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/otl_v1/config.ini
```
Config example:  
```ini
[spark]
base_address = http://localhost
username = admin
password = 12345678

[caching]
# 24 hours in seconds
login_cache_ttl = 86400
# Command syntax defaults
default_request_cache_ttl = 100
default_job_timeout = 100
```

3. Configure storages for `readFile` and `writeFile` commands:  
```bash
   vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/readFile/config.ini
   
```
Config example:  
```ini
[storages]
lookups = /opt/otp/lookups
pp_shared = /opt/otp/shared_storage/persistent
```

### Run range
Use `pp` to run range command:  
```bash
pp
Storage directory is /tmp/pp_cmd_test/storage
Commmands directory is /tmp/pp_cmd_test/pp_cmd
query: | otl_v1 <# makeresults count=100 #> |  range "new_col", 1, 37, number=100
```
## Deploy
Unpack archive `pp_cmd_range` to postprocessing commands directory