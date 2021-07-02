from parse import Parse

if __name__ == "__main__":
    parse = Parse("source.xlsx")
    parse.process("OutputFile.tsv")
    parse.process_dask("Output_Dask.tsv")