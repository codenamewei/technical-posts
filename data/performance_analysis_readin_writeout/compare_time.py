#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : codenamewei
# Created Date: 2023-11-10
# Updated Date: 2023-11-16
# version ='1.0'
# ---------------------------------------------------------------------------
from line_profiler import LineProfiler
import click

def merge_with_io(files : list[str], outputfile : str, header : str) -> None:
    
    fout = open(outputfile, 'w')
    
    fout.write(header)
    
    for file in files:
        
        fin = open(file, 'r')
        header = fin.readline() # remove the header
        
        while True:
            
            inputline = fin.readline()
            if not inputline:
                break 

            fout.write(inputline)
            
        fin.close()
            
    fout.close()           
            
def merge_with_pandas(files: list[str], outputfile : str) -> None:
    import pandas as pd

    dfout = pd.DataFrame()

    for file in files:
        df = pd.read_csv(file)
        dfout = pd.concat([dfout, df], axis=0, ignore_index=True)
    dfout.to_csv(outputfile, index = False)


def merge_with_polars(files: list[str], outputfile : str) -> None:
    import polars as pl

    dfout = pl.DataFrame()

    for file in files:
        df = pl.read_csv(file, infer_schema_length=0)
        dfout = pl.concat([dfout, df])
    dfout.write_csv(outputfile)


def merge_with_modin_pandas(files: list[str], outputfile : str) -> None:
    from distributed import Client
    import ray
    ray.init()
    client = Client()
    
    import modin.pandas as pd
    
    dfout = pd.DataFrame()

    for file in files:
        df = pd.read_csv(file)
        dfout = pd.concat([dfout, df], axis=0, ignore_index=True)
    dfout.to_csv(outputfile, index = False)
        
@click.command()
@click.option('--engine', default="pandas", help='(Required) Engine to process data.\nSupported options: [io, pandas, polars, modin]')
@click.option('--datapath', default="data/", help='(Optional) Datapath where csv file exists (without filename).\nDefault: data/')
@click.option('--csvfilename', default="winequality-red", help='(Optional) Csvfilename (without extension).\nSupported options: [train_essays_7_prompts_v2, winequality-red]. Default: winequality-red')
@click.option("--duplicate", default=10, type = int, help="(Optional) Number of times to duplicate the dataframe.\nDefault: 10")
def compare_time(engine: str, datapath: str, csvfilename: str, duplicate : int):
    
    SUPPORTED_ENGINES = ["pandas", "polars", "io", "modin"]
    if engine not in SUPPORTED_ENGINES:

        raise ValueError(f"Input {engine} invalid. Only supports {SUPPORTED_ENGINES}")

    SUPPORTED_FILENAME = ["train_essays_7_prompts_v2", "winequality-red"]

    if csvfilename not in SUPPORTED_FILENAME:

        raise ValueError(f"Input {csvfilename} invalid. Only supports {SUPPORTED_FILENAME}")

    else:

        if csvfilename == SUPPORTED_FILENAME[0]:
            headerlist = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol', 'quality']
        
        elif csvfilename == SUPPORTED_FILENAME[1]:
            headerlist = ["text", "label"]

        else:

            print("DEFINE YOUR OWN HEADER! Only needed for io method.")
    print(f"Run filename: {csvfilename}.csv") 
    files = [f"{datapath}/{csvfilename}.csv"] * duplicate
    header = ", ".join(headerlist) + "\n"
    
    lp = LineProfiler()
    if engine == "io":
        print("Run io method")
        nativeoutputfile = f"{datapath}/{csvfilename}_native.csv"
        lp_wrapper = lp(merge_with_io)
        lp_wrapper(files, nativeoutputfile, header)

    elif engine == "polars":
        print("Run polars method")
        ploutputfile = f"{datapath}/{csvfilename}_pl.csv"
        lp_wrapper = lp(merge_with_polars)
        lp_wrapper(files, ploutputfile)

    elif engine == "pandas":
        print("Run pandas method")
        pdoutputfile = f"{datapath}/{csvfilename}_pd.csv"
        lp_wrapper = lp(merge_with_pandas)
        lp_wrapper(files, pdoutputfile)

    elif engine == "modin":
        print("Run modin method")
        modinpdoutputfile = f"{datapath}/{csvfilename}_modin_pd.csv"
        lp_wrapper = lp(merge_with_modin_pandas)
        lp_wrapper(files, modinpdoutputfile)
    
    lp.print_stats()
        
    
if __name__ == "__main__":

    compare_time()
