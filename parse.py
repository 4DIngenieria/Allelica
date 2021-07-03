import pandas as pd
import dask.dataframe as dd

class Parse:

    """
    Here We Create the Class --> "Parse"

    """
    def __init__(self, path):
        self.path = path

    def process(self, outpath):

        """
        Read the csv From "self.path" and 
        Process it and Save it Into $outpath
        Without Dask.

        """

        df = pd.read_excel(self.path)
        gb = df.groupby(['Run #','Sample ID'])['Array Position'].agg([lambda x: ','.join(map(str, x))])
        res = gb.reset_index()

        res.columns = ['Run #','Sample ID', 'Array Position']
        res.to_csv(outpath,sep='\t', index=False)

    def process_dask(self, outpath, part):

        """
        Read the csv From "self.path" and 
        Process it and Save it Into $outpath
        Using Dask.

        """

        df = pd.read_excel(self.path)
        ddf = dd.from_pandas(df, npartitions=part)
        out = ddf.groupby(['Run #','Sample ID'])['Array Position'].apply(lambda x: ','.join(map(str, x)), meta=pd.Series(dtype='str', name='Array Position'))
        out = out.compute()
        
        out = out.to_frame().reset_index()
        out.to_csv(outpath,sep='\t', index=False)