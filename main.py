# Import The Class.
from parse import Parse

if __name__ == "__main__":

	# Add The Path To The Excel_File:
    parse = Parse("source.xlsx")

    # Use "process()" Without dask:
    parse.process("OutputFile.tsv")

    # Use "process_dask()" Using dask:
    parse.process_dask("Output_Dask.tsv", 4) # '4' ==> Number Of Partitions.