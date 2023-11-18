## Dependencies
Install using the command 
```
python -m pip install -r requirements.txt
```


## Data

### Get Wine Quality CSV 
```
https://github.com/aniruddhachoudhury/Red-Wine-Quality/blob/master/winequality-red.csv
```

## How to run
```
python compare_memory.py --help
python compare_memory.py --engine=pandas
python compare_memory.py --engine=pandas
python compare_memory.py --engine=polars
```

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
