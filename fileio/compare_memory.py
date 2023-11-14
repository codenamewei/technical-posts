from memory_profiler import profile
import click

@profile
def merge_with_io(files : list[str], outputfile : str, header : str) -> None:
    
    fout = open(outputfile, 'w')
    
    fout.write(header)
    
    for file in files:
        
        fin = open(file, 'r')
        header = fin.readline() # remove the header
        
        while True:
            
            inputline = fin.readline()
            if not inputline:
                break #inputline is False when file reached the end 

            fout.write(inputline)
            
        fin.close()
            
    fout.close()           
            
@profile
def merge_with_pandas(files: list[str], outputfile : str) -> None:
    
    import pandas as pd

    dfout = pd.DataFrame()

    for file in files:
        df = pd.read_csv(file)
        dfout = pd.concat([dfout, df], axis=0, ignore_index=True)
    dfout.to_csv(outputfile, index = False)

    del df
    del dfout



@profile
def merge_with_polars(files: list[str], outputfile : str) -> None:
    
    import polars as pl
    
    dfout = pl.DataFrame()

    for file in files:
        df = pl.read_csv(file, infer_schema_length=0)
        dfout = pl.concat([dfout, df])
    dfout.write_csv(outputfile)



@profile
def merge_with_modin_pandas(files: list[str], outputfile : str) -> None:
    from distributed import Client

    client = Client()
    import modin.pandas as pd

    dfout = pd.DataFrame()

    for file in files:
        df = pd.read_csv(file)
        dfout = pd.concat([dfout, df], axis=0, ignore_index=True)
    dfout.to_csv(outputfile, index = False)

        
@click.command()
@click.option('--engine', default="pandas", help='Engine to process data')
def compare_memory(engine: str):

    SUPPORTED_ENGINES = ["pandas", "polars", "io"]
    if engine not in SUPPORTED_ENGINES:

        raise ValueError(f"Input {engine} invalid. Only supports {SUPPORTED_ENGINES}")
    
    duplicates = 100
    
    key = "sampleinput"
    files = [f"data/{key}.csv"] * duplicates
    header = "key, counter\n"
    
    nativeoutputfile = f"data/{key}_native.csv"
    pdoutputfile = f"data/{key}_pd.csv"
    
    key = "winequality-red"
    files = [f"data/{key}.csv"] * duplicates
    
    headerlist = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol', 'quality']
    
    header = ", ".join(headerlist) + "\n"
    
    nativeoutputfile = f"data/{key}_native.csv"
    pdoutputfile = f"data/{key}_pd.csv"
    ploutputfile = f"data/{key}_pl.csv"
    modinpdoutputfile = f"data/{key}_modin_pd.csv"


    if engine == "io":
        print("Run io method")
        merge_with_io(files, nativeoutputfile, header)

    elif engine == "polars":
        print("Run polars method")   
        merge_with_polars(files, ploutputfile)

    elif engine == "pandas":
        print("Run pandas method")   
        merge_with_pandas(files, pdoutputfile)

    elif engine == "modin":
        print("Run modin method")
        merge_with_modin_pandas(files, modinpdoutputfile)


if __name__ == "__main__":

    compare_memory()