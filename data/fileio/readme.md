## Dependencies (To be fixed)
```
pip install memory_profiler
pip install line_profiler
pip install pandas==1.5.2
pip install polars
pip install modin[all]
pip install cchardet
```


## Data

### Get Wine Quality CSV 
```
https://github.com/aniruddhachoudhury/Red-Wine-Quality/blob/master/winequality-red.csv
```

### Get llm prompt
```
to be added
```



## How to run (To be fixed)
```
python compare_memory.py --help
python compare_memory.py --engine=pandas
python compare_memory.py --engine=pandas
python compare_memory.py --engine=polars
```

## Computer Specifications
`To-be-filled`

## Performance

### Time

|Engine | winequality-red.csv (0.15 Mb~) | train_essays_7_prompts_v2.csv (36 Mb~)|
|--|--|--|
|Native IO| 0.013 s | 1.993 s |
|Polars| 0.178 s | 3.932 s  |
|Pandas| 0.458 s | 10.120 s |
|Modin| 10.089 s  | 16.561 s|

_Note_: 
- Modin do not shows leverage for small size files due to relative long initialization time (< 5Mb~>)
- Pandas processing time increase significantly with increase file size, while Polars shows a slight increment
- Consider use IO method to maximize the saving of time (comes with the inconvenience with dealing with the file especially for data analysis)

### Memory (Maximum Memory Usage)   
|Engine | winequality-red.csv (0.15 Mb~) | train_essays_7_prompts_v2.csv (36 Mb~)|
|--|--|--|
|Native IO| 42.8 MiB | 42.9 MiB |
|Polars| 75.3 MiB  | 692.0 MiB |
|Pandas| 145.5 MiB | 503.9 MiB |
|Modin| 260.9 MiB  | 256.1 MiB |


_Note_: 
- Likewise in the measurement of time, Modin consume comparatively more memory for small size file. However, Modin do not shows significantly increasing consumption with increasing of size (makes it suitable to manage large files)
- Consider use this method to find out which library to utilize in the long run (whether it's to save time, memory or both). There are no one-size fits all approach. 

## Notes
- Pandas hold in memory, while native fileio write to file
- Which one more memory consuming?
```
The memory consumption of libraries like Polars, Pandas, and Modin can depend on various factors, such as the size of the data, the operations being performed, and the specific implementation details. However, I can provide a general comparison based on common use cases.

Pandas:
Pandas is a widely used data manipulation library in Python. It loads the entire dataset into memory, which can lead to high memory consumption for large datasets. For very large datasets that do not fit into memory, Pandas may not be the most memory-efficient option.

Polars:
Polars is designed to be memory-efficient and performant, especially for large datasets. It uses techniques like lazy evaluation and arrow memory layout to minimize memory usage. Polars can be a good choice for handling large datasets that don't fit into memory.

Modin:
Modin is a library that aims to accelerate Pandas by parallelizing operations. It can use multiple cores and distribute computations, potentially reducing memory usage by efficiently utilizing available resources. However, the memory consumption will still depend on the specific operations and the size of the data being processed.

In summary, for large datasets that don't fit into memory, Polars and Modin may provide better memory efficiency compared to Pandas. However, the actual performance can vary based on the specific use case and the operations being performed. It's often a good idea to test the libraries with your specific data and operations to determine the most suitable choice for your needs.
```