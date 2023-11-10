from memory_profiler import profile


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

        
        
if __name__ == '__main__':
    
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
    modinpdoutputfile = f"data/{key}_modin_pd.csv"

    
    
#     lp = LineProfiler()

#     lp_wrapper = lp(merge_with_io)
#     lp_wrapper(files, nativeoutputfile, header)
    
#     lp_wrapper = lp(merge_with_pandas)
#     lp_wrapper(files, pdoutputfile)
#     lp.print_stats()

    print("Run io method")
    merge_with_io(files, nativeoutputfile, header)

    print("Run pandas method")   
    merge_with_pandas(files, pdoutputfile)


    print("Run modin method")
    merge_with_modin_pandas(files, modinpdoutputfile)


    