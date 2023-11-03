from line_profiler import LineProfiler
import pandas as pd

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
            
def merge_with_pandas(files: list[str], outputfile : str) -> None:
    
    dfout = pd.DataFrame()

    for file in files:
        df = pd.read_csv(file)
        dfout = pd.concat([dfout, df], axis=0, ignore_index=True)
    dfout.to_csv(outputfile, index = False)

        
        
if __name__ == '__main__':
    
    duplicates = 1000
    
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
    
    
    lp = LineProfiler()

    lp_wrapper = lp(merge_with_io)
    lp_wrapper(files, nativeoutputfile, header)
    
    lp_wrapper = lp(merge_with_pandas)
    lp_wrapper(files, pdoutputfile)
    lp.print_stats()